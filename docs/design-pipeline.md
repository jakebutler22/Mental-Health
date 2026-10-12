# Campus Pause design pipeline

Source authority: [supplied assignment summary](assignment-source.md), [class rules](class-working-rules.md). These differ from selected design choices below. Audience and visual palette are choices, not clinical effectiveness claims. Research counts are feedback mentions from 15 patients, 13 clinicians, 15 prototype sessions and 150 participant-task combinations; no raw dataset is available or required.

Review [flow diagram](design-flow.svg) and [screen mockup](screen-mockup.html). Mockup is static design evidence, not an implemented application. Balloon states are schematic candidates, not proof of hyperrealism.

## Journey and application authority
Open with a short fixed invitation: “Want a brief pause? You can chat, or choose an exercise.” Optional fictional input receives a brief contextual acknowledgement and two skill choices. Direct breathing/grounding buttons are always available; model failure leaves them usable. Choosing a skill opens its first instruction; no compulsory onboarding. Home, history and support remain reachable. Stop exits immediately with neutral “Stopped” state, no penalty, score or completion pressure. Pause freezes exercise; resume continues. Returning home never automatically restarts. Reload marks active sessions interrupted and offers a fresh start rather than resuming silently.

Breathing: six cycles, inhale four seconds, exhale six; no holds or forceful instructions. Balloon stays visible at minimum, changes smoothly, labels stay clear. An optional color picker before or during exercise remembers only explicit choice; red default. Reduced motion replaces size changes with a stable balloon and timed phase text/progress. No mandatory end survey.

Grounding: one instruction at a time: five seen, four felt, three heard, two smelled, one tasted. User identifies things privately; no text required. Next/skip advances with the fixed sequence, pause and stop always available. At intended pace allow 12 seconds per stage (60 total), 2 seconds for initial orientation and at most 3 seconds final transition (65 seconds). No enforced timeout; users can take longer. The timer does not auto-advance sensory steps. A skip is recorded, never mislabeled completed in full.

Support is a persistent, clearly labeled entry on every screen and failure state, opens an app-owned panel directly, accessible by keyboard. No live numbers are asserted in this design; region-specific resource verification is an implementation dependency. Static resources must be bundled independently of model/backend availability. Panel explains no monitoring and coursework role. Proposed crisis-input handling: bounded phrase matching for explicit danger phrases opens an offer of support, never blocks skills or auto-routes. False positives/negatives, indirect language and location uncertainty mean this is not reliable distress detection or risk assessment. Model/classifier never gates support. Verify actual copy/resources before runtime use.

## MVC and planned file map (files below do not exist yet)
| Responsibility | Planned file | Input / output |
|---|---|---|
| View shell/navigation | frontend/src/App.vue | selected view -> chat/skill/history/support; choices stay user-owned |
| Views | components/ChatPanel.vue, BreathingExercise.vue, BreathingBalloon.vue, GroundingExercise.vue, HistoryPanel.vue, SupportPanel.vue under frontend/src/ | typed props/events -> accessible UI; fixed skill copy |
| Frontend exercise controller | frontend/src/controllers/exerciseClock.js | monotonic time, pause/resume -> phase, elapsed, inflation, cycle; shared frozen clock |
| Frontend request controller | frontend/src/lib/api.js | typed request/id -> validated result/loading/error; abort and ignore stale responses |
| HTTP boundary | backend/app/main.py; backend/app/routes.py | validated JSON -> status/JSON, sanitized errors |
| Conversation controller | backend/app/controllers/conversations.py | message/request_id/conversation_id -> persisted bounded response plus choices |
| Session controller | backend/app/controllers/sessions.py | validated transition/elapsed/version -> session state; optimistic conflict checking |
| History controller | backend/app/controllers/history.py | pagination/conversation ID -> transcripts and session summaries |
| Model service/config | backend/app/model_client.py; config.py | bounded fixed context -> validated acknowledgement/allowed choice IDs; safe health status |
| Data model/repository | backend/app/database.py; schemas.py; repositories.py | parameterized CRUD -> committed rows with enforced relationships |

All paths in component row are beneath frontend/src/. MVC domain model is distinct from the conversational model. App controller owns timing, state, choice, exits and safety.

## Controller contracts and boundary rules
Proposed routes:
- GET /api/health -> service/db readiness and key/model configured booleans; no values or upstream call.
- POST /api/conversations -> new ID; GET /api/conversations?limit=20&cursor=... -> bounded history.
- POST /api/conversations/{id}/messages {request_id,text} -> message IDs, short acknowledgement, choices [breathing,grounding], mode mock/live, request status. Trimmed 1–500 characters; reject empty/501; one active call, duplicate request_id returns saved result. Persist user message and request state before provider call; persist valid assistant reply after. Failed requests remain visible and can be retried explicitly. No invented assistant answer.
- GET /api/conversations/{id} -> ordered messages and linked sessions; missing ID 404.
- POST /api/sessions {request_id,skill,conversation_id?} -> active session; direct entry permits null conversation; allow only selected two skills.
- PATCH /api/sessions/{id} {version,state,active_elapsed_ms,step,cycles,skipped_steps} -> updated row. Allowed active↔paused, active/paused→stopped/completed; terminal state cannot resume (409). Nonnegative elapsed; malformed phase/step/cycle rejects 422. Repeated clicks share ID; stale version 409 then reread.
- GET /api/sessions -> paginated summary. PATCH /api/preferences {balloon_color?,simple_view?} -> allowlisted values. No automatic journey routing.

Ordinary example: direct breathing creates null-conversation session, pause at inhale 2s preserves same size on resume, stop at 25s saves stopped, reload shows history. Boundaries: 500-character chat accepted/501 rejected; unknown skill rejected; sixth exhale ends planned instruction but does not force navigation; paused time excluded; repeated start creates one record. DB unavailable exposes unsaved status, buffers only pending operation in memory for explicit retry, never falsely claims saved. Skills and bundled support continue; reload can lose unsaved state, documented limitation.

## Proposed persistent data
SQLite own ignored backend/data/campus-pause.sqlite3; no travel data/credential copy or CSV seed. Tables:
- conversations(id PK, created_at, updated_at, fictional_title).
- messages(id PK, conversation_id FK, role user/assistant, text, created_at, request_id, status); stable ordered IDs, unique request/role pairing prevents duplicate messages.
- model_requests(request_id PK, conversation_id FK, status pending/succeeded/failed/interrupted, mode mock/live, configured_model_id, sanitized_error_code, created_at); no keys/raw provider payloads.
- sessions(id PK, conversation_id nullable FK, skill enum, state enum, started_at, ended_at, active_elapsed_ms, step, cycles, skipped_steps JSON, version). Separate accumulated active time and wall timestamps.
- preferences(singleton PK, explicit_balloon_color nullable, simple_view bool). Recent skill derived from sessions, presented as shortcut without auto-start.
Foreign keys enforced; transaction per mutation; fixed queries, no generated SQL. Startup migration preserves records and marks unresolved pending requests/active sessions interrupted. Preference and session writes are durable after restart. History shows date, skill, active duration, completed/stopped/interrupted/skipped status and linked transcript; transcript shows mock/live and failed-request labels. No clinical score or inferred distress. Local single-user prototype, no authentication; use fictional data only.

## Model contribution and limits
One bounded call per explicit message. Fixed relevant context includes supplied two skill definitions, coursework boundary, last six conversation messages (bounded total), and optional recent skill metadata; no unrelated database rows. Model helps acknowledge a fictional exam/roommate scenario and explain the difference between choices, staying concise. It cannot invent therapeutic advice, alter steps, trigger exercise, diagnose, score distress or remove support. Prefer validated structured acknowledgement plus allowlisted choices; reject invalid shape/length and any attempted new skill instructions; use safe app-owned failure text. Exact semantic safety validator still needs design/testing; structured output alone cannot guarantee harmless text. No tool calling, SQL generation, embeddings or speech needed. Mock mode default for peers; host-enforced live session counter stops at 50 and returns to mocks. Verify model availability separately from config presence.

## Research-linked decisions and tradeoffs
| Evidence | Choice and alternative/tradeoff |
|---|---|
| R1 38 | 60s breathing/65s grounding intended; longer 90s breathing allowed by source but six cycles minimizes attention burden. Response time is assumed, not enforced. |
| R2 30 | Direct persistent support panel vs multistep settings; consumes small fixed space. |
| R3 39 | Stop and pause always visible, no penalty vs completion incentives; completion rate is not success metric. |
| R4 68 | Chat or either exercise, recent shortcut only vs automatic recommended routing; adds small choice burden. |
| D1 54 | User-selected simpler view hides chat/history detail while retaining controls/support vs inferred distress detection; no validated detector exists. |
| D2 100 | One sensory instruction or breathing phase at a time vs full checklist; requires navigation but reduces scanning. |
| D3 148 | Private identification and Next/skip; no mandatory typing or model wait vs written journaling; less detailed records. |
| D4 31 | Persistent support including exercise/pause/error vs home-only access; must avoid overlap at narrow widths. |
| D5 49 | Explicit remembered color, optional recent-skill shortcut vs profile questionnaire; local preferences are modest, resettable and never prescribe. |
| D6 97 | Cream/sage, plain neutral language, restrained motion vs gamification; balloon red remains intentional focal pacing cue, isolated within quiet surroundings. Color change and reduced motion mitigate visual demands. |

## Balloon feasibility gate
| Approach | Fidelity/color/timing/performance/dependency tradeoff |
|---|---|
| High-resolution original latex asset + controlled deformation | Promising texture/highlights/knot; hue mask must preserve neutral highlights and realistic shading. Shared-clock transform is cheap, but stretched texture/fixed highlights may fail realism. Need original/authorized asset, low/mid/full visual review. No new runtime package initially. |
| SVG gradients/mesh or CSS | Easy recolor, deterministic clock, small payload/no package. Current mockup uses SVG as schematic; appearance is illustrative, insufficient proof of hyperrealism. |
| Canvas/WebGL shaded geometry | Volume/light can respond convincingly; material tuning, mobile GPU cost, code and possible libraries increase scope. Consider only after simpler candidate fails and installation review. |
| Prerendered frame sequence | Convincing photographed/rendered states; memory/download cost, recolor complexity and frame stepping. More assets and reduced flexibility. |

Tentative first experiment: original high-resolution asset with modest continuous shape deformation and separate knot, low/mid/full states. No renderer selected as final. Inflation parameter comes from same monotonic clock as labels: inhale p=t/4, exhale p=1-t/6, smoothly interpolated shape with endpoint continuity; min size >0. Shared active elapsed freezes on pause and resumes without jumps. Measure phase accuracy on actual browser, not setInterval tick counts. Hidden tab pauses rather than fast-forwarding. Reduced motion uses same duration with static image/labels. Review red plus one alternative color at three sizes, highlight/material continuity, no neck detachment or clipping, and intended screen sizes before implementation approval.

## Unresolved decisions and milestones
Review title/copy, balloon candidate, grounding response-time assumptions, history details, simple-view prominence and support resource region. Selected provider configuration is verified only in prior file; exact class slug/current live access and new config are pending. Installed dependency compatibility, available ports and semantic output guard remain unverified.

3.1: this implementable design and artifacts, model/data/MVC, rationale, alternatives and questions. 3.2: at least one complete skill, useful live model contribution, SQLite persistence, timing and actual browser/DB failure/exit evidence. Plan breathing first then grounding. 3.3: both skills, refined history/preferences, clean-checkout run, 15 fictional scenarios plus three invariants, deterministic mocks and small repeated live selection, surprising result/untested limitation, finished demo plus failure-process recording and generated-code explanation. See verification plan.
