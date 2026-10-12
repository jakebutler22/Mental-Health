# Part 3.3 — Guac integration, evaluation and demonstration

Repository: https://github.com/jakebutler22/Mental-Health
Submitted source commit: 7c7742b1da5be66ea6a3bae9cb5ab4d7babcb1a2
[Exact independently verified source](https://github.com/jakebutler22/Mental-Health/tree/7c7742b1da5be66ea6a3bae9cb5ab4d7babcb1a2). Source publication completed; no LMS submission occurred.

Guac implements both selected skills with Vue, FastAPI and SQLite on localhost. The avocado visual system and original mark frame an optional contextual conversation plus direct entry. One bounded model request returns reflection, recommendation and reason; application validation enforces current choice, negation, correction and a persistent one-question limit. Recommended skill/reason and actual chosen skill are saved separately. Mocks are labeled; live success remains pending valid access. Historical milestone sources are preserved.

| Requirement | Evidence | Status |
|---|---|---|
| Bespoke Guac design and both skills | [design](../../docs/design-pipeline.md), [desktop](../../docs/evidence/guac-desktop-home.jpg), [browser observations](../../docs/guac-browser-observations.md) | Agent inspected |
| Whole guided duration ≤90 seconds at intended pace | [breathing60.018s](../../docs/evidence/guac-breathing-timing.json), [grounding80.134s](../../docs/evidence/guac-grounding-timing.json) | Verified, including transitions and operator overhead |
| Realistic green balloon; red option, reduced motion, pause/stop | [green](../../docs/evidence/guac-balloon-green.jpg), [red/reduced](../../docs/evidence/guac-mobile-red-reduced.jpg), [pause](../../docs/evidence/guac-pause-inhale.json) | Browser inspected; clock unchanged |
| Contextual recommendation and deliberate alternative | [recommendation](../../docs/evidence/guac-breathing-recommendation.jpg), [history](../../docs/evidence/guac-history.jpg), [independent evaluation](../../docs/guac-review.md) | Mock/browser verified; live pending |
| SQLite provenance, historical data and preferences after restart | [DB after restart](../../docs/evidence/guac-db-after-restart.json) | Prior IDs preserved, FK check clear |
| Independent support and failure recovery | [timeout](../../docs/evidence/guac-timeout.jpg), [keyboard support return](../../docs/evidence/guac-mobile-support-paused.jpg) | Actual browser verified |
| At least 15 fictional cases and three cross-case behaviors | [26context cases](../../docs/evidence/guac-context-evaluation.json), [20general cases](../../docs/evidence/backend-evaluation.json), [evaluation](../../docs/guac-evaluation.md) | All pass; mock/API/Node distinguished from browser/live |
| Mobile, focus, touch, contrast | [mobile](../../docs/evidence/guac-mobile-home.jpg), [short viewport](../../docs/evidence/guac-short-viewport-input.jpg), [computed colors](../../docs/evidence/guac-rendered-styles.json) | Desktop viewport checks pass; physical software keyboard pending |
| Exact-source fresh checkout and README | [clean checkout](../../docs/guac-clean-checkout.md) |54backend/20frontend/20general/26context cases, build and actual browser smoke pass; another person’s run pending |
| Live repeated interpretation | [prior actual401](../../docs/evidence/live-browser-request.json), [current catalog](../../docs/evidence/guac-provider-catalog.json) | Valid own key required; no successful live result |
| Demo/process recording and generated-code explanation | [exact updated script](../../docs/recordings/recording-script.md) | No video exists; recording control unavailable |
| AI use, curated failures and review | [AI use](../../AI-USE.md), [evidence log](../../docs/evidence-log.md), [agent review](../../docs/guac-review.md) | Recorded; student review separate and pending |

Actual findings: feeling-only corrections initially erased an explicit preference/prohibition; common contraction/negation wording and ordinary “bus stop” exposed other boundary errors. Independent first expected/observed failures are preserved, fixes are scoped and all 26 cases pass. Preference-only reflection no longer invents a feeling. No new rendering dependency was needed: the original photographic latex asset retains highlights/knot through clock-driven deformation and recoloring. Grounding 80.134s includes a corrected operator selector delay, rather than excluding it from the result.

Remaining actions: enter a valid OpenRouter key locally in ignored backend/.env and run the revised small repeated live evaluation plus real browser round trip; capture and review actual demo/process recordings using the prepared script; test a physical mobile keyboard; student reviews source/design/app, another person follows the clean checkout README using mocks, and student submits the report files. No keys in chat/Git, paid fallback, clinical validation, monitoring or public runtime deployment. Source publication does not complete these requirements or LMS submission.

Preserved milestone reports: [3.1](../3.1/report.md) and [3.2](../3.2/report.md), retaining their original real source checkpoints. Part 3.3 selects the later Guac source. Documentation-only updates retain the verified source SHA; source/run-instruction changes require a new verification.
