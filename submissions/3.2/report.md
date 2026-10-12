# Part 3.2 — Working Application and Safety

Repository: https://github.com/jakebutler22/Mental-Health
Submitted source commit: **PENDING checkpoint**.

Both selected skills are implemented in Vue/FastAPI/SQLite. Breathing runs six four-second inhale/six-second exhale cycles; grounding preserves five seen, four felt, three heard, two smelled, one tasted. Short optional chat and direct entry coexist. Stop/pause, persistent independent support, saved conversation/session history and explicit preferences work in actual localhost browser observations.

Actual guided instruction-frame measurements: **breathing60.017seconds** (active60000ms/sixcycles), **grounding68.300seconds** (scripted12seconds per sense plus interaction overhead; persisted68273ms/step5). No voluntary pause/support exclusions in these measured runs; entry separately recorded. Slower90.7second operator-delayed grounding and HMR interruption are retained honestly. No forced timeout or navigation.

Evidence: [browser record and screenshots](../../docs/browser-observations.md), [breathing timing](../../docs/evidence/breathing-timing.json), [grounding timing](../../docs/evidence/grounding-timing.json), [route roundtrip](../../docs/evidence/route-roundtrip.json), [SQLite restart inspection](../../docs/evidence/browser-after-restart.json), [model timeout](../../docs/evidence/model-timeout.jpg), [support](../../docs/evidence/support-in-exercise.jpg), [balloon states](../../docs/evidence/balloon-states.json), [verification](../../docs/verification.md), [AI use](../../AI-USE.md).

Agent review and actual checks:30backend tests,15frontend tests,20repeatable evaluation cases, production build. Model makes a constrained contextual selection; safe app templates own acknowledgement and steps. Mock contribution observed through two different fictional inputs and real browser requests. Actual live request was rejected: [authentication failure](../../docs/evidence/live-browser-request.json). A valid own backend-local OpenRouter key is required to demonstrate successful live contribution; no successful model identifier/variation invented.

Coursework prototype only, fictional scenarios; no diagnosis, therapy, clinical effectiveness or monitoring. Source published; runtime remains localhost. Student review and successful live contribution remain pending; this is not a claim of completed submission.
