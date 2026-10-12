# Guac — Part 3.1 Research and Design

Guac is designed for general everyday use: a short optional conversation and direct access to paced breathing or sensory grounding. Review examples are fictional busy days, work presentations and difficult conversations. The current deliverable is **Part 3.1 only**. Parts 3.2 and 3.3 are pending until requested; earlier autonomous continuation instructions are superseded.

Start with the [design specification](docs/design-pipeline.md), [reviewable mockup](docs/screen-mockup.html), [flow diagram](docs/design-flow.svg), [design verification](docs/part31-verification.md) and [Part 3.1 report](submissions/3.1/report.md). Public repository: [Mental-Health](https://github.com/jakebutler22/Mental-Health). Source publication does not deploy Guac or submit coursework.

## Review the artifacts

GitHub renders the SVG flow diagram and PNG design captures directly. Download the repository and open `docs/screen-mockup.html` in a normal browser for the static desktop/mobile design. Its labels represent proposed states; it does not call a model, start timed exercises or save data. The relative balloon image uses the preserved original local asset.

Optional local static preview, requiring only Python's standard library:

```bash
cd "/Users/jakebutler/Documents/ChatGPT/Mental Health"
python3 -m http.server 5175 --bind 127.0.0.1
```

Open `http://127.0.0.1:5175/docs/screen-mockup.html`. Stop the preview with Ctrl-C. No Vue/FastAPI install, database or model credential is needed to review Part 3.1.

## Design boundaries and preserved work

Planned stack: Vue, FastAPI, SQLite and localhost. The model proposes one allowed skill with a short reflection/reason; deliberate user selection starts it. Fixed steps, timing, pause/stop and persistent support belong to the application. No diagnoses, clinical scores, fix promises or monitoring. Intended everyday use is a product direction, not evidence of clinical effectiveness or production readiness.

Existing `frontend/`, `backend/`, tests and later reports were created under the earlier broader scope and remain preserved. This revision changes audience copy only in that code; it does not expand functionality. Historical verification applies to the exact earlier source identified in its evidence, not automatically to this revision. [Implementation README archive](docs/implementation-readme-archive.md) retains earlier run instructions; [status distinction](docs/part31-verification.md) separates proposed design, preserved code and current checks. Do not automatically run later evaluations or complete later milestones.

Current authority: [scope correction](prompts/12-part31-scope-correction.md), [AGENTS](AGENTS.md), [handoff](handoffs/current.md). Assignment provenance and R/D findings: [source summary](docs/assignment-source.md). AI tools and roles: [AI use](AI-USE.md). Curated evidence: [log](docs/evidence-log.md).

Part 3.1 is due October15,2026 at11:59PM Eastern. Student review and LMS submission remain human actions. Complete the verified design checkpoint and stop.
