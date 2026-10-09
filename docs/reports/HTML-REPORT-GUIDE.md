# HTML-first stock research report

Version 0.1 · 2026-10-09 · Authoring specification, not a runtime integration

Start with the [reusable HTML template](../../templates/stock-report/Stock-Report-Web-Template.html) and the [dot first-report walkthrough](FIRST-REPORT-WITH-DOT.md). The template is an inert scaffold: placeholders, example components and missing images are intentional. It is not a completed report. No private report or supplied third-party style prompt is included.

## Educational use and privacy

Decision ≥ Prediction is educational research and decision support. It presents evidence, exposure, assumptions and scenarios so users make their own decisions and predictions. It does not provide portfolio advisory, prescribe trades or allocations, or issue Buy/Hold/Add/Trim/Sell instructions. Older engine/schema names containing “recommendation” describe model artifacts, not personal advice; the dot reporting flow must not present them as recommended actions.

For optional portfolio context, recommend a redacted CSV or screenshot with names, account numbers and other identifiers removed before sharing. Keep only necessary holdings/exposure fields and the as-of date; verify extracted values. The project creator is not an intended recipient of inputs or outputs. The selected agent, model, storage or hosting provider may process or retain data under its own policies. Verify the actual workflow and destination; this documentation does not guarantee that all deployments are local-only or that a creator can never receive data. Do not upload private data to GitHub, public hosting or a new provider without required permission.

### Scoped data-flow review

A source review at commit `5bfe72972ee9b3ade55923e5419ca7ede1ac70ba` found no creator collection endpoint or telemetry sender in the reviewed plugin, scripts and configuration. The built-in network connector uses user-directed public GET requests ([web connector](../../plugins/capital-decision-lab/capital_decision_lab/connectors/web_connector.py)); the [command dispatcher](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py) reads contained local inputs and prints outputs to its calling host. Explicit decision recording can write a [local ledger](../../plugins/capital-decision-lab/capital_decision_lab/recommendation/records.py). This is a scoped source finding, not an audit of every dependency, deployment, host, model provider or remote storage service, nor a guarantee against user-initiated sharing. These documentation/template changes add no telemetry or upload mechanism.

A minimal redacted CSV/screenshot can supply qualitative context, but it is not necessarily compatible with the current [portfolio importer](../../plugins/capital-decision-lab/capital_decision_lab/research/portfolio.py), whose schema requires eight fields including cash, borrowed amount and margin requirements. Validate the actual schema before an engine import. Do not invent zeroes for missing balances or fields; if the user does not want to provide them, keep the relevant calculation unavailable and proceed with supported qualitative context.

## Editorial identity and reading order

Use the company’s common name as the large centered serif masthead; the ticker is metadata. Use an original editorial deck, dated issue line, thin-rule navigation, cream paper, dark ink, restrained yellow highlights, generous text and square geometry. Do not reproduce another publication’s branding, name or logo. HTML is primary; PDF is an optional, separately verified print edition. Never shrink type or omit evidence just to meet a page target.

The enhanced reading edition uses ten sections:

1. Decision-support takeaway: analytical conclusion, uncertainty, strongest counterargument and what changes the decision.
2. Portfolio context: optional, unavailable until supplied; never infer holdings, leverage or risk limits.
3. Business evidence: sources, cash conversion, adverse facts and open questions.
4. Valuation: explicit cases, assumptions, horizon, units and unavailable inputs.
5. Risk: model sensitivity, survivability and conditional sizing mathematics as labeled educational scenarios; no recommended allocation.
6. Four original investor perspectives.
7. Four remaining original perspectives, followed by a separate Scott Page robustness note.
8. Dated sources, next decisions, exact calculation/audit downloads and completeness ledger.
9. Nine-block Business Model Canvas and Hamilton Helmer’s Seven Powers.
10. Final generated sketchnote with a recorded, simulated investor lens and full text equivalent.

### Relationship to the existing report specification

The older [13-section anatomy](../../skills/decision-prediction/references/monocle-report-anatomy.md) remains the underlying analytical checklist. This reading edition reorganizes presentation; it does not silently waive required work or claim legacy order compliance. Record the following mapping in the completeness ledger: position → 2; frameworks → 9 (include Porter separately when required); Bayesian update → 3; Sharpe/Kelly/survivability → 5; engines → 8; convexity → 4; simulation → 5; margin → 2/5; options → 5; barbell → 2/5; investor commentary → 6/7; metrology → 8; verdict → 1/8. Mark each as completed, unavailable, not run or not applicable, with reason and consequence. A reduced public-data sample is explicitly a bounded first report, not full-specification compliance. Required work cannot disappear behind a polished layout.

## All eight original lenses, plus Page

Read the actual [repository cards](../platforms/common.md#the-lens-inventory). Include Scott Galloway; Brad Gerstner; Chris Camillo; Thomas and Philippe Laffont / Coatue; Michael Mauboussin; Warren Buffett and Charlie Munger; Martin Shkreli; and Ed Thorp. Scott Page is a separate ninth robustness lens, not a substitute or an additional independent vote.

Each original perspective needs a distinct question, supported assessment, contrary evidence, missing input or abstention and implication for the user’s own decision. Preference changes emphasis, not factual outcomes or coverage. State: “Simulated analytical perspectives inspired by repository playbooks. These are not statements, advice, endorsements or participation by the named individuals or their firms.” Use third-person summaries, never invented quotations. Narrative lenses are not eight executable engines or independent forecasts.

## Legacy output boundary

Existing engine schemas or historical reports may still contain action labels or model-implied “recommendation” fields. This documentation does not migrate those implementations or certify older reports against the educational boundary. The host/report adapter must explain raw model fields as assumption-dependent artifacts, preserve provenance, and avoid presenting Buy/Hold/Add/Trim/Sell labels, debt-payment directives or position sizes as personalized recommendations. Present neutral exposure/scenario comparisons and user-controlled decision questions instead. A historical private report is not a sanitized public sample.

## Evidence and deterministic calculations

Use Measured, Calculated, Modeled and Forecasted labels at the claim, with source publication/as-of/retrieval dates, units and scope. Use Narrative and Unknown/unavailable when appropriate. A screenshot transcription remains Observed transcription · unconfirmed until the exact extraction is actually confirmed. Calculated derivatives inherit uncertain inputs. Modeled arithmetic remains Modeled · calculated in Python.

Run financial arithmetic through the reviewed deterministic Python path only when genuinely available. Preserve source version, command, input identity, formula identifiers, units, assumptions, outputs, issues and audit hashes. Separate supplemental calculations from engine output. Never describe a narrative estimate as a completed engine run; do not fabricate prices, probability distributions, calibration, simulations or measured API costs. Formal Bayesian updates require the documented evidence, prior, likelihood and execution gates. Runtime failure or missing data must remain visible.

Presentation-only edits do not refresh market cutoffs, update holdings, change probability sets, alter fractioning conventions, regenerate audit bytes or confer trade authority. A later substantive research update records new evidence and reruns affected calculations with version history.

## Business Model Canvas and Seven Powers

Scope the canvas to a defined core business model; separate materially different adjacent models. Provide all nine blocks: key partnerships, key activities, key resources, value propositions, customer relationships, channels, customer segments, cost structure and revenue streams. Attribute dated company evidence separately from analyst synthesis. Reflow the connected desktop canvas into readable semantic cards on narrow screens.

Assess Scale Economies, Network Economies, Counter-Positioning, Switching Costs, Branding, Cornered Resource and Process Power. Each needs an economic benefit, imitation barrier, dated evidence, qualitative strategic judgment, confidence/uncertainty, strengthening signal and weakening signal. Size, growth or attractive margins alone do not prove durable Power. Missing evidence means unproven, not absent. Do not invent numeric moat scores.

Consult [Strategyzer’s Business Model Canvas](https://www.strategyzer.com/library/the-business-model-canvas) and [Helmer’s synopsis](https://7powers.com/synopsis/) alongside company primary sources. Record the actual date consulted; these links are framework references, not company-specific proof.

## Final generated sketchnote and rotation

Keep the actual generated raster image as the final narrative section after strategy. A placeholder, generic icon or HTML diagram is not completion. Use one named simulated investor lens from the original eight. For the first report choose the user’s preferred lens, or explain a balanced starting choice. Record report ID, edition date, selected lens, previous lens, rotation index and reason in the private report metadata. Rotate to the next lens only on a requested or explicitly scheduled substantive update; formatting repairs and retries retain the existing lens and image unless correction is necessary. Rotation never removes the eight analytical perspectives.

Apply Dan Roam’s 6×5 approach as a planning checklist: six visual questions (who/what, how much, where, when, how, why) crossed with SQVID choices (simple/elaborate, quality/quantity, vision/execution, individual/comparison, change/status quo). Record the chosen treatment and question coverage; do not imply all 30 combinations require separate panels. Render conceptual relationships as conceptual, not as measured plots. Exact values and source labels must match the retained report.

Include concise alt text, a factual caption, the simulated-perspective disclaimer and a complete accessible text equivalent covering all six questions. Inspect the actual image for legibility, labels, invented numbers, misleading scale and unsupported causal claims. If generation is unavailable, deliver a clearly incomplete edition with a text summary and explicit image blocker; never report the requested sketchnote as delivered.

## Self-contained and accessible

Prefer a single HTML file with embedded final PNG and audit payloads, native fonts, semantic headings and no external scripts, fonts, trackers or automatically loaded assets. Source links should activate only on reader action. Keep report inputs and outputs private/local by default in the authorized environment. Local storage does not imply local-only model processing; verify data destinations before sensitive input leaves the device. Public hosting or publishing personal reports requires separate permission.

Use native links/buttons, visible keyboard focus, readable labels, sensible heading order and text equivalents. Tables need headings, units and labeled scrolling regions. If adding presentation controls, include matching immutable JSON and a usable static view without JavaScript. Controls only select precomputed cases, expose assumptions and reset; they cannot recalculate finance, persist changes, make API calls or place orders. Use textContent for readouts and avoid HTML injection.

Use conserved quantities and one width scale for Sankey diagrams, zero-baseline bars for comparable amounts and explicit qualitative labels for conceptual maps. Do not fabricate a time series, probability, confidence score or set size to fill a design slot.

## Acceptance and honest limits

Before a completed edition is delivered:

- Check all ten sections, eight original perspectives plus Page, nine canvas blocks and seven complete power assessments.
- Resolve every template token and unsafe URL; verify dates, source links, calculations, evidence labels and audit-byte identity.
- Confirm final image presence, actual pixel inspection, alt/caption/text equivalence and recorded rotation.
- Open HTML in a supported browser at desktop and mobile widths; inspect overflow, long names, navigation, focus/order, every control/reset, downloads and print output. Test unavailable assets and JavaScript-disabled reading where applicable.
- Verify the recipient can open the chosen private artifact. A browser may restrict file downloads or embedded assets; test the actual delivery route. Do not silently publish a website to solve access.
- Record passed, failed and not-run checks separately. Source tests cannot establish browser layout or assistive-technology conformance.

This publication provides a template and instructions only. Browser visual QA of this HTML is unverified, and no prior PDF or design score transfers to it. No numerical design score, native integration, zero-click installation, current provider access, completed new-user journey, or working recurring schedule is claimed.
