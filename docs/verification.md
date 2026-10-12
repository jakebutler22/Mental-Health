> HISTORICAL / PRESERVED WORK. Current scope is [Part3.1 only](../prompts/12-part31-scope-correction.md). Later milestones remain pending; this record does not authorize continuation. Earlier audience framing and observations describe earlier source, not the current everyday design.

# Verification plan and capability record

Current Guac checks: [backend checkpoint](guac-backend-checkpoints.md), [frontend checkpoint](guac-frontend-checkpoints.md), [evaluation](guac-evaluation.md), [actual browser observations](guac-browser-observations.md). The initial notes below are historical phase-specific observations; they do not describe the current implemented app.

## Historical initial inspection

No working application tests have run. Design artifact inspection is distinct from browser behavior verification.

Observed host tools: Python 3.14.7, Node v24.12.0, screencapture and qlmanage present. ffmpeg and dot not found on PATH. No project dependency imports/install checks performed. CUA inventory exposes Chrome extension and Codex in-app browser, plus native Safari/Chrome and DB Browser. Chrome has an earlier localhost app tab; it was not operated. Browser recording API is not exposed in CUA documentation; screen recording workflow/encoding remains unverified. Presence of screencapture does not prove video permission/capability. Existing SVG/HTML preview needs no app dependencies.

## Actual checks this step
Root/files/unborn main/no remotes checked; prior manifests/source/config read without secrets; docs and link verification recorded in evidence log. No installs, databases, app processes, commits or remote mutations. Mockup visual review status in evidence log.

## Timing protocol
Start at first exercise instruction painted, finish at final planned step painted; include app transition delays. Record entry/setup separately, model latency separately (never prerequisite for skills), wall duration and active guided duration. Exclude user-selected pause/support time explicitly. Six 10-second cycles = 60s animation; allow 2s orientation +3s final transition =65s expected breathing. Grounding assumes 12s per stage +2s orientation +3s final =65s. Test <=90s at intended pace; record slower self-paced use honestly, no forced exit or step completion. Use monotonic clock and paint timestamps, test start/phase/end/pause/resume/background and reduced-motion alignment.

## Balloon acceptance
Visually review low/middle/full inflation (mockup schematic only), red and alternative color, convincing latex volume/highlights/neck/knot, no artifacts, clipping or abrupt reset, minimum visible size, smooth 4s expansion/6s contraction. Labels and phase clock agree within proposed 100ms test tolerance; pause freezes both and resume continues same state. Measure frame performance on actual browser; dependency-free candidate must pass visual check before selected. Reduced motion has identical timing and useful static cue. Optional chosen color persists after restart.

## Part 3.2 observations
Known-input mocked controller round trip first; manually inspect configuration then controller then routes in separate prompts before frontend integration. After approval install only missing dependencies in new project's environments. Test input limits, loading/no-result/failure/stale response/repeated click. Browser observes breathing full run, grounding flow when ready, pause/resume/stop, persistent support on every view and model failure, keyboard access, mobile layout, reduced motion. Inspect disposable SQLite rows/relationships before/after create/update/history, refresh and full restart; preserve unrelated processes. Verify pending/interrupted status on restart and truthful unsaved UI on DB failure. No production/user data.

## Part 3.3 evaluation matrix (planned, not observed)
Record expected/observed/fixture-or-live/evidence for at least these 15 fictional cases: exam worry chat; roommate noise chat; direct breathing; direct grounding; pause/resume inhale; pause/resume exhale; stop then restart; reload mid-skill; skipped grounding sense; reduced motion; alternate color/restart; empty history then saved transcript; provider timeout; malformed model output; repeated send/stale reply. Also test DB failure, explicit danger phrase and phrase-miss support access.

Three invariants across cases: (1) support and immediate stop remain reachable regardless of model state, (2) app-owned fixed steps/timing cannot be changed by model output, (3) completed/stopped/interrupted and chat records remain correctly related after restart without duplicate writes. Mocks for repeatability and peers by default; repeat exam/roommate/failure-recovery live selections to study variation after verifying provider. Host limit <=50 live calls per peer session enforced in backend, no paid fallback. Report one observed surprise and one untested limitation only after actual evidence. Verify another person follows clean-checkout README. Record finished app and process failure→evidence→decision; explain generated clock/controller code. Recording method remains pending.

## Part 3.1 traceability
| Required item | Design/evidence |
|---|---|
| Implementable design/sketch/flow | design-pipeline.md, design-flow.svg, screen-mockup.html |
| Model role/limits/context | design-pipeline.md model section; reuse-audit.md provider distinctions |
| Expected stored data and useful history | design-pipeline.md persistent schema and contracts |
| R1–R4/D1–D6 decisions | design-pipeline.md rationale table |
| Personalization/user control | explicit color/recent skill/simple view, stop/pause/direct entry |
| Alternatives/tradeoffs/unresolved questions | rendering table, rationale, unresolved section |
| Useful README/AGENTS/design | README.md, AGENTS.md, class-working-rules.md |
| Report, AI use, curated evidence | submissions/3.1/report.md, AI-USE.md, evidence-log.md |
| Real URL/source commit/accessibility | PENDING; no remote/commit exists, hosted links not checked |

Artifact preview outcome: Codex file opening queued; in-app browser file:// preview rejected by protocol policy. No browser workaround attempted. Visual rendering review is pending; XML/link checks are not visual QA. Documentation completion does not imply submission readiness.

## Executed independent checkpoints (updated)
Backend30pytest cases, frontend15Node cases, deterministic backend evaluation20/20, production build passed. Root test-import failure corrected with pytest.ini; strict integer/coercion, late-write/offline-session loss, lost-response version conflict and deletion/in-flight boundaries drove actual regressions. See backend/frontend checkpoints and agent-review.md. No upstream deprecation warning hidden.

Actual Chrome frontend5174 works; direct backend-page navigation blocked by client, so no general browser capability failure claimed. Grounding frozen build guided rendered-frame duration68.300seconds at scripted12seconds per sense plus tool/interaction overhead. No voluntary pauses/support excluded from that run. First90.7second operator-delayed run and HMR-interrupted rerun are retained as nonpassing/intended-pace evidence. Balloon low/middle/full observed0.000578/0.490026/0.993213inflation, attached knot/neutral highlights visible. Final breathing timing and other UI checks recorded in browser-observations.md.

Live attempts were rejected by provider401; configured provider/model and successful live access remain distinct. Valid key and repeated live variation pending. Native recorder could not expose controllable recording window and browser capabilities have no video; exact fallback script exists. No recording claimed. Student review/peer run/LMS submission have not occurred.

## Current Guac verified source

7c7742b1da5be66ea6a3bae9cb5ab4d7babcb1a2: root and fresh clone54backend/20frontend/20general/26context cases plus production build pass. Real desktop/mobile/short-height/focus/support/whole-timing/persistence/failure evidence in guac-browser-observations.md. Exact clone Git clean, own database/config/dependencies, no runtime copied. Final strict publication audit addresses finalized source references separately.
