import sqlite3
import pytest
from fastapi.testclient import TestClient
from app.main import create_app
from app.database import connect_database

@pytest.fixture
def runtime(tmp_path):
    path=tmp_path/'fictional.sqlite3'
    with TestClient(create_app(path)) as client:
        yield client,path

def start(client,skill='breathing',request_id='one',conversation_id=None):
    response=client.post('/api/sessions',json=dict(request_id=request_id,skill=skill,conversation_id=conversation_id))
    assert response.status_code==201
    return response.json()

def patch(client,row,**changes):
    data={key:row[key] for key in ('version','state','active_elapsed_ms','step','cycles','skipped_steps')}
    data.update(changes)
    return client.patch('/api/sessions/'+row['id'],json=data)

def test_crud_restart_relationships(tmp_path):
    path=tmp_path/'restart.sqlite3'
    with TestClient(create_app(path)) as client:
        with connect_database(path) as db:
            assert db.execute('SELECT count(*) FROM sessions').fetchone()[0]==0
            assert db.execute('PRAGMA foreign_keys').fetchone()[0]==1
        cid=client.post('/api/conversations').json()['id']
        row=start(client,conversation_id=cid)
        row=patch(client,row,state='paused',active_elapsed_ms=2000).json()
        assert client.patch('/api/preferences',json={'explicit_balloon_color':'blue','simple_view':True}).status_code==200
        with connect_database(path) as db:
            stored=dict(db.execute('SELECT * FROM sessions').fetchone())
            assert stored['conversation_id']==cid and stored['state']=='paused'
            with pytest.raises(sqlite3.IntegrityError):
                db.execute("INSERT INTO sessions(id,request_id,conversation_id,skill,state,started_at,active_elapsed_ms,step,cycles,skipped_steps,version) VALUES('bad','bad','absent','breathing','active','x',0,0,0,'[]',0)")
    with TestClient(create_app(path)) as client:
        row=client.get('/api/sessions').json()['items'][0]
        assert row['state']=='interrupted' and row['active_elapsed_ms']==2000 and row['ended_at']
        assert client.get('/api/conversations/'+cid).json()['sessions'][0]['id']==row['id']
        assert client.get('/api/preferences').json()['explicit_balloon_color']=='blue'
        assert patch(client,row,state='active').status_code==409
        assert client.delete('/api/history').json()=={'cleared':True}
        with connect_database(path) as db:
            assert db.execute('SELECT count(*) FROM sessions').fetchone()[0]==0
            assert db.execute('SELECT count(*) FROM conversations').fetchone()[0]==0

def test_breathing_boundary_idempotency_conflicts(runtime):
    client,path=runtime
    row=start(client)
    assert start(client)['id']==row['id']
    assert client.post('/api/sessions',json={'request_id':'one','skill':'grounding'}).status_code==409
    assert patch(client,row,state='completed',active_elapsed_ms=59999,cycles=5).status_code==422
    assert patch(client,row,active_elapsed_ms=11000,cycles=0).status_code==422
    paused=patch(client,row,state='paused',active_elapsed_ms=4500).json()
    assert patch(client,row,state='stopped').status_code==409
    assert patch(client,paused,state='active',active_elapsed_ms=5000).status_code==422
    resumed=patch(client,paused,state='active').json()
    completed=patch(client,resumed,state='completed',active_elapsed_ms=60000,cycles=6).json()
    assert completed['state']=='completed' and completed['ended_at']
    assert patch(client,completed,state='active').status_code==409

def test_grounding_skips_and_ordinary_completion(runtime):
    client,_=runtime
    row=start(client,'grounding')
    assert patch(client,row,state='completed',step=5).status_code==422
    for step in range(1,6):
        response=patch(client,row,step=step,active_elapsed_ms=step*12000,skipped_steps=[0],state='completed' if step==5 else 'active')
        assert response.status_code==200,response.text
        row=response.json()
    assert row['skipped_steps']==[0] and row['state']=='completed'

def test_invalid_preferences_and_request_boundaries(runtime):
    client,_=runtime
    assert client.post('/api/sessions',json={'request_id':'bad','skill':'STOP'}).status_code==422
    assert client.post('/api/sessions',json={'request_id':'bad','skill':'breathing','conversation_id':'missing'}).status_code==404
    assert client.get('/api/conversations/missing').status_code==404
    assert client.patch('/api/preferences',json={'explicit_balloon_color':'neon'}).status_code==422
    assert client.patch('/api/preferences',json={'simple_view':None}).status_code==422
    assert client.get('/api/sessions?limit=101').status_code==422
    assert client.delete('/api/preferences').json()=={'explicit_balloon_color':None,'simple_view':False,'reduced_motion':False}

def test_pending_requests_interrupted_on_restart(tmp_path):
    path=tmp_path/'pending.sqlite3'
    with TestClient(create_app(path)) as client:
        cid=client.post('/api/conversations').json()['id']
        with connect_database(path) as db:
            db.execute("INSERT INTO model_requests(request_id,conversation_id,status,mode,configured_model_id,sanitized_error_code,created_at) VALUES('r',?,'pending','mock',NULL,NULL,'x')",(cid,))
            db.execute("INSERT INTO messages(conversation_id,role,text,created_at,request_id,status) VALUES(?,'user','Fictional exam','x','r','pending')",(cid,))
    with TestClient(create_app(path)) as client:
        msg=client.get('/api/conversations/'+cid).json()['messages'][0]
        assert msg['status']=='interrupted' and msg['sanitized_error_code']=='restart_interrupted'
