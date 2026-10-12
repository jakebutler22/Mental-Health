> HISTORICAL INSTRUCTION — superseded by [Part 3.1-only scope](12-part31-scope-correction.md). Preserve as evidence; do not execute later phases or automatic continuation.

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
