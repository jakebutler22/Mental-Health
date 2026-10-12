import threading
from concurrent.futures import ThreadPoolExecutor
from fastapi.testclient import TestClient
from app.main import create_app
from app.config import Settings
from app.model_client import ModelController
from app.database import connect_database
import pytest

@pytest.mark.parametrize('behavior,code',[('timeout','provider_timeout'),('empty','empty_response'),('malformed','malformed_response'),('conflict','instruction_conflict'),('failure','provider_unavailable')])
def test_failed_request_persistence(tmp_path,behavior,code):
    path=tmp_path/'failure.sqlite3'
    with TestClient(create_app(path,Settings(mock_behavior=behavior))) as client:
        cid=client.post('/api/conversations').json()['id']
        payload={'request_id':'failure','text':'Fictional exam tomorrow'}
        response=client.post(f'/api/conversations/{cid}/messages',json=payload)
        assert response.status_code==200
        value=response.json()
        assert value['status']=='failed' and value['error_code']==code and value['result'] is None
        assert client.post(f'/api/conversations/{cid}/messages',json=payload).json()==value
        with connect_database(path) as db:
            assert db.execute('SELECT count(*) FROM messages').fetchone()[0]==1
            assert db.execute("SELECT count(*) FROM messages WHERE role='assistant'").fetchone()[0]==0
            assert db.execute('SELECT status FROM model_requests').fetchone()[0]=='failed'

def test_known_roundtrip_and_context_isolation(tmp_path):
    controller=ModelController(Settings())
    original=controller.respond
    seen=[]
    def respond(text,history,recent,**kwargs):
        seen.append((text,history,recent))
        return original(text,history,recent,**kwargs)
    controller.respond=respond
    with TestClient(create_app(tmp_path/'chat.sqlite3',model_controller=controller)) as client:
        cid=client.post('/api/conversations').json()['id']
        other=client.post('/api/conversations').json()['id']
        url=f'/api/conversations/{cid}/messages'
        payload={'request_id':'exam','text':'Fictional exam tomorrow'}
        result=client.post(url,json=payload).json()
        assert result['result']['category']=='contextual' and result['mode']=='mock' and len(result['messages'])==2
        assert client.post(url,json=payload).json()==result and len(seen)==1
        assert client.post(url,json={**payload,'text':'different'}).status_code==409
        assert client.post(f'/api/conversations/{other}/messages',json=payload).status_code==409
        assert client.post(url,json={'request_id':'roommate','text':'Fictional roommate noise'}).json()['result']['category']=='contextual'
        assert len(seen[-1][1])==2
        client.post(f'/api/conversations/{other}/messages',json={'request_id':'separate','text':'Fictional club meeting'})
        assert seen[-1][1]==[]
        assert client.post(url,json={'request_id':'invalid','text':' '*5}).status_code==422
        assert client.post(url,json={'request_id':'invalid','text':'x'*501}).status_code==422
        assert client.post('/api/conversations/missing/messages',json=payload).status_code==404

def test_atomic_pending_claim(tmp_path):
    entered=threading.Event()
    release=threading.Event()
    controller=ModelController(Settings())
    original=controller.respond
    def blocked(*args,**kwargs):
        entered.set()
        assert release.wait(5)
        return original(*args,**kwargs)
    controller.respond=blocked
    with TestClient(create_app(tmp_path/'race.sqlite3',model_controller=controller)) as client:
        cid=client.post('/api/conversations').json()['id']
        url=f'/api/conversations/{cid}/messages'
        payload={'request_id':'one','text':'Fictional exam'}
        with ThreadPoolExecutor(max_workers=2) as pool:
            first=pool.submit(client.post,url,json=payload)
            assert entered.wait(5)
            assert client.post(url,json=payload).status_code==409
            assert client.post(url,json={**payload,'request_id':'two'}).status_code==409
            release.set()
            assert first.result().json()['status']=='succeeded'
        assert len(client.get('/api/conversations/'+cid).json()['messages'])==2

@pytest.mark.parametrize('bad',[True,'1',1.0])
def test_skips_require_integer(tmp_path,bad):
    with TestClient(create_app(tmp_path/'strict.sqlite3')) as client:
        row=client.post('/api/sessions',json={'request_id':'one','skill':'grounding'}).json()
        response=client.patch('/api/sessions/'+row['id'],json={'version':0,'state':'active','active_elapsed_ms':1,'step':2,'cycles':0,'skipped_steps':[bad]})
        assert response.status_code==422

def test_history_clear_during_provider_never_resurrects(tmp_path):
    entered=threading.Event()
    release=threading.Event()
    controller=ModelController(Settings())
    original=controller.respond
    def blocked(*args,**kwargs):
        entered.set()
        assert release.wait(5)
        return original(*args,**kwargs)
    controller.respond=blocked
    path=tmp_path/'deleted.sqlite3'
    with TestClient(create_app(path,model_controller=controller)) as client:
        cid=client.post('/api/conversations').json()['id']
        with ThreadPoolExecutor(max_workers=1) as pool:
            pending=pool.submit(client.post,f'/api/conversations/{cid}/messages',json={'request_id':'one','text':'Fictional exam'})
            assert entered.wait(5)
            assert client.delete('/api/history').status_code==200
            release.set()
            response=pending.result()
            assert response.status_code==410 and response.json()=={'detail':'history_cleared'}
        with connect_database(path) as db:
            for table in ('conversations','messages','model_requests','sessions'):
                assert db.execute(f'SELECT count(*) FROM {table}').fetchone()[0]==0

def test_guac_saved_clarification_recommendation_and_choice(tmp_path):
    path=tmp_path/'guac.sqlite3'
    with TestClient(create_app(path)) as client:
        cid=client.post('/api/conversations').json()['id']
        url=f'/api/conversations/{cid}/messages'
        first=client.post(url,json={'request_id':'vague1','text':'Things are mixed.'}).json()
        assert first['result']['action']=='clarify'
        second=client.post(url,json={'request_id':'vague2','text':'Still unclear.'}).json()
        assert second['result']['clarification'] is None
        reply=client.post(url,json={'request_id':'tense','text':'The fictional exam has me tense and keyed up.'}).json()
        assert reply['result']['recommended_skill']=='breathing'
        # User deliberately selects the alternative, not the inferred recommendation.
        chosen=client.post('/api/sessions',json={'request_id':'choice','skill':'grounding','conversation_id':cid,'recommendation_request_id':'tense'}).json()
        assert chosen['skill']=='grounding' and chosen['recommended_skill']=='breathing'
        assert chosen['recommendation_reason']==reply['result']['reason']
        assert client.post('/api/sessions',json={'request_id':'invalid','skill':'grounding','conversation_id':cid,'recommendation_request_id':'missing'}).status_code==422
        other=client.post('/api/conversations').json()['id']
        assert client.post('/api/sessions',json={'request_id':'cross','skill':'grounding','conversation_id':other,'recommendation_request_id':'tense'}).status_code==422
        transcript=client.get('/api/conversations/'+cid).json()['messages']
        assert transcript[-1]['recommendation']['recommended_skill']=='breathing'
    with TestClient(create_app(path)) as client:
        saved=client.get('/api/sessions').json()['items'][0]
        assert saved['skill']=='grounding' and saved['recommended_skill']=='breathing'
        third=client.post(url,json={'request_id':'vague3','text':'Things feel mixed.'}).json()
        assert third['result']['clarification'] is None


def test_additive_legacy_sessions_preferences_migration(tmp_path):
    path=tmp_path/'legacy.sqlite3'
    # Simulate the pre-Guac schema, which lacks recommendation fields.
    with connect_database(path) as db:
        db.executescript("""
        CREATE TABLE sessions(id TEXT PRIMARY KEY,request_id TEXT UNIQUE,conversation_id TEXT,skill TEXT,state TEXT,started_at TEXT,ended_at TEXT,active_elapsed_ms INTEGER,step INTEGER,cycles INTEGER,skipped_steps TEXT,version INTEGER);
        INSERT INTO sessions VALUES('legacy','legacy',NULL,'breathing','completed','2026-10-12',NULL,60000,0,6,'[]',2);
        CREATE TABLE preferences(singleton INTEGER PRIMARY KEY,explicit_balloon_color TEXT,simple_view INTEGER,reduced_motion INTEGER);
        INSERT INTO preferences VALUES(1,'red',1,0);
        """)
    with TestClient(create_app(path)) as client:
        legacy=client.get('/api/sessions').json()['items'][0]
        assert legacy['id']=='legacy' and legacy['state']=='completed' and legacy['recommended_skill'] is None
        assert client.get('/api/preferences').json()['explicit_balloon_color']=='red'
