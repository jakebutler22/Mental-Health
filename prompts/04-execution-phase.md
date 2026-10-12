PHASE 4: CONFIGURE THE MODEL AND VERIFY HEALTH
======================================================================

Read the current project instructions and handoff. Inspect the existing class provider configuration pattern without revealing key values. Use already available authorized model access where possible; missing live credentials do not block deterministic implementation or mocked evaluation.

CHECK: Identify the intended backend-local configuration file, exact variable names, selected provider/model identifiers, and how the backend currently loads settings. Confirm .gitignore excludes secrets and inspect whether any secret-bearing file is already tracked.

TAKE ACTION: Implement configuration loading and a safe health endpoint only. Reuse the existing class provider setup where suitable. Create an example configuration with blank secret values and document where I should enter the real key locally. Do not copy the old project's .env wholesale or put credentials in the frontend.

Runtime credential access is covered by my authorization to reuse the existing class model setup. Prefer an already configured process environment. If needed and accessible within scope, a local runner may read only OPENROUTER_API_KEY from the explicitly identified prior project's ignored backend/.env and pass it privately in the new backend process environment. Do not print the value, embed it in command arguments or recordings, copy the old .env wholesale, persist that prior secret into this repository, or search unrelated credential locations. This is a temporary verification setup, not an application dependency on the old project; the new app must independently accept its documented environment/configuration. Keep actual credentials out of source and public Git history. If authorized live access is still unavailable, complete mock-backed work and mark live verification pending.

The health response must report configuration availability without revealing values. Distinguish mock mode, missing configuration, and configured live mode. Document restart requirements. Keep the deterministic exercises and crisis-support route available regardless of configuration status.

Do not add the model controller, model route, or frontend integration in this prompt. Use the standing installation authorization if a necessary dependency is missing.

VERIFY: Run the backend and open the actual health endpoint in the browser. Check configured and missing-configuration behavior using safe temporary test settings. Record the observed response and actual address. A configured key is not evidence of a successful provider request.

Save the prompt and update the verification notes, evidence log, and handoff. Perform the endpoint inspection, record its result and a short reproducible inspection step, then continue to the next phase.

======================================================================
