"""Explicit backend-local settings; secrets never enter responses or logs."""
import os
from dataclasses import dataclass, field
from pathlib import Path
from dotenv import load_dotenv

BACKEND_DIRECTORY = Path(__file__).resolve().parent.parent

@dataclass(frozen=True)
class Settings:
    mode: str = 'mock'
    api_key: str = field(default='', repr=False)
    model: str = ''
    live_call_limit: int = 50
    mock_behavior: str = 'success'

    @property
    def live_configured(self):
        return bool(self.api_key and self.model and self.model.startswith('nvidia/nemotron-') and self.model.endswith(':free'))

    def health(self):
        return {'mode':self.mode,'configuration_status':'mock' if self.mode=='mock' else ('configured_live' if self.live_configured else 'missing_configuration'), 'key_configured':bool(self.api_key),'model_configured':bool(self.model),'live_verified':False,'live_call_limit':self.live_call_limit}


def load_settings(env_path=None):
    load_dotenv(dotenv_path=env_path or BACKEND_DIRECTORY/'.env', override=False)
    mode=os.getenv('MODEL_MODE','mock').strip().lower()
    if mode not in ('mock','live'):
        mode='mock'
    try:
        limit=max(0,min(50,int(os.getenv('LIVE_CALL_LIMIT','50'))))
    except ValueError:
        limit=50
    behavior=os.getenv('MOCK_BEHAVIOR','success')
    if behavior not in ('success','timeout','empty','malformed','conflict','failure'):
        behavior='success'
    return Settings(mode=mode,api_key=os.getenv('OPENROUTER_API_KEY','').strip(),model=os.getenv('OPENROUTER_MODEL','').strip(),live_call_limit=limit,mock_behavior=behavior)
