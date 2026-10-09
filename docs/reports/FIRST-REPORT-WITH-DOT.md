# Your first Decision ≥ Prediction report with dot

The first useful result should be an understandable decision brief, not a setup project. This is a proposed, testable onboarding flow using the [HTML report guide](HTML-REPORT-GUIDE.md) and [template](../../templates/stock-report/Stock-Report-Web-Template.html). It does not implement automatic installation or public hosting.

## Educational decision support

Decision ≥ Prediction is educational research and decision support. It presents evidence, exposure, assumptions and scenarios so users make their own decisions and predictions. It does not provide portfolio advisory, prescribe trades or allocations, or issue Buy/Hold/Add/Trim/Sell instructions. Older engine/schema names containing “recommendation” describe model artifacts, not personal advice; the dot reporting flow must not present them as recommended actions.

For optional portfolio context, recommend a redacted CSV or screenshot with names, account numbers and other identifiers removed before sharing. Keep only necessary holdings/exposure fields and the as-of date; verify extracted values. The project creator is not an intended recipient of inputs or outputs. The selected agent, model, storage or hosting provider may process or retain data under its own policies. Verify the actual workflow and destination; this documentation does not guarantee that all deployments are local-only or that a creator can never receive data. Do not upload private data to GitHub, public hosting or a new provider without required permission.

## One request to start

> Use Decision ≥ Prediction to research [company or ticker]. Start with public information and a balanced overview. Give me the decision takeaway, supporting evidence, strongest counterargument and what would change the conclusion. Use the HTML report template and clearly flag anything you cannot run.

A ticker is enough to begin public research. Portfolio information is optional and should not block the first useful result. Do not assume ownership, account size, liquidity needs, concentration limits, borrowing permission or risk tolerance.

## What dot should do

1. Verify access to the repository, source materials and the selected execution/delivery environment. Resolve supported setup steps within existing permission; ask only for missing access or required decisions. Explain what is available without claiming a native integration.
2. Ask one compact preference question: “Which company should we start with, and would you like a balanced view or a particular investor perspective? Is there a research horizon you want me to use?” Omit questions already answered. Explain that portfolio exposure and hypothetical sizing calculations need separate inputs if later requested, and are educational rather than allocation advice. Do not turn an analytical horizon into an inferred risk limit.
3. Bound the first edition: one company, public filings/company disclosures, dated market data if available, one explicit information cutoff, no private account data and no portfolio-specific recommendation. Label assumptions and unresolved items. Do not use stale observations as live prices.
4. Lead with a concise decision takeaway that distinguishes business quality, valuation and missing portfolio context. Provide the strongest disagreement, source trail and conditions that would change the conclusion. If evidence cannot justify a decision, make the conclusion “insufficient evidence” and identify the next needed fact.
5. Build the HTML reading edition with all eight original analytical lenses and Page, the canvas, powers and final generated sketchnote where supported. Keep it private in the authorized environment. Deliver a directly usable artifact through the supported private route; verify opening. If some capabilities are unavailable, provide the useful bounded brief now with explicit incompleteness, rather than inventing outputs or demanding repeated user coaching.
6. After the sample, recommend optional redacted portfolio CSV/screenshot context. Establish horizon, liquidity, exposure, leverage constraints and risk limits before illustrating hypothetical risk or sizing scenarios, without prescribing an allocation. Obtain required permission for any private data destination; never infer permission to send it to another provider.
7. Only then offer recurring research if wanted. Five stocks per day, a weekly chosen-company update and a weekly macro review are possible choices, not defaults. Agree the stock list/selection rule, timing, time zone, sources, destination, retention and costs where relevant. Create a schedule only after explicit user choice and verify its actual host registration. Documentation alone configures no automation.

## Later editions

Keep one report identity with dated versions. Lead with “what changed,” the new evidence, whether the analytical conclusion or the user’s recorded decision changed and why, including unchanged conclusions when warranted. Keep source snapshots and calculation provenance comparable. Rotate the final visual lens on authorized substantive editions according to the recorded sequence; retain all eight analytical perspectives. Never refresh private account figures by assumption.

## First-user acceptance test

Test a new user who provides only a ticker, without hidden setup knowledge. Success requires a useful public-data decision brief without repeated coaching; verified opening of the private artifact in the selected environment; source/audit traceability; explicit missing-data/runtime gates; no invented portfolio or risk limits; and faithful distinction between qualitative work and actual Python results.

Also test unavailable runtime, missing sources, image-generation failure, blocked artifact opening and interrupted onboarding. Preserve useful work, give the smallest supported next step and never claim an unavailable stage passed. If a recurring workflow is chosen, separately verify schedule creation and a successful scheduled delivery. No such end-to-end new-user acceptance test is established by these documentation changes.
