from fastapi.testclient import TestClient
from app.config import Settings,load_settings
from app.main import create_app

def test_health_modes_do_not_leak(tmp_path):
    cases=[(Settings(),'mock'),(Settings(mode='live'),'missing_configuration'),(Settings(mode='live',api_key='fictional-secret',model='nvidia/nemotron-test:free'),'configured_live')]
    for index,(settings,status) in enumerate(cases):
        with TestClient(create_app(tmp_path/f'{index}.sqlite3',settings)) as client:
            response=client.get('/api/health')
            assert response.status_code==200
            assert response.json()['configuration_status']==status
            assert response.json()['live_verified'] is False
            assert 'fictional-secret' not in response.text
            assert settings.model not in response.text or not settings.model
            assert 'fictional-secret' not in repr(settings)

def test_explicit_dotenv_process_precedence_limit(tmp_path,monkeypatch):
    for key in ('MODEL_MODE','OPENROUTER_API_KEY','OPENROUTER_MODEL','LIVE_CALL_LIMIT','MOCK_BEHAVIOR'):
        monkeypatch.delenv(key,raising=False)
    env=tmp_path/'.env'
    env.write_text('MODEL_MODE=live\nOPENROUTER_API_KEY=fictional-env\nOPENROUTER_MODEL=nvidia/nemotron-test:free\nLIVE_CALL_LIMIT=200\n')
    monkeypatch.setenv('OPENROUTER_API_KEY','fictional-process')
    settings=load_settings(env)
    assert settings.api_key=='fictional-process' and settings.live_configured
    assert settings.live_call_limit==50
    monkeypatch.setenv('LIVE_CALL_LIMIT','-1')
    assert load_settings(env).live_call_limit==0
    monkeypatch.setenv('OPENROUTER_MODEL','paid-model')
    assert not load_settings(env).live_configured
