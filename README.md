# Capital Decision Lab

Capital Decision Lab is a local-first decision-support tool for adults making uncertain capital, finance, business, and opportunity-cost decisions.

It is part of the Hermes Thrice Great NHI family, but it is not an UnCommon Core module, not an education product, and not a curriculum system.

Capital Decision Lab helps you compare alternatives, label assumptions, calculate risk and return, model possible outcomes, and record human-authorized decisions in a local ledger.

It does not provide financial advice.

---

## What It Does

Capital Decision Lab helps answer questions like:

- Should I pay down debt or invest?
- Should I keep more cash or take a risky opportunity?
- Should I reduce a concentrated position?
- Is this private investment worth the downside?
- How much exposure is mathematically implied by my assumptions?
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

Most personal finance tools track what happened.

Capital Decision Lab focuses on decision quality before and after the choice.

It asks:

- What are the alternatives?
- What capital is at risk?
- What assumptions are being made?
- What does the math say under those assumptions?
- What is unavailable or uncertain?
- What exposure did the user explicitly choose?
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
- proposal/authorization separation
- atomic local ledger append
- clean-checkout test verification

Known limitations:

- historical tail metrics use discrete observations;
- Monte Carlo currently supports seeded normal draws only;
- proposals and authorizations must be authored explicitly;
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

