# Read-only reuse audit — October 12, 2026

Confirmed new root: /Users/jakebutler/Documents/ChatGPT/Mental Health. Initial state: only .git, unborn main, no tracked files or configured remote. No existing unfinished application or handoff. Ancestor /Users/jakebutler/README.md says only “# instagram-card”; no relevant ancestor AGENTS found.

Confirmed reference root: /Users/jakebutler/Documents/ChatGPT/Expedia-lite, readable. Read README.md, AGENTS.md, handoffs/current.md and relevant source. No prior app run, database inspection or modification occurred. Historical test/live claims in its handoff are documentary evidence, not observations repeated today.

| Actual reference file | Reuse decision |
|---|---|
| frontend/package.json; vite.config.js | Vue/Vite scaffold pattern. Declares Vue 3.5.42, Vite 8.2.2, plugin 6.0.8, Leaflet 1.9.4. Dependencies are declarations, not new-project installed packages. Omit Leaflet. Verify approved versions/runtime later. |
| frontend/src/App.vue | Composition API, loading/disabled submit/error/history patterns. Monolithic travel/map UI is unsuitable for copying wholesale; extract patterns into small new views. |
| frontend/src/hotelInsights.js | Injectable fetch and response-validation/error patterns; replace hotel contracts; add abort/stale-result protection. |
| backend/app/config.py | Explicit python-dotenv load from backend-local .env; os.getenv normalizes values; process environment can take precedence. Reuse pattern only with own path/config. |
| backend/app/openrouter.py | httpx REST transport, 20-second timeout, sanitized failure types, explicit model and no automatic paid fallback. Replace Expedia title, SQL/answer stages and hotel prompts with constrained conversation contract. |
| backend/app/main.py | create_app, lifespan, per-request connection dependency, CORS and typed routes/error mapping patterns. Replace domain routes and startup seed. |
| backend/app/database.py | SQLite Row, enforced foreign keys, per-request connection and transactions; cross-thread cleanup rationale is useful. Replace travel schema/CSV seed entirely. |
| backend/app/hotel_insights.py | Injectable requester/controller test seam and input validation. Two-call generated-SQL pipeline is not suitable; use fixed app queries for context. |

Provider reference is OpenRouter at https://openrouter.ai/api/v1/chat/completions. Source restricts model to NVIDIA Nemotron :free slugs. Read-only safe configuration inspection found backend/.env present, OPENROUTER_API_KEY nonempty (value never printed), OPENROUTER_MODEL = nvidia/nemotron-3.5-lightning:free. This verifies a file-selected model, not effective process configuration, key validity, present catalog availability/pricing, or successful live access. Prior README says this was a user-approved substitute, not a verified exact class demonstration slug. Do not silently claim it is the exact instructor model.

Requirements manifest: fastapi>=0.116,<1; uvicorn>=0.35,<1; pytest>=8.4,<10; httpx>=0.28,<1; python-dotenv>=1,<2. New project has no manifests or environment yet. No credentials/database copied. Verify provider choice/catalog and arrange separate backend-local credentials during configuration checkpoint; never expose secrets to frontend, logs, prompts or recordings.
