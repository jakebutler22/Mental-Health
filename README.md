# Campus Pause

Individual Assignment 3 coursework skills prototype for fictional college-student scenarios. Required stack: Vue frontend, Python/FastAPI backend, SQLite, localhost. This design does not diagnose, provide therapy, imply monitoring, or offer real mental health support. Do not deploy it.

Status: Part 3.1 documentation/design stage. No working app, installed project dependencies, database, or runtime commands exist yet. Title is provisional; folder remains Mental Health.

Start with [assignment source](docs/assignment-source.md), [working rules](docs/class-working-rules.md), [design](docs/design-pipeline.md), [flow](docs/design-flow.svg), [screen mockup](docs/screen-mockup.html), [verification](docs/verification.md), [reuse audit](docs/reuse-audit.md), and [handoff](handoffs/current.md).

Organization: frontend/ and backend/ are structural placeholders; docs/ contains design/evidence; prompts/ contains numbered instructions; submissions/3.1/report.md is the milestone report; AI-USE.md records tool roles. README run instructions will be verified against a clean checkout during 3.3.

Selected skills: six cycles of four-second inhale/six-second exhale and 5-4-3-2-1 sensory grounding. Short opening chat is optional; direct exercise entry never waits for the model. SQLite will persist conversations, messages, exercise sessions and optional preferences. History will show transcripts and session outcomes.

Independence plan: own backend/.venv, frontend manifests/lockfile, ignored backend/.env, and backend/data/campus-pause.sqlite3. Proposed ports 8001/5174 avoid the earlier app's 8000/5173; availability is unverified. Explicit local API URL and CORS match those ports. No imports or symlinks into the earlier project. Necessary project-local installation has standing user authorization; record exact commands and environments.

Milestones (Eastern, 11:59 PM): 3.1 October 15, 3.2 October 22, 3.3 October 29, 2026. Repository URL and submitted source commit are pending; this package is not submission-ready.
