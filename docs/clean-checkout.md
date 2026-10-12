> HISTORICAL EVIDENCE. Current [Part3.1-only scope](../prompts/12-part31-scope-correction.md) supersedes earlier audience and automatic continuation. Preserve these observations tied to earlier source; do not expand later stages.

# Exact-source clean checkout verification — October 12, 2026

Verified source commit: **8497873908b4318be2a1b8112c0401f466cd695b** ([source](https://github.com/jakebutler22/Mental-Health/tree/8497873908b4318be2a1b8112c0401f466cd695b)). This is the main merge checkpoint, not a guessed hash or an uncommitted working tree. Clone directory: `/Users/jakebutler/Documents/ChatGPT/Mental Health/.verification/checkout`, ignored by outer project.

Commands actually run from the outer root:
```bash
git clone --branch main https://github.com/jakebutler22/Mental-Health.git .verification/checkout
git -C .verification/checkout checkout --detach 8497873908b4318be2a1b8112c0401f466cd695b
```
Initial clone Git status was empty; no credentials, database or uncommitted source copied. From that checkout followed README:
```bash
python3 -m venv backend/.venv
backend/.venv/bin/python -m pip install -r backend/requirements.txt
npm ci --prefix frontend
backend/.venv/bin/python -m pytest -q
npm --prefix frontend test
npm --prefix frontend run build
PYTHONPATH=backend backend/.venv/bin/python scripts/evaluate_backend.py
cp backend/.env.example backend/.env
backend/.venv/bin/python -m uvicorn app.main:app --app-dir backend --host 127.0.0.1 --port 8001
# Separate terminal, same checkout:
npm --prefix frontend run dev
```

Observed: installation succeeded with fresh project environments (cached registry wheels permitted, no old environment copied); npm zero audit vulnerabilities. Backend30tests passed with known upstream deprecation warning, frontend15tests passed, eval20/20, Vite7.3.7 build passed. Identical generated evaluation output did not dirty source; Git status after checks empty. Runtime/database/config/dependencies ignored.

Stopped only owned root test processes to free default8001/5174, then started exact clone source using README commands. Chrome displayed default mock/red/full-motion/empty history; fictional assignment-deadline input returned bounded workload acknowledgement and choices. Direct breathing, pause and stop worked, support stayed visible, console warning/error log empty. SQLite contained1conversation/2messages/1request/1stopped linked session; foreign_key_check empty. Backend fully restarted; rows/counts preserved. [Actual record](evidence/clean-checkout.json), [browser screenshot](evidence/clean-checkout-smoke.jpg).

No source code/run instructions changed after this verified SHA. Later reports/evidence/handoff changes are documentation-only and preserve this reference. Agent clean-checkout/main-source smoke is complete; **another person's independent run remains pending**, as do successful live output variation and recordings. No student review inferred.
