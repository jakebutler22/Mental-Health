# Guac — Part 3.1 design specification

Current authority: [scope correction](../prompts/12-part31-scope-correction.md). This is an implementable **proposed design**, not a declaration of completed application behavior. Existing later-stage code is preserved from earlier work; [status and verification](part31-verification.md) records the distinction. Reviewable artifacts: [static mockup](screen-mockup.html) and [flow diagram](design-flow.svg).

## Audience, purpose and entry

Guac is intended for general everyday use. Fictional examples include a busy day, a work presentation and a difficult conversation. The design offers a small pause without onboarding, a mood questionnaire or required disclosure. It does not diagnose, provide therapy, infer an emotional profile or promise that an exercise will solve a problem. General everyday use is the product direction; the supplied research is not validation for this audience or a production release.

Home has the Guac avocado mark/wordmark, optional chat and two direct exercise actions. “What’s taking up space today?” is the conversation invitation. On desktop the conversation is dominant and direct actions sit beside it; mobile shows brief entry and compact direct actions before extended example content or decoration. History and preferences use progressive disclosure. One primary action per task state, plain labels,44px minimum targets, visible focus and predictable return navigation reduce effort.

## Proposed conversation and decision rules

1. Optional current message (max500 characters) plus bounded recent conversation context → one model request.
2. Return a short reflection, `recommended_skill` breathing/grounding/null, visible `reason`, optional `clarification` and `action` offer/clarify/decline. Application validates structure, lengths, allowed skills and known instruction conflicts; rejects unsupported output rather than inventing an assistant answer.
3. Show one primary “Begin breathing” or “Begin grounding,” an easy alternative and “Neither right now.” Only a deliberate selection starts a skill. Both direct actions remain available on loading/failure; a late reply cannot interrupt an active exercise.
4. For mixed/vague input ask at most one optional question per conversation; no answer required. Accept neither, correction and stop without persuasion.

| Fictional input | Proposed reflection/recommendation/reason | User control |
|---|---|---|
| “I feel keyed up before tomorrow’s work presentation.” | Reflect the stated presentation tension; breathing may offer a steady rhythm | Accept, choose grounding or neither |
| “I keep replaying a difficult conversation.” | Reflect the stated looping thoughts; grounding may redirect attention to present surroundings | Both direct choices remain available |
| “A busy day. I’m not sure what I need.” | Acknowledge uncertainty; optional “Would a rhythm or noticing surroundings suit this moment?” | Skip answering and begin either skill |
| “No breathing. Actually I feel tense.” | Preserve prohibition despite feeling correction; optional grounding or no recommendation | Never recommend the prohibited skill |
| “I prefer grounding, though I feel tense.” | Explicit current preference overrides inference or previous exercise | Explain that choice takes priority |
| “Neither. Stop.” | Neutral acceptance, no recommendation or further persuasion | Leave or continue later |

These are tentative product rules, not clinical prescriptions. Current choice events must be distinct from feeling corrections. Mock interpretation may use deterministic rules for later testing, but is not a substitute for contextual live-model verification.

## Planned model role and boundary

Reuse the verified class setup pattern: backend-only OpenRouter REST transport and explicit backend-local dotenv loading, variables `OPENROUTER_API_KEY` and `OPENROUTER_MODEL`. Earlier documented model `nvidia/nemotron-3.5-lightning:free` and catalog evidence are recorded in [reuse audit](reuse-audit.md) and [dated catalog](evidence/guac-provider-catalog.json). Availability and successful access must be rechecked only when later live work is requested. Configured key is not proof of successful access; earlier authentication failed. No credentials are needed for this design review.

Planned context: current input≤500 characters, newest six messages≤3000 characters, up to three recent chosen-skill summaries and a persisted clarification-used flag. One brief response normally combines reflection and recommendation; finite20 second provider timeout, no silent retry or paid fallback, host attempted-call cap≤50 with labeled mock fallback. Provider cannot own exercise instructions, timing, navigation, stopping, saved state or support. A lexical validation layer cannot prove all generated prose safe; semantic evaluation remains a later unresolved task. Do not infer certainty, diagnosis, scores or a hidden profile.

## Skills, balloon and timing specification

Breathing: six cycles, each four seconds inhaling and six seconds exhaling;60 seconds of animation, no holds or forceful instructions. Hyperrealistic latex balloon: avocado green by default; preserve explicitly chosen color, with red available outside the active task. Convincing rounded volume, latex gloss, neutral highlights, shading and attached knot; remain visible at low inflation and avoid abrupt phase resets. Size is a pacing cue, not measured lung volume. Clock drives both label and smooth shape change. Pause freezes clock and size at the same phase; resume continues; stop is immediate. Reduced motion uses a static balloon and the same4/6 labels/countdown/60 seconds.

Grounding: five things seen → four felt → three heard → two smelled → one tasted, one sense per screen. Identify privately; typing is optional, with transient notes never sent to model or database. Next/skip/pause/stop are explicit; no forced progression. Intended response assumption12 seconds/sense gives60 seconds plus brief transitions.

Whole guided-duration target≤90 seconds from first painted instruction to final planned step, including app delays. Design budget:60 seconds guidance plus≤5seconds transitions, about65 seconds total. Entry/setup and model latency are separate; voluntary pause/support time is explicitly excluded. Grounding may take longer by choice; no forced timeout/exit. These are **design targets**, not measurements of this revision. Earlier app timings remain historical evidence tied to their source.

Rendering proposal: reuse the existing original transparent photographic balloon with modest CSS deformation/hue change, driven by the application clock. The static mockup shows representative low/middle/full states, not animation proof. No new dependency is required for the proposal. Image deformation keeps real texture/highlights but does not physically recompute reflections; inspect artifacts/performance if later implementation is requested. Alternatives: CSS-only gradients are cheap but less realistic; WebGL mesh/material offers lighting control but adds complexity, bundle size and device cost. Adopt a new renderer only if visual evidence justifies it.

## Avocado identity and accessible interaction

| Token | Value | Use |
|---|---|---|
| Peel |#243D25| Text on light surfaces, support action |
| Leaf |#4D7137| Primary buttons with cream text |
| Flesh |#DCE8AD| Recommendation/direct breathing surfaces |
| Lime |#B8D45B| Small decorative accent with peel text |
| Cream |#FAF8EF| Background and leaf-button text |
| Pit |#8B563B| Avocado center and visible focus |

Reuse Guac’s original code-native avocado mark and warm serif wordmark. Joy comes from shape, spacing and warm writing, not competing movement or congratulatory scores. Home can be expressive; active tasks simplify to one instruction. Peel/cream11.16:1, peel/flesh9.15:1, cream/leaf5.29:1 meet normal-text contrast; leaf/flesh4.34:1 and cream/lime1.57:1 do not, so avoid those small-text pairs. Verify real focus/hover/disabled states later. Responsive layout, keyboard access, reduced motion and persistent support reserve usable space. Physical software-keyboard and low-end-device behavior remain unverified.

## Proposed data, history and personalization

| Entity | Proposed fields/relationships | Purpose and limit |
|---|---|---|
| Conversation | id, timestamps, optional title | Group the optional conversation |
| Model request | request_id, conversation_id, status/mode, sanitized failure, structured result | Replay protection, truthful failed/pending history; no credentials/raw provider errors |
| Message | id, conversation_id, request_id, role, text, timestamp/status | Review actual messages; never fabricate assistant success |
| Exercise session | id/request_id, optional conversation/recommendation_request_id, actual skill, recommended_skill/reason snapshot, state, active time, cycles/step/skips, version, timestamps | Distinguish recommendation from actual selection and completed/stopped/interrupted; no clinical progress claim |
| Preferences | explicit balloon color nullable, simpler view, reduced motion | Optional deliberate choices; null color means green default |

History offers date, actual skill, active duration, outcome, linked transcript and recommended versus chosen detail. “Recommended grounding; you chose breathing” is an activity record, not effectiveness. Recent skill is an optional repeat shortcut, never an automatic route or hidden “usual mood.” Current choice overrides previous activity. Clear history requires confirmation and removes linked records while preserving preferences; reset preferences is separate. Single local SQLite history has no multi-user protection. Retain the legacy database filename only for preserved setup continuity; do not copy data or credentials from the prior project.

## Planned MVC and file map

| Layer/files | Planned responsibility | Existing status |
|---|---|---|
| Vue `App.vue`, `style.css`, `GuacMark.vue` | Identity, navigation, explicit choices, progressive settings | Preserved earlier code; copy corrected only |
| `ChatPanel.vue`, `RecommendationPanel.vue`, `chatController.js` | Input/recommendation/loading/error/stale response | Existing earlier implementation; later verification pending |
| FastAPI `config.py`, `model_client.py`, `recommendations.py`, `routes.py`, `schemas.py` | Explicit config, bounded interpretation, validated contracts | Existing earlier code; not expanded for Part 3.1 |
| SQLite `database.py`, Vue `sessionPersistence.js` | Owned schema, relationships and truthful save/retry/version states | Existing earlier implementation preserved |
| `exerciseClock.js`, exercise views, `BreathingBalloon.vue` | Fixed app clock/steps and balloon presentation | Preserved unchanged behavior |
| `HistoryPanel.vue`, `SupportPanel.vue` | History and independent bundled support | Preserved code; no new support lookup/contact |

Reuse prior Vue loading/cancellation, FastAPI factory, SQLite transactions/foreign keys, explicit configuration and sanitized one-call transport patterns. Exclude travel SQL generation, maps, prior databases/credentials and unrelated features. This project remains independently runnable on its ownlocalhost 8001/5174 with own config/database; static Part 3.1 review uses 5175 and requires no model/backend.

## Research-linked choices, alternatives and tradeoffs

The instructor’s supplied table is the source:15 patients,13 clinicians,15 prototype evaluation sessions,150 participant-task combinations. Mention counts are feedback, not outcomes. Original screenshots were not independently opened; supplied summary provenance is explicit in [assignment source](assignment-source.md).

| Finding/count | Decision | Alternative and tradeoff |
|---|---|---|
| R1 /38 | About60 seconds plus transitions; target≤90; no forced finish | Longer instruction adds detail but effort/attention cost |
| R2 /30 | One-step support on every state | Nested support saves space but adds friction |
| R3 /39 | Immediate stop/leave/neither, no penalty | Completion rewards may pressure continuation |
| R4 /68 | Explain optional recommendation; deliberate accept/alternative/direct choices | Automatic routing reduces clicks but removes agency |
| D1 /54 | User-selected simpler view | Inferred distress detection is unsupported; manual toggle adds one optional action |
| D2 /100 | One instruction/primary task at a time | All steps together reduce navigation but compete for attention |
| D3 /148 | Optional chat/question and private sensory response; no questionnaire | More disclosure may personalize more but adds effort/data |
| D4 /31 | Persistent support including active, loading, failure and history | Fixed space reduces usable area; reserve it in layouts |
| D5 /49 | Explicit color, reduced motion and optional recent repeat | Hidden profiling or mandatory setup adds burden; current choice wins |
| D6 /97 | Warm restrained palette, neutral context reflection, calm active scene | High-energy game/clinical tone may add stimulus or judgment |

Support opens independently of model/backend decisions and pauses active guidance. No monitoring, automatic contacts or risk-assessment claim. Region resources must be verified/bundled for the intended setting before later release; preserved US resources remain documented historically, not universal coverage. Optional phrase-based support offers can miss indirect wording and never gate manual access.

## Unresolved questions and stop boundary

Unresolved: contextual live response quality and semantic guard limits; physical mobile keyboard/readability; low-end animation/material fidelity; preferred support-region coverage and locale choice; privacy and whether optional saved chats should default on; human response-time assumptions; student review of design/research interpretation. A valid model key is a later dependency, not a Part 3.1 blocker. No clinical effectiveness or public-release readiness is established.

Part 3.1 requires this implementable design, reviewable flow/mockup, rationale/data/model/control/tradeoffs, accurate source/AI evidence and a verified public design commit/report. Existing code and earlier checks are acknowledged, not expanded or recertified as later milestone completion. After publication verification, **STOP**. Parts 3.2/3.3 remain pending until requested.
