> HISTORICAL EVIDENCE. Current [Part3.1-only scope](../prompts/12-part31-scope-correction.md) supersedes earlier audience and automatic continuation. Preserve these observations tied to earlier source; do not expand later stages.

# Backend execution checkpoints

## Phase 3 CHECK
Python 3.14.7 available; backend contains no implementation or installed environment. Prior SQLite helper inspected read-only: reuse row factory, foreign keys, and per-request connection pattern; no travel schema/data copied.

TAKE ACTION: required packages installed into this project's backend/.venv with:
```
python3 -m venv backend/.venv
backend/.venv/bin/python -m pip install fastapi uvicorn pytest httpx python-dotenv
```
No global installation. SQLite is Python standard library. Configuration/controller/route phases remain separate.

## Phase 3 VERIFY
`cd backend && .venv/bin/python -m pytest -q`: 5 passed. Real disposable SQLite rows inspected before creation, after linked session/pause, after restart and deletion. PRAGMA foreign_keys=1; invalid relationship raises IntegrityError. Restart preserves preferences/transcript and marks active/paused sessions/pending requests interrupted. Boundary checks cover incomplete breathing, wrong cycle count, paused elapsed freeze, stale versions, terminal resume, unknown skills, missing references, allowlisted colors, grounding step order and honest skip storage. No model route/configuration added. Current FastAPI143/Starlette1.7 TestClient produces a deprecation warning for httpx; tests still pass. No extra dependency introduced merely to suppress it.

API foundation contracts are implemented in `backend/app/main.py` and validation in `schemas.py`; storage is `database.py`. List endpoints return `{items:[]}`, bounded limit1..100/offset. Preferences add explicit `reduced_motion` boolean. Grounding step0..5 and skipped indices0..4; completed with skips remains stored with skips and must be labeled honestly by view. Session start request_id is idempotent, payload reuse conflicts409. PATCH requires exact version, increments atomically; active time never decreases. Breathing completed requires >=60000ms and cycles=6. Grounding steps advance one at a time. Support remains frontend-owned and independent of API.

## Phase 4 CHECK / TAKE ACTION
Foundation passed before configuration. Own `backend/app/config.py` explicitly loads own `backend/.env` via path derived from source, preserving process environment precedence. `.env.example` blank key/model; no credentials written. MODEL_MODE mock default or live; OPENROUTER_API_KEY and OPENROUTER_MODEL backend-only. LIVE_CALL_LIMIT clamps 0..50 (attempt cap), optional host-only MOCK_BEHAVIOR reserved for deterministic demos. No user route controls these. Invalid mode safely defaults mock. Live requires explicit NVIDIA Nemotron :free identifier; missing or unsupported setting is missing_configuration. Health reports booleans/status only and live_verified=false; no upstream call.

Reproduce startup: `MODEL_MODE=mock backend/.venv/bin/python -m uvicorn app.main:app --app-dir backend --host 127.0.0.1 --port 8001`. Configure an independently supplied key in own ignored backend/.env or process environment, set MODEL_MODE=live and OPENROUTER_MODEL=nvidia/nemotron-3.5-lightning:free, then restart. Parent performs actual browser health inspection before controller phase.

## Phase 4 VERIFY
Backend pytest: 7 passed (including foundation). Config tests use fictional secrets only, verify redaction, safe mock/missing/configured statuses and live_verified=false; explicit dotenv/process precedence and cap50 tested. No controller/route added. Actual browser health checkpoint remains parent-owned.

Actual revised approach: parent ran root test command and found ModuleNotFoundError app during collection; parent adds root pytest.ini with pythonpath=backend. Backend-directory command passed; root command verification belongs to parent after its fix.

## Phase 5 CHECK / TAKE ACTION / VERIFY
Parent inspected actual health HTTP response; browser navigation blocked by client URL control, recorded separately. Independent controller implemented without HTTP route/frontend integration in `model_client.py`. Official current catalog checked by parent: prior free Nemotron supports max_tokens/temperature/reasoning but does not advertise response_format, so use JSON-only system context and strict local enum validation.

Controller input: trimmed fictional text1..500; last6 role-valid messages capped500 each/3000 total; latest3 allowed terminal skill/state metadata. Finite20-second httpx timeout; one attempt, no retries or paid/model fallback. Output stable dataclass with app-owned acknowledgement, contextual category, optional suggested skill, both choices, mock/live label and configured/returned model identifiers. Provider-returned identity accepts only requested identifier with optional :free suffix removal. No arbitrary generated prose enters UI: model categorizes exam/roommate/workload/social/general and suggests one allowed skill. Tradeoff: narrower conversational richness, stronger protection against invented instructions/diagnosis. Enum selection remains model contribution responsive to scenario and history; app controls actual steps and user decision.

Host session cap counts every attempted provider call before network, including failures. Thread lock protects process-wide controller count. At cap<=50 subsequent requests become explicitly labeled mocks. Backend process restart begins a new host session; browser navigation/history deletion never resets cap. Missing live configuration fails safely. Mock behavior is host configuration only, not user request payload.

Root pytest: 18 passed. Mock transport verifies request context/input variation, identity, ordinary response, empty/malformed/conflicting output, timeout/network/provider failure, and failed-attempt cap fallback. These are deterministic simulated-provider tests, NOT live-model results. Live controller check remains parent-owned using privately injected runtime credentials.

## Phase 5 live result (parent observation)
Two real controller calls failed provider_unavailable. Parent diagnostic established HTTP401 from OpenRouter using authorized prior runtime credential; no successful live-model contribution observed. `docs/evidence/live-controller.json` records sanitized outcome. Controller now maps401/403 to provider_authentication and429 to provider_rate_limit, without upstream body or key. Exact remaining live action: replace invalid/expired authorized credential with a valid OpenRouter key in own ignored backend configuration or process environment, restart and rerun small fictional cases. Mock-backed independent work continues.

## Phase 6 CHECK / TAKE ACTION / VERIFY
After controller inspection, route added in `backend/app/routes.py` and registered by app factory. Constructor accepts injected controller for repeatable verification. POST `/api/conversations/{id}/messages` takes exactly request_id/text1..500, trimmed; rejects missing conversation404/empty422. Response stable `{request_id,conversation_id,status,mode,error_code,messages,result}` for mocked/live success and known failure. Success result contains acknowledgement/category/suggested_skill/choices/mode/configured_model_id/returned_model_id/limit_reached. Failed result=null; user message remains failed, no invented assistant. Known provider failures return HTTP200 with explicit failed status (UI must inspect status); validation and conflict retain422/409. Duplicate finished request returns persisted identical response; failed retry requires a fresh explicit request_id.

SQLite transaction BEGIN IMMEDIATE claims pending request and user message before releasing lock for provider I/O. Duplicate pending request or another pending request in same conversation returns409. Different-conversation context cannot leak. Structured sanitized application result stored in new result_json column using preserving additive migration, enabling stable idempotent results after restart. Raw provider payload/credentials never stored. Strict skipped_steps schema now rejects bool/string/float before normalization.

Root pytest:29 passed. New tests inspect actual saved request/message records for success/failures; atomic concurrent pending claim yields one call/two messages; repeated request remains identical; different scenario/category affects result and history isolation is verified. Timeout/empty/malformed/instruction-conflict/failure simulations persist one user/no assistant, invalid request checks pass. These tests use injected/mock transports and are not actual browser observations. Parent owns actual endpoint + SQLite checkpoint before chat integration.

Phase6 robustness revision: source review identified history deletion while provider call is pending. Before assistant finalization, new BEGIN IMMEDIATE checks retained request/conversation. If deleted, returns410 history_cleared without resurrecting data. Slow-controller concurrent deletion test inspects all four tables empty after completion. Root pytest30 passed. No new dependency.
