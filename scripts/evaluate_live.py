"""Repeat a small fictional live selection; read only this app's environment/config."""
import json
import time
from dataclasses import asdict, replace
from pathlib import Path
from app.config import load_settings
from app.model_client import ModelController, ModelFailure

settings = load_settings()
if settings.mode != 'live' or not settings.live_configured:
    raise SystemExit('Set MODEL_MODE=live and valid backend-local OpenRouter key/model. No secret is printed.')
controller = ModelController(replace(settings, live_call_limit=min(6, settings.live_call_limit)))
results = []
for repetition in range(2):
    for text in ('Fictional student: I feel tense and keyed up before an exam tomorrow.', 'Fictional student: My thoughts keep looping about roommate noise; I feel scattered.'):
        started = time.monotonic()
        try:
            observed = asdict(controller.respond(text))
            expected = 'breathing' if 'keyed up' in text else 'grounding'
            matches = observed['mode'] == 'live' and observed['recommended_skill'] == expected and bool(observed['reflection']) and bool(observed['reason'])
            result = {'status': 'passed' if matches else 'unexpected', 'expected_skill': expected, 'result': observed}
        except ModelFailure as error:
            result = {'status': 'failed', 'code': error.code}
        result.update(input=text, repetition=repetition + 1, elapsed_seconds=round(time.monotonic()-started, 3), attempts=controller.attempts)
        results.append(result)
        print(json.dumps(result))
output = Path(__file__).resolve().parents[1] / 'docs/evidence/live-evaluation.json'
output.write_text(json.dumps({'provider': 'OpenRouter', 'configured_model': settings.model, 'results': results}, indent=2)+'\n')
if any(r['status'] != 'passed' or r['result']['mode'] != 'live' for r in results):
    raise SystemExit('Live evaluation incomplete; inspect safe result codes. Mock fallback is not a live pass.')
