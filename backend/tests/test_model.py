import json
import httpx
import pytest
from app.config import Settings
from app.model_client import ModelController,ModelFailure,bounded_context,validate_selection

LIVE=Settings(mode='live',api_key='fictional-secret',model='nvidia/nemotron-test:free')

def reply(content='{"category":"exam","suggested_skill":"breathing"}',model='nvidia/nemotron-test',status=200):
    return httpx.Response(status,json={'model':model,'choices':[{'message':{'content':content}}]})

def test_known_input_and_bounded_context():
    captured=[]
    def handler(request):
        captured.append(json.loads(request.content))
        assert request.headers['Authorization']=='Bearer fictional-secret'
        return reply()
    controller=ModelController(LIVE,httpx.MockTransport(handler))
    result=controller.respond('Fictional exam tomorrow',[{'role':'user','text':'x'*800}]*10,[{'skill':'grounding','state':'completed'}])
    assert result.mode=='live' and result.category=='exam' and result.returned_model_id=='nvidia/nemotron-test'
    assert controller.live_verified and controller.attempts==1
    messages=captured[0]['messages']
    assert len(messages)==8 and sum(len(m['content']) for m in messages[1:-1])==3000
    assert messages[-1]['content']=='Fictional exam tomorrow'
    assert 'grounding' in messages[0]['content'] and 'response_format' not in captured[0]
    controller.respond('Fictional roommate noise')
    assert captured[-1]['messages'][-1]['content']=='Fictional roommate noise'

@pytest.mark.parametrize('response,code',[(reply(''),'empty_response'),(reply('bad'),'malformed_response'),(reply('{"category":"exam","suggested_skill":"STOP"}'),'instruction_conflict'),(reply('{"category":"exam","suggested_skill":"breathing","steps":"hold"}'),'instruction_conflict'),(reply(model='other'),'model_identity_mismatch'),(reply(status=429),'provider_rate_limit'),(reply(status=401),'provider_authentication')])
def test_failed_response_sanitized(response,code):
    controller=ModelController(LIVE,httpx.MockTransport(lambda request:response))
    with pytest.raises(ModelFailure) as exc:controller.respond('Fictional exam')
    assert str(exc.value)==code and not controller.live_verified and controller.attempts==1

@pytest.mark.parametrize('exception,code',[(httpx.ReadTimeout('private upstream details'),'provider_timeout'),(httpx.ConnectError('private upstream details'),'provider_unavailable')])
def test_transport_failure(exception,code):
    def handler(request):raise exception
    with pytest.raises(ModelFailure) as exc:ModelController(LIVE,httpx.MockTransport(handler)).respond('Fictional exam')
    assert str(exc.value)==code

def test_cap_counts_failed_attempts_and_returns_mock():
    calls=[]
    def handler(request):calls.append(1);return reply(status=503)
    controller=ModelController(Settings(mode='live',api_key='fictional',model=LIVE.model,live_call_limit=1),httpx.MockTransport(handler))
    with pytest.raises(ModelFailure):controller.respond('Fictional exam')
    result=controller.respond('Fictional roommate')
    assert len(calls)==1 and controller.attempts==1 and result.mode=='mock' and result.limit_reached
    assert result.suggested_skill=='grounding'

def test_mock_missing_and_input():
    assert ModelController(Settings()).respond('Fictional exam').mode=='mock'
    with pytest.raises(ModelFailure,match='missing_configuration'):ModelController(Settings(mode='live')).respond('Fictional exam')
    for text in ('',' '*5,'x'*501):
        with pytest.raises(ModelFailure,match='invalid_input'):ModelController(Settings()).respond(text)
    for text in ('[]','{"category":"diagnosis","suggested_skill":"breathing"}','{"category":[],"suggested_skill":"breathing"}'):
        with pytest.raises(ModelFailure):validate_selection(text)
