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
