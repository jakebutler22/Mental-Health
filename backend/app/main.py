"""Localhost coursework API. Application owns all exercise rules."""
import json
import os
import sqlite3
from contextlib import asynccontextmanager
from pathlib import Path
from uuid import uuid4
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .config import load_settings
from .model_client import ModelController
from .routes import register_model_routes
from .database import DEFAULT_DATABASE_PATH, connect_database, initialize_database, now, row_dict
from .schemas import SessionStart, SessionUpdate, PreferencesUpdate


def create_app(database_path=None, settings=None, model_controller=None):
    settings = settings or load_settings()
    path = Path(database_path or os.environ.get("DATABASE_PATH") or DEFAULT_DATABASE_PATH)
    @asynccontextmanager
    async def lifespan(app):
        initialize_database(path)
        yield
    app = FastAPI(title='Campus Pause localhost coursework', lifespan=lifespan)
    app.state.database_path = path
    app.state.settings = settings
    app.state.model_controller = model_controller or ModelController(settings)
    app.add_middleware(CORSMiddleware, allow_origins=['http://localhost:5174','http://127.0.0.1:5174'], allow_methods=['GET','POST','PATCH','DELETE'], allow_headers=['Content-Type'])

    @app.exception_handler(sqlite3.Error)
    async def database_error(request, error):
        return JSONResponse(status_code=503, content={'detail':'storage_unavailable'})

    @app.get('/api/health')
    def health():
        with connect_database(path) as db:
            db.execute('SELECT 1').fetchone()
        return {'status':'ok','database_ready':True, **settings.health(), 'live_verified':app.state.model_controller.live_verified,'live_attempts':app.state.model_controller.attempts}

    @app.post('/api/conversations', status_code=201)
    def create_conversation():
        value = {'id':str(uuid4()),'created_at':now(),'updated_at':now(),'fictional_title':'Fictional campus conversation'}
        with connect_database(path) as db:
            db.execute('INSERT INTO conversations VALUES(:id,:created_at,:updated_at,:fictional_title)', value)
        return value

    @app.get('/api/conversations')
    def conversations(limit: int = Query(20, ge=1,le=100), offset:int=Query(0,ge=0)):
        with connect_database(path) as db:
            return {'items':[row_dict(r) for r in db.execute('SELECT * FROM conversations ORDER BY updated_at DESC LIMIT ? OFFSET ?', (limit,offset))]}

    @app.get('/api/conversations/{conversation_id}')
    def conversation(conversation_id:str):
        with connect_database(path) as db:
            value=row_dict(db.execute('SELECT * FROM conversations WHERE id=?',(conversation_id,)).fetchone())
            if value is None: raise HTTPException(404,'conversation_not_found')
            value['messages']=[row_dict(r) for r in db.execute('SELECT messages.*, model_requests.mode, model_requests.sanitized_error_code FROM messages JOIN model_requests USING(request_id) WHERE messages.conversation_id=? ORDER BY messages.id',(conversation_id,))]
            value['sessions']=[row_dict(r) for r in db.execute('SELECT * FROM sessions WHERE conversation_id=? ORDER BY started_at',(conversation_id,))]
            return value

    @app.post('/api/sessions', status_code=201)
    def start_session(data:SessionStart):
        with connect_database(path) as db:
            existing=row_dict(db.execute('SELECT * FROM sessions WHERE request_id=?',(data.request_id,)).fetchone())
            if existing:
                if existing['skill']!=data.skill or existing['conversation_id']!=data.conversation_id: raise HTTPException(409,'request_id_conflict')
                return existing
            if data.conversation_id and not db.execute('SELECT 1 FROM conversations WHERE id=?',(data.conversation_id,)).fetchone(): raise HTTPException(404,'conversation_not_found')
            sid=str(uuid4())
            db.execute("INSERT INTO sessions VALUES(?,?,?,?,'active',?,NULL,0,0,0,'[]',0)",(sid,data.request_id,data.conversation_id,data.skill,now()))
            return row_dict(db.execute('SELECT * FROM sessions WHERE id=?',(sid,)).fetchone())

    @app.get('/api/sessions')
    def sessions(limit:int=Query(20,ge=1,le=100),offset:int=Query(0,ge=0)):
        with connect_database(path) as db:
            return {'items':[row_dict(r) for r in db.execute('SELECT * FROM sessions ORDER BY started_at DESC LIMIT ? OFFSET ?',(limit,offset))]}

    @app.get('/api/sessions/{session_id}')
    def session(session_id:str):
        with connect_database(path) as db:
            value=row_dict(db.execute('SELECT * FROM sessions WHERE id=?',(session_id,)).fetchone())
            if value is None: raise HTTPException(404,'session_not_found')
            return value

    @app.patch('/api/sessions/{session_id}')
    def update_session(session_id:str,data:SessionUpdate):
        with connect_database(path) as db:
            old=row_dict(db.execute('SELECT * FROM sessions WHERE id=?',(session_id,)).fetchone())
            if old is None: raise HTTPException(404,'session_not_found')
            if old['version']!=data.version: raise HTTPException(409,'stale_version')
            if old['state'] not in ('active','paused'): raise HTTPException(409,'terminal_session')
            if data.active_elapsed_ms<old['active_elapsed_ms']: raise HTTPException(422,'elapsed_cannot_decrease')
            if old['state']=='paused' and data.active_elapsed_ms!=old['active_elapsed_ms']: raise HTTPException(422,'paused_elapsed_must_freeze')
            skips=data.skipped_steps
            if len(set(skips))!=len(skips) or any(type(s) is not int or s<0 or s>4 for s in skips): raise HTTPException(422,'invalid_skipped_steps')
            if old['skill']=='breathing':
                if data.step!=0 or skips: raise HTTPException(422,'breathing_has_no_sensory_steps')
                if data.cycles!=min(6,data.active_elapsed_ms//10000): raise HTTPException(422,'cycles_disagree_with_clock')
                if data.state=='completed' and data.active_elapsed_ms<60000: raise HTTPException(422,'breathing_not_complete')
            else:
                if data.cycles or data.step<old['step'] or data.step>old['step']+1 or any(s>=data.step for s in skips) or not set(old['skipped_steps']).issubset(skips): raise HTTPException(422,'invalid_grounding_progress')
                if data.state=='completed' and data.step!=5: raise HTTPException(422,'grounding_not_complete')
            ended=now() if data.state in ('completed','stopped','interrupted') else None
            changed=db.execute('UPDATE sessions SET state=?,active_elapsed_ms=?,step=?,cycles=?,skipped_steps=?,ended_at=?,version=version+1 WHERE id=? AND version=?',(data.state,data.active_elapsed_ms,data.step,data.cycles,json.dumps(skips),ended,session_id,data.version)).rowcount
            if changed!=1: raise HTTPException(409,'stale_version')
            return row_dict(db.execute('SELECT * FROM sessions WHERE id=?',(session_id,)).fetchone())

    @app.get('/api/preferences')
    def preferences():
        with connect_database(path) as db:
            value=row_dict(db.execute('SELECT * FROM preferences WHERE singleton=1').fetchone())
            value.pop('singleton')
            return value

    @app.patch('/api/preferences')
    def set_preferences(data:PreferencesUpdate):
        fields=data.model_dump(exclude_unset=True)
        if any(fields.get(k) is None for k in ('simple_view','reduced_motion') if k in fields): raise HTTPException(422,'boolean_required')
        with connect_database(path) as db:
            for key,value in fields.items():
                db.execute(f'UPDATE preferences SET {key}=? WHERE singleton=1',(value,))
        return preferences()

    @app.delete('/api/preferences')
    def reset_preferences():
        with connect_database(path) as db:
            db.execute('UPDATE preferences SET explicit_balloon_color=NULL,simple_view=0,reduced_motion=0')
        return preferences()

    @app.delete('/api/history')
    def clear_history():
        with connect_database(path) as db:
            db.execute('DELETE FROM conversations')
            db.execute('DELETE FROM sessions')
        return {'cleared':True}

    register_model_routes(app)
    return app

app = create_app()
