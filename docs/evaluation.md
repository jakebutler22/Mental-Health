# Fictional scenario evaluation

October 12, 2026. Actual repeatable backend checks: **20 passed, 0 failed**. Run `backend/.venv/bin/python scripts/evaluate_backend.py` from the project root. Temporary databases are created beneath this root and removed afterward. No actual provider network call occurs; injected `httpx.MockTransport` responses are explicitly fixture evidence even when exercising the live transport branch.

Machine-readable expected/observed results: [backend evaluation](evidence/backend-evaluation.json). Tests evaluate API behavior and persisted SQLite rows; they do not establish browser observations, human response time, visual fidelity, or successful live model access.

| Case | Fictional input/action | Expected | Mode | Observed | Evidence/status |
|---|---|---|---|---|---|
| E01 | Fictional exam tomorrow | Context category affects safe acknowledgement; both skills remain choices | TestClient/mock | `{"category":"exam","mode":"mock","message_count":2,"choices":["breathing","grounding"]}` | [JSON](evidence/backend-evaluation.json) · pass |
| E02 | Fictional roommate noise | Context category affects safe acknowledgement; both skills remain choices | TestClient/mock | `{"category":"roommate","mode":"mock","message_count":2,"choices":["breathing","grounding"]}` | [JSON](evidence/backend-evaluation.json) · pass |
| E03 | Fictional assignment deadline | Context category affects safe acknowledgement; both skills remain choices | TestClient/mock | `{"category":"workload","mode":"mock","message_count":2,"choices":["breathing","grounding"]}` | [JSON](evidence/backend-evaluation.json) · pass |
| E04 | Fictional club meeting | Context category affects safe acknowledgement; both skills remain choices | TestClient/mock | `{"category":"social","mode":"mock","message_count":2,"choices":["breathing","grounding"]}` | [JSON](evidence/backend-evaluation.json) · pass |
| E05 | Fictional campus afternoon | Context category affects safe acknowledgement; both skills remain choices | TestClient/mock | `{"category":"general","mode":"mock","message_count":2,"choices":["breathing","grounding"]}` | [JSON](evidence/backend-evaluation.json) · pass |
| E06 | Fictional exam; injected timeout | Failed user message preserved; no invented assistant | TestClient/mock | `{"status":"failed","error_code":"provider_timeout","assistant_messages":0}` | [JSON](evidence/backend-evaluation.json) · pass |
| E07 | Fictional exam; injected empty | Failed user message preserved; no invented assistant | TestClient/mock | `{"status":"failed","error_code":"empty_response","assistant_messages":0}` | [JSON](evidence/backend-evaluation.json) · pass |
| E08 | Fictional exam; injected malformed | Failed user message preserved; no invented assistant | TestClient/mock | `{"status":"failed","error_code":"malformed_response","assistant_messages":0}` | [JSON](evidence/backend-evaluation.json) · pass |
| E09 | Fictional exam; injected conflict | Failed user message preserved; no invented assistant | TestClient/mock | `{"status":"failed","error_code":"instruction_conflict","assistant_messages":0}` | [JSON](evidence/backend-evaluation.json) · pass |
| E10 | Fictional exam; injected failure | Failed user message preserved; no invented assistant | TestClient/mock | `{"status":"failed","error_code":"provider_unavailable","assistant_messages":0}` | [JSON](evidence/backend-evaluation.json) · pass |
| E11 | Live mode with absent key/model | Honest missing-configuration failure | TestClient/mock | `{"status":"failed","error_code":"missing_configuration","actual_provider_attempts":0}` | [JSON](evidence/backend-evaluation.json) · pass |
| E12 | Repeat same request ID; then alter its text | Idempotent replay; conflicting text rejected | TestClient/mock | `{"same_saved_response":true,"message_count":2,"changed_input_status":409}` | [JSON](evidence/backend-evaluation.json) · pass |
| E13 | Direct breathing, save pause, restart API | No model dependency; record remains interrupted and related | TestClient/mock | `{"conversation_id":null,"duplicate_records":1,"restart_state":"interrupted","saved_elapsed_ms":2500,"foreign_key_violations":0}` | [JSON](evidence/backend-evaluation.json) · pass |
| E14 | Five API grounding steps with first sense skipped | Completion retains skip; no claim of full unskipped sequence | TestClient/mock | `{"state":"completed","step":5,"skipped_steps":[0],"synthetic_active_ms":60000,"duration_measured_in_browser":false}` | [JSON](evidence/backend-evaluation.json) · pass |
| E15 | Choose blue/simple/reduced, restart, clear preferences | Explicit preferences durable and resettable | TestClient/mock | `{"color_survived_restart":"blue","simple_view":true,"reduced_motion":true,"reset_verified":true}` | [JSON](evidence/backend-evaluation.json) · pass |
| E16 | Empty, maximum, over-maximum fictional messages | Reject empty and >500; accept 500 | TestClient/mock | `{"empty_status":422,"501_characters_status":422,"500_characters_status":200}` | [JSON](evidence/backend-evaluation.json) · pass |
| E17 | 50 failed injected provider attempts, then next request | Cap counts failed attempts and returns labeled mock | httpx.MockTransport; no live access | `{"mock_transport_attempts":50,"actual_network_attempts":0,"failed_attempts_counted":50,"next_mode":"mock","limit_reached":true}` | [JSON](evidence/backend-evaluation.json) · pass |
| E18 | Injected model tries to add breath-hold instructions | Extra fields rejected before UI result | httpx.MockTransport; no live access | `{"error_code":"instruction_conflict","generated_instructions_displayed":false,"actual_network_attempts":0}` | [JSON](evidence/backend-evaluation.json) · pass |
| E19 | Inspect mock health configuration | Honest safe health without secret values | TestClient/mock | `{"mode":"mock","live_verified":false,"live_attempts":0,"secret_value_fields":0}` | [JSON](evidence/backend-evaluation.json) · pass |
| E20 | Clear linked fictional conversation and session history | Cascade removes history; deliberate preference retained | TestClient/mock | `{"deleted_table_counts":{"conversations":0,"messages":0,"model_requests":0,"sessions":0},"preference_preserved":"plum","foreign_key_violations":0}` | [JSON](evidence/backend-evaluation.json) · pass |

## Browser-dependent scenario checks

These checks require actual interface observation. Parent-agent observations communicated during this review are identified as such; they are not independently witnessed by this reviewer. Add the final browser/database log for source-backed timing and state evidence.

| Scenario | Expected | Current evidence/status |
|---|---|---|
| Direct breathing without typing/model wait | Exercise starts immediately | Parent reports full browser run; [completion capture](evidence/breathing-complete.jpg); exact browser log pending |
| Whole breathing duration | Six 4/6 cycles, whole guided sequence ≤90s | Parent reports elapsed 60000 ms and conservative observed whole ≤64.838s; measurement log pending |
| Grounding 5/4/3/2/1 privately | Fixed one-step sequence; intended 12s/sense | [First step](evidence/grounding-first.jpg); whole browser sequence evidence pending |
| Pause/resume inhale and exhale | Frozen clock/balloon; resumes without jumps | Helper tests pass; actual browser case pending |
| Leaving and restarting | Interrupted/stopped distinguishable; saved history retained | API restart E13 passes; final browser evidence pending |
| Color, recent shortcut and override | Explicit preference persists; both choices remain available | API E15 passes; final browser color/shortcut evidence pending |
| Simpler/reduced motion | User choice; stable visual with identical timing | API E15 plus source review; browser evidence pending |
| Chat loading/failure/stale/repeated click | Explicit status; support and direct skills usable | API E06–E12 pass; current frontend integration/retest pending |
| Fictional danger phrase | App-owned support offer; no implied monitoring | Frontend policy browser check pending |

## Three cross-case behaviors

| Behavior | Verified evidence | Remaining scope |
|---|---|---|
| A. Support stays visible and usable during loading/failure | Static component/source review; exercise/support paths independent of API | Actual browser loading/failure and keyboard check pending |
| B. Choice/pause/stop/change direction without forced conversation or penalty | Direct null-conversation session E13; paused restart; helper clock tests | Final browser direction-change, queue-loss and stop checks pending |
| C. App-owned steps/timing/persistence survive model output | E10/E18 reject instruction conflicts; E13/E14/E20 inspect lifecycle/relationships; clock tests preserve 4/6 and 5/4/3/2/1 | Final App integration/persistence race tests and browser observation pending |

## Live variation and limits

Actual live attempts are separate from these fixtures. Parent reports two application live calls failed and an isolated provider diagnostic returned authentication failure (401); no successful live model contribution or repeated live-case variation is established. See [live-controller evidence](evidence/live-controller.json). Required small repeated live sample remains **pending valid authorized OpenRouter access**. Peer testing defaults to mocks. E17 confirms all 50 failed injected attempts count toward the per-backend-process maximum and subsequent request is labeled mock; restarting the process begins a new host session.

## Finding, revised approach and untested limitation

Surprising confirmed finding: Pydantic originally coerced `True`, numeric strings and whole floats in skipped-step lists before route checks could reject them. The controller boundary changed to strict integer items; the backend regression tests now cover those malformed inputs. This is a validation finding, not an observed clinical result.

The model design was revised from free-form acknowledgement to a two-field allowlisted category/skill selection; app-owned contextual acknowledgements prevent generated exercise instructions from entering the UI. E18 verifies extra instruction fields are rejected. Real provider correctness and variation remain untested successfully because authorized credentials failed authentication. This prototype has no clinical validation, distress detector, multi-user access protection or emergency monitoring; the evaluation uses fictional data only.

Reviewer: delegated Codex agent. Student review/peer testing and student authorship of any recording are not claimed.

## Actual browser coverage added by primary agent

All observations are from Chrome/real localhost frontend+FastAPI and disposable SQLite, not injected page state. See [browser record](browser-observations.md) and linked screenshots/JSON.

| Scenario/action | Expected | Mode | Observed/status | Evidence |
|---|---|---|---|---|
| Fictional exam chat | Relevant bounded ack/choices, records | Browser/mock | Waiting then succeeded user+assistant, both choices; pass | [evidence](evidence/chat-mock-roundtrip.jpg) |
| Direct breathing without text | Starts immediately | Browser | Sixcycles/60000ms; pass | [evidence](evidence/breathing-timing.json) |
| Choose grounding after chat | User-owned choice | Browser/mock | Exact5/4/3/2/1; stop/skip linked record; pass | [evidence](evidence/grounding-stopped.jpg) |
| Complete breathing | Guided<=90s, no forced exit | Browser |60.017s, stays until return; pass | [evidence](evidence/breathing-final-complete.jpg) |
| Grounding at12s/sense | Guided<=90s | Browser |68.300s including overhead; pass | [evidence](evidence/grounding-timing.json) |
| Pause/resume both phases | Clock/image freeze | Browser |1582.5ms inhale/4998.9ms exhale identical after wait; pass | [evidence](evidence/pause-freeze.json) |
| Leave active skill | Interrupted persisted | Browser/DB | interrupted4998ms, old rows survive; pass | [evidence](evidence/browser-after-restart.json) |
| Blue/reduced preference | Explicit choice remembered | Browser/DB |Blue/reduced returned after full restart; pass | [evidence](evidence/reduced-motion.jpg) |
| History/transcript restart | Rows/relations unchanged | Browser/DB |All8 prior sessions, earlier messages/prefs preserved; pass | [evidence](evidence/success-transcript-after-restart.jpg) |
| Recent repeat/override | No automatic route | Browser |Repeatbreathing then choosegrounding; pass | [evidence](browser-observations.md) |
| Simpler/reduced view | User controls, identical timing | Browser |Full/simpler toggles, constant image with advancing clock; pass | [evidence](evidence/simpler-view.jpg) |
| Mock timeout | User failed/no assistant, other controls | Browser/mock |provider_timeout visible, support usable; pass | [evidence](evidence/model-timeout.jpg) |
| Malformed/extra instructions | Reject, no changed steps | ASGI mock/Node |Deterministic regression passes; browser variant not repeated | [evidence](evidence/backend-evaluation.json) |
| Fictional danger phrase | Offer support, no gating | Browser/mock |Offer visible even timeout; pass | [evidence](evidence/crisis-offer.jpg) |
| Missing/live/mock status | Accurate labels | Browser |Missing/configured labels and live401failure; status behavior passes, live success pending | [evidence](evidence/live-authentication-failure.jpg) |
| Clear/reset/new request | No staleID/resurrection | Browser/DB |Empty history, prefs preserved thenreset; freshchat/session/FK[]; pass | [evidence](evidence/after-history-reset.json) |
| Mobile390×844 | Support/stop visible/no overflow | Browser |Recorded bounds visible; pass | [evidence](evidence/mobile-breathing.jpg) |
| Native background | Visibility hook freezes | Browser debugger |document.hidden stayedfalse; unverified | [evidence](browser-observations.md) |

Invariants A/B/C have actual browser evidence for ordinary/direct/chat/pause/stop/failure/support scenarios plus deterministic backend boundary cases. The full matrix exceeds15 distinct fictional scenarios. Mock failure/limit tests do not prove live variation. Surprise: strict integer coercion and HMR disruption required changes to validation and verification process. Untested limitations: successful live output variation and real low-end-device performance/native background events.
