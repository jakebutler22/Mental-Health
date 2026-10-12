Continue in the confirmed project root:
"/Users/jakebutler/Documents/ChatGPT/Mental Health"

Your audit reported an initialized Git repository on main with no commits and only .git. Recheck that state once. An unborn main branch is a valid starting state. Read README.md, AGENTS.md, and handoffs/current.md only if they now exist. Keep this project in its current folder and quote paths containing spaces.

This prompt supplies the missing assignment context and authorizes the Part 3.1 documentation and design work. Use the supplied brief below; do not require the absent screenshots before doing this work. When later prompts say "read the assignment," use the source documents created here.

CHECK

1. Confirm the root, files, Git state, and any configured remote without changing them. Follow any applicable workspace instructions.
2. Check whether this historical prior-project candidate currently exists and is readable:
   "/Users/jakebutler/Documents/ChatGPT/Expedia-lite"
   This path was used previously; it has not been verified as current.
3. If accessible within the permitted workspace scope, inspect relevant README/AGENTS files, manifests, Vue components, FastAPI controllers, configuration-loading code, and SQLite helpers read-only. Identify reusable components and evidence of any conversational-model integration. Distinguish provider references in code from a verified selected provider/model and from successful live access.
4. Do not run or modify the earlier application, install into it, copy its database or credentials, or print secret values. If the candidate is missing or inaccessible, record that finding and continue the design with reuse and provider details pending. Do not search the whole computer or substitute another project silently.
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
3. Ask before dependency installation; show missing packages, exact commands, and target environments.
4. AutoLoop: run the agreed check, inspect failure, make the smallest in-scope fix, and rerun. Stop when passing, after five correction cycles, or when extra permission is required.
5. SmokeTest observes the actual browser without editing. "AutoLoop: run the smoke test" authorizes scoped fixes and retests.
6. Map MVC responsibilities to real or explicitly planned files and define controller inputs/outputs.
7. Inspect actual database records and relationships before/after relevant CRUD operations using disposable test data; verify persistence after restart.
8. Define business rules with ordinary and boundary examples.
9. Keep secrets in ignored backend-local configuration; never expose them in frontend code, prompts, logs, or recordings.
10. Explicitly load backend configuration and provide a safe health check. Configured credentials and a successful provider request are separate facts.
11. Keep API configuration, controller, and route work in separate prompts with manual inspection checkpoints before frontend integration.
12. Prove one known-input round trip before expanding to real input. Verify loading, no-result, failure, stale-result, and repeated-click behavior.
13. Review visual references and the proposed design before implementation. Verify both appearance and behavior.
14. Make coherent verified Git checkpoints. Review diffs and personally try applicable behavior before commits. After the initial main checkpoint, use feature branches; verify, review, commit, push, merge completed work, test main, and push main. Preserve unfinished changes and show conflicts/proposed resolutions before proceeding.
15. Maintain docs/design-pipeline.md, docs/verification.md, numbered prompts, and handoffs/current.md. Ground the handoff in actual branch/files/commit state, completed and unfinished work, checks run, and next task.

TAKE ACTION

Complete the missing reuse inspection where possible, then create the Part 3.1 design package now. Unverified reuse/provider details should remain documented implementation dependencies while design work proceeds.

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

Do not install dependencies, implement the working app, initialize another repository, change remotes, commit, push, or deploy in this step.

VERIFY

Check the design package against every Part 3.1 requirement and verify that the files expected by Prompt 3 exist. Distinguish source requirements, selected design choices, verified local findings, and unresolved dependencies.

Return:
1. Files created or changed.
2. Requirement-to-design/evidence mapping for Part 3.1.
3. Verified reuse findings, with provider/model status stated precisely.
4. Checks actually performed and what remains unverified.
5. The concrete design/diff items for my review before the initial source commit.
6. The next action: design review and the initial reviewed source checkpoint, obtain or verify the real repository URL, then continue with Prompt 3.

Report "Part 3.1 design package prepared" only if it is complete. Do not report submission-ready while required repository/commit fields or design evidence remain pending.