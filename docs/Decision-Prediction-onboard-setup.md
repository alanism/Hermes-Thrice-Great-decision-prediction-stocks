# Decision Prediction setup and owner manual

Document version 0.4 · Updated 2026-10-09 UTC

This manual explains what the reviewed Decision > Prediction setup can do, how to choose analytical perspectives, and how to distinguish a successful calculation from a complete investment research report. It revises version 0.3 for public customer use. Start with synthetic inputs and an on-demand report. Recurring reviews and private-data workflows require their own setup.

**Current status:** a pinned, patched, read-only Python adapter has recorded verification evidence. A supervised research-to-engine workflow has also been exercised. This is not a portable installer, native assistant integration, autonomous broker connection, fully compliant report generator or demonstration of investment performance. This documentation update did not rerun the engine or create any runtime integration.

## First time setup

1. Read the [platform guide index](platforms/README.md) and [shared onboarding requirements](platforms/common.md). An assistant should proactively describe the available research lenses once it has verified access to them.
2. Identify the actual execution environment: managed cloud, VPS, local machine or local VM. Verify the code, Python runtime, allowed commands, file access and available sources. A chat interface or subscription alone does not establish code execution.
3. Begin with a reviewed synthetic example. Confirm that the result is successful and understandable before introducing private information.
4. Choose primary analysis lenses separately from risk/sizing discipline. Balanced analysis is a reasonable starting point when no preference is given.
5. Deliver one on-demand report with an explicit completeness check. Agree any recurring schedule separately.

Reading documentation does not install or register a tool. A first-use guide must be explicitly linked or supplied to the host; automatic loading is unverified until tested in that host. Each platform guide must describe this honestly.

## Choosing analysis lenses and risk discipline

The source contains eight original narrative playbooks: Galloway, Gerstner, Camillo, Laffont, Mauboussin, Buffett/Munger, Shkreli and Thorp. Scott Page is an additional many-model lens. The [shared inventory](platforms/common.md#the-lens-inventory) links the exact case-sensitive files.

A user can choose Gerstner and Laffont to lead technology/growth analysis, with Thorp-inspired sizing and survival checks. Another can choose Buffett and Munger to lead business-quality and valuation analysis. Preferences change emphasis and explanation, not the underlying facts, recorded calculations or safety constraints. Do not assume that a preferred investor’s historical concentration, leverage or payoff assumptions suit the user.

Ask for the analysis lens preference and the relevant risk constraints separately. Establish horizon, liquidity needs, leverage restrictions, concentration limits and tolerance for loss before presenting portfolio sizing as useful for that user. Choosing a style does not authorize a trade or borrowing.

A full report retains all eight original perspectives and a separate Page section, with dissent and binding constraints. A focused request may be labeled Single-lens analysis or Focused lens comparison; it remains a partial view and must retain material contrary evidence. Simulated narrative consensus is not eight independent engine runs or calibrated votes.

Every panel must say that these are simulated analytical perspectives inspired by repository playbooks, not statements, advice, endorsements or participation by the named people or firms. Avoid fabricated first-person quotations.

## What is supported and what is conditional

| Capability | Reviewed status |
| --- | --- |
| Deterministic calculations from supplied cases | Exercised through the reviewed read-only adapter |
| Synthetic validation, analysis and comparison | Recorded full-suite and adapter-smoke evidence; see verification scope below |
| Portfolio CSV/JSON import and validation | Allowlisted, returns JSON; real portfolio ingestion and a first-user mapping walkthrough are not validated here |
| Narrative playbook review | Files available at the reviewed source; generated commentary must still be grounded and labeled |
| Public research plus privately prepared inputs | Exercised as a supervised host workflow; not adapter-native live retrieval |
| Registered method-pack inventory | `core`, `thorp`, `mauboussin`, `contrarian_filings`, `committee`, `page` |
| Arbitrary method-pack execution through this adapter | Not exposed; `method list` is available, `method run` is not in its allowlist |
| Formal belief-update writes, recommendation generation and decision-record writes | Outside the read-only adapter allowlist |
| Broker authentication, trade execution, native assistant plugin, daemon or cron | Not provided by this adapter |
| Recurring reports | Conditional on separate, explicitly chosen and verified host scheduling |
| Portable customer installation | Not yet established by the reviewed workspace evidence |

A capability declaration describes an expected interface, not installed OCR, browsing, authentication or scheduling. A full upstream engine may support functions unavailable in the reviewed adapter. Check the actual exposed command boundary before making claims.

## Source identity and verification scope

Reviewed repository: [alanism/Hermes-Thrice-Great-decision-prediction-stocks](https://github.com/alanism/Hermes-Thrice-Great-decision-prediction-stocks/tree/5bfe72972ee9b3ade55923e5419ca7ede1ac70ba).

- Base commit: `5bfe72972ee9b3ade55923e5419ca7ede1ac70ba`
- Adapter identity: `aya-stock-readonly-v1`
- Local patch identity: `windows-path-containment`
- Patched source: `plugins/capital-decision-lab/capital_decision_lab/privacy/containment.py`
- Added regression tests: `tests/contracts/test_foreign_path_containment.py`
- Recorded runtime: Linux x86_64, Python 3.12.14
- Declared Python range: 3.11–3.13; other versions not verified here
- macOS and native Windows: untested; the adapter’s POSIX timeout is a portability gap
- Hermes 0.16.0 runtime: not installed or tested in this verification environment

The passing candidate included an uncommitted containment patch and external adapter bundle. The linked commit alone is not that candidate. A public customer release must package the exact reviewed source, patch, manifest, adapter, fixtures and instructions before claiming reproducibility. This manual is not that bundle.

Recorded evidence from the previous setup manual:

| Evidence set | Result | What it does not establish |
| --- | --- | --- |
| Guarded upstream pytest on patched source | 340 passing tests, including two added containment regressions | Investment accuracy or all operating systems |
| Adapter smoke | 11 passing groups | Fresh customer installation or live account integration |
| Earlier arithmetic review | Eight expected-result assertions | A separate full-suite pass |
| Supervised research example | Seven read-only adapter calls across initial and scenario cases | Broker authentication or automatic portfolio ingestion |
| Report calculation checks | 19 initial checks, 52 scenario checks and 35 independent arithmetic assertions | Full research/report specification compliance |

These counts describe different scopes; do not add them into a single homogeneous test total. They are retained historical evidence, not checks rerun for this document. The earlier partial harness and the initial failing full-suite attempt are superseded by the final recorded patched-suite result.

Implementation tests do not establish calibration, profitability, suitability, complete portfolio risk modeling or faithful use of every research lens. Existing report review found omitted required lens commentary and other incomplete sections. Subsequent commentary repairs do not prove that the entire skill was applied. Use the completeness gate below rather than inheriting a blanket compliance claim.

Review the repository’s [LICENSE](../LICENSE) for the intended use. Do not assume that personal evaluation permission covers hosting, redistribution or a commercial product.

## Calculation boundary and safe first run

The adapter is a Python shell wrapper. It checks source hashes and inventory, restricts command prefixes, requires an existing contained input directory, and applies a POSIX timeout. Its guardrails block network access, subprocesses and ordinary writes during normal invocation. They are defense in depth, not a replacement for an appropriately restricted execution environment.

The current allowlist is:

- `validate --synthetic`
- `analyze --case …`
- `compare --case …`
- `portfolio import --file …`
- `portfolio validate --file …`
- `method list`
- `host capabilities`

`--assumption-update` is blocked. The adapter does not create an input directory, save a portfolio database or write a report. Input preparation and report persistence are separate host actions.

Once a reviewed bundle is actually available, the following is an illustrative invocation pattern, not an installer or a command ready to paste unchanged:

```text
<approved-python> -I -B <reviewed-adapter>/capital_adapter.py \
  --local-root <existing-approved-input-directory> \
  analyze --case <contained-synthetic-case.json>
```

Replace the placeholders only after verifying the actual bundle and paths. The historical adapter contained a fixed repository path; relocation needs a reviewed configuration change and regression checks. Do not merely copy it to another machine and assume it works.

For the first run:

1. Validate bundled synthetic contracts and inspect nested issues.
2. Run the bundle’s smoke checks, including containment, blocked commands and repeatability.
3. Analyze and compare the synthetic case.
4. Require a zero exit code, `result.status: ok`, empty issues and the expected source identity.
5. Retain stdout, stderr, command, input identity and output identity in the chosen private evaluation destination.
6. Confirm key arithmetic, units and unavailable fields before explaining the result.

A nonempty JSON response is not proof of success. An unavailable metric is not zero. Capture early source/path errors and timeouts even when they occur outside the normal JSON error envelope. Do not bypass guards, invent confirmation, or regenerate a manifest blindly to make an example pass.

## Evidence labels and data provenance

Use these exact customer-facing labels at each applicable figure or claim:

- **Measured:** a sourced observation with an as-of time and the required verification. Screenshot-derived values require genuine user confirmation of the exact extraction first. Until then label them **Observed transcription · unconfirmed**, not Measured. Confirmation does not independently authenticate the broker or prove freshness.
- **Calculated:** deterministic arithmetic with formula, units and input references. Retain input limitations; arithmetic does not authenticate its inputs.
- **Modeled:** a hypothetical or assumption-dependent output. Use **Modeled · calculated in Python** when appropriate. State probabilities, horizon, benchmark, constraints and omitted risks.
- **Forecasted:** a forward-looking estimate or belief with its source/author, horizon and uncertainty. Company guidance is company-provided forecast, not realized performance.

Keep qualitative Narrative and Unknown/unavailable visibly distinct. Preserve the engine’s schema classes and fields alongside these reader labels; never rewrite raw provenance to make a report look stronger. Missing and stale inputs remain missing and stale.

The original skill is stricter than the former manual’s screenshot wording: user confirmation is required before screenshot-derived values become Measured. A legacy report that used Measured with an unconfirmed caveat must disclose or correct that gap. A report repair does not retroactively create confirmation. User verification must come from a genuine interaction identifying the exact values, not a manually set flag or synthetic authorization object.

## Updating beliefs and keeping a decision diary

Use the sequence prior belief → new evidence → revised belief → decision or no change. Preserve dated evidence, uncertainty, contrary observations and the reason for the change. Keep publication/as-of, retrieval, capture and review times separate.

A formal numerical Bayesian update requires genuinely `user_verified` evidence, a matching thesis sensitivity rule for direction, an explicit prior and likelihood model, dependence assumptions, the configured update cap and an actual calculation. Pending or rejected proposals cannot alter beliefs. The read-only adapter does not expose belief-update writes. If the gate is incomplete, describe a qualitative belief revision and visibly mark the formal update not run.

A Polymarket quote is an observed market price at a time; the implied event expectation is a participant forecast, not automatically the analyst’s calibrated probability. Compare only the same contract, outcome, resolution horizon and quote field. Preserve question, resolution rules, identifiers when available, source URL and retrieval time. Flag thin liquidity, missing rules, stale displays and contract changes. The first snapshot is a baseline, not a week-over-week change.

Do not double-count correlated headlines and market prices as independent evidence. Do not map macro event probabilities directly to stock-return scenarios or allocations. A decision diary records reasoning; it is not trading authorization. Agree private persistence and retention before saving sensitive inputs or a durable decision record.

## Supervised host to engine workflow

1. **Define the question.** Set decision scope, reporting cutoff, horizon and benchmark. A cached quote is not an authenticated live exchange feed.
2. **Prepare authorized inputs privately.** Extract only necessary fields, reconcile units and totals, and obtain required value-specific confirmation. Keep account inputs out of public queries, examples and source control.
3. **Build cases with explicit provenance.** Separate observations, assumptions and unavailable information; preserve source references, timestamps, hashes and units. Unconfirmed observations must not be promoted into the confirmed-input workflow.
4. **Run the available calculations.** Use only allowed commands and contained case files. Save returned results unchanged in the authorized destination. Identify precisely which engines or supplemental Python calculations ran.
5. **Check independently.** Verify arithmetic, denominators, input/output identities, seed and horizon. Explain output wording that is too broad for a synthetic or scenario input.
6. **Add analytical perspectives.** Use the actual playbooks, grounded in the same dated evidence. For each lens, explain support, strongest objection, missing inputs and what would change the view. Preserve disagreement.
7. **Apply the full-report gate.** Report missing work visibly. Preview the result, check navigation and ensure no simulated statement is attributed to a real person.
8. **Deliver and review.** Explain uncertainty, financing/covariance gaps and alternatives. A successful calculation does not authorize trade execution, external sharing or durable decision writes.

## Metric interpretation

- **Scenario Sharpe:** the inspected risk module uses population standard deviation. Probability-weighted possible states are not historical observations. Match the return horizon, benchmark and annualization; do not call prospective scenario statistics empirical risk estimates.
- **Convexity:** weighted positive payoff divided by absolute weighted negative payoff describes payoff asymmetry. It is not option gamma or proof of edge. Endpoint ratios and break-even probabilities have narrower meanings. The worst supplied state is not maximum possible loss.
- **Kelly:** the adapter’s stock interface is binary. A separate multi-outcome optimizer must be labeled supplemental, not attributed to the adapter. Distinguish raw, confidence-adjusted, fractional, clipped and capped results. Omitted tails, financing assumptions and uncertain probabilities can materially change the result.
- **Margin:** the simplified model is not broker cross-margin truth. Broker rules, collateral, liquidity and financing may differ. Margin danger takes precedence over attractive Kelly output.
- **Simulation:** record seed, distribution, horizon and iterations. Seeded reproducibility does not validate normality or tail behavior.
- **Portfolio context:** a standalone stock-versus-cash model does not establish an optimal multi-asset allocation without covariance, financing costs, collateral rules, taxes, liquidity and user constraints.

## Full report completeness gate

Before saying the tool was fully applied, read the entire [skill](../skills/decision-prediction/SKILL.md) and [canonical anatomy](../skills/decision-prediction/references/monocle-report-anatomy.md). Retain the fixed section order below. For every item record **Completed**, **Not run**, **Unavailable**, or **Not applicable**, with a reason and consequence. A missing input may justify unavailable content; it never justifies an invented result or silent omission.

1. **Position:** dated inputs, units, source freshness, required screenshot confirmations and evidence labels. No fictitious holdings for a public-company-only report.
2. **Frameworks:** Porter’s five forces, Helmer’s seven powers and Business Model Canvas, grounded in sources.
3. **Bayesian Update:** market evidence and qualitative belief revision; prior/likelihood/posterior only when formal gates are satisfied.
4. **Sharpe and Kelly:** return/risk metrics and sizing stages with assumptions, formula references and limits.
5. **Engines:** exact calculations invoked, inputs, source/version identity and retained outputs; distinguish supplemental Python.
6. **Convexity:** required four-state Bear/Base/Bull/Moonshot analysis and ratios, or explicit missing-state/metric disclosure. Do not relabel a three-state model as complete.
7. **Simulation:** actual seeded run and parameters, P5/P50/P95 and mean terminal result, or not run/unavailable.
8. **Margin:** supplied balances, maintenance assumptions and stress results, or unavailable/not applicable. Do not imply brokerage verification.
9. **Options:** dated strikes, expiries, asks and breakevens if available; otherwise disclose unavailable chains.
10. **Barbell:** supported structure/alternatives and relevant constraints, without implying suitability or permission to execute.
11. **DLC:** all eight original simulated perspectives, dissent and synthesis; add Page separately. State exactly what is commentary and whether any executable packs ran.
12. **Metrology:** actual usage and measured cost where available; separate estimates with current verified prices. Never reuse historical price/cache tables as current facts. Check the skill’s static/dynamic cache separation when an external model call is made; do not claim caching or savings without evidence. Mark missing measurements unavailable.
13. **Verdict and decision receipt:** evidence, uncertainty, binding constraints, triggers to change the view and limitations. Keep a report’s human-readable decision summary distinct from any authorized engine record operation.

Also verify the required masthead/navigation, evidence sidebar and relevant charts without inventing absent data; preview at readable sizes; check links and output integrity; keep dated version history and a learning entry. A section heading alone does not satisfy its content requirement.

If work is missing, say “Partial Decision > Prediction report” and name the gaps near the summary. Completing all calculations is not enough. Adding every lens is not enough. Complete means the applicable requirements were actually satisfied, and conditional sections are honestly handled rather than silently dropped.

## Optional recurring reviews

These are selectable workflows, not defaults imposed on every customer:

- Five stocks per day from an agreed watchlist or portfolio list, with explicit rotation and event-priority rules.
- At least weekly refresh of the same chosen ticker report. META is an example, not a required holding or universal selection.
- A separate macro review with comparable market contracts and official statistics.

Before enabling, agree schedule and time zone, tickers, input freshness, report destination, permitted private-data use and retention. Verify the actual host schedule before announcing it is enabled; configuration evidence is not evidence of a completed run. The adapter does not install operating-system cron or create a daemon. Keep report identity stable with dated version history. Old prices remain dated old prices on weekends or when sources are unavailable.

Missing access or stale inputs must produce a visible gap, not fabricated analysis. Recurring research does not enable trades, external disclosure or new account access. Users can change or stop their chosen schedule separately from the read-only calculations.

## Known limitations and release gates

- Recommendation code uses the smallest position cap across holdings; clarify intended portfolio-wide versus per-position semantics before relying on it.
- The simplified margin code validates `cash_equity` but omits it from calculated equity; clarify semantics before use with an actual account.
- CSV capture time is import time; preserve the source snapshot date separately.
- Data flags alone do not prove genuine human confirmation or authorization.
- Built-in public URL retrieval needs DNS/redirect hardening and remains disabled in the reviewed adapter.
- A source card or pack catalog entry does not establish runtime access to that method.
- Hard-coded paths, timeout portability, dependency provenance, supported OS/Python combinations and clean-room setup/removal remain release work.

Before a customer release, package a uniquely identified complete bundle, reproduce synthetic success and blocked/malformed cases on a fresh environment, test rollback, review licensing and support ownership, and define explicit retrieval/confirmation/persistence boundaries. Keep a last-known-good bundle; review changed code and hashes before updating manifests. Never weaken containment merely to make an upgrade work.

## Troubleshooting

| Symptom | Safe response |
| --- | --- |
| Source hash or inventory changed | Review the upgrade or restore the reviewed bundle; do not blindly accept new hashes |
| Missing or relocated adapter/source files | Obtain the complete reviewed bundle and a validated path configuration |
| Missing input directory | Supply the existing authorized directory; the adapter does not create it |
| `PATH_ESCAPE_FORBIDDEN` | Use legitimate contained files; preserve containment checks |
| Invalid/malformed local document | Reproduce with synthetic data and validate the schema |
| `status: blocked` | Respect the allowlist; do not bypass it to run an unsupported action |
| Timeout or unsupported POSIX signal | Record the failure and platform limitation; do not claim portability |
| Missing live sources or host tools | Mark affected inputs and sections unavailable; continue only supported work |
| Lenses absent despite green calculation tests | Repair commentary and run the full report gate; do not claim historical completeness |

## Learning and version history

Keep a private, user-authorized decision diary separate from the public [customer lessons appendix](dot-onboarding-lessons.md). A useful entry records date, question, prior view, evidence, assumptions, calculation identity, strongest dissent, decision/no change, outcome when known, and the process lesson. Later outcomes should not rewrite the original reasoning.

### Version 0.4 on 2026-10-09

- Added proactive first-use lens discovery and separate analysis/risk preferences.
- Inventoried the eight original cards plus Page; distinguished commentary, executable packs and actual adapter calls.
- Added single-lens requests while preserving dissent and negative facts.
- Corrected screenshot-label guidance and made the formal Bayesian verification gate explicit.
- Added whole-skill report preflight and honest partial-report labeling.
- Removed owner-specific schedules, identities and workspace locations from the reusable customer edition.
- Preserved historical verification scopes and adapter limitations without claiming new runtime tests or full report compliance.

Versions 0.1–0.3 established the reviewed read-only adapter, containment repair, verification evidence, supervised case workflow, four-label system, belief diary and optional review scheduling. This edition retains their useful setup lessons while separating generic customer guidance from private deployment details.
