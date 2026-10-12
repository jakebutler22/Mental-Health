# Assignment 3 source


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

Explain design choices using R1–R4 and D1–D6, including alternatives and tradeoffs. A user-selected simpler view is our possible response to D1, not a finding that the study established reliable distress detection. The general everyday audience is a project design choice; the supplied study does not establish effectiveness for that audience.

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


## Current selected direction

The latest user scope is [Part 3.1 only](../prompts/12-part31-scope-correction.md). Guac is intended for general everyday use. Fictional busy days, work presentations and difficult conversations are review examples, not a restricted product audience. Avocado identity, contextual optional chat, direct breathing/grounding, green realistic latex balloon (red optional),4-second inhale/6-second exhale/six cycles and equally timed reduced motion are retained design choices. Current [design](design-pipeline.md) distinguishes proposals from preserved implementation. Earlier education-specific direction is historical and superseded. No later milestone is authorized until requested.
