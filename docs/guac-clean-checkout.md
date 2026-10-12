# Guac exact-source clean checkout

Verified source **7c7742b1da5be66ea6a3bae9cb5ab4d7babcb1a2**, fetched from the real public remote and checked out detached in `/Users/jakebutler/Documents/ChatGPT/Mental Health/.verification/guac`. [Machine record](evidence/guac-clean-checkout.json). Parent Codex agent performed this run; another person's run remains pending.

Followed README: new `backend/.venv`, installed frozen requirements, copied only tracked blank `.env.example` to own ignored `.env`, `npm ci --prefix frontend`. No root/prior credentials, database or uncommitted files copied. Clone created its own empty default SQLite. Root canonical database preserved.

Actual results: **54 backend tests, 20 frontend tests, 20 general evaluation and 26 Guac evaluation cases pass**; Vite production build passes; npm reports zero vulnerabilities. Expected upstream Starlette/httpx deprecation warning remains. Clone Git status empty after evaluation/build/browser; SHA unchanged. Source-index publication audit passes with explicit pending-report allowance because final report fields are written in the following documentation commit. The final publication set is audited strictly without that flag.

Actual Chrome smoke: fresh Guac/default mock; fictional roommate looping thoughts → grounding/reflection/reason; deliberate breathing alternative → default green balloon; pause/stop saved locally. SQLite chosenbreathing/recommendedgrounding stored separately; FK check clear. [Chat](evidence/guac-clean-checkout-chat.jpg), [balloon](evidence/guac-clean-checkout-balloon.jpg). This is a smoke test, separate from full measured exercises in [browser observations](guac-browser-observations.md).

Afterward stopped only owned clone processes, restored root localhost8001/5174 default mock and existing canonical history/preferences. Clone remains ignored for reproducibility. No source or run-instruction edits after this verification. Historical [clean checkout](clean-checkout.md) retains its original SHA.
