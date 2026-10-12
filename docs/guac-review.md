> HISTORICAL / PRESERVED WORK. Current scope is [Part3.1 only](../prompts/12-part31-scope-correction.md). Later milestones remain pending; this record does not authorize continuation. Earlier audience framing and observations describe earlier source, not the current everyday design.

# Guac revision — independent agent review

## Requirement checkpoint

Read the full product revision in `prompts/11-guac-product-direction.md`, current README, AGENTS, design pipeline, handoff, Git changes and prior model/database implementation. Reviewer: delegated Codex agent, not student or peer. Historical Campus Pause evidence/source references remain immutable; current Guac source needs a new verified checkpoint and clean checkout because product code changes.

Required implementation boundaries:
- Guac visible name/page metadata/provider header; distinctive custom avocado mark and wordmark. Current documents reconciled; historical evidence accurately labeled.
- Conversation-first contextual reflection, one optional recommendation plus visible reason, one explicit action to accept and one easy alternative. Direct actions remain independent and late responses cannot route an active exercise.
- Explicit current preference overrides inference and previous saved actions. Negation must block the declined skill. Corrections consider the latest stated feeling/preference; neither/stop must end suggestion without persuasion.
- Vague/mixed input permits at most one optional clarification per conversational thread, never mandatory disclosure. Both direct exercises remain reachable.
- Validate structured model recommendations/reasons/reflections; unsupported skills/invented steps/diagnosis/guarantees rejected. No new provider or paid fallback.
- Persist recommendation separately from actual chosen session; no inferred clinical profile/emotion score. Additive migration preserves existing conversations/results/session relationships/preferences.
- Avocado-green default applies only when explicit color is absent; red remains selectable and existing red/blue/plum choices preserved. Clock, 4/6 six cycles, exact sensory sequence, support, pause/stop/reduced motion remain intact.

## Meaningful independent case plan

Fictional cases: tense before presentation → breathing/reason; repetitive thoughts after disagreement → grounding/reason; no breathing while tense → grounding; no grounding/prefer breathing → breathing; correcting “wound up” to “scattered” → grounding; explicit preference despite inferred feeling; neither/both declined/stop → no recommendation; vague input → one optional question; second vague turn → no repeated question; mixed feelings → optional rather than mandatory clarification; response to clarification resolves using context; “I don't feel tense” must not be treated as affirmative tension; unsupported output → safe failure; stale response → no exercise routing; timeout → independent direct choices; recommendation accepted versus alternative chosen must persist distinct values; legacy schema migration preserves previous records; saved explicit color overrides new default.

No live-model success is assumed: prior authorized provider key returned authentication failure. New independent fixtures are labeled mocks/injected transport; actual browser and live evidence are separate. Contrast will be mathematically evaluated from actual CSS tokens plus rendered checks owned by the parent.

Status: backend contract pending revised implementation; no revised behavior is claimed as observed in this initial review.

## Initial token contrast math

WCAG sRGB relative-luminance formula evaluated directly on the supplied token hex values. This is token math, not rendered-state QA. Normal text threshold is 4.5:1; large text/nontext relevant threshold is 3:1.

| Foreground/background | Ratio | Normal text |
|---|---|---|
| peel / cream | 11.16:1 | pass |
| peel / flesh | 9.15:1 | pass |
| peel / lime | 7.13:1 | pass |
| cream / leaf | 5.29:1 | pass |
| cream / peel | 11.16:1 | pass |
| pit / cream | 5.65:1 | pass |
| leaf / cream | 5.29:1 | pass |
| leaf / flesh | 4.34:1 | fail |
| cream / lime | 1.57:1 | fail |

Dark peel on cream/flesh/lime and cream on leaf meet normal-text contrast. Cream on lime fails; lime should remain a decorative surface with dark peel text. Actual hover/disabled/focus/muted-text colors must be evaluated after CSS is stable. Parent owns rendered contrast/layout/keyboard inspection.

## Revised contextual checks and CSS source review

Independent first evaluation: 23 cases, 22 passed, one failed (explicit grounding preference lost after a feeling-only correction). Expanded common-control cases: 26 cases, 22 passed, four failed; added ordinary bus-stop false decline, contraction preference “I’d like grounding,” and “don’t want to do breathing.” Actual expected/observed evidence retained in `evidence/guac-context-evaluation-first.json` and `evidence/guac-context-evaluation-revised-first.json`. Backend owner received scoped corrections; final retest pending. These are deterministic fixtures, not provider observations.

Updated existing backend evaluation meaningfully to contextual feelings/recommendations: 20 passed. Earlier Campus Pause JSON preserved as `evidence/backend-evaluation-campus-pause.json`. Live evaluation script uses repeated tense/scattered cases and requires live mode plus reflection/reason/expected skill; it was edited but **not run against the network**.

Final CSS source pairs inspected below; browser-computed/rendered checks remain parent-owned. Small labels on flesh are explicitly overridden to peel. Primary hover uses cream on peel; default primary cream on leaf. Focus pit on neighboring cream/flesh passes nontext threshold; disabled controls are inactive and exempt from normal contrast criterion, while state indication still needs visual review.

| CSS foreground/background | Contrast | Criterion |
|---|---|---|
| muted / cream | 6.08:1 | normal text passes |
| muted / card | 6.40:1 | normal text passes |
| muted / flesh | 4.98:1 | normal text passes |
| muted / settings | 5.63:1 | normal text passes |
| muted / reply | 5.66:1 | normal text passes |
| placeholder / cream | 4.92:1 | normal text passes |
| peel / hover1 | 8.41:1 | normal text passes |
| peel / hover2 | 9.19:1 | normal text passes |
| pit / cream | 5.65:1 | normal text passes |
| pit / flesh | 4.64:1 | normal text passes |

## Independent final retest

Backend owner corrected all four scoped findings. Actual rerun: **26/26 Guac cases passed, 20/20 current backend evaluation cases passed**. Script compile checks passed for Guac/backend/live evaluation scripts. No actual provider call was made; live success remains pending valid authorized access. Historical failed evaluations remain preserved.

| Case | Input/action | Expected | Observed | Mode/status |
|---|---|---|---|---|
| G01 | Fictional exam tomorrow; my shoulders feel tight and I am tense. | breathing; offer; brief reflection/reason | `{"reflection":"With the upcoming exam, you describe feeling keyed up.","recommended_skill":"breathing","reason":"A steady rhythm may suit the keyed-up feeling you described.","clarification":null,"action":"offer"}` | mock/TestClient · pass |
| G02 | Fictional roommate disagreement; I keep replaying it and my thoughts are looping. | grounding; offer; brief reflection/reason | `{"reflection":"With the roommate situation, you describe feeling pulled into several thoughts.","recommended_skill":"grounding","reason":"Noticing your surroundings may suit the scattered thoughts you described.","clarification":null,"action":"offer"}` | mock/TestClient · pass |
| G03 | No breathing. I feel keyed up before a fictional presentation. | grounding; offer; brief reflection/reason | `{"reflection":"With this campus situation, you describe feeling keyed up.","recommended_skill":"grounding","reason":"You ruled out the other exercise, so this is an optional alternative.","clarification":null,"action":"offer"}` | mock/TestClient · pass |
| G04 | No grounding. I prefer breathing before a fictional exam. | breathing; offer; brief reflection/reason | `{"reflection":"You prefer breathing for the upcoming exam.","recommended_skill":"breathing","reason":"You asked for breathing; that choice takes priority.","clarification":null,"action":"offer"}` | mock/TestClient · pass |
| G05 | I feel wound up. Actually I feel scattered about the fictional club meeting. | grounding; offer; brief reflection/reason | `{"reflection":"With the social situation, you describe feeling pulled into several thoughts.","recommended_skill":"grounding","reason":"Noticing your surroundings may suit the scattered thoughts you described.","clarification":null,"action":"offer"}` | mock/TestClient · pass |
| G06 | No breathing. Actually I feel keyed up before a fictional exam. | grounding; offer; brief reflection/reason | `{"reflection":"With the upcoming exam, you describe feeling keyed up.","recommended_skill":"grounding","reason":"You ruled out the other exercise, so this is an optional alternative.","clarification":null,"action":"offer"}` | mock/TestClient · pass |
| G07 | No breathing. Actually I prefer breathing before a fictional exam. | breathing; offer; brief reflection/reason | `{"reflection":"You prefer breathing for the upcoming exam.","recommended_skill":"breathing","reason":"You asked for breathing; that choice takes priority.","clarification":null,"action":"offer"}` | mock/TestClient · pass |
| G08 | I prefer grounding before the fictional exam. | grounding; offer; brief reflection/reason | `{"reflection":"You prefer grounding for the upcoming exam.","recommended_skill":"grounding","reason":"You asked for grounding; that choice takes priority.","clarification":null,"action":"offer"}` | mock/TestClient · pass |
| G09 | Neither, thanks. | None; decline; brief reflection/reason | `{"reflection":"Neither is okay. You can leave things here or choose something later.","recommended_skill":null,"reason":"Your choice stays yours.","clarification":null,"action":"decline"}` | mock/TestClient · pass |
| G10 | Stop. | None; decline; brief reflection/reason | `{"reflection":"Neither is okay. You can leave things here or choose something later.","recommended_skill":null,"reason":"Your choice stays yours.","clarification":null,"action":"decline"}` | mock/TestClient · pass |
| G11 | No breathing and no grounding. | None; decline; brief reflection/reason | `{"reflection":"Neither is okay. You can leave things here or choose something later.","recommended_skill":null,"reason":"Your choice stays yours.","clarification":null,"action":"decline"}` | mock/TestClient · pass |
| G12 | A fictional campus afternoon feels unclear. | None; clarify; brief reflection/reason | `{"reflection":"There may be a few things mixed together around this campus situation.","recommended_skill":null,"reason":"You can choose either exercise without explaining more.","clarification":"Would a steady rhythm or noticing your surroundings suit this moment?","action":"clarify"}` | mock/TestClient · pass |
| G13 | I feel tense and scattered before the fictional exam. | None; clarify; brief reflection/reason | `{"reflection":"There may be a few things mixed together around the upcoming exam.","recommended_skill":null,"reason":"You can choose either exercise without explaining more.","clarification":"Would a steady rhythm or noticing your surroundings suit this moment?","action":"clarify"}` | mock/TestClient · pass |
| G14 | I do not feel tense about this fictional situation. | None; clarify; brief reflection/reason | `{"reflection":"There may be a few things mixed together around this campus situation.","recommended_skill":null,"reason":"You can choose either exercise without explaining more.","clarification":"Would a steady rhythm or noticing your surroundings suit this moment?","action":"clarify"}` | mock/TestClient · pass |
| G15 | I prefer breathing although my fictional roommate situation leaves me scattered. | breathing; offer; brief reflection/reason | `{"reflection":"With the roommate situation, you describe feeling pulled into several thoughts.","recommended_skill":"breathing","reason":"You asked for breathing; that choice takes priority.","clarification":null,"action":"offer"}` | mock/TestClient · pass |
| G16 | I prefer grounding. Actually I feel tense about the fictional exam. | grounding; offer; brief reflection/reason | `{"reflection":"With the upcoming exam, you describe feeling keyed up.","recommended_skill":"grounding","reason":"You asked for grounding; that choice takes priority.","clarification":null,"action":"offer"}` | mock/TestClient · pass |
| G24 | I feel tense waiting at the fictional campus bus stop. | breathing; offer; brief reflection/reason | `{"reflection":"With this campus situation, you describe feeling keyed up.","recommended_skill":"breathing","reason":"A steady rhythm may suit the keyed-up feeling you described.","clarification":null,"action":"offer"}` | mock/TestClient · pass |
| G25 | I'd like grounding before the fictional exam. | grounding; offer; brief reflection/reason | `{"reflection":"You prefer grounding for the upcoming exam.","recommended_skill":"grounding","reason":"You asked for grounding; that choice takes priority.","clarification":null,"action":"offer"}` | mock/TestClient · pass |
| G26 | I don't want to do breathing; I feel keyed up about the fictional exam. | grounding; offer; brief reflection/reason | `{"reflection":"With the upcoming exam, you describe feeling keyed up.","recommended_skill":"grounding","reason":"You ruled out the other exercise, so this is an optional alternative.","clarification":null,"action":"offer"}` | mock/TestClient · pass |
| G17 | Second vague input after optional clarification | No second clarification; both choices available | `{"reflection":"There may be a few things mixed together around this campus situation.","recommended_skill":null,"reason":"You can choose either exercise without explaining more.","clarification":null,"action":"offer"}` | mock/TestClient · pass |
| G18 | Short followup on tense prior input | Relevant bounded conversational context retained | `{"reflection":"With this campus situation, you describe feeling keyed up.","recommended_skill":"breathing","reason":"A steady rhythm may suit the keyed-up feeling you described.","clarification":null,"action":"offer"}` | mock/TestClient · pass |
| G19 | Preference-only input; no stated feeling | Reflect preference without inventing scattered feelings | `{"reflection":"You prefer grounding for the upcoming exam.","recommended_skill":"grounding","reason":"You asked for grounding; that choice takes priority.","clarification":null,"action":"offer"}` | mock/TestClient · pass |
| G20 | Unsupported skill, promise and breath hold in structured model output | Reject unsafe/unsupported output before UI | `{"rejected_count":3,"error_codes":["instruction_conflict","instruction_conflict","instruction_conflict"]}` | mock/TestClient · pass |
| G21 | Vague turn/restart/vague turn/correction/choose alternative/replay | At most one persisted optional question; recommendation distinct from chosen skill | `{"clarification_after_restart":null,"recommended_skill":"grounding","chosen_skill":"breathing","duplicate_session_count":1,"foreign_key_violations":0}` | mock/TestClient · pass |
| G22 | Injected provider timeout then direct exercise; invalid failed-result reference | Direct skill independent; failed recommendation cannot be snapshotted | `{"chat_status":"failed","code":"provider_timeout","direct_session_status":201,"failed_recommendation_link_status":422}` | mock/TestClient · pass |
| G23 | Additive migration from fictional pre-Guac schema | Preserve legacy records and explicit red; new columns nullable | `{"legacy_completed_record_preserved":true,"new_recommendation_reference":null,"explicit_color_preserved":"red","foreign_key_violations":0}` | mock/TestClient · pass |

Machine-readable evidence: [Guac evaluation](evidence/guac-context-evaluation.json). This establishes recommendation/choice records, correction and negation boundaries, one optional clarification across restart, no generated unsupported instructions, migration and durable explicit red preference. It does not establish live semantic accuracy or all possible natural-language wording. Conservative lexical choice/guard handling can still miss indirect preferences or false-match unusual language; document that limitation rather than presenting a general emotion detector.
