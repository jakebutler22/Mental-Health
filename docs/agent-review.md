# Agent review checkpoints

## Design and publication boundary — October 12, 2026

Reviewer: delegated Codex agent. This is agent review, not student or peer testing. Read the full supplied `Assignment_3_Codex_Prompts.txt`, README, current handoff, assignment source, working rules, design pipeline, verification plan, reuse audit, Part 3.1 report, AI disclosure, ignore rules, flow SVG source, and HTML mockup source. Inspected actual Git status: untracked design package on unborn main. No application behavior or rendered visual appearance was tested in this review.

### CHECK

The design specifies every substantive Part 3.1 item: an implementable flow/sketch, relevant model context and limits, persistent conversation/session/history schema, all R1–R4/D1–D6 decisions, optional personalization, user control, alternatives and open questions. Source provenance appropriately identifies the supplied summary and does not claim independent screenshot or Canvas inspection. The college audience and balloon appearance are labeled project choices; research counts are not efficacy evidence.

The HTML mockup includes chat/direct entry, three balloon states, grounding, history, stop/pause, and persistent support. Its source candidly labels the balloon schematic and all controls static. Visual appearance still requires actual rendered inspection. The flow source has all principal paths and explicitly says arrows denote available choices rather than automatic routing.

### TAKE ACTION — review findings

- The new execution directive supersedes old documentation-only authorization and approval pauses in README, AGENTS, class rules and handoff. Update those records before implementation; do not infer personal student approval or testing.
- Actual repository URL, source commit and accessible hosted artifact links must replace pending Part 3.1 fields after verified publication.
- Keep API configuration, controller, route and frontend integration as distinct recorded inspection checkpoints even during continuous execution.
- Test model output validation semantically as well as structurally. A valid JSON acknowledgement can still contain invented instructions or diagnostic claims.
- Test repeated request IDs concurrently, retries after failure, stale responses, session version conflicts, hidden-tab pause and DB failure before claiming the documented contracts.
- Count every actual live attempt, including retries, toward the host's maximum of 50; report mock fallback honestly.
- Measure whole guided duration separately from the 60-second breathing animation. Grounding remains user-paced and assumptions must be disclosed.
- Verify original balloon asset licensing/provenance and actual low/mid/full/color appearance before claiming hyperrealism.

### VERIFY

Ignore rules cover backend-local configuration, `.venv`, node_modules, build outputs, runtime SQLite and sidecars while permitting blank `.env.example`. No secret values were read or printed by this reviewer. No database or prior-project files were copied. Prior configuration presence and successful live provider use remain distinct facts. Public source publication is authorized; localhost runtime deployment is outside scope.

Design review passes as an implementable, candid plan. Submission readiness remains pending actual visual review, source/repository fields and hosted evidence. Student review remains unperformed. Later implementation/evaluation review will be recorded below, based on actual code and checks.

## Initial publication audit — October 12, 2026

Created `scripts/audit_publication.py` using Python standard library only. It examines the actual Git index publication set for forbidden configuration/runtime/dependency paths, likely credential signatures (file/line only), broken relative Markdown links, repository fields and locally resolvable exact source commits. It does not inspect ignored databases or print candidate secret values. Stage new files before using it to audit a proposed commit; untracked files are outside its scope. Pattern scanning is a limited review aid, not proof that all possible secrets are absent.

Actual check: `python3 scripts/audit_publication.py` passed against 20 index files, 14 Markdown files and Part 3.1 source `afe33f9f605c9e536fc3b7ebdfa39f3c525862d7`; zero findings. The first invocation used unavailable `python`; corrected to the observed `python3` executable. No Git mutation performed by this reviewer. Parent reported public repository creation; this review independently confirms the report URL and local source commit existence, not remote visibility.

## Foundation implementation review — October 12, 2026

Read Vue App, all exercise/support/history components, exercise clock/API helpers, CSS, FastAPI routes, SQLite schema/initialization, request schemas and current tests. This was code review plus helper checks, not browser observation. The parent reports both health browser surfaces blocked by `ERR_BLOCKED_BY_CLIENT`; this reviewer made no browser attempt or workaround.

Actual check: `node --test frontend/tests/*.test.js` passed all five current helper tests. Direct Pydantic probe with `PYTHONPATH=backend backend/.venv/bin/python` confirmed `skipped_steps` normalizes booleans, numeric strings and whole floats to integers; route-level type checks therefore cannot reject their original malformed types. Initial probe import and missing-required-field mistakes were corrected before recording the actual result.

Actionable findings relayed to parent for scoped correction:
1. A PATCH awaited in `flushSaves` can resolve after a new session starts and overwrite the new `saved` record or shift its queue, unless generation is rechecked after await and queues are isolated. Starting another session also discards old unsaved operations.
2. Lost PATCH response after successful server commit produces a permanent stale-version retry failure without GET/reconciliation.
3. Active progress persisted only on pause/stop/step at the reviewed snapshot, so restart loses active elapsed duration. Periodic snapshots and truthful checkpoint precision are needed; abrupt reload must remain interrupted rather than complete.
4. `start` may replace an active session without recording interruption if another enabled direct-entry action is selected after the first create finishes.
5. Support dialog initially lacked focus transfer/trap/Escape/restoration despite aria-modal. Parent reports a subsequent fix; recheck current code before treating this finding as unresolved.
6. Strict skipped-step integers must reject pre-coercion malformed types.

Clock phase endpoints, pause exclusion, six-cycle clamp and fixed 5/4/3/2/1 array are supported by helper tests. Reduced-motion rendering uses a stable inflation parameter with unchanged clock, based on code inspection. Actual appearance, measured whole sequence, responsive support placement, DOM keyboard behavior, queue integration and persistence under abrupt reload remain separate browser/integration evidence requirements. Parent reports generation guards, support focus fixes and 5-second checkpoints added after the reviewed snapshot; retest is required before closure.

Follow-up source inspection confirms support initial focus, Tab boundary wrapping, Escape close and focus restoration are now implemented. It also confirms five-second active elapsed snapshots and a post-await success generation guard. These findings are closed at source-review level only; actual DOM keyboard/persistence behavior remains unobserved. The failure catch still writes shared error state after stale requests, and successful preference writes clear the session error. A pending or failed exercise save therefore needs its own error/pending status rather than a shared preference error flag. Lost-response reconciliation and old-session unsaved-queue preservation remain open at this inspection.

## Controller and repeatable evaluation review — October 12, 2026

Actual checks now pass: 29 backend pytest cases; 12 frontend Node helper/controller cases; 20 standalone repeatable API/database/model-fixture evaluation cases. See `docs/evidence/backend-evaluation.json`. Starlette emitted a TestClient/httpx deprecation warning; tests passed with current dependencies. No live provider success or browser observation was performed by this reviewer.

Retested fixes: strict skipped-step integer tests pass; session persistence now isolates each record/queue, retains offline old-session writes, and reconciles an accepted PATCH whose response was lost by rereading on 409. Three targeted frontend tests pass for those exact failures. Preference error and session pending/error state are now separate. Five-second checkpoint precision and in-memory unsaved lifetime are disclosed in the interface. Support focus handling remains source-reviewed. Model returns only allowlisted category/skill fields; app-owned acknowledgement prevents generated exercise text from display. MockTransport evaluation proves 50 failed attempted calls count against cap and next result is labeled mock.

Remaining concrete review finding relayed to parent: clearing history deletes conversations while the mounted chat controller and App retain that conversation ID, so the next chat/session can target a deleted record. Reset active chat linkage after clear and cancel/settle pending saves so explicit deletion cannot be resurrected by queued retries. Retest browser return-home chat/direct entry after deletion.

## Final frozen-source review — October 12, 2026

Read the final session persistence controller, App/history/chat clear/reset wiring, related regression tests and publication auditor. Parent reports the frozen source passed 30 backend tests, 14 frontend tests, production build and 20 evaluation cases; no unchanged tests were rerun by this reviewer. Actual source confirms fractional cycle handling uses the same floored saved-millisecond value for cycles, strict step inputs are enforced, old-session queues are independent, lost accepted responses are reconciled, and confirmed history clear remounts chat/reset linkage after waiting for pending records. The publication auditor skips URI links such as `tel:` and has an explicitly optional pre-source pending-report flag; **final submission audit must run without `--allow-pending-reports`**.

Parent reports actual browser grounding first-to-final painted duration 68.300 seconds, with a slower first run and development HMR interruption retained as honest evidence. Parent also reports final red balloon low/mid/full captures and visible support rectangle inside viewport. These are parent observations, not independent browser tests by this reviewer; final evidence log/JSON should carry exact artifacts and values.

One final concurrency concern relayed: `discardAll` waits existing queues then removes all current records, while history clear presently leaves repeat/navigation usable. A newly created record during the wait can be unintentionally removed. Prevent new exercise actions while confirmed clearing or remove only the snapshotted records and define UI behavior; a targeted regression is appropriate if source changes. Other previously reported persistence and stale-chat findings are closed by source review/regression evidence. Successful actual live-model variation and required recording capability remain separate completion items, not implied by mocked passing tests.

## Final resolved review checkpoint
Primary agent delegated final history-clear/new-session concurrency finding for scoped fix: clear mutex blocks create/update, shared in-flight promise and snapshot removal; App/History clearing controls block conflicting starts/navigation while support stays available. Regression included in15passing frontend cases. Root30backend cases,20evaluation and production build passed. Actual browser confirmed clear/reset/fresh chat without stale404; separate clock/render measurements retained because that correction did not change timing code. No student review or successful live variation claimed. Publication privacy/link audit passes with pending report fields explicitly permitted only before source SHA exists; final audit must use strict default.
