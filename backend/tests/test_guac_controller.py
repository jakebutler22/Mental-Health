import json
import httpx
import pytest
from app.config import Settings
from app.model_client import ModelController,ModelFailure

LIVE=Settings(mode='live',api_key='fictional',model='nvidia/nemotron-test:free')

def provider_value(**changes):
    value={'reflection':'The fictional exam has you feeling tense.','recommended_skill':'breathing','reason':'A steady rhythm is an optional pause.','clarification':None,'action':'offer'}
    value.update(changes)
    return value

@pytest.mark.parametrize('text,skill',[
    ('The exam is tomorrow and my shoulders are tense; I feel keyed up.','breathing'),
    ('After the roommate disagreement I keep replaying it and feel scattered.','grounding'),
    ('I am tense, but no breathing please.','grounding'),
    ('I felt tense. Actually I am not tense; I am scattered.','grounding'),
    ('I used grounding earlier, but I want breathing now.','breathing'),
    ('I prefer breathing. Actually I want grounding.','grounding')])
def test_context_and_current_choices(text,skill):
    result=ModelController(Settings()).respond(text)
    assert result.recommended_skill==skill and result.reason and result.reflection
    assert result.mode=='mock' and result.action=='offer'

@pytest.mark.parametrize('text',['Neither, thank you.','Stop please.','No breathing and no grounding.'])
def test_decline_without_persuasion(text):
    result=ModelController(Settings()).respond(text)
    assert result.action=='decline' and result.recommended_skill is None and result.clarification is None


def test_vague_one_optional_question_and_context_followup():
    controller=ModelController(Settings())
    first=controller.respond('Things feel mixed.')
    assert first.action=='clarify' and first.clarification
    second=controller.respond('Still unsure.',clarification_used=True)
    assert second.action=='offer' and second.clarification is None and second.recommended_skill is None
    followup=controller.respond('Still that way.',history=[{'role':'user','text':'The fictional exam has me tense and keyed up.'}])
    assert followup.recommended_skill=='breathing'


def test_live_negation_app_override_and_provider_header():
    seen=[]
    def handler(request):
        seen.append(request)
        return httpx.Response(200,json={'model':'nvidia/nemotron-test','choices':[{'message':{'content':json.dumps(provider_value())}}]})
    result=ModelController(LIVE,httpx.MockTransport(handler)).respond('No breathing. I want grounding.')
    assert result.recommended_skill=='grounding'
    assert seen[0].headers['X-Title']=='Guac coursework'
    assert result.configured_model_id==LIVE.model

@pytest.mark.parametrize('changes',[{'recommended_skill':'STOP'},{'reason':'Hold your breath for a minute.'},{'reflection':'This disorder can be cured.'},{'action':'clarify','clarification':'Which?','recommended_skill':'breathing'}])
def test_unsupported_or_instruction_conflicting_output(changes):
    def handler(request):
        return httpx.Response(200,json={'model':'nvidia/nemotron-test','choices':[{'message':{'content':json.dumps(provider_value(**changes))}}]})
    with pytest.raises(ModelFailure,match='instruction_conflict'):
        ModelController(LIVE,httpx.MockTransport(handler)).respond('Fictional exam')

def test_correction_retains_prohibition_until_explicitly_reversed():
    controller=ModelController(Settings())
    assert controller.respond('No breathing. Actually I feel keyed up.').recommended_skill=='grounding'
    assert controller.respond('No breathing. Actually I prefer breathing.').recommended_skill=='breathing'
    result=controller.respond('I prefer grounding before my exam.')
    assert 'prefer grounding' in result.reflection
    assert 'thoughts' not in result.reflection and 'feeling' not in result.reflection

@pytest.mark.parametrize('phrase',['This will fix your problem.','Grounding will solve it.'])
def test_promises_rejected(phrase):
    def handler(request):
        return httpx.Response(200,json={'model':'nvidia/nemotron-test','choices':[{'message':{'content':json.dumps(provider_value(reason=phrase))}}]})
    with pytest.raises(ModelFailure):ModelController(LIVE,httpx.MockTransport(handler)).respond('Fictional exam')

@pytest.mark.parametrize('text,skill',[
    ('I prefer grounding. Actually I feel tense about the fictional exam.','grounding'),
    ('I feel tense waiting at the fictional campus bus stop.','breathing'),
    ("I'd like grounding before the fictional exam.",'grounding'),
    ("I don't want to do breathing; I feel keyed up.",'grounding')])
def test_independent_review_control_boundaries(text,skill):
    result=ModelController(Settings()).respond(text)
    assert result.recommended_skill==skill and result.action=='offer'
