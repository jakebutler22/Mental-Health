"""Validated conversation boundary. Failed calls persist without invented replies."""
from dataclasses import asdict
import json
from fastapi import HTTPException
from .database import connect_database, row_dict, now
from .schemas import ChatMessage
from .model_client import ModelFailure


def register_model_routes(app):
    path=app.state.database_path
    controller=app.state.model_controller

    def saved_response(db,request):
        messages=[row_dict(r) for r in db.execute('SELECT * FROM messages WHERE request_id=? ORDER BY id',(request['request_id'],))]
        # Structured result stored separately; never raw provider payload.
        result=json.loads(request['result_json']) if request['result_json'] else None
        return {'request_id':request['request_id'],'conversation_id':request['conversation_id'],'status':request['status'],'mode':request['mode'],'error_code':request['sanitized_error_code'],'messages':messages,'result':result}

    @app.post('/api/conversations/{conversation_id}/messages')
    def message(conversation_id:str,data:ChatMessage):
        text=data.text.strip()
        if not text: raise HTTPException(422,'text_required')
        # BEGIN IMMEDIATE serializes claim before provider I/O. No DB lock held across call.
        with connect_database(path) as db:
            db.execute('BEGIN IMMEDIATE')
            if not db.execute('SELECT 1 FROM conversations WHERE id=?',(conversation_id,)).fetchone(): raise HTTPException(404,'conversation_not_found')
            old=db.execute('SELECT * FROM model_requests WHERE request_id=?',(data.request_id,)).fetchone()
            if old:
                user=db.execute("SELECT text FROM messages WHERE request_id=? AND role='user'",(data.request_id,)).fetchone()
                if old['conversation_id']!=conversation_id or not user or user['text']!=text: raise HTTPException(409,'request_id_conflict')
                if old['status']=='pending': raise HTTPException(409,'request_in_progress')
                return saved_response(db,old)
            if db.execute("SELECT 1 FROM model_requests WHERE conversation_id=? AND status='pending'",(conversation_id,)).fetchone(): raise HTTPException(409,'conversation_request_in_progress')
            history=[row_dict(r) for r in db.execute('SELECT role,text FROM messages WHERE conversation_id=? ORDER BY id DESC LIMIT 6',(conversation_id,))][::-1]
            recent=[row_dict(r) for r in db.execute("SELECT skill,state FROM sessions WHERE conversation_id=? AND state IN ('completed','stopped','interrupted') ORDER BY started_at DESC LIMIT 3",(conversation_id,))]
            db.execute('INSERT INTO model_requests(request_id,conversation_id,status,mode,configured_model_id,created_at) VALUES(?,?,?,?,?,?)',(data.request_id,conversation_id,'pending',controller.settings.mode,controller.settings.model or None,now()))
            db.execute("INSERT INTO messages(conversation_id,role,text,created_at,request_id,status) VALUES(?,'user',?,?,?,'pending')",(conversation_id,text,now(),data.request_id))
        try:
            result=asdict(controller.respond(text,history,recent))
            code=None
        except ModelFailure as error:
            result=None
            code=error.code
        with connect_database(path) as db:
            db.execute('BEGIN IMMEDIATE')
            if not db.execute('SELECT 1 FROM model_requests WHERE request_id=?',(data.request_id,)).fetchone() or not db.execute('SELECT 1 FROM conversations WHERE id=?',(conversation_id,)).fetchone():
                raise HTTPException(410,'history_cleared')
            status='succeeded' if result else 'failed'
            mode=result['mode'] if result else controller.settings.mode
            db.execute('UPDATE model_requests SET status=?,mode=?,sanitized_error_code=?,result_json=? WHERE request_id=?',(status,mode,code,json.dumps(result) if result else None,data.request_id))
            db.execute('UPDATE messages SET status=? WHERE request_id=?',(status,data.request_id))
            if result:
                db.execute("INSERT INTO messages(conversation_id,role,text,created_at,request_id,status) VALUES(?,'assistant',?,?,?,'succeeded')",(conversation_id,result['acknowledgement'],now(),data.request_id))
            db.execute('UPDATE conversations SET updated_at=? WHERE id=?',(now(),conversation_id))
            return saved_response(db,db.execute('SELECT * FROM model_requests WHERE request_id=?',(data.request_id,)).fetchone())
