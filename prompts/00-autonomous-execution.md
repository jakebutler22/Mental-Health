ASSIGNMENT 3: MENTAL HEALTH SKILLS APPLICATION
Autonomous execution instructions for the existing Codex chat
Updated October 12, 2026 after the user authorized full execution and public GitHub publication


EXECUTION DIRECTIVE: CONTINUE THE EXISTING PROJECT TO COMPLETION

This file is one continuous instruction to the Codex chat named "Assess Assignment 3 setup". It replaces the earlier one-prompt-at-a-time workflow. Work in the existing project; inspect its current state before deciding which phase is next. Do not return only a proposal, ask me to paste later phases, or stop at a normal phase boundary.

I authorize you to complete this Assignment 3 project autonomously. This includes required project-local dependency installation, implementation and scoped fixes, browser and database checks, fictional model requests needed for evaluation, documentation and recordings using available tools, Git branches and commits, merging completed work into main, creating the project's own public GitHub repository, and pushing verified source and submission materials. Choose reasonable implementation details without asking me again for these approvals.

This authorization replaces the earlier procedural pauses for my approval of dependency installation, design checkpoints, commits, merges, and public pushes. Keep the inspection and verification work at those checkpoints. Record agent review honestly; permission to proceed does not establish that I personally tested or reviewed anything. If the class requires student review or a student-created recording, identify the remaining student action accurately while finishing all independent work.

Respect platform permissions and access controls. Do not bypass an approval rejection or invent access. A missing credential, unavailable recording capability, failed authentication, or inaccessible required resource is a concrete blocker only for work that depends on it. Complete everything else first, and report the exact remaining action. A failed local repair loop should not end unrelated achievable work.

Use CHECK → TAKE ACTION → VERIFY within each phase. Treat the ten phases below as a dependency-ordered runbook. Resume verified completed phases rather than rebuilding them. Save progress and evidence throughout so compaction or a runtime interruption does not lose the objective. If subagents are available, delegate independent implementation or review tasks with clear file ownership.

Publish only this project's source and intentionally prepared coursework materials. Keep credentials, runtime databases, private chat content, and unrelated prior-project files out of Git. The source repository is public; the application remains a localhost coursework prototype and is not deployed as a public mental-health support service. Do not submit to the learning-management system or claim student authorship/review beyond the actual record.

GitHub: the planning session verified the authenticated account jakebutler22 and found no matching Mental Health or Campus repository at the time of checking. Recheck from this execution environment. Prefer an existing verified remote for this project. Otherwise create a new public repository named Mental-Health under the authenticated intended account if that name is available, then set this project's remote and push. If the name exists but belongs to another project, choose a clear unique assignment-specific name. Do not overwrite or repurpose another repository or change Expedia-lite. Record the actual final URL.

Finish with actual repository and source commit links, milestone report paths, observed checks, recording links if created, remaining limitations, and any unavoidable human or access-dependent action. Never label live-model checks, browser observations, recordings, or assignment submission complete unless they actually occurred.

PROJECT BRIEF

Working title: Campus Pause. This is a provisional name, not a requirement.
Confirmed project root from the user's Codex audit: /Users/jakebutler/Documents/ChatGPT/Mental Health
Reported starting state: Git initialized on main with no commits; only .git was present. The initial audit was already run. Recheck current state and resume with the first incomplete phase; the source-recovery/design phase below is self-contained.
Audience: Fictional college-student scenarios.
Entry: A short conversational interface, with a direct path to an exercise without typing or waiting for the model.
Final skills: Paced breathing (4-count inhale, 6-count exhale) and 5-4-3-2-1 sensory grounding.
Visual direction: Warm, minimal cream and muted sage surroundings. The breathing exercise centers on a hyperrealistic latex balloon, red by default, with an optional user-selected color.
Starting point: A separate project that selectively reuses suitable Expedia-lite or class-chatbot code.
Model: Inspect and reuse the existing class provider and configuration pattern where suitable.
Required stack and environment: Vue, FastAPI, SQLite, localhost.
Milestones: Part 3.1 on October 15, Part 3.2 on October 22, and Part 3.3 on October 29, 2026. All are due at 11:59 PM Eastern.

The balloon is a visual pacing cue. It inflates smoothly during a four-second inhale and deflates smoothly during a six-second exhale. Six cycles supply 60 seconds of breathing animation. The whole guided exercise, from its first instruction to its final planned step, must be measured separately and remain within 90 seconds at its intended pace. Do not introduce breath holds, forceful breathing instructions, claims about measured lung capacity, or claims of clinical effectiveness.

Use the instructor's supplied research table as the assignment's research source. Its findings are:
R1: Short exercises; attention declined beyond roughly 90–100 seconds.
R2: Frictionless crisis access.
R3: Permission to stop or leave without penalty.
R4: User control over the journey.
D1: Progressive interface contraction: as distress rises, the interface should contain less. The study does not establish how the system would detect this or exactly what should contract. A user-controlled simpler view is this project's proposed implementation.
D2: One action or skill step at a time.
D3: Minimize the effort of feeling, disclosing, or performing.
D4: Persistently visible safety access, including inside exercises.
D5: Personalization without mandatory setup.
D6: Low-stimulus, nonjudgmental language and presentation.

Treat the college-student audience and balloon design as this project's design choices. Do not imply the source study clinically validated this specific application or population.

HOW TO EXECUTE THIS FILE

1. Keep the existing project selected at /Users/jakebutler/Documents/ChatGPT/Mental Health. Do not rename it or create a competing application elsewhere.
2. The source-recovery phase supplies the assignment digest and class rules. Missing original attachments no longer block implementing this supplied brief. Preserve its stated provenance.
3. Inspect the historical local prior project at /Users/jakebutler/Documents/ChatGPT/Expedia-lite if accessible. A verified read-only remote fallback is https://github.com/jakebutler22/Expedia-lite. Do not mistake remote committed configuration for current Mac-local configuration or successful live access.
4. Phase 1 is retained as an audit checklist. Skip work already established by current evidence, then proceed through Phases 2–10 in this run without waiting for additional prompts.
5. Create or verify this project's own public GitHub remote at the first useful verified checkpoint. Standing authorization is supplied above.
6. Preserve sequential inspection of configuration, controller, route, and frontend integration. Perform these inspections yourself and record evidence, then continue. Do not invent personal student review.
7. Phases 1–2 prepare Part 3.1; Phases 3–7 prepare Part 3.2; Phases 8–10 complete Part 3.3. Preserve distinct milestone reports and source references as work progresses.

Source basis: The supplied Assignment 3 screenshots and Vibe Coding working-rules markdown, plus the project preferences selected in this conversation and the requested realistic balloon interaction.

VERIFIED PRIOR-REPOSITORY REFERENCE

The ChatGPT planning session inspected the public GitHub snapshot of:
https://github.com/jakebutler22/Expedia-lite
Pinned source commit: 8052604890c164ed09fbc92c145985559c07c3ba
Audit date: October 12, 2026.

This is evidence about committed source. It does not establish the current Mac checkout, installed dependencies, live credentials, or current provider availability. Compare the local prior project if accessible; otherwise use the pinned remote as a read-only reference. Do not copy its databases, credentials, travel data, hotel-specific prompts, or unrelated features.

Verified model setup:
- Provider: OpenRouter, through https://openrouter.ai/api/v1/chat/completions.
- Variables: OPENROUTER_API_KEY and OPENROUTER_MODEL.
- Loader: backend/app/config.py calls load_dotenv with an explicit backend/.env path derived from the source file. That .env is ignored.
- README documents nvidia/nemotron-3.5-lightning:free as the model approved for the October 8 run. The committed .env.example leaves key/model values blank. Treat this as the documented prior model, not a verified current runtime setting.
- backend/app/openrouter.py uses httpx, a finite 20-second provider timeout, backend-only authorization, sanitized error classes, and explicit response validation. It accepts an explicit NVIDIA Nemotron :free identifier and has no automatic or paid fallback.
- Check the current official provider catalog and model compatibility before live use. Preserve the existing OpenRouter/free-Nemotron constraint. Prefer the documented prior model; if that exact entry is unavailable, select a currently available free NVIDIA Nemotron entry only when its catalog pricing and compatibility are verified, and record the changed identifier and reason. Do not switch providers or introduce a paid fallback. If no compatible free entry is available, document that dependency and finish independent mocked work.

Suitable patterns to adapt:
- backend/app/main.py: FastAPI app factory/lifespan and per-request SQLite connection lifecycle.
- backend/app/database.py: sqlite3.Row, enforced foreign keys, and transaction/connection management. Build this app's own schema and database filename.
- backend/app/config.py and backend/app/openrouter.py: explicit configuration loading, provider transport, and error boundary. Use this application's own identity/header.
- backend/app/hotel_insights.py: injected request functions for deterministic mock testing. Do not reuse the travel-specific SQL-generation/two-request workflow.
- frontend/src/hotelInsights.js: injected fetch, response validation, and sanitized errors.
- frontend/src/App.vue: Vue Composition API request state and stale-result handling; adapt only the useful patterns.

This snapshot does not provide persistent chat conversations or exercise sessions. Build conversations, messages, exercise sessions, preferences, and the useful history interface specifically for Campus Pause. Do not claim this new persistence was already available in the earlier project.

Manifest observations, not claims about installed versions:
- Vue 3.5.42; Vite 8.2.2; @vitejs/plugin-vue 6.0.8.
- FastAPI, Uvicorn, pytest, httpx, and python-dotenv are declared in backend/requirements.txt; SQLite uses Python's standard library.
- Leaflet and Geoapify serve the travel app and are unnecessary here.
Select compatible project dependencies after inspecting the actual execution environment; this audit does not require copying every old version.

Pinned evidence URLs:
https://github.com/jakebutler22/Expedia-lite/blob/8052604890c164ed09fbc92c145985559c07c3ba/README.md
https://github.com/jakebutler22/Expedia-lite/blob/8052604890c164ed09fbc92c145985559c07c3ba/backend/app/config.py
https://github.com/jakebutler22/Expedia-lite/blob/8052604890c164ed09fbc92c145985559c07c3ba/backend/app/openrouter.py
https://github.com/jakebutler22/Expedia-lite/blob/8052604890c164ed09fbc92c145985559c07c3ba/backend/app/database.py

======================================================================
PHASE 1: AUDIT THE SOURCES AND LOCK THE REQUIREMENTS
======================================================================

Read the supplied assignment digest and class working rules in Phase 2 and the verified prior-repository reference above. Read original screenshots or rules only if they are now available; their absence does not block this supplied brief. Read any README.md, AGENTS.md, and handoffs/current.md that already exist in the selected project. Confirm its absolute root, Git state, existing files, and unfinished work before changing files.

This is a new, separate Assignment 3 application. Check whether the historical candidate /Users/jakebutler/Documents/ChatGPT/Expedia-lite exists and is readable, then inspect it as a read-only reference for suitable Vue, FastAPI, SQLite, and class-chatbot components. Verify the actual model provider, model identifier, configuration pattern, and reusable controllers without displaying secret values. Do not assume a provider, installed dependency, browser capability, or previous feature is available.

Use this agreed project direction:
- Fictional college-student scenarios.
- A warm, minimal cream-and-sage interface that opens with a short chat.
- A direct way to begin an exercise without typing or waiting for a model.
- Paced breathing and 5-4-3-2-1 grounding as the final skill scope.
- A hyperrealistic latex breathing balloon, red by default, with an optional color choice. It expands during four seconds of inhaling and contracts during six seconds of exhaling.
- A separate codebase with selective reuse of suitable earlier code and the existing class model setup.
- Vue, FastAPI, SQLite, and localhost.

CHECK: Compare the sources, existing code, and agreed direction. Identify reusable components, missing capabilities, actual configuration needs, and the requirements for Parts 3.1, 3.2, and 3.3. Preserve the distinction between required work and optional examples.

TAKE ACTION: Propose the smallest coherent implementation and a file map. Explain which code can be reused, which changes are needed, and how the two projects stay independently runnable. Evaluate a feasible rendering approach for the realistic balloon before proposing new dependencies.

VERIFY: Record the confirmed roots, source-backed requirements, reuse inventory, known unknowns, and next task, then continue to the first incomplete phase. Identify any missing source or path precisely. Do not install, initialize Git, edit files, copy databases or credentials, or invent inspection results.

======================================================================
PHASE 2: RECOVER SOURCE CONTEXT AND CREATE THE PART 3.1 DESIGN
======================================================================

Continue in the confirmed project root:
"/Users/jakebutler/Documents/ChatGPT/Mental Health"

Your audit reported an initialized Git repository on main with no commits and only .git. Recheck that state once. An unborn main branch is a valid starting state. Read README.md, AGENTS.md, and handoffs/current.md only if they now exist. Keep this project in its current folder and quote paths containing spaces.

This phase supplies the missing assignment context and begins the Part 3.1 documentation and design work within the authorized full-project run. Use the supplied brief below; do not require the absent screenshots before doing this work. When later prompts say "read the assignment," use the source documents created here.

CHECK

1. Confirm the root, files, Git state, and any configured remote without changing them. Follow any applicable workspace instructions.
2. Check whether this historical prior-project candidate currently exists and is readable:
   "/Users/jakebutler/Documents/ChatGPT/Expedia-lite"
   This path was used previously; it has not been verified as current.
3. If accessible within the permitted workspace scope, inspect relevant README/AGENTS files, manifests, Vue components, FastAPI controllers, configuration-loading code, and SQLite helpers read-only. Identify reusable components and evidence of any conversational-model integration. Distinguish provider references in code from a verified selected provider/model and from successful live access.
4. Do not run or modify the earlier application, install into it, copy its database or credentials, or print secret values. If the local candidate is missing or inaccessible, record that finding and use the pinned read-only GitHub reference above. Only local differences, runtime configuration, credential access, and current live availability remain unverified. Do not search the whole computer or substitute another project silently.
5. Inspect which design-preview, browser, and recording capabilities are actually available. Do not install tools to resolve those questions in this step.

SUPPLIED ASSIGNMENT SOURCE

Provenance: This is a structured summary of the instructor's Assignment 3 overview and Vibe Coding working rules, checked against the screenshots and Markdown supplied in the ChatGPT planning conversation. Record this provenance. Do not claim that you opened Canvas or independently inspected the absent original images.

Assignment 3: Mental Health Skills Application
- Individual coursework project.
- Vue frontend, Python/FastAPI backend, SQLite database, running on localhost.
- Combine a conversational model with relevant context, persistent conversation and session records, and a useful way to review saved history. These are explicit requirements.
- Choose one or more of the four supplied skills. Our chosen final scope is paced breathing and sensory grounding.
- Preserve the supplied skill steps. Do not have the model invent therapeutic advice.
- Use interaction and motion where they serve the skill. Speech input/output is optional and is outside our selected scope.
- The application controls skill sequences, timing, saved state, navigation, exit controls, and independent crisis-support access. A system prompt alone does not satisfy those responsibilities.

Research foundation:
The instructor supplies a summary from an ongoing study of digital skills support for people with borderline personality disorder. It included 15 patients, 13 clinicians, 15 prototype evaluation sessions, and 150 participant-task combinations. The supplied table is the research source; no separate research dataset is required or provided. Mention counts describe feedback, not clinical effectiveness.

R1, 38 mentions: Around 60 seconds was comfortable; exercises beyond roughly 90–100 seconds lost attention.
R2, 30 mentions: Crisis access should be frictionless, without navigating through multiple screens.
R3, 39 mentions: Users need permission to stop or leave without consequence or penalty.
R4, 68 mentions: Users control their journey and should receive choices rather than be routed automatically.
D1, 54 mentions: Progressive interface contraction as distress rises. The study does not establish how the system detects distress or precisely what should contract.
D2, 100 mentions: One atomic skill or action at a time.
D3, 148 mentions: Minimize the effort of feeling, disclosing, or performing.
D4, 31 mentions: Safety access must stay persistently visible, including inside an exercise.
D5, 49 mentions: Personalization should use prior actions without burdensome configuration.
D6, 97 mentions: Use low-stimulus, nonjudgmental presentation. Clinical phrasing could feel diagnostic, excessive cheerfulness could feel condescending, and saturated color or motion could add demands.

Explain design choices using R1–R4 and D1–D6, including alternatives and tradeoffs. A user-selected simpler view is our possible response to D1, not a finding that the study established reliable distress detection. Our college-student audience is a project design choice, not a population for which this prototype has established clinical effectiveness.

Skill definitions:
- Paced breathing: inhale for a count of four and exhale for a count of six, repeating for roughly 60–90 seconds.
- Sensory grounding: identify five things seen, four felt, three heard, two smelled, and one tasted. Minimize unnecessary typing.
- STOP and the one-minute cognitive reframe are other permitted assignment options, but are not in our selected final scope.

Timing and user control:
- Design the guided exercise to take no more than 90 seconds at its intended pace.
- Measure from the first exercise instruction through the final planned step, including application delays.
- State assumptions about user response time. Report entry/setup separately.
- User-chosen pauses and time accessing crisis support are outside this duration measure.
- Do not force completion or exit when a timer expires.
- Crisis-support information must remain clearly reachable throughout the experience, including after model failure, independently of model or classifier decisions. Document any crisis-input handling and its limits.
- Use only fictional scenarios for evaluation and demonstrations. Accurately describe the app as a coursework skills prototype. It must not diagnose, claim therapy, or imply someone is monitoring the user. Do not deploy or offer it as real mental health support.

Milestones, each worth 100 points and equally weighted:
Part 3.1, Research and Design, due October 15, 2026, 11:59 PM Eastern:
Present an implementable design with a sketch or flow diagram, the model's role and limits, expected stored data, R/D-linked decisions, personalization, user control, alternatives/tradeoffs, and unresolved questions. Keep README, AGENTS, and design notes useful. A working application is not required.

Part 3.2, Working Application and Safety, due October 22, 2026, 11:59 PM Eastern:
Demonstrate at least one complete chosen skill, useful model contribution, conversation/session persistence in SQLite, measured exercise duration, independent crisis access, request failure, and leaving an exercise. Support claims with actual browser observations and database inspection. Be honest about unfinished work.

Part 3.3, Integration, Evaluation, and Demonstration, due October 29, 2026, 11:59 PM Eastern:
Complete and refine the selected application, history, and personalization. Revisit design decisions and verify another person can run a clean checkout from the README.
Evaluate at least 15 fictional scenarios plus three explicit behaviors that should hold across cases. Cover ordinary use, interruptions, and failures, recording expected and observed results.
Use saved/mocked responses for repeatable checks, and repeat a small relevant selection of live-model cases to examine variation. Report a surprising finding and an untested limitation.
Peer testing uses mocks by default. If live peer calls are used, enforce a host-set limit of no more than 50 model calls for the session and return to mocked responses afterward.
Provide a finished-app demonstration and a process screencast showing a failure, the evidence used to understand it, and the resulting decision. Explain a relevant generated-code section. One recording with marked sections or two recordings is allowed.

Submission:
- One report.md per milestone, with the real repository URL, submitted source commit, accessible links to relevant design/evidence/recordings, completed work, and unresolved work.
- Include AI-USE.md naming actual tools/models, available versions or identifiers, and their roles.
- Maintain a curated, redacted evidence log connecting selected prompts, changes, tests/browser observations, and decisions, including at least one failed or revised approach.
- Do not invent citations, commits, recordings, provider verification, or observed test results.

AGREED PROJECT DIRECTION

Use Campus Pause as a provisional app title; keep the actual folder named Mental Health.
- Fictional college-student situations.
- Warm, minimal cream-and-sage surroundings.
- Open with a short chat, while offering direct access to breathing or grounding without required disclosure or a model wait.
- Finish both breathing and grounding by the final milestone.
- Reuse suitable existing class code and model setup only after verification.

The breathing exercise's central visual is a hyperrealistic latex balloon:
- Red by default, with optional user-selected color that preserves realistic highlights and shading.
- Convincing volume, latex material, neck or knot, and smooth shape changes.
- Smooth inflation over four seconds of inhaling and deflation over six seconds of exhaling.
- Six cycles provide 60 seconds of animation. Measure the entire guided sequence separately against the 90-second requirement.
- Keep the balloon visible at its smallest size; avoid abrupt resets.
- Pause/resume freezes and resumes both the phase clock and balloon state together.
- Provide clear inhale/exhale labels and an equally timed reduced-motion alternative.
- Remember an explicitly chosen color without requiring configuration before exercise.
- Treat size as a pacing cue, not a measurement of actual lung volume. Do not add breath holds or forceful breathing instructions.

Evaluate feasible rendering approaches against visual fidelity, color changes, timing, performance, and dependency cost. A high-resolution asset with controlled deformation is a candidate, not verified proof of hyperrealism. Show the proposed low, middle, and full inflation states. Do not lock in an approach or claim the final appearance without a visual check.

CLASS WORKING RULES

Carry these into the project:
1. Inspect before editing; keep all writes inside the confirmed project root and preserve existing changes.
2. Use CHECK → TAKE ACTION → VERIFY.
3. Show missing packages, exact installation commands, and target environments. The original notes require asking before installation; the user supplied standing authorization on October 12, 2026, so execute necessary project-local installs and record them without another approval question.
4. AutoLoop: run the agreed check, inspect failure, make the smallest in-scope fix, and rerun. Stop that repair loop when passing, after five correction cycles, or at a real access/scope limit. Record unresolved results and continue independent achievable work.
5. SmokeTest observes the actual browser without editing. "AutoLoop: run the smoke test" authorizes scoped fixes and retests.
6. Map MVC responsibilities to real or explicitly planned files and define controller inputs/outputs.
7. Inspect actual database records and relationships before/after relevant CRUD operations using disposable test data; verify persistence after restart.
8. Define business rules with ordinary and boundary examples.
9. Keep secrets in ignored backend-local configuration; never expose them in frontend code, prompts, logs, or recordings.
10. Explicitly load backend configuration and provide a safe health check. Configured credentials and a successful provider request are separate facts.
11. Keep API configuration, controller, and route work in separate sequential phases with an actual inspection checkpoint before frontend integration. The user authorized continuous execution, so perform and document each inspection without waiting for a new prompt.
12. Prove one known-input round trip before expanding to real input. Verify loading, no-result, failure, stale-result, and repeated-click behavior.
13. Review visual references and the proposed design before implementation. Verify both appearance and behavior.
14. Make coherent verified Git checkpoints. Review diffs and actually exercise applicable behavior before commits; identify the reviewer as the agent where appropriate. Record student review separately and only when it happened. After the initial main checkpoint, use feature branches; verify, review, commit, push, merge completed work, test main, and push main. Preserve unfinished work, inspect conflicts, and resolve routine in-scope conflicts without discarding user work. Commit/merge/push authorization is already supplied.
15. Maintain docs/design-pipeline.md, docs/verification.md, numbered prompts, and handoffs/current.md. Ground the handoff in actual branch/files/commit state, completed and unfinished work, checks run, and next task.

TAKE ACTION

Complete the missing reuse inspection where possible, then create the Part 3.1 design package now. Use the verified remote reference above and document only the remaining local/runtime/provider-access uncertainties as implementation dependencies while design work proceeds.

Create or update:
- README.md with purpose, required stack, coursework role, project organization, and current design-stage status.
- AGENTS.md with the class rules, source-document locations, agreed scope, and read/write boundaries.
- .gitignore excluding secrets, .venv, node_modules, build outputs, and future runtime database files while retaining safe examples and fictional fixtures.
- docs/assignment-source.md containing the supplied assignment brief and its provenance.
- docs/class-working-rules.md containing the supplied working rules.
- docs/design-pipeline.md containing the user flow, MVC file map, controller contracts, proposed data model, model responsibilities, and R1–R4/D1–D6 design rationale.
- An actual flow diagram and a reviewable screen mockup artifact linked from the design notes. Show chat/direct entry, breathing and balloon states, grounding, history, stopping, and persistent support access.
- docs/verification.md with planned checks, timing definitions, balloon acceptance criteria, and honest capability limitations.
- docs/evidence-log.md with the actual audit, decisions, and observations so far.
- AI-USE.md with actual known planning/development tools and roles; label unavailable model identifiers as unknown.
- frontend/ and backend/ as structural folders only.
- prompts/02-design-and-source-recovery.md containing this prompt.
- handoffs/current.md describing the actual state, unresolved reuse/provider items, and next checkpoint.
- submissions/3.1/report.md with the design summary, evidence links, unresolved questions, and clearly pending repository URL/source commit if not yet available.

Keep design choices explainable. Specify how conversations and sessions will persist and what history shows. Propose optional remembered color/recent-skill behavior while preserving choice, stopping, and a simpler view. Record why the balloon's intentional color/motion is useful within the otherwise quiet interface.

Use existing tools to inspect the diagram/mockup if available. If visual inspection is unavailable, mark it pending and continue the documentation. Do not claim an implemented application or completed browser test.

Keep this design phase focused on documents and design artifacts. After its verification, proceed to the initial source/repository checkpoint and the implementation phases; publication permission is already supplied. Do not initialize a second local repository or deploy a public runtime service.

VERIFY

Check the design package against every Part 3.1 requirement and verify that the files expected by Phase 3 exist. Distinguish source requirements, selected design choices, verified local findings, and unresolved dependencies.

Record this phase checkpoint and proceed:
1. Files created or changed.
2. Requirement-to-design/evidence mapping for Part 3.1.
3. Verified reuse findings, with provider/model status stated precisely.
4. Checks actually performed and what remains unverified.
5. The concrete design/diff items inspected and any remaining student-review requirement.
6. The next action: perform the design/diff review, make the initial verified source checkpoint, create or verify the real public repository, record Part 3.1 source/report references, and continue with Phase 3 under the existing authorization.

Report "Part 3.1 design package prepared" only if it is complete. Do not report submission-ready while required repository/commit fields or design evidence remain pending.


======================================================================
PHASE 3: BUILD THE FOUNDATION AND EXERCISE STATE
======================================================================

Read README.md, AGENTS.md, docs/design-pipeline.md, and handoffs/current.md. Inspect the branch and unfinished changes. Continue the reviewed Part 3.1 design.

CHECK: Inspect Python, Node.js, project dependencies, source components approved for reuse, and the actual environments. Show missing packages, exact installation commands, and their target environments. Install the necessary project dependencies under the standing authorization above; use the appropriate project environment and record the exact commands.

TAKE ACTION: After verified setup, build the Vue, FastAPI, and SQLite foundation inside this project. Reuse only the approved code and configuration patterns. Create this app's own database with fictional fixtures.

Implement the agreed data models and controller contracts for conversations, messages, exercise sessions, and minimal preferences. Establish deterministic exercise state for entering, starting, pausing, resuming, leaving, and completing a skill. Keep an interrupted session distinguishable from a completed one. Build the simple interface shell with chat entry, direct skill access, and exercise screens showing one current step.

Implement the breathing timeline independently of its visual renderer: four seconds of inhale, six seconds of exhale, six cycles. Expose the current phase and normalized inflation progress for the balloon. Implement the unchanged grounding sequence: five things seen, four felt, three heard, two smelled, and one tasted. Let users identify them without mandatory typing.

Add a persistently visible, application-controlled route to crisis-support information now. It must remain usable from chat and inside exercises, including while the model is unavailable. Verify displayed resource information against current official sources and record those sources. Implement the documented crisis-input policy without implying that the app reliably detects every crisis, provides therapy, or monitors anyone.

Keep the guided exercises usable without a model response. Show the coursework-prototype role concisely. Use fictional information throughout.

VERIFY: Run approved version/import checks and relevant backend/frontend checks. Start the actual app and inspect the shell, state transitions, stop/support controls, and database relationships. Verify disposable record creation, updates, and persistence after restart. Document any temporary visual scaffolding honestly; the balloon's final realism is verified in Phase 7.

Save this prompt, update the handoff and evidence log, and show the files changed, checks actually run, and unresolved issues. Use AutoLoop only within the class limits.

======================================================================
PHASE 4: CONFIGURE THE MODEL AND VERIFY HEALTH
======================================================================

Read the current project instructions and handoff. Inspect the existing class provider configuration pattern without revealing key values. Use already available authorized model access where possible; missing live credentials do not block deterministic implementation or mocked evaluation.

CHECK: Identify the intended backend-local configuration file, exact variable names, selected provider/model identifiers, and how the backend currently loads settings. Confirm .gitignore excludes secrets and inspect whether any secret-bearing file is already tracked.

TAKE ACTION: Implement configuration loading and a safe health endpoint only. Reuse the existing class provider setup where suitable. Create an example configuration with blank secret values and document where I should enter the real key locally. Do not copy the old project's .env wholesale or put credentials in the frontend.

Runtime credential access is covered by my authorization to reuse the existing class model setup. Prefer an already configured process environment. If needed and accessible within scope, a local runner may read only OPENROUTER_API_KEY from the explicitly identified prior project's ignored backend/.env and pass it privately in the new backend process environment. Do not print the value, embed it in command arguments or recordings, copy the old .env wholesale, persist that prior secret into this repository, or search unrelated credential locations. This is a temporary verification setup, not an application dependency on the old project; the new app must independently accept its documented environment/configuration. Keep actual credentials out of source and public Git history. If authorized live access is still unavailable, complete mock-backed work and mark live verification pending.

The health response must report configuration availability without revealing values. Distinguish mock mode, missing configuration, and configured live mode. Document restart requirements. Keep the deterministic exercises and crisis-support route available regardless of configuration status.

Do not add the model controller, model route, or frontend integration in this prompt. Use the standing installation authorization if a necessary dependency is missing.

VERIFY: Run the backend and open the actual health endpoint in the browser. Check configured and missing-configuration behavior using safe temporary test settings. Record the observed response and actual address. A configured key is not evidence of a successful provider request.

Save the prompt and update the verification notes, evidence log, and handoff. Perform the endpoint inspection, record its result and a short reproducible inspection step, then continue to the next phase.

======================================================================
PHASE 5: BUILD AND VERIFY THE MODEL CONTROLLER
======================================================================

Read the current project instructions and handoff. Confirm the configuration checkpoint actually passed.

CHECK: Inspect the provider's current official documentation, the approved reuse inventory, and the existing controller contracts. Define the controller's request inputs, relevant context, response fields, finite timeout, and failure behavior before editing.

TAKE ACTION: Implement one small backend model controller without adding its HTTP route or frontend integration. Use the selected class model and approved skill descriptions as context. Include relevant conversation/session history within a documented context limit. Reuse suitable retrieval logic only where it helps this small approved knowledge set.

Make the model's contribution brief, nonjudgmental, and responsive to fictional college-student situations. It may explain available choices and offer a relevant skill; the user retains the choice. The application, not generated text, owns the fixed exercise sequence, timing, state, stop controls, and support route. Do not allow generated content to rewrite those steps or invent therapeutic advice.

Return a stable application response. Validate structure and handle timeout, provider failure, empty responses, malformed output, and relevant instruction-conflict cases. Provide an explicitly identified mocked-response mode. Keep logs and recorded evidence free of credentials and private content.

VERIFY: Use deterministic mocked responses for ordinary and failure cases. If configured live access is available within the existing authorized setup, make a small fictional live request to establish provider connectivity and record the actual provider/model identifier. Clearly distinguish that observation from mocked tests. If live access is unavailable, identify the blocker and leave live verification pending.

Install only packages needed for this agreed project under the standing authorization. Do not change the selected provider silently. Save the prompt and update the handoff, evidence log, and controller documentation.

======================================================================
PHASE 6: CONNECT AND VERIFY THE MODEL API ROUTE
======================================================================

Read the current project instructions and handoff. Inspect the configuration and controller verification evidence before continuing.

CHECK: Confirm the controller's inputs and outputs, the conversation/session schema, and the actual backend address. Identify the smallest route change needed.

TAKE ACTION: Add the backend route that calls the verified model controller. Validate user input and relevant session identifiers. Connect conversation/session persistence according to the approved data model. Define how failed requests and user messages are represented without creating duplicate successful assistant messages.

Keep the response contract stable across live success, mocked success, and known failures. Pass application data to the frontend without provider credentials or raw secret-bearing errors. Preserve the independent exercise and support behavior.

Do not build or modify the chat frontend in this prompt.

VERIFY: Open the route's interactive API documentation or use a direct endpoint request against the running backend. Start with one known fictional input, then a different input. Confirm that submitted text and selected context affect the actual request. Inspect SQLite to verify the saved messages and session relationships.

Exercise a mocked timeout, malformed response, and invalid request. Compare HTTP responses with the database state and documented expectations. Record actual outputs, not merely that the endpoint exists. Perform and record the precise endpoint inspection checkpoint before frontend integration, then continue.

Save the prompt and update the verification notes, evidence log, and handoff.

======================================================================
PHASE 7: COMPLETE THE CORE EXPERIENCE AND PART 3.2
======================================================================

Read the instructions, approved design, and handoff. Verify the backend configuration, controller, and route checkpoints before connecting the interface.

CHECK: Inspect the running shell and exercise state. List the files needed to finish chat, the two guided skills, and the realistic balloon. Preserve working API contracts and stored data.

TAKE ACTION: Connect the chat UI to the verified backend, first proving one complete round trip with a known fictional input and then enabling real input. Keep short conversational entry and direct access to breathing or grounding. Handle loading, no response, failures, stale results, and repeated clicks visibly and predictably.

Complete the breathing balloon to the requested visual standard:
- A convincing three-dimensional latex form with realistic highlights, shading, material appearance, and a neck or knot.
- Red by default, with optional color selection that preserves realistic material lighting. Remember a chosen color without requiring setup.
- Smooth changes in apparent volume and shape during each four-second inhale and six-second exhale. Keep the balloon visible at its smallest state and avoid abrupt resets between cycles.
- Drive all phases and inflation progress from the exercise clock. Do not base elapsed time on frame count or model responses.
- Keep pause/resume synchronized with the exact current phase and balloon state. Stopping remains immediately available.
- Use cream and sage for the surrounding interface with little competing motion.
- Provide clear inhale/exhale text and a usable reduced-motion pacing alternative with the same four-second/six-second phase timing. Keep color selection outside the active breathing task.
- Inspect the current rendering result and choose the simplest approach that achieves the required realism. If a new rendering dependency is needed, document the concrete limitation, install it under the standing authorization, and verify its actual visual benefit.

Finish grounding with the exact 5-4-3-2-1 sequence, one step at a time, optional text entry, and easy leaving. Keep support access visible throughout both exercises. Do not force a person to finish or leave when the planned exercise time ends.

Persist real conversation and session records, chosen skill, actual completion/interruption status, and relevant minimal preferences.

VERIFY: AutoLoop: run the smoke test. Operate the real browser through chat, a full breathing exercise, a full grounding exercise where implemented, pause/resume, leaving, and a failed model request. Inspect SQLite before and after, restart the app, and verify persistence. Inspect the balloon at low, middle, and full inflation, during transitions, and after a color change. Check resizing and reduced-motion behavior.

Measure the entire guided sequence from first instruction to final planned step, including application delays. Six breathing cycles equal 60 seconds of animation; report the measured whole sequence separately. State grounding-response assumptions and distinguish entry/setup and permitted exclusions. Keep the intended guided duration within 90 seconds.

Create submissions/3.2/report.md and evidence demonstrating a complete skill, useful model contribution, SQLite conversation/session persistence, measured duration, independent support access, request failure, and leaving an exercise. Report any unfinished grounding or visual work honestly while retaining both skills as the final scope.

Prepare the reviewed milestone checkpoint. After your actual diff review and relevant verification, commit and push the verified feature branch under my standing authorization, confirm a clean working tree without discarding work, merge into main, smoke-test main, and push main. Record the real submitted source commit, repository URL, and accessible evidence links tied to that version where feasible. Commit report updates separately if needed. Update the prompt log, AI-USE.md, and handoff.

======================================================================
PHASE 8: REFINE HISTORY, PERSONALIZATION, AND USER CONTROL
======================================================================

Read the current instructions, Part 3.1 decisions, Part 3.2 evidence, and handoff. Inspect the actual stored schema and running app.

CHECK: Identify unfinished work in the two agreed skills, history, personalization, and visual quality. Compare implementation with the original design and explain meaningful changes.

TAKE ACTION: Complete both skills and refine the user's ability to review saved conversations and exercise sessions. Show accurate dates, chosen skills, and completed or interrupted status. Use understandable language without implying clinical progress or effectiveness.

Offer a recent or usual skill as an optional repeat action. Remember a deliberately selected balloon color. Keep both skill choices available and let the user change or clear saved preferences. Add the reviewed simpler view as a user-controlled choice; do not infer a clinical distress level.

Make saved-history behavior and any deletion/reset controls match the documented data rules. Avoid required onboarding, long forms, or preferences that add effort before an exercise. Finish any remaining balloon-realism issues without changing its verified timing.

VERIFY: Use fictional records to test history before and after an app restart, repeated sessions, changed preferences, overrides of a suggestion, interrupted sessions, and clearing/resetting data where supported. Check the UI against the actual database. Confirm one user's single local history is not presented as clinical assessment.

Update the design rationale, MVC file map, data documentation, evidence log, AI-use disclosure, and handoff. Record a real revised approach and the evidence behind it when one occurs.

======================================================================
PHASE 9: RUN THE REQUIRED EVALUATION
======================================================================

Read the assignment, project instructions, current design, verification notes, and handoff. Use only fictional scenarios.

CHECK: Create an evaluation table with at least fifteen distinct scenarios. Record each input/action, expected result, execution mode, observed result, evidence link, and pass/fail/unverified status. Include ordinary use, interruptions, and failures.

Cover at least:
1. First chat with a fictional college-student situation.
2. Direct breathing entry without disclosure or a model wait.
3. Chat leading to a user-chosen grounding exercise.
4. A complete breathing sequence and measured whole duration.
5. Complete 5-4-3-2-1 grounding with stated timing assumptions.
6. Pause/resume during both inhale and exhale.
7. Leaving an exercise and accurate interrupted-session persistence.
8. Choosing and recalling a different balloon color.
9. History and conversations surviving a restart.
10. Repeating a recent skill and overriding its suggestion.
11. Switching to and from the simpler or reduced-motion experience.
12. Model timeout or unavailable network.
13. Malformed or instruction-conflicting model output.
14. Fictional crisis-related text and the documented application response.
15. Missing configuration, mocked mode, and honest live-mode status.

Also define and test three separate behaviors across cases:
A. Support access stays visible and usable, including during loading and model failure.
B. The user can choose, pause, stop, or change direction without a forced conversation or penalty.
C. Application-owned exercise steps, breathing timing, and persistence rules remain intact regardless of model output.

TAKE ACTION: Run repeatable checks with saved or mocked responses. Perform actual browser interactions and database inspections where needed. Repeat a small, relevant selection of live-model cases to examine variation, clearly labeling these separately from mocked results.

Peer testing uses mocked responses by default. If live peer calls are used, enforce a host-set session limit of no more than fifty provider calls, counting actual attempts including retries, and return to clearly identified mocked responses when the limit is reached.

VERIFY: AutoLoop: run the agreed checks, inspect failures, make the smallest in-scope corrections, and retest, stopping at the class limit. Preserve expected-versus-observed evidence and any real failed or revised approach. Report a surprising finding and a limitation that remains untested. Never invent a passing result or a failure history.

Update the evaluation results, evidence log, verification instructions, design changes, AI-use disclosure, and handoff. Keep only a curated, redacted selection of useful evidence.

======================================================================
PHASE 10: FINAL DEMONSTRATION AND PART 3.3 SUBMISSION
======================================================================

Read the assignment and the actual repository state. Review the existing milestone reports and Part 3.3 draft if present, along with the evaluation results, design notes, AI-USE.md, and handoff.

CHECK: Audit every Part 3.3 requirement against actual files and evidence. Confirm both agreed skills are complete, the realistic balloon matches the chosen design, and timing, model behavior, history, personalization, stopping, and independent support access work as documented.

TAKE ACTION:
1. Finalize README instructions so another person can run a clean checkout using the actual Vue, FastAPI, SQLite, and model configuration setup.
2. Prepare the complete final source version. Review the diff and observed checks, record the agent review, and identify any student review still required. Under the standing authorization, commit the verified feature branch, merge it into main with a clean working tree, and smoke-test main. Retain the exact resulting full source commit SHA.
3. Verify a clean checkout of that exact source commit in an explicitly scoped disposable directory under the project root, excluded from project tracking. Follow the README and use the standing dependency-installation authorization. Preserve the working database and do not copy uncommitted files into the checkout. Record what actually ran. If source code or run instructions change afterward, create and verify a new submitted source commit.
4. Create the finished-app demonstration and a process screencast showing one actual failure, the evidence used to understand it, and the resulting decision. Explain a relevant generated-code section, preferably how the exercise clock controls the balloon and pause/resume.
5. Use one recording with clear sections or two recordings. If recording tools are unavailable, prepare an exact short recording script, screen order, fictional inputs, and files to show. State that the recording is pending; do not claim it exists.
6. Finalize submissions/3.3/report.md with the repository URL, the exact source commit verified above, accessible design/evaluation/recording links, completed work, findings, remaining limitations, and unresolved items.
7. Verify AI-USE.md names the actual tools/models, identifiers or versions where available, and their roles. Keep the curated evidence log connected to prompts, changes, tests/browser observations, and decisions, including a failed or revised approach. Remove credentials, real personal information, research-participant information, and private third-party content.
8. Preserve the earlier submitted milestone reports and source checkpoints. Keep this as a localhost coursework prototype evaluated with fictional scenarios.

VERIFY: Confirm the exact submitted source commit passed the clean-checkout checks. Verify links, repository state, and report references. Review the final report/evidence-only diff, then commit that documentation separately under the standing authorization without changing the verified source reference. Push to the confirmed repository and verify the remote source commit and submission files. Reverify the source if a later change affects the application or its run instructions.

Return a concise submission-readiness table: requirement, evidence, and verified/pending status. Identify the exact report.md to upload for each milestone and the real recording links. Do not call the project finished while a required live verification, recording, source commit, or submission link remains pending.

