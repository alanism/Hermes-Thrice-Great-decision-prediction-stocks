# Capital Decision Lab

Capital Decision Lab is a local-first stock exposure research engine for Kelly sizing, convex upside, margin safety, and evidence intelligence.

It is part of the Hermes Thrice Great NHI family, but it is not an UnCommon Core module, not an education product, and not a curriculum system.

Its default use case is evaluating concentrated stock exposure under uncertainty: asymmetric stock theses, high-upside/high-volatility positions, margin exposure, survivability before upside arrives, and user-constrained sizing. It also retains its broader decision-lab capabilities for return, risk, risk-adjusted performance, allocation, scenarios, simulation, comparison, and local decision records.

Capital Decision Lab is a self-directed capital research and decision-support tool. Users supply or verify assumptions, evidence, and decision preferences. The system calculates, models, forecasts, compares, flags risks, and may produce model-implied sizing or exposure outputs. The user decides whether to act. The system does not execute trades, connect to brokerages, guarantee outcomes, or treat assumptions as facts.

---

## What It Does

Capital Decision Lab helps answer questions like:

- What exposure does Kelly imply under my probability and payoff assumptions?
- Is the supplied stock thesis convex enough to compensate for its downside?
- How far can the position fall before reaching an estimated margin threshold?
- Which stress scenarios breach the supplied maintenance requirement?
- Can the position survive adverse movement before a high-upside scenario arrives?
- What happens in bear, base, and bull scenarios?
- How sensitive is this decision to one fragile assumption?
- What did I believe when I made this decision?

The tool separates:

1. measured facts,
2. user assumptions,
3. calculated results,
4. modeled estimates,
5. user-selected decisions,
6. unavailable results.

Every semantic output is provenance-labeled so the system does not blur facts, assumptions, formulas, models, and human choices.

---

## Four Primary Capabilities

### 1. Kelly Criterion

Calculates full Kelly, confidence-adjusted Kelly, fractional Kelly references, and exposure capped by an explicit user constraint. It detects negative or zero edge, validates probabilities and payoff assumptions, and can approximate expected log growth across multiple supplied scenarios.

### 2. Convexity for Stock Upside

Measures asymmetric upside through upside/downside multiples, breakeven probability, probability-weighted upside and downside, expected value, expected return, payoff skew, scenario dispersion, tail outcomes, and a conservative convexity score.

### 3. Margin Management

Calculates current equity, margin ratio, loan-to-value, maintenance requirements, estimated margin-call price, liquidation buffer, and manual stress rows showing losses, remaining equity, margin ratios, and threshold breaches.

### 4. Evidence Intelligence

Analyzes user-verified local evidence from Polymarket, X/Twitter, Reddit, and manual notes. It calculates event-market and social signals, maps them through an explicit thesis sensitivity map, performs bounded Bayesian updates, and creates pending assumption-update proposals. Only an explicitly approved proposal can flow into the main analysis.

These pillars change the product priority, not its mathematical breadth. The existing return, risk, risk-adjusted, allocation, scenario, Monte Carlo, comparison, authorization, and ledger capabilities remain available.

---

## What It Can Calculate

### Return Metrics

- absolute gain or loss
- ROI
- CAGR
- expected value
- expected return

### Risk Metrics

- volatility
- downside deviation
- maximum drawdown
- loss probability
- value at risk
- expected shortfall
- correlation when sufficient paired observations exist

### Risk-Adjusted Metrics

- Sharpe ratio
- Sortino ratio
- Calmar ratio
- return-to-drawdown ratio

### Allocation Metrics

- Kelly Criterion
- fractional Kelly
- capped fractional Kelly
- unavailable results when assumptions or denominators are invalid

### Convexity and Upside Asymmetry

- upside/downside multiple
- breakeven probability
- probability-weighted upside and downside
- convexity score
- payoff skew and scenario dispersion
- tail upside and tail downside
- optionality note from supplied assumptions

### Margin Safety

- current equity and margin ratio
- loan-to-value
- maintenance margin threshold
- estimated margin-call price
- liquidation buffer
- manual price-decline stress table
- maintenance-threshold warnings

### Scenario and Simulation

- bear/base/bull scenario analysis
- seeded Monte Carlo simulation
- deterministic repeated outputs for identical inputs and seeds
- simulation metadata including seed, distribution family, parameters, iteration count, input hashes, and limitations

---

## What It Does Not Do

Capital Decision Lab does not:

- provide financial, investment, tax, legal, brokerage, fiduciary, or trading advice;
- recommend securities;
- tell users what to buy or sell;
- execute transactions;
- connect to bank accounts;
- connect to brokerage accounts;
- fetch live market data;
- import transaction data;
- perform tax planning;
- sync to the cloud;
- send telemetry;
- create financial facts with an AI model;
- authorize decisions on behalf of the user.

The system may compare alternatives under supplied assumptions, but the user remains responsible for all assumptions, decisions, actions, and outcomes.

---

## Product Philosophy

Most market tools track what happened or automate an action.

Capital Decision Lab focuses on decision quality before and after the choice.

It asks:

- What are the alternatives?
- What capital is at risk?
- What assumptions are being made?
- What does the math say under those assumptions?
- What is unavailable or uncertain?
- What exposure did the user explicitly choose?
- Is the payoff asymmetric enough under the supplied scenarios?
- What adverse movement can the margin structure absorb before its threshold?
- Was that decision authorized by the user?
- What can be reviewed later for calibration?

The goal is not automation. The goal is disciplined thinking under uncertainty.

---

## Local-First Design

Capital Decision Lab is local-first.

Private user data belongs in:

```text
local/
```

The `local/` directory is ignored by Git except for:

```text
local/README.md
```

Real decision cases, assumptions, analyses, proposals, authorizations, ledgers, reports, outcomes, and logs should never be committed.

The staging system is deny-by-default and rejects private paths.

---

## CLI Commands

```bash
capital doctor
```

Checks Hermes compatibility, distribution identity, profile identity, network/model-call restrictions, and staging integrity.

```bash
capital validate --synthetic
```

Validates synthetic fixtures without private data, network access, or ledger writes.

```bash
capital analyze --case <path>
```

Analyzes a local decision case and emits deterministic, provenance-labeled results.

An approved evidence-driven assumption update may be supplied with `--assumption-update <path>`. Pending, rejected, and expired proposals do not change the analysis.

```bash
capital evidence validate --file <path>
capital evidence analyze-event-market --snapshot <path>
capital evidence analyze-polymarket --snapshot <path>
capital evidence analyze-social --batch <path>
capital evidence synthesize --inputs <path>
capital belief update --case <path> --synthesis <path> --sensitivity <path>
capital assumption propose --belief-update <path>
```

These commands operate only on local files. There are no live fetch, scraping, or account-connection commands.

```bash
capital compare --case <path>
```

Compares alternatives under supplied assumptions without selecting or recommending one.

```bash
capital record --analysis <path> --authorization <path>
```

Records a decision only after validating a separate proposal and explicit human authorization bound by canonical hashes.

---

## Decision Contracts

Capital Decision Lab uses versioned JSON contracts:

```text
decision-case.v1.schema.json
assumption-register.v1.schema.json
decision-analysis.v1.schema.json
decision-comparison.v1.schema.json
decision-proposal.v1.schema.json
decision-authorization.v1.schema.json
decision-ledger.v1.schema.json
evidence-source.v1.schema.json
evidence-item.v1.schema.json
evidence-batch.v1.schema.json
event-market-snapshot.v1.schema.json
event-market-signal.v1.schema.json
social-evidence-signal.v1.schema.json
thesis-sensitivity-map.v1.schema.json
belief-state.v1.schema.json
bayesian-update.v1.schema.json
assumption-update-proposal.v1.schema.json
```

Proposal and authorization are separate by design.

A proposal describes the user-selected action or exposure being considered.

An authorization is the explicit human confirmation required before appending to the local ledger.

No proposal can authorize itself.
No analysis can authorize itself.
No ledger entry can be written without valid hash-bound authorization.

---

## Evidence Provenance

Every decision-content output must use one provenance class:

```text
measured
assumed
calculated
modeled
forecast
decided
unavailable
```

This prevents the system from treating assumptions as facts, modeled estimates as predictions, or calculations as decisions.

---

## Safety Boundaries

Capital Decision Lab is comparison-only decision-support software.

Allowed language:

- “under the supplied assumptions”
- “calculated result”
- “modeled estimate”
- “user-selected exposure”
- “unavailable due to insufficient inputs”

Disallowed behavior:

- claiming to provide financial advice;
- presenting modeled ranges as predictions;
- recommending purchases or sales;
- creating facts from model output;
- authorizing decisions for the user;
- connecting to accounts or executing transactions.

---

## Development Status

Current version: `v0.1.0-cli-mvp`

Implemented:

- local-first CLI foundation
- Hermes NHI profile identity
- clean-room containment from UCC
- anti-UCC leakage scanner
- anti-advice-language scanner
- private-data exclusion
- versioned contracts
- provenance atoms
- deterministic return, risk, allocation, and simulation engines
- stock-focused Kelly analysis with confidence haircuts and user caps
- convexity and upside-asymmetry analysis
- margin threshold, liquidation-buffer, and stress analysis
- local event-market and social evidence analysis
- thesis-specific sensitivity mapping
- bounded Bayesian belief updates
- pending assumption-update proposals with approved-only analysis flow
- proposal/authorization separation
- atomic local ledger append
- clean-checkout test verification

Known limitations:

- historical tail metrics use discrete observations;
- Monte Carlo currently supports seeded normal draws only;
- proposals and authorizations must be authored explicitly;
- external evidence must be entered locally and verified or corrected by the user;
- no live source retrieval, OCR, scraping, or browser automation is included;
- evidence synthesis uses transparent bounded heuristics rather than calibrated empirical likelihood models;
- all ratios use decimal representation.

---

## Testing

Run:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Expected current result:

```text
88 passed
```

---

## License

Capital Decision Lab is released under a Fair Source license.

You may use, inspect, modify, and run it for personal, educational, research, evaluation, and small-team internal use.

Commercial redistribution, hosted competing services, enterprise deployment, brokerage/account integrations, financial-services embedding, resale, and SaaS use require a separate commercial license.

Each source file converts to Apache-2.0 four years after its first public release date.

Capital Decision Lab is decision-support software only. It does not provide financial, investment, tax, legal, brokerage, fiduciary, or trading advice.

See `LICENSE` for details.

---

## Relationship to Hermes and UCC

Capital Decision Lab uses Hermes-style governance patterns:

- deterministic calculations,
- explicit assumptions,
- canonical hashes,
- append-only records,
- local-first containment,
- human authorization,
- provenance labeling,
- adversarial tests.

It is not part of UnCommon Core.

It does not use UCC student, parent, curriculum, assessment, mastery, practice, or pedagogy contracts.
