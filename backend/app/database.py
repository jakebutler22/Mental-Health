"""Own single-user SQLite storage; no prior-project imports or seed data."""
import json
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_DATABASE_PATH = Path(__file__).resolve().parent.parent / 'data' / 'campus-pause.sqlite3'


def now():
    return datetime.now(timezone.utc).isoformat()


@contextmanager
def connect_database(path=DEFAULT_DATABASE_PATH):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path, timeout=5, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    connection.execute('PRAGMA foreign_keys = ON')
    try:
        with connection:
            yield connection
    finally:
        connection.close()


def row_dict(row):
    if row is None:
        return None
    result = dict(row)
    if 'skipped_steps' in result:
        result['skipped_steps'] = json.loads(result['skipped_steps'])
    for key in ('simple_view', 'reduced_motion'):
        if key in result:
            result[key] = bool(result[key])
    return result


def initialize_database(path):
    with connect_database(path) as db:
        db.executescript('''
        CREATE TABLE IF NOT EXISTS conversations (
          id TEXT PRIMARY KEY, created_at TEXT NOT NULL, updated_at TEXT NOT NULL,
          fictional_title TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS model_requests (
          request_id TEXT PRIMARY KEY, conversation_id TEXT NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
          status TEXT NOT NULL CHECK(status IN ('pending','succeeded','failed','interrupted')),
          mode TEXT NOT NULL CHECK(mode IN ('mock','live')), configured_model_id TEXT,
          sanitized_error_code TEXT, created_at TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS messages (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          conversation_id TEXT NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
          role TEXT NOT NULL CHECK(role IN ('user','assistant')), text TEXT NOT NULL,
          created_at TEXT NOT NULL, request_id TEXT NOT NULL REFERENCES model_requests(request_id) ON DELETE CASCADE,
          status TEXT NOT NULL, UNIQUE(request_id,role));
        CREATE TABLE IF NOT EXISTS sessions (
          id TEXT PRIMARY KEY, request_id TEXT NOT NULL UNIQUE,
          conversation_id TEXT REFERENCES conversations(id) ON DELETE CASCADE,
          skill TEXT NOT NULL CHECK(skill IN ('breathing','grounding')),
          state TEXT NOT NULL CHECK(state IN ('active','paused','completed','stopped','interrupted')),
          started_at TEXT NOT NULL, ended_at TEXT,
          active_elapsed_ms INTEGER NOT NULL CHECK(active_elapsed_ms>=0),
          step INTEGER NOT NULL CHECK(step BETWEEN 0 AND 5),
          cycles INTEGER NOT NULL CHECK(cycles BETWEEN 0 AND 6),
          skipped_steps TEXT NOT NULL DEFAULT '[]', version INTEGER NOT NULL DEFAULT 0);
        CREATE TABLE IF NOT EXISTS preferences (
          singleton INTEGER PRIMARY KEY CHECK(singleton=1), explicit_balloon_color TEXT,
          simple_view INTEGER NOT NULL DEFAULT 0, reduced_motion INTEGER NOT NULL DEFAULT 0);
        INSERT OR IGNORE INTO preferences(singleton) VALUES(1);
        ''')
        columns={r['name'] for r in db.execute('PRAGMA table_info(model_requests)')}
        if 'result_json' not in columns:
            db.execute('ALTER TABLE model_requests ADD COLUMN result_json TEXT')
        db.execute("UPDATE sessions SET state='interrupted',ended_at=?,version=version+1 WHERE state IN ('active','paused')", (now(),))
        db.execute("UPDATE model_requests SET status='interrupted',sanitized_error_code='restart_interrupted' WHERE status='pending'")
        db.execute("UPDATE messages SET status='interrupted' WHERE request_id IN (SELECT request_id FROM model_requests WHERE status='interrupted')")
