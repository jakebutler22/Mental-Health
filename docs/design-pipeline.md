# Guac design pipeline — current product direction

Authority: [assignment summary](assignment-source.md), [working rules](class-working-rules.md), [Guac revision](../prompts/11-guac-product-direction.md). The college audience and recommendation rules are product choices, not established clinical effectiveness. [Original design archive](design-campus-pause-archive.md), initial diagrams/mockup, screenshots and source checkpoints retain their historical Campus Pause/red-default identity; they have not been retroactively relabeled.

## Journey

Guac opens with a generous conversation surface: “What’s taking up space?” Optional fictional input → short reflection + recommended skill + concise reason, normally one bounded model request. A recommendation panel has one clear primary “Begin …” action and an easy alternative. Nothing auto-starts; the person deliberately chooses. Direct breathing and grounding stay available without disclosure or model wait. History/preferences use progressive disclosure; no onboarding or mood score.

Feeling wound up/tense/keyed up may suggest breathing for a steady rhythm; scattered/repetitive-thought context may suggest grounding for noticing surroundings. These are tentative UX rules. Explicit current preference, negation and correction outrank an inferred choice or previous action. “No breathing” cannot recommend breathing; neither/stop is accepted without persuasion. Vague/mixed input permits at most one optional clarification per conversation; no answer required, both direct actions remain available. No diagnosis, emotion score, inferred profile, certainty about hidden feelings or fix promise.

## Responsibility and persistence

| Files | Responsibility / inputs and outputs |
|---|---|
| frontend/src/App.vue, style.css, components/GuacMark.vue | Guac identity/tokens, navigation, explicit choice and settings/history disclosure |
| components/ChatPanel.vue, controllers/chatController.js | Bounded input, loading/error/recommendation UI, response validation and cancellation; never own exercise timing |
| backend/app/model_client.py | Bounded current context/history → validated reflection, structured recommendation and reason; finite provider timeout/cap |
| backend/app/routes.py, main.py, schemas.py | HTTP validation, request claims/replay, conversation and exercise CRUD; enforce eligible recommendation linkage |
| backend/app/database.py | Own SQLite additive migration and relationships; preserve legacy records and explicitly chosen colors |
| controllers/sessionPersistence.js | Per-session queue, explicit retry, version reconciliation, no resurrected cleared records |
| controllers/exerciseClock.js, BreathingExercise.vue, GroundingExercise.vue | App-owned 4/6 six-cycle clock, exact sensory sequence, pause/stop/finish |
| BreathingBalloon.vue, public/balloon.png | Original latex material plus controlled deformation; avocado default, legacy chosen colors preserved |
| HistoryPanel.vue, SupportPanel.vue | Saved recommended vs chosen detail; persistent app-owned independent support |

Store each structured recommendation with its originating model request, reflection/reason, and optional clarification/decline status. Link an explicitly started session to the originating eligible request when available; actual skill remains separate, so choosing the alternative is accurately represented. Direct entry can have no recommendation. Preserve conversation/message/request records and existing session/preferences data. No clinical/emotional profile table. Legacy database filename remains backend/data/campus-pause.sqlite3 to preserve the working setup; runtime branding is Guac.

## Visual system and tradeoffs

Peel #243D25, leaf #4D7137, flesh #DCE8AD, lime #B8D45B, cream #FAF8EF, pit #8B563B. Original code-native avocado mark and rounded expressive wordmark provide identity without a runtime image dependency. Warm typography, asymmetrical avocado shapes and lime accents add joy on home; active exercises keep one focused instruction and the balloon. Interaction comes before decoration on mobile. Cream on leaf primary buttons and peel on light surfaces are intended readable pairs; actual computed states need browser checks. Leaf on flesh is insufficient for small text, so use peel or a darker muted color there. Large tap targets/focus/keyboard order, restrained motion and reduced-motion option are required.

Avocado green replaces red only when no color was explicitly saved. Existing red/sage/blue/plum values stay intact; red remains optional. Same original photographic latex asset, highlights/shading/knot and min-visible geometry. No new renderer dependency is justified unless browser inspection reveals a concrete failure. Clock/phase durations unchanged; color stays outside active breathing.

## Research rationale (feedback, not outcomes)

| Source | Current choice, alternative and tradeoff |
|---|---|
| R1 /38 | Six-cycle ~60s breathing and grounding at12s/sense keep intended guidance below90s; slower self-paced use allowed. No forced finish. |
| R2 /30; D4 /31 | Persistent one-step support including loading/failure/exercises vs nested menu; reserves fixed space. |
| R3 /39 | Pause/stop/neither accepted, no penalty or persuasion vs completion incentives. |
| R4 /68 | Recommendation explains an option, never starts it; alternative/direct actions vs forced routing. |
| D1 /54 | User-controlled simpler view vs unvalidated distress detection; no hidden score. |
| D2 /100 | One exercise instruction or recommendation primary action vs simultaneous tasks; direct alternatives remain reachable. |
| D3 /148 | Optional conversation/clarification and private sensory identification vs required questionnaire; less disclosure/detail stored. |
| D5 /49 | Explicit color/recent shortcut, current choice overrides prior action vs inferred profile; no mandatory setup. |
| D6 /97 | Welcoming avocado visual identity on home, calm exercise state, neutral reflection matched to shared text vs clinical/gamified cheering. Saturated lime is an accent; no competing exercise motion. |

## Verification and unresolved work

[Guac review](guac-review.md), [backend checkpoint](guac-backend-checkpoints.md), [frontend checkpoint](guac-frontend-checkpoints.md), [evaluation](guac-evaluation.md), and [browser evidence](guac-browser-observations.md) distinguish source review, deterministic mocks, actual rendering and pending live cases. Test contextual choices, negated/corrected preferences, one optional clarification, decline, unsupported model output, delayed response/failure, accurate recommended-vs-chosen persistence, migration and unchanged timing. Inspect desktop/narrow/keyboard-constrained layout, focus/contrast/touch sizes, green/red balloon and reduced motion.

Valid live key was absent at revision audit; prior authorized key was rejected401. No successful live variation is implied by mock checks. Actual screen recordings, student review and another person’s run remain pending until observed. Updated code/run instructions need a new exact source checkpoint/clean-checkout verification; earlier milestone SHA/evidence stays archived.

Verified Guac source: [7c7742b1da5be66ea6a3bae9cb5ab4d7babcb1a2](https://github.com/jakebutler22/Mental-Health/tree/7c7742b1da5be66ea6a3bae9cb5ab4d7babcb1a2); [exact-source clean checkout](guac-clean-checkout.md). Actual browser refinements include larger supporting text and peel labels on flesh to meet contrast. Remaining live/recording/student/mobile-device checks are explicit in Part3.3.
