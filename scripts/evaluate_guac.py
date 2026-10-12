"""Independent Guac contextual fixtures and SQLite checks; no network calls."""
import json
import sys
import sqlite3
import tempfile
from pathlib import Path
from dataclasses import asdict
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'backend'))
from fastapi.testclient import TestClient
from app.main import create_app
from app.config import Settings
from app.model_client import ModelController,ModelFailure,validate_selection
ROOT=Path(__file__).resolve().parents[1]
records=[]
class EvaluationMismatch(AssertionError):
    def __init__(self,observed):self.observed=observed
def expect(condition):
    if not condition:raise AssertionError('Expectation not met')
def check(case,action,expected,function):
    try:observed=function();status='pass'
    except Exception as error:observed=getattr(error,'observed',{'error_type':type(error).__name__});status='fail'
    records.append(dict(case=case,action=action,expected=expected,mode='mock/TestClient; no network',observed=observed,status=status))
def result_case(text,skill,action='offer',history=(),clarified=False):
    result=asdict(ModelController(Settings()).respond(text,history,clarification_used=clarified))
    if not (result['recommended_skill']==skill and result['action']==action and result['reflection'] and result['reason']):raise EvaluationMismatch({k:result[k] for k in ('reflection','recommended_skill','reason','clarification','action')})
    return {k:result[k] for k in ('reflection','recommended_skill','reason','clarification','action')}
def run():
    cases=[
      ('G01','Fictional exam tomorrow; my shoulders feel tight and I am tense.','breathing','offer'),
      ('G02','Fictional roommate disagreement; I keep replaying it and my thoughts are looping.','grounding','offer'),
      ('G03','No breathing. I feel keyed up before a fictional presentation.','grounding','offer'),
      ('G04','No grounding. I prefer breathing before a fictional exam.','breathing','offer'),
      ('G05','I feel wound up. Actually I feel scattered about the fictional club meeting.','grounding','offer'),
      ('G06','No breathing. Actually I feel keyed up before a fictional exam.','grounding','offer'),
      ('G07','No breathing. Actually I prefer breathing before a fictional exam.','breathing','offer'),
      ('G08','I prefer grounding before the fictional exam.','grounding','offer'),
      ('G09','Neither, thanks.','None','decline'),
      ('G10','Stop.','None','decline'),
      ('G11','No breathing and no grounding.','None','decline'),
      ('G12','A fictional campus afternoon feels unclear.','None','clarify'),
      ('G13','I feel tense and scattered before the fictional exam.','None','clarify'),
      ('G14','I do not feel tense about this fictional situation.','None','clarify'),
      ('G15','I prefer breathing although my fictional roommate situation leaves me scattered.','breathing','offer'),
      ('G16','I prefer grounding. Actually I feel tense about the fictional exam.','grounding','offer'),
      ('G24','I feel tense waiting at the fictional campus bus stop.','breathing','offer'),
      ('G25',"I'd like grounding before the fictional exam.",'grounding','offer'),
      ('G26',"I don't want to do breathing; I feel keyed up about the fictional exam.",'grounding','offer'),
    ]
    for name,text,skill,action in cases:
        check(name,text,f'{skill}; {action}; brief reflection/reason',lambda t=text,s=skill,a=action:result_case(t,None if s=='None' else s,a))
    check('G17','Second vague input after optional clarification','No second clarification; both choices available',lambda:result_case('Still unclear in this fictional moment.',None,'offer',clarified=True))
    check('G18','Short followup on tense prior input','Relevant bounded conversational context retained',lambda:result_case('Still tense','breathing',history=[{'role':'user','text':'Fictional exam tomorrow; I feel tense.'}]))
    def no_invented():
        result=result_case('I prefer grounding before the fictional exam.','grounding');expect('scattered' not in result['reflection'] and 'pulled into' not in result['reflection']);return result
    check('G19','Preference-only input; no stated feeling','Reflect preference without inventing scattered feelings',no_invented)
    def unsupported():
        rejected=[]
        for skill,reason in [('STOP','An optional pause.'),('breathing','This will fix your anxiety.'),('breathing','Hold your breath.')]:
            try:validate_selection(json.dumps(dict(reflection='A fictional exam can feel demanding.',recommended_skill=skill,reason=reason,clarification=None,action='offer')))
            except ModelFailure as error:rejected.append(error.code)
        expect(len(rejected)==3);return {'rejected_count':3,'error_codes':rejected}
    check('G20','Unsupported skill, promise and breath hold in structured model output','Reject unsafe/unsupported output before UI',unsupported)
    with tempfile.TemporaryDirectory(prefix='.guac-eval-',dir=ROOT) as temporary:
        folder=Path(temporary)
        def conversation():
            path=folder/'context.sqlite3'
            with TestClient(create_app(path,Settings())) as client:
                cid=client.post('/api/conversations').json()['id'];url=f'/api/conversations/{cid}/messages'
                first=client.post(url,json={'request_id':'vague','text':'Fictional campus moment feels unclear.'}).json();expect(first['result']['action']=='clarify')
            with TestClient(create_app(path,Settings())) as client:
                second=client.post(url,json={'request_id':'vague2','text':'Still unclear in this fictional moment.'}).json();expect(second['result']['clarification'] is None and second['result']['action']=='offer')
                corrected=client.post(url,json={'request_id':'correct','text':'Actually I feel scattered; no breathing.'}).json();expect(corrected['result']['recommended_skill']=='grounding')
                selected=client.post('/api/sessions',json={'request_id':'chosen','skill':'breathing','conversation_id':cid,'recommendation_request_id':'correct'}).json();expect(selected['skill']=='breathing' and selected['recommended_skill']=='grounding')
                same=client.post('/api/sessions',json={'request_id':'chosen','skill':'breathing','conversation_id':cid,'recommendation_request_id':'correct'}).json();expect(same['id']==selected['id'])
                detail=client.get('/api/conversations/'+cid).json();expect(any(m.get('recommendation',{}).get('recommended_skill')=='grounding' for m in detail['messages'] if m.get('recommendation')))
                with sqlite3.connect(path) as db:expect(db.execute('PRAGMA foreign_key_check').fetchall()==[]);counts=db.execute('SELECT count(*) FROM sessions').fetchone()[0]
            return {'clarification_after_restart':None,'recommended_skill':'grounding','chosen_skill':'breathing','duplicate_session_count':counts,'foreign_key_violations':0}
        check('G21','Vague turn/restart/vague turn/correction/choose alternative/replay','At most one persisted optional question; recommendation distinct from chosen skill',conversation)
        def failed():
            with TestClient(create_app(folder/'failed.sqlite3',Settings(mock_behavior='timeout'))) as client:
                cid=client.post('/api/conversations').json()['id'];result=client.post(f'/api/conversations/{cid}/messages',json={'request_id':'timeout','text':'Fictional exam; tense.'}).json();expect(result['status']=='failed' and result['result'] is None)
                direct=client.post('/api/sessions',json={'request_id':'direct','skill':'grounding'});expect(direct.status_code==201)
                invalid=client.post('/api/sessions',json={'request_id':'invalid','skill':'grounding','conversation_id':cid,'recommendation_request_id':'timeout'});expect(invalid.status_code==422)
            return {'chat_status':'failed','code':'provider_timeout','direct_session_status':201,'failed_recommendation_link_status':422}
        check('G22','Injected provider timeout then direct exercise; invalid failed-result reference','Direct skill independent; failed recommendation cannot be snapshotted',failed)
        def migration():
            path=folder/'legacy.sqlite3'
            # Create this project legacy schema via fixture SQL, never copy runtime data.
            with sqlite3.connect(path) as db:
                db.executescript("""CREATE TABLE conversations(id TEXT PRIMARY KEY,created_at TEXT NOT NULL,updated_at TEXT NOT NULL,fictional_title TEXT NOT NULL);
CREATE TABLE model_requests(request_id TEXT PRIMARY KEY,conversation_id TEXT NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,status TEXT NOT NULL,mode TEXT NOT NULL,configured_model_id TEXT,sanitized_error_code TEXT,created_at TEXT NOT NULL,result_json TEXT);
CREATE TABLE messages(id INTEGER PRIMARY KEY AUTOINCREMENT,conversation_id TEXT NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,role TEXT NOT NULL,text TEXT NOT NULL,created_at TEXT NOT NULL,request_id TEXT NOT NULL REFERENCES model_requests(request_id),status TEXT NOT NULL,UNIQUE(request_id,role));
CREATE TABLE sessions(id TEXT PRIMARY KEY,request_id TEXT NOT NULL UNIQUE,conversation_id TEXT REFERENCES conversations(id),skill TEXT NOT NULL,state TEXT NOT NULL,started_at TEXT NOT NULL,ended_at TEXT,active_elapsed_ms INTEGER NOT NULL,step INTEGER NOT NULL,cycles INTEGER NOT NULL,skipped_steps TEXT NOT NULL,version INTEGER NOT NULL);
CREATE TABLE preferences(singleton INTEGER PRIMARY KEY,explicit_balloon_color TEXT,simple_view INTEGER NOT NULL DEFAULT 0,reduced_motion INTEGER NOT NULL DEFAULT 0);
INSERT INTO conversations VALUES('legacy','2026-10-12','2026-10-12','Fictional legacy exam');
INSERT INTO sessions VALUES('old','old','legacy','breathing','completed','2026-10-12','2026-10-12',60000,0,6,'[]',1);
INSERT INTO preferences VALUES(1,'red',0,0);""")
            with TestClient(create_app(path,Settings())) as client:
                row=client.get('/api/sessions/old').json();expect(row['skill']=='breathing' and row['state']=='completed' and row['recommendation_request_id'] is None)
                expect(client.get('/api/preferences').json()['explicit_balloon_color']=='red');expect(client.get('/api/conversations/legacy').status_code==200)
                with sqlite3.connect(path) as db:expect(db.execute('PRAGMA foreign_key_check').fetchall()==[])
            return {'legacy_completed_record_preserved':True,'new_recommendation_reference':None,'explicit_color_preserved':'red','foreign_key_violations':0}
        check('G23','Additive migration from fictional pre-Guac schema','Preserve legacy records and explicit red; new columns nullable',migration)
    result={'scope':'Guac deterministic fixtures/API/database; no actual live network or browser calls','cases':records,'passed':sum(x['status']=='pass' for x in records),'failed':sum(x['status']=='fail' for x in records)}
    (ROOT/'docs/evidence/guac-context-evaluation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'cases':len(records),'passed':result['passed'],'failed':result['failed']}))
    return bool(result['failed'])
if __name__=='__main__':raise SystemExit(run())
