# Shared Decision Prediction onboarding requirements

Version 0.1 · Reviewed 2026-10-09 · Documentation only

This guide describes how an assistant should introduce Decision > Prediction when a user first requests investment research and the repository is available. It makes the research lenses discoverable, asks for useful preferences, and keeps calculations, evidence and permissions separate. It does not install a plugin, run a scheduler, grant account access or place trades.

## Educational reporting boundary

Decision ≥ Prediction is educational research and decision support. It presents evidence, exposure, assumptions and scenarios so users make their own decisions and predictions. It does not provide portfolio advisory, prescribe trades or allocations, or issue Buy/Hold/Add/Trim/Sell instructions. Older engine/schema names containing “recommendation” describe model artifacts, not personal advice; the dot reporting flow must not present them as recommended actions.

For optional portfolio context, recommend a redacted CSV or screenshot with names, account numbers and other identifiers removed before sharing. Keep only necessary holdings/exposure fields and the as-of date; verify extracted values. The project creator is not an intended recipient of inputs or outputs. The selected agent, model, storage or hosting provider may process or retain data under its own policies. Verify the actual workflow and destination; this documentation does not guarantee that all deployments are local-only or that a creator can never receive data. Do not upload private data to GitHub, public hosting or a new provider without required permission.

## HTML-first report experience

Use the [first-report flow](../reports/FIRST-REPORT-WITH-DOT.md) and [HTML authoring guide](../reports/HTML-REPORT-GUIDE.md) for the enhanced reading edition. Its ten-section presentation maps the older thirteen-section checklist explicitly; it does not waive missing work or claim legacy-order compliance. The [template](../../templates/stock-report/Stock-Report-Web-Template.html) is an inert scaffold, not a finished report.

## First use and discoverability

When this file is made available to the assistant, read it together with the complete [Decision Prediction skill](../../skills/decision-prediction/SKILL.md), its [report anatomy](../../skills/decision-prediction/references/monocle-report-anatomy.md), and the [setup manual](../Decision-Prediction-onboard-setup.md). Inspect the actual files and current execution capabilities before describing anything as installed or working.

Merely adding a file named a platform onboarding guide does not guarantee that a host discovers or loads it. The installation or host integration must explicitly make this document discoverable. Link it from `README.md` and `START_HERE.md` during an approved documentation release. Until automatic discovery has been implemented and tested, a user or host must supply the repository or this document on first use.

The current Hermes staging allowlist excludes the `docs` directory and the eight original root cards; it includes `dlc-page.md`. These source-repository guides and original cards are therefore not automatically installed in that staged profile. Host discovery and distribution integration require a separate implementation and tests. This documentation does not change the allowlist.

After checking availability, proactively explain the available lenses and ask for preferences. Do not wait for the user to know the card names. Use an introduction like this, adjusting the capability statement to what was actually verified:

> I found Decision > Prediction’s research playbooks: eight investor-inspired perspectives plus Scott Page’s many-model lens. For a requested report, I’ll label evidence, keep assumptions visible, show disagreement and preserve the calculation results. The Python calculations can run only where the reviewed runtime is available. Which perspectives would you like to lead the analysis, and what risk discipline should I use? For example, Gerstner and Laffont for growth analysis with Thorp for sizing and survival, or Buffett and Munger for business quality and valuation. We can start with a balanced overview. Recurring reviews are optional.

Never say “I have it installed” solely because the Markdown exists. If execution is unavailable, offer a clearly labeled qualitative review and state which numerical outputs cannot be produced. Do not claim a complete Decision > Prediction run.

## The lens inventory

These descriptions summarize the repository’s playbooks. They are analytical prompts, not authenticated statements of what these people would say today. Do not copy historical holdings, market claims, numerical rules or quotations from a card as current verified evidence.

| Perspective | Repository card | Useful analytical questions |
| --- | --- | --- |
| Scott Galloway | [dlc-Galloway](../../dlc-Galloway) | What supports durable wealth creation, diversification and disciplined capital allocation? |
| Brad Gerstner | [dlc-Gerstner](../../dlc-Gerstner) | Is a technology adoption cycle real, and what expectations are already priced into growth? |
| Chris Camillo | [dlc-camillo](../../dlc-camillo) | Do observed changes in customer behavior offer an information edge, and how can they be verified? |
| Thomas and Philippe Laffont / Coatue | [dlc-laffont](../../dlc-laffont) | Do thematic growth claims survive detailed financial modeling and data checks? |
| Michael Mauboussin | [dlc-mauboussin](../../dlc-mauboussin) | What do base rates, expectations and the outside view imply? What separates skill from luck? |
| Warren Buffett and Charlie Munger | [dlc-munger-buffett](../../dlc-munger-buffett) | Is the business understandable, durable and sensibly valued, with capable capital allocation? |
| Martin Shkreli | [dlc-shkreli](../../dlc-shkreli) | Does detailed primary-source cash-flow and balance-sheet work challenge the consensus? |
| Ed Thorp | [dlc-thorp](../../dlc-thorp) | Is the assumed edge credible, and does sizing survive model error, leverage and downside? |
| Scott Page, additional lens | [dlc-page.md](../../dlc-page.md) | Do genuinely different models agree, and where do tail risk, regimes or adoption dynamics undermine the conclusion? |

The original report specification requires the first eight. Page is an additional many-model lens, not a replacement for an original member. The root `dlc` file duplicates the Thorp card at the reviewed source version; do not count it as a tenth distinct perspective.

**Required disclaimer:** “Simulated analytical perspectives inspired by repository playbooks. These are not statements, advice, endorsements or participation by the named individuals or their firms.” Write third-person analytical summaries, not invented quotations attributed to real people.

## Ask for two separate preferences

1. **Primary analysis lenses:** choose one or more perspectives, or use a balanced overview. These determine emphasis, question order and explanation style.
2. **Risk and sizing discipline:** establish time horizon, liquidity needs, leverage restrictions, concentration limits and tolerance for loss before interpreting portfolio sizing. A Thorp-inspired discipline may emphasize fractional Kelly, uncertainty haircuts and survival; it does not establish an actual suitable allocation by itself.

A user may prefer Gerstner and Laffont analysis while using Thorp-inspired risk discipline. Another may prefer Buffett and Munger analysis with the same conservative risk constraints. Do not convert a style preference into permission to concentrate, borrow, buy options, trade, or apply numerical limits copied from a playbook.

For the first report, offer these ordinary-language defaults and let the user change them:

- Balanced analysis if no leading lens is chosen.
- All eight original perspectives in a full report, with Page in a separate additional section.
- Evidence and unfavorable facts retained regardless of preferences.
- No assumed borrowing or exposure increase; sizing remains conditional until necessary inputs and constraints are established.
- On-demand research only until a recurring workflow is explicitly chosen.

The user can change or reset these preferences at any time. Record only preferences the user actually chooses. Restate the chosen analysis lenses and risk constraints in the next report so the user can correct them. These are proposed host behaviors, not a new executable configuration schema.

## Full committee and focused questions

A full report keeps every original lens, the strongest disagreement, missing evidence, and a synthesis that identifies the binding constraint. Preferred lenses can lead the summary; they cannot suppress negative facts, a contrary valuation, or a risk warning. Different narratives from one language model are not independent voters or evidence of calibrated consensus.

Users may also request focused follow-ups:

- “Review this company through the Gerstner lens. What would invalidate the growth thesis?”
- “Use Laffont’s financial-modeling questions, then apply Thorp-inspired risk checks.”
- “Give me a Buffett and Munger view of business quality and valuation.”
- “Show the strongest disagreement with my preferred lenses.”
- “Use Page to identify models whose different assumptions could change the answer.”

Label a focused response **Single-lens analysis** or **Focused lens comparison**. It need not reproduce the full committee, but it must retain material contrary evidence and risk warnings. It is not a full-specification report. A single-lens addendum does not erase the committee in the underlying full report.

## Narrative cards and executable calculations

The reviewed Python catalog registers `core`, `thorp`, `mauboussin`, `contrarian_filings`, `committee` and `page`. The eight narrative cards do not imply eight executable engines, eight independent runs or eight allocation votes. Page’s qualitative card and its executable model pack are separate things.

The reviewed read-only adapter supports `method list`; it does not expose arbitrary `method run` execution. An upstream pack can exist without being callable in the current host. Claim a pack ran only when an actual invocation and retained result prove it. Never describe narrative commentary as engine output.

Keep deterministic Python outputs intact, including formula identifiers, source references, assumptions, units, hashes, limits and unavailable results. Put supplemental calculations and narrative lens commentary in separately labeled sections. Same inputs, version and applicable seed should reproduce calculations; repeatability is not investment predictability.

## Evidence and belief updates

Use the customer-facing labels **Measured**, **Calculated**, **Modeled** and **Forecasted** for applicable figures. Keep Narrative and Unknown/unavailable visibly distinct, and preserve original engine provenance fields.

- Screenshot-derived figures remain **Observed transcription · unconfirmed**, not Measured, until the user confirms the exact extraction. Preserve the file hash, source/capture time and confirmation reference privately. A JSON `user_verified` flag is not evidence that confirmation happened.
- A modeled payoff calculated in Python remains **Modeled · calculated in Python**. Correct arithmetic does not validate assumptions.
- A formal Bayesian update requires genuinely `user_verified` evidence, a matching thesis sensitivity rule, a documented prior and likelihood model, bounded update size and an actual calculation. The read-only adapter does not permit belief-update writes. Otherwise use a qualitative belief revision and explain the missing gate.
- Record prior view, new evidence, revised view, decision or no change, uncertainty and what would change the view. Keep source publication/as-of, retrieval and review timestamps separate.

## Preflight before delivering a full report

Read the entire skill and its referenced anatomy, not just the numeric engine instructions. Use the [manual’s completeness gate](../Decision-Prediction-onboard-setup.md#full-report-completeness-gate) on every report. For the legacy edition, keep its canonical 13-section order. For the enhanced HTML reading edition, use the explicit ten-section mapping in the HTML guide while retaining the complete analytical checklist. Mark required work that was not run or is unavailable, and explain the reason and consequence. Do not hide omitted work behind successful calculation tests.

Measured provider usage and cost may be unavailable. Report that gap; use current verified provider pricing if an estimate is needed. Historical model prices and cache discounts in older instructions are not current pricing authority.

## Optional recurring reviews

Offer setup only after a useful on-demand example. Options include five stocks per day from a chosen list, a weekly update to a chosen ticker report, and a separate macro review. META can be a weekly example; it is not mandatory for every user.

Before setup, agree tickers, selection rules, schedule, time zone, sources, report identity/destination, private-data use and retention. Verify an actual host schedule before saying it is enabled. Keep the same report identity with dated version history and comparable source snapshots. Installation alone creates no schedule. The adapter does not install cron, run a daemon, authenticate a broker or trade.

## Release and privacy boundary

Do not silently make paid external model calls or send portfolio data to a new model provider, platform, or recipient. A lens preference is not authorization for additional provider charges or financial-data sharing. Before a new external workflow, establish the provider, data being sent, purpose, retention and any required spending authorization. If the needed permission is absent, keep the dependent step pending and continue only the work already authorized.

This document is intended for a public repository. Use public or synthetic examples only. Keep financial accounts, balances, screenshot identifiers, credentials and private reports out of source control. Publishing this guide does not authorize publishing a user's inputs. See the [customer lessons](../dot-onboarding-lessons.md) for the failure modes this onboarding is designed to prevent.

Reviewed source: `5bfe72972ee9b3ade55923e5419ca7ede1ac70ba`. Review paths and capabilities again when upgrading. This documentation does not prove runtime onboarding, report compliance, recurring execution or investment performance.

