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
    def respond(text,history,recent):
        seen.append((text,history,recent))
        return original(text,history,recent)
    controller.respond=respond
    with TestClient(create_app(tmp_path/'chat.sqlite3',model_controller=controller)) as client:
        cid=client.post('/api/conversations').json()['id']
        other=client.post('/api/conversations').json()['id']
        url=f'/api/conversations/{cid}/messages'
        payload={'request_id':'exam','text':'Fictional exam tomorrow'}
        result=client.post(url,json=payload).json()
        assert result['result']['category']=='exam' and result['mode']=='mock' and len(result['messages'])==2
        assert client.post(url,json=payload).json()==result and len(seen)==1
        assert client.post(url,json={**payload,'text':'different'}).status_code==409
        assert client.post(f'/api/conversations/{other}/messages',json=payload).status_code==409
        assert client.post(url,json={'request_id':'roommate','text':'Fictional roommate noise'}).json()['result']['category']=='roommate'
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
    def blocked(*args):
        entered.set()
        assert release.wait(5)
        return original(*args)
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
    def blocked(*args):
        entered.set()
        assert release.wait(5)
        return original(*args)
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
