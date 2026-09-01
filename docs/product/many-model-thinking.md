# Product Requirements Document — Many-Model Thinking Extension

Status: Authoritative product outcome specification.  
Task: T03  
Primary Hero: `Bret Taylor`  
Verifier Hero: `Ryan Lopopolo`  

---

## 1. Core Requirements & Outcomes

### User
A concentrated barbell equity investor managing real capital across tech, defense, minerals & energy, and fintech, using a local Hermes desktop agent harness without connecting to a brokerage or exposing private financial data.

### Job
Stress-test an investment thesis and capital-allocation sizing against diverse, formal mental models (heavy-tail power laws, Markov regime shifts, Bass diffusion adoption, bandit research value) to detect hidden failure modes, invalid moment assumptions, and brittle adoption narratives before allocating or adjusting exposure.

### Current Failure
The existing decision engine evaluates single-framework metrics (Kelly, convexity, margin, Bayesian updates). However, it cannot mechanically detect when a thesis secretly depends on:
1. An invalid normal/thin-tail distribution assumption in a power-law domain (leading to catastrophic underestimation of extreme downside and invalid Kelly/Sharpe calculations when the mean or variance is undefined);
2. A transient state intervention that washes out under long-term Markov regime equilibrium;
3. An unrealistic S-curve adoption trajectory that violates discrete-time diffusion limits;
4. Chronic under-exploration of alternative information sources.

### Baseline Metric
* Recommendation vocabulary: strictly 6 model-implied strings (`avoid margin`, `pause`, `watch`, `hold current exposure`, `trim to fractional Kelly`, `increase exposure under this assumption set`).
* Permission gates: Margin survival and model health currently provide the only automated safety vetoes.
* Baseline outcome on representative cases: Models without tail-awareness evaluate exposure using raw moment calculations regardless of underlying distribution stability.

### Target
Produce a machine-readable decision delta on at least one of two representative theses:
1. A changed recommendation outcome within the closed 6-string vocabulary; or
2. A newly binding, machine-readable permission veto that blocks positive exposure increases or downstream variance calculations when moment assumptions fail.

Better prose, descriptive explanations, and simulated personas do **not** count toward this target.

### Non-Goals
* No automated trade execution or brokerage integration.
* No LLM-driven freehand mathematical calculations or raw multi-model voting/averaging.
* No modification of existing runtime dependencies (Python standard library only).
* No transmission of real portfolio, thesis, or credential data to external services.
* No inclusion of unverified/dormant models in v1 (SIR, Schelling, Blotto, Polya, NK, UCB1, Thompson sampling, and Gittins are deferred).

---

## 2. Decision Delta Specifications

### Six-String Recommendation Delta
The system operates strictly within the existing closed 6-string recommendation vocabulary:
1. `avoid margin` (highest priority constraint; triggered when margin survival is breached)
2. `pause` (triggered on untrusted required inputs, unavailable required diagnostic, or binding tail safety veto)
3. `watch` (triggered on unresolved multi-model disagreement or downside without valid sizing basis)
4. `hold current exposure` (informative evidence that does not warrant exposure change)
5. `trim to fractional Kelly` (downside edge compression requiring position reduction)
6. `increase exposure under this assumption set` (robust positive multi-model support with zero binding vetoes)

### Binding-Permission Delta
When the power-law diagnostic yields $\alpha \le 2$ (undefined mean), the system generates a binding machine-readable safety veto (`HEAVY_TAIL_UNDEFINED_MEAN`). This veto:
* Suppresses `increase exposure under this assumption set`;
* Forces the decision permission to `pause` or `watch`;
* Disallows downstream Kelly sizing when probability/payoff assumptions depend on that invalid tail model.
When $2 < \alpha \le 3$ (infinite variance), the system marks variance-dependent metrics (Sharpe/Sortino) as `unavailable` with reason code `INFINITE_VARIANCE_UNDEFINED`.

### Zero-Delta Branch
If neither of the two representative local thesis runs demonstrates a decision-relevant delta (a changed recommendation outcome or a newly binding permission veto):
* Tasks T13 through T24 are automatically marked `CUT`.
* The extension completes and ships as a power-law-only safety diagnostic via adapted release tasks T25–T29.
* This branch is mechanical and non-waivable.

### Input Owner and Location
* Real portfolio files, thesis assumptions, and case documents are owned solely by the user and located strictly within the gitignored `local/` directory (e.g., `local/theses/`, `local/cases/`).
* Synthetic test cases and contract fixtures reside in `fixtures/valid/contracts/` and `fixtures/cases/`.
* No real private data is ever committed to source control.

---

## 3. Two Named Local Thesis-Run Descriptors

### Thesis Run 1: High-Growth Semiconductor / Hardware Acceleration Thesis (`local/theses/thesis_run_1_heavy_tail.json`)
* **Case Description:** High-conviction thesis assuming continuous compound revenue upside modeled with thin-tail / normal distribution assumptions.
* **Tested Vulnerability:** Empirical observation tail reveals $\alpha \le 2.0$ (heavy power-law tail with infinite theoretical mean and variance).
* **Expected Decision Delta:** Baseline pipeline computes a positive fractional Kelly allocation and recommends `increase exposure under this assumption set`. With Page Many-Model extension enabled, the power-law safety hook detects $\alpha \le 2$, applies binding veto `HEAVY_TAIL_UNDEFINED_MEAN`, and changes recommendation to `pause`, vetoing the exposure increase.

### Thesis Run 2: Biotech Catalyst / Platform Turnaround Thesis (`local/theses/thesis_run_2_markov_regime.json`)
* **Case Description:** Thesis betting that a recent regulatory approval or management change creates a permanent shift in operating profitability.
* **Tested Vulnerability:** Transition matrix reveals an ergodic, irreducible chain where the stationary equilibrium yields 75% baseline state and 25% turnaround state, demonstrating that one-off state intervention washes out.
* **Expected Decision Delta:** Baseline pipeline recommends `increase exposure` based on short-term optimistic catalyst. Page Markov regime diagnostic shows long-run stationary reversion, generating a `contradicts` claim on the catalyst durability, shifting the synthesis from `increase exposure under this assumption set` to `watch`.
