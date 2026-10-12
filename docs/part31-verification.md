# Part 3.1 design verification

Confirmed root `/Users/jakebutler/Documents/ChatGPT/Mental Health`; initial Git clean on main304102c03ee7496dfe324ee5177dcc83ec8c681d. Reviewed README, AGENTS, design, assignment summary, class rules and current handoff before changing anything. Feature branch codex/guac-part31. Current user instruction supersedes all automatic later-stage execution.

| Part 3.1 requirement | Prepared evidence | Verification/status |
|---|---|---|
| Implementable design + reviewable sketch/flow | [specification](design-pipeline.md), [mockup](screen-mockup.html), [flow](design-flow.svg) | Actual static Chrome visual review, SVG XML parse and links checked |
| Guac everyday audience, avocado identity/efficient interaction | Original mark, six tokens, warm typography, mobile direct choices before extended examples | [desktop](evidence/part31-guac-desktop.jpg), [mobile](evidence/part31-guac-mobile.jpg) inspected |
| Proposed recommendation conversation | Work presentation, difficult conversation, busy day, negation/preference/decline boundaries | Design table and static illustrated response; not a live model result |
| Planned model role and limits | One bounded structured request, current preference enforcement, app-owned timing/support, finite timeout/cap, no paid fallback | Source-backed reuse pattern; provider successful access remains a later question |
| Data/history/personalization | Five entities, links/statuses, recommended versus chosen, explicit color/simple/reduced, optional recent repeat | Proposed schema and file map; no new database or migration executed |
| Stop/user control/independent support | Direct access, optional question, deliberate selection, pause/stop/leave, persistent support | Proposed flow and static state panels; no current timed behavior claim |
| R1–R4 and D1–D6 decisions | All10findings with mention counts, decisions, alternatives/tradeoffs | Manually reconciled to supplied assignment summary; feedback is not clinical outcome data |
| Balloon/exercise timing retained | Realistic photographic candidate with green default/red option,4/6×6, static reduced-motion alternative, exact5/4/3/2/1 | Images loaded; low/mid/full mockup inspected. About65s/≤90s are targets, not revision measurements |
| Alternatives/unresolved questions | Renderer cost/fidelity, model semantics/access, support region, privacy, physical keyboard/device/human timing | Explicit design questions; not blockers for Part 3.1 |
| Useful README/AGENTS/handoff/evidence/AI use | Current scope and stop rules, numbered scope source, archive notices | Old all-phase instructions clearly superseded |
| Real repository, design commit and report links | [report](../submissions/3.1/report.md) | Design aa2993dd6e7362e561ba9f308f57fb42dd02a4a1 publicly verified; finalized report links recorded in a separate documentation checkpoint |

Actual static review: Chrome via CUA on localhost 5175; desktop six proposed state panels, original mark/balloon material; narrow 390×844 has scrollWidth 390, loaded 3/3 balloon assets, sample controls 44–64px; keyboard Tab shows 3px pit focus. Flow rendered and reviewed; one header overflow was shortened, and direct-entry path rerouted around failure annotation for clarity. No timed application exercise, model call, database CRUD or video was performed for this milestone. Static labels and illustration are not functional tests. PNG/JPEG captures are evidence of visual review, not human user testing.

Existing later-stage code: Vue/FastAPI/SQLite app, clock, controllers, persistence and tests already existed before scope correction. Preserved behavior; only education-specific visible labels, example placeholder, default title/context and model identity copy changed to everyday/general terms. No feature, dependency, schema, timing or exercise-controller expansion. Existing tests rerun as a copy-regression check: initial53/54 backend pass with old provider header assertion; expected header updated to Guac prototype and54/54 pass.20 frontend tests/build pass. This does not complete or reopen Parts 3.2/3.3 or establish live interpretation.

Historical evidence/reports retain original source references under archive notices. Earlier design afe33f9f605c9e536fc3b7ebdfa39f3c525862d7 and implementation7c7742b remain preserved. New Part 3.1 source checkpoint must be recorded separately; report-only commit can reference that verified design without self-referential hashes.

Reviewer: primary Codex agent; no student review, peer run or LMS submission claimed. Stop after verified public Part 3.1 checkpoint; await user request for Parts 3.2/3.3. Valid key/live variation, physical mobile keyboard/device checks and recordings are later-stage questions, not required completion gates for the current design.

Published design source: [aa2993dd6e7362e561ba9f308f57fb42dd02a4a1](https://github.com/jakebutler22/Mental-Health/tree/aa2993dd6e7362e561ba9f308f57fb42dd02a4a1). [Exact publication evidence](evidence/part31-design-checkpoint.json) confirms public access and byte-for-byte reviewed text artifacts. Parts 3.2/3.3 remain pending.
