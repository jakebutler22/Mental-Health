# Part 3.3 — Integration, Evaluation and Demonstration

Repository: https://github.com/jakebutler22/Mental-Health
Submitted source commit: 8497873908b4318be2a1b8112c0401f466cd695b
[Exact verified source](https://github.com/jakebutler22/Mental-Health/tree/8497873908b4318be2a1b8112c0401f466cd695b). This is the selected coursework source checkpoint; no LMS submission has occurred.

Both skills, original realistic latex balloon, cream/sage optional-chat/direct-entry UI, SQLite conversation/session history, explicit color/reduced-motion/simple-view preferences, recent repeat/override, stopping and model-independent support are implemented. Model classifies bounded fictional context and suggests an optional skill; templates/app controllers preserve exact steps and timing. Public source; localhost runtime only.

| Requirement | Evidence | Status |
|---|---|---|
| Both chosen skills and realistic balloon | [browser observations](../../docs/browser-observations.md), [three inflation states](../../docs/evidence/balloon-states.json), [asset provenance](../../docs/balloon-asset.md) | Agent browser verified |
| Whole guided timing <=90s at intended pace | [breathing60.017s](../../docs/evidence/breathing-timing.json), [grounding68.300s](../../docs/evidence/grounding-timing.json) | Verified; no voluntary exclusions in measured runs |
| Persistence/history/preferences/restart | [before/after DB evidence](../../docs/evidence/browser-after-restart.json), [transcript](../../docs/evidence/success-transcript-after-restart.jpg), [clear/reset regression](../../docs/evidence/after-history-reset.json) | Verified |
| Choice/pause/stop/support/failure | [pause data](../../docs/evidence/pause-freeze.json), [timeout](../../docs/evidence/model-timeout.jpg), [support](../../docs/evidence/support-in-exercise.jpg), [mobile](../../docs/evidence/mobile-breathing.jpg) | Verified |
| At least15fictional scenarios +3behaviors | [expected/observed evaluation matrix](../../docs/evaluation.md), [20repeatable results](../../docs/evidence/backend-evaluation.json) | Mock/ASGI/browser coverage complete; successful live variation pending |
| Exact-source clean checkout and README | [agent clean checkout](../../docs/clean-checkout.md), [actual record](../../docs/evidence/clean-checkout.json) |30backend/15frontend/20evaluation/build/browser pass; another person's run pending |
| Useful live model contribution/repeated variation | [actual rejected live request](../../docs/evidence/live-browser-request.json), [safe health](../../docs/evidence/configured-live-health.json) | Pending valid key; OpenRouter401, no successful live result |
| Finished-app + failure-process screencasts/code explanation | [exact recording script](../../docs/recordings/recording-script.md) | Pending actual recordings; no video exists |
| AI tools/versions/roles and curated revisions | [AI use](../../AI-USE.md), [evidence log](../../docs/evidence-log.md), [agent review](../../docs/agent-review.md), [design reconciliation](../../docs/design-pipeline.md) | Recorded; student review pending |

Evaluation findings: strict Pydantic integer coercion unexpectedly accepted boolean/string/float sensory-step inputs, so strict field validation and regression checks were added. Concurrent writes could contaminate a newer session or resurrect cleared history; per-session queues, exact409reconciliation and a clear mutex fixed these review findings. Development HMR interrupted a timing run; frozen preview measured the intended sequence instead. First operator-delayed90.7s grounding retained honestly rather than called a pass.

Untested limitations: successful live-output variation, real low-end-device animation performance, native background-event pause outside debugger (document.hidden remainedfalse in automation), and multi-user/production behavior (outside scope). No clinical effectiveness established for this audience; feedback mention counts are not outcome data.

Exact remaining actions:
1. Set a valid OpenRouter key locally in ignored backend/.env; MODEL_MODE=live, OPENROUTER_MODEL=nvidia/nemotron-3.5-lightning:free. Recheck official catalog before later use. Run `PYTHONPATH=backend backend/.venv/bin/python scripts/evaluate_live.py`, observe actual browser live roundtrip/persistence, and add successful evidence/variation. No key in chat/Git or paid fallback.
2. Capture finished-app and actual failure-process recording(s), narrating the generated clock/controller section using the prepared script. Review/redact, publish actual accessible video links and update this report; no recording link is invented.
3. Student reviews the app/code/design, another person follows README from clean source with mocks by default, and student submits appropriate report.md files to the LMS. Agent authorization is not evidence these human actions occurred.

Preserved reports: [3.1](../3.1/report.md), [3.2](../3.2/report.md). 3.2 and3.3 select the same final application SHA because the autonomous run completed both skills/refinements before the source checkpoint. Recording/evidence-only follow-ups can retain it; code/run-instruction changes require a new verified source SHA.

**Independent achievable work prepared and published; not fully submission-ready while live verification, recordings and required human actions are pending.**
