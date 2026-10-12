> HISTORICAL INSTRUCTION — superseded by [Part 3.1-only scope](12-part31-scope-correction.md). Preserve as evidence; do not execute later phases or automatic continuation.

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
