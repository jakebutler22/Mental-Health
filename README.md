# Campus Pause

Campus Pause is an individual Assignment 3 localhost coursework prototype for **fictional college-student scenarios**. Vue presents a short optional conversation, paced breathing and sensory grounding. FastAPI owns validated APIs and SQLite stores conversations, requests, exercise sessions and preferences. It does not diagnose, provide therapy, imply monitoring, or establish clinical effectiveness. Do not deploy it as mental health support.

The application is implemented. Mock-backed tests and evidence are in [evaluation](docs/evaluation.md); successful live model verification and human review remain separate requirements. Milestone reports: [3.1](submissions/3.1/report.md), [3.2](submissions/3.2/report.md), [3.3](submissions/3.3/report.md). Public source: [Mental-Health](https://github.com/jakebutler22/Mental-Health). Publishing source does not deploy the application.

## Run locally

Verified development runtime: Python **3.14.7**, Node **24.12.0**, npm **11.6.2**. A different runtime has not been independently verified. Use two terminals from the repository root; quote paths containing spaces.

```bash
cd "/Users/jakebutler/Documents/ChatGPT/Mental Health"
python3 -m venv backend/.venv
backend/.venv/bin/python -m pip install -r backend/requirements.txt
cp backend/.env.example backend/.env
backend/.venv/bin/python -m uvicorn app.main:app --app-dir backend --host 127.0.0.1 --port 8001
```

For a clone in another folder, replace the `cd` path with that checkout. First backend startup creates its own ignored `backend/data/campus-pause.sqlite3`; no prior database, credentials or seed files are needed. Later starts preserve history/preferences and mark unfinished sessions/requests interrupted.

Second terminal, same repository root:

```bash
npm ci --prefix frontend
npm --prefix frontend run dev
```

Open **http://127.0.0.1:5174/**. Vite proxies `/api` to **http://127.0.0.1:8001**; ports are strict to avoid silently testing another app. The earlier travel project uses 8000/5173 and is independently runnable. No runtime imports, symlinks or dependencies on that project exist. API documentation: http://127.0.0.1:8001/docs. Health: `/api/health` returns status/configured booleans, mode and attempted-call count, never secret values. If direct API browser navigation is blocked, inspect health through an HTTP client; this is distinct from UI testing.

## Model configuration

Default `MODEL_MODE=mock` needs no credential; replies are explicitly labeled simulated. For live verification set only in ignored **backend/.env** (or the backend process environment):

```dotenv
MODEL_MODE=live
OPENROUTER_API_KEY=<enter your valid key locally>
OPENROUTER_MODEL=nvidia/nemotron-3.5-lightning:free
LIVE_CALL_LIMIT=50
MOCK_BEHAVIOR=success
```

Never place keys in frontend configuration, a `VITE_` variable, Git, prompts or recordings. Restart the backend after changing configuration. Process settings take precedence over `.env`. [Official catalog check](docs/provider-catalog.json) confirms the prior model's zero prompt/completion price on October 12, 2026; verify availability before a later live run. No paid/model fallback. Missing configuration is labeled unavailable; a configured key is not evidence of provider success. The prior authorized key returned HTTP401 in this run; see [live evidence](docs/evidence/live-controller.json).

Model contribution is intentionally bounded: it classifies fictional context and suggests one optional skill from two allowed choices. Safe application templates supply the acknowledgement; the model cannot emit new exercise instructions. Last six messages (at most3000characters), current input(max500), and last three linked session summaries provide context. One provider attempt per explicit request, finite20second transport timeout. The host cap counts attempted live calls including failures; after at most50 it switches to clearly labeled mocks. This cap is per backend process/session; restart starts a new host session. Peers use mock mode by default. No provider retries occur silently.

Host-only mock behaviors `success`, `timeout`, `empty`, `malformed`, `conflict`, `failure` permit repeatable failure demonstrations. Set `MOCK_BEHAVIOR=timeout` with mock mode and restart for the failure recording, then restore success.

## Use and data rules

Either exercise starts directly without typing or waiting for a model. Breathing is six cycles of4seconds in/6seconds out, no holds; red latex balloon is a pacing cue. Color is chosen outside exercise and remembered explicitly. Reduced motion keeps the image still with identical phase timing. Grounding follows5seen/4felt/3heard/2smelled/1tasted, one sense per screen. Private identification needs no text; optional notes remain local to a step and never reach database/model. At intended12seconds per sense the guided sequence is about60seconds; slower use is allowed without forced exit.

Pause freezes active time and balloon; support/hidden tabs pause automatically. Stop retains stopped state, navigation retains interrupted state. Every5seconds checkpoints elapsed time: reload/crash may lose up to5seconds since last checkpoint. Pending unsaved operations are retained for this visit with explicit retry; reload can lose unsaved operations. The UI distinguishes saved state from pending/failed writes. History shows dates, active duration, outcome, skipped senses and linked transcripts, not a clinical score. Clearing history requires confirmation, deletes conversations/requests/messages/sessions, and preserves preferences; reset preferences is separate. This is one local user's history with no authentication; use fictional data only.

Support stays visible and is bundled independently of the backend/model. [Verified US resources and limits](docs/support-sources.md). Phrase matching can offer support for explicit fictional danger text, but is not risk assessment and can miss indirect statements. No contacts, monitoring or automatic routing occur.

## Checks and organization

```bash
backend/.venv/bin/python -m pytest -q
npm --prefix frontend test
npm --prefix frontend run build
PYTHONPATH=backend backend/.venv/bin/python scripts/evaluate_backend.py
python3 scripts/audit_publication.py
```

The publication audit examines Git's staged/tracked snapshot; stage intentional files before using it. Backend and evaluation tests use disposable databases and mocked provider transport; they do not count as live calls or browser observations. An upstream Starlette/TestClient httpx deprecation warning is known and does not fail tests.

For a stable browser measurement use `npm --prefix frontend run build` then `npm --prefix frontend run preview`, rather than an editing/HMR session. See [verification](docs/verification.md), [browser evidence](docs/browser-observations.md), [recording instructions](docs/recordings/recording-script.md) and [clean-checkout evidence](docs/clean-checkout.md) for actual outcomes and pending checks.

- `frontend/src/`: Vue views, deterministic clock, session queues and chat request guards; original balloon asset in `frontend/public/`.
- `backend/app/`: FastAPI boundary, own SQLite schema, configuration and constrained model controller; `backend/tests/` disposable checks.
- `docs/`: [assignment provenance](docs/assignment-source.md), [working rules](docs/class-working-rules.md), [design](docs/design-pipeline.md), [review](docs/agent-review.md), [evidence log](docs/evidence-log.md).
- `prompts/`: preserved autonomous instructions and numbered phase sources.
- `handoffs/current.md`: current Git/checkpoint/unfinished state; `AI-USE.md`: actual tools and roles.

Milestones: October15,22,29,2026, all11:59PM Eastern. Student review, peer clean-checkout run and LMS submission are never claimed as agent actions.
