# Many-Model Thinking Build — Engineering Learning & Troubleshooting Log

**Purpose:** Comprehensive living record of engineering challenges, edge cases, root-cause analyses, and solutions encountered during the implementation of Many-Model Thinking in Hermes Thrice Great Decision-Prediction. This log serves as an authoritative troubleshooting guide and knowledge base for coding agents and future maintainers.

---

## Architecture & Build Governance Invariants

1. **Deterministic Standard-Library Engine:** All mathematical and scientific model logic (`power_law`, `markov`, `bass`, `bandit`, `claim_compiler`) must run purely on the Python standard library with zero runtime external dependencies and zero network/filesystem egress.
2. **Epistemic Provenance Hierarchy:** All output data are packaged into `$defs.evidence_atom` instances with explicit `provenance_class` (`measured`, `assumed`, `calculated`, `modeled`, `forecast`, `decided`, `unavailable`). No raw primitives are permitted in data payloads.
3. **Four-Tier Trust Isolation:** Data trust classes (`synthetic_test`, `user_verified`, `verified_local`, `untrusted_external`) are decoupled from provenance. Externally supplied text is hostile by default; `untrusted_external` inputs must never enter calculation engines without explicit user confirmation.
4. **TDD Protocol & Immutability of Frozen Tests:** The verifier authors RED tests and freezes their SHA-256 hashes. The implementer may only modify production files. Assertion-level RED (never syntax/import/collection errors) is strictly required before code is added.

---

## Logged Issues, Root Causes, and Standardized Solutions

### Entry 01: Substring Collision in Epistemic Provenance Key Names
* **Task:** T08 / T09 (Power-Law Diagnostic Contract)
* **Observed Failure:**
  ```python
  AssertionError: assert 'proven' not in str(result).lower()
  ```
* **Root Cause:** A test asserting that goodness-of-fit diagnostics do not overclaim ("not rejected does not constitute proof/proven") used a naive `str(result).lower()` substring search. Every single evidence atom dictionary contains the mandatory schema key `"provenance_class"`, which starts with the substring `"proven"`.
* **Solution Pattern:** Do not run broad substring searches over raw JSON/dictionary string representations when schema keys may collide. Instead, explicitly inspect user-facing fields:
  ```python
  for lim in result["limitations"]:
      assert "proven" not in lim.lower()
  for atom_val in result["data"].values():
      if "reason" in atom_val and atom_val["reason"]:
          assert "proven" not in atom_val["reason"].lower()
  ```
* **Agent Rule:** Always target specific semantic fields (`limitations`, `reason`, `claims`) rather than converting dictionary objects to strings when asserting prohibited wording.

---

### Entry 02: `unavailable_result` Signature Contract & Keyword Arguments
* **Task:** T09 (Power-Law Diagnostic Implementation)
* **Observed Failure:**
  ```python
  TypeError: unavailable_result() got an unexpected keyword argument 'formula_ref'
  ```
* **Root Cause:** In `capital_decision_lab.contracts.validation`, `unavailable_result(reason, *, unit=None, input_refs=None, limitations=None)` creates an evidence atom where `provenance_class == "unavailable"`. In the repository's schema rules, an unavailable atom requires `reason` and does not carry a `formula_ref` (which is reserved for `calculated` atoms). Passing `formula_ref` raised a `TypeError`.
* **Solution Pattern:** When generating unavailable atoms, use only allowed keyword arguments:
  ```python
  unavailable_result(reason, unit="exponent", limitations=["Fit unavailable"])
  ```
* **Agent Rule:** Verify helper signatures in `capital_decision_lab/contracts/validation.py` before calling them. Only atoms with `provenance_class="calculated"` or `"modeled"` accept `formula_ref`.

---

### Entry 03: JSON Schema Enforcement for Typed Model Parameters & Booleans
* **Task:** T06 / T07 (Shared Contracts & Validator Enforcement)
* **Observed Failure:**
  ```python
  FAILED test_model_input_rejects_boolean_as_number
  ```
* **Root Cause:** In `schemas/model-input.v1.schema.json`, `"parameters": {"type": "object"}` was initially unconstrained. When a boolean (`True`) was passed for `xmin`, the validator accepted it because the internal keys were not schema-validated. Python's `isinstance(True, int)` evaluates to `True`, so explicit typing was required.
* **Solution Pattern:** Fully specify internal properties in `parameters` within `model-input.v1.schema.json`:
  ```json
  "parameters": {
    "type": "object",
    "properties": {
      "xmin": {"type": "number"},
      "observations": {"type": "array", "items": {"type": "number"}}
    }
  }
  ```
* **Agent Rule:** In JSON Schema definitions under `schemas/`, always enumerate expected numeric fields as `{"type": "number"}` or `{"type": "integer"}` to ensure `_matches_type()` rejects booleans.

---

### Entry 04: Synchronizing Supported Contract Versions in Global Fixture Tests
* **Task:** T07 (Contract Registration)
* **Observed Failure:**
  ```python
  FAILED tests/contracts/test_contract_fixtures.py::test_schema_loader_resolves_all_contract_versions
  ```
* **Root Cause:** `test_contract_fixtures.py` contains a hardcoded tuple assertion of all supported contract version strings in alphabetical order to protect against accidental contract version registration or drift.
* **Solution Pattern:** Whenever registering new schemas in `_SCHEMA_FILES` (`validation.py`), update the expected tuple in `test_contract_fixtures.py` in exact lexicographical order:
  - `"nhi.ensemble_result.v1"`
  - `"nhi.model_input.v1"`
  - `"nhi.model_result.v1"`
* **Agent Rule:** After adding contracts to `_SCHEMA_FILES`, immediately verify `tests/contracts/test_contract_fixtures.py` and ensure the expected version list is updated.

---

### Entry 05: PowerShell Multi-Command Execution & Python Import Paths
* **Task:** T07 (Separate Process Replay Verification)
* **Observed Failure:**
  ```powershell
  =plugins/capital-decision-lab : The term '=plugins/capital-decision-lab' is not recognized
  ```
* **Root Cause:** In PowerShell on Windows, syntax like `export VAR=val` or `$env:VAR=val; python -c ...` can fail depending on shell parsing and quotation rules.
* **Solution Pattern:** Use Python's built-in `sys.path.insert(0, ...)` directly inside one-liners for reliable cross-platform standalone execution:
  ```powershell
  C:\Users\alani\.venvs\capital-decision-lab\Scripts\python.exe -c "import sys; sys.path.insert(0, 'plugins/capital-decision-lab'); from capital_decision_lab.contracts.canonical import contract_payload_hash; print(contract_payload_hash(...))"
  ```
* **Agent Rule:** For separate-process verification scripts, use `import sys; sys.path.insert(0, ...)` to eliminate shell environment variable escaping issues.

---

### Entry 06: Deterministic Seed Derivation for Parametric Bootstraps
* **Task:** T08 / T09 (Goodness-of-Fit Parametric Bootstrap)
* **Design Decision:** The continuous power-law diagnostic requires 250 bootstrap trials to compute the empirical KS distance $p$-value. To ensure reproducibility across runs without requiring the caller to supply a random seed, the diagnostic derives a deterministic 64-bit integer seed from the SHA-256 digest of the canonical sorted inputs:
  ```python
  def _derive_canonical_seed(observations: list[float], xmin: float, trials: int) -> int:
      hasher = hashlib.sha256()
      hasher.update(f"{xmin}:{trials}:".encode("utf-8"))
      for x in sorted(observations):
          hasher.update(f"{x:.10e},".encode("utf-8"))
      return int(hasher.hexdigest()[:16], 16)
  ```
* **Agent Rule:** Any stochastic calculation engine (e.g. bootstrap, Monte Carlo, multi-armed bandits) must support canonical deterministic seed derivation when `seed=None` to ensure byte-identical reproducibility.

---

### Entry 07: Moment Safety Veto Precedence Over Kelly Sizing
* **Task:** T10 / T11 (Heavy-Tail Decision Hook)
* **Design Decision:** If a power-law fit detects $\alpha \le 2.0$ (infinite/undefined mean), moment-dependent exposure sizing is mathematically invalid.
* **Precedence Order:**
  1. `HOST_EVIDENCE_CONFIRMATION_REQUIRED` / `PORTFOLIO_VERIFICATION_REQUIRED` / `BELIEF_UPDATE_NOT_APPROVED`
  2. `MARGIN_OVERRIDE` (`avoid_margin`) — *Always takes absolute priority*
  3. `MODEL_HEALTH_BLOCK` / `MODEL_HEALTH_DEGRADING`
  4. `HEAVY_TAIL_UNDEFINED_MEAN` / `HEAVY_TAIL_FIT_UNAVAILABLE` — *Vetoes any exposure increase, downgrading target exposure to current exposure and type to `"watch"` or `"hold"`*
  5. `EVIDENCE_CONTRADICTION` / `EVIDENCE_QUALITY_WEAK`
  6. `KELLY_ABOVE_CURRENT` (`increase_exposure`)
  7. `KELLY_BELOW_CURRENT` (`trim_to_kelly`)
  8. `EXPOSURE_ALIGNED` (`hold`)

---

### Entry 08: Exact Ergodic Verification for Markov Chains (Irreducibility & Aperiodicity)
* **Task:** T13 / T14 (Markov Stationary Distribution Diagnostic)
* **Mathematical Challenge:** Computing stationary distributions via power iteration requires the chain to be ergodic (both irreducible and aperiodic). If reducible, power iteration may converge to initial-distribution-dependent vectors; if periodic (e.g. 2-state oscillation), power iteration oscillates and fails to converge.
* **Exact Standard-Library Algorithm:**
  1. **Irreducibility:** Run BFS reachability from each state $i \in \{0, \dots, n-1\}$. The reachable set must have cardinality $n$ for all $i$ (strongly connected digraph).
  2. **Aperiodicity:** In a strongly connected digraph, the chain period equals the greatest common divisor of all directed cycle lengths. Using BFS from root 0 to assign tree levels $L(u)$, for every edge $(u, v) \in E$, the cycle difference length is $|L(u) - L(v) + 1|$. The period is $g = \gcd_{(u, v)} |L(u) - L(v) + 1|$. If $g == 1$, the chain is aperiodic.
  3. **Power Iteration:** Initialize $\pi_0 = [1/n, \dots, 1/n]$, iterate $\pi_{k+1} = \pi_k T$, and terminate when $\|\pi_{k+1} - \pi_k\|_1 \le 10^{-12}$.
* **Agent Rule:** Always reject reducible and periodic chains with explicit unavailable evidence atoms before running power iteration.

---

### Entry 09: Discrete Bass Diffusion Conservation and Edge Boundaries
* **Task:** T15 / T16 (Bass Diffusion Discrete Dynamical Model)
* **Mathematical Invariants:**
  - **Discrete equation:** $\Delta N(t) = \left( p + q \frac{N(t)}{M} \right) (M - N(t))$ with $N(t+1) = \min(M, N(t) + \Delta N(t))$.
  - **Non-negativity & capacity constraints:** $N(t) \le M$ and $\Delta N(t) \ge 0$ for all $t \in [0, T]$.
  - **Stagnation condition:** If $p = 0$ and $N_0 = 0$, adoption can never ignite ($\Delta N(t) = 0$ for all $t$). This is rejected with explicit unavailable reason.
  - **Capacity bounds:** Market potential $M \in (0, 10^9]$, horizon $T \in [1, 10000]$.
* **Agent Rule:** When modeling discrete diffusion, ensure conservation clamping at carrying capacity $M$ and prevent non-ignited parameters from generating deceptive flat curves without an explicit limitation/unavailable indicator.

---

### Entry 10: Multi-Armed Bandit Draw Order and Local RNG Isolation
* **Task:** T17 / T18 (Bernoulli Multi-Armed Bandit Simulation Engine)
* **Architectural Invariants:**
  - **Local RNG Instance:** Never use global `random` functions. Always instantiate `rng = random.Random(seed)` locally to prevent test flakiness and cross-thread/process non-determinism.
  - **Deterministic Draw Order:** For exploration vs exploitation rounds, draw sequence must be fixed: (1) exploration test $u_1 < \epsilon_t$, (2) if explore, uniform arm choice $u_2$, (3) Bernoulli outcome test $u_3 < p_{\text{chosen}}$.
  - **Exact Supported Policy Whitelist:** Only `greedy`, `sample_then_greedy`, and `adaptive_epsilon` are supported in v1. Complex heuristic policies (e.g. UCB1, Thompson Sampling) must be explicitly rejected if requested, rather than silently substituted.
* **Agent Rule:** Always isolate stochastic simulations to local RNG instances with canonical parameter-hash seed derivation when `seed=None`.

---

### Entry 11: Deterministic Claim Ensemble Compilation & Supermajority Aggregation
* **Task:** T19 / T20 (Deterministic Claim Compiler)
* **Design Invariants:**
  - **No Heterogeneous Raw Voting:** Different model families compute qualitatively different quantities (tail index $\alpha$, stationary vector $\pi$, adoption rate $\Delta N(t)$, regret $R$). Models never average numbers across families; they emit discrete claims targeting a specific `claim_id` with a direction (`positive`, `negative`, `neutral`).
  - **Supermajority Threshold:** $\text{threshold} = \max(2, \lceil 2A/3 \rceil)$, where $A$ is the number of independent contributing voting entities.
  - **Two-Family Minimum:** At least 2 distinct model families must independently support a claim for it to qualify as `robust_positive`. A single family with multiple parameter sweeps cannot claim ensemble robustness (clamped to `conditional`).
  - **Correlation Group Collapsing:** Multiple model instances belonging to the same correlation group (e.g. momentum cluster) collapse to a single net vote to prevent double-counting.
  - **Binding Veto Precedence:** Any active binding veto in the input suppresses `robust_positive` across the entire ensemble.
* **Agent Rule:** Always compile multi-model claims strictly on matching `claim_id` with two-family and supermajority thresholds.

---

### Entry 12: Executable Method Pack Registration & Runner Integration
* **Task:** T21 / T22 (Executable Page Method Pack Integration)
* **Architectural Boundaries:**
  - **Executable Packs vs DLC Markdown:** Executable packs must live as typed Python catalog entries in `capital_decision_lab.methods.packs.PACKS` with formal schemas and steps. Root markdown files like `dlc-page.md` or `dlc-contrarian.md` are documentation / persona voices only, and must never be treated as executable packs.
  - **Runner Contract Validation:** When adding new method pack contracts (e.g. `nhi.method_pack_result.v1`, `nhi.committee_result.v1`), they must be registered in `_SCHEMA_FILES` inside `validation.py` and reflected in `test_contract_fixtures.py`.
  - **Six-String Vocabulary:** All method pack recommendation outputs must conform strictly to the standard money-path vocabulary (`pause`, `hold`, `avoid_margin`, `decrease_exposure`, `watch`, `increase_exposure`, `trim_to_kelly`).
* **Agent Rule:** Always verify that newly introduced method packs integrate with both `capital method run --pack <name>` and `capital analyze-position --method <name>`.

---

### Entry 13: Committee Synthesis Closed Vocabulary & Elimination of Silent Fallbacks
* **Task:** T23 / T24 (Hardening Committee Integration)
* **Security & Money-Path Invariants:**
  - **Vulnerability Identified:** Previously, `run_committee()` computed synthesis by `next((item for item in priority if item in recommendations), recommendations[0])`. If an unknown, hostile, or corrupted recommendation string appeared in `recommendations`, it would silently fall through to `recommendations[0]`, bypassing the prioritization hierarchy.
  - **Hardened Fix:** Validate all pack recommendations against `ALLOWED_COMMITTEE_RECOMMENDATIONS`. If any recommendation is outside the whitelist, immediately raise `ValueError("UNKNOWN_RECOMMENDATION_OUTPUT")`.
  - **Deterministic Priority Hierarchy:**
    `"avoid margin"` > `"pause"` > `"trim to fractional Kelly"` / `"trim to kelly"` > `"watch"` > `"hold current exposure"` / `"hold"` > `"decrease exposure"` > `"increase exposure under this assumption set"` / `"increase exposure"`.
* **Agent Rule:** Never allow fallback default selection on untrusted/unvalidated lists in decision synthesis functions. Always validate inputs against an explicit enum whitelist.

---

### Entry 14: Adversarial Security Review, Release Verification & Build Closure
* **Task:** T27 / T28 / T29 (Adversarial Audit, Final Release Gate & Build Closure)
* **Key Lessons & Retrospective Summary:**
  - **Adversarial Input Hardening:** All mathematical diagnostics must defensively reject nonfinite numbers (`NaN`, `+Inf`, `-Inf`) and Python booleans passed as numeric floats, returning standard typed `unavailable` contract envelopes rather than raising unhandled exceptions or returning corrupted numeric values.
  - **Prompt Injection Neutralization:** The deterministic claim compiler operates exclusively on structured claims (`claim_id`, `model_family`, `direction`, `receipt_hash`). Malicious prompt-injection strings placed in metadata, reason codes, or correlation group labels cannot perturb numerical outcomes, supermajority thresholds, or binding safety vetoes.
  - **Strict TDD Ledger Efficacy:** The multi-agent TDD protocol (verifier authors RED tests, freezes SHA-256 test hashes, implementer writes code, green verification confirms test hash unchanged, mutation testing kills mutants) resulted in **98 newly added passing tests** with **0 regressions** and **0 lockfile drift** across the entire 30-task build (`T00`–`T29`).
* **Agent Rule:** Always generate an end-to-end retrospective document (`docs/retrospective_build_page.md`) upon project completion to synthesize architectural design, mathematical formulations, and engineering receipts for future agent pairs.

---

### Entry 15: Engineering Council Remediation of Codex NO-GO Findings
* **Task:** T12, T21–T24, T26–T29 (Engineering Council Remediation Phase)
* **Defects Caught by Codex & Resolutions Applied:**
  1. **Page Runner Multi-Model Integration:** Previously `runner.py` only invoked `power_law`. We wired all four model engines (`power_law`, `markov`, `bass`, `bandits`) into `_run_page_method_pack()`, compiled claims through `compile_claim_ensemble()`, and attached the full `nhi.ensemble_result.v1` envelope to `calculations["ensemble_result"]`.
  2. **Trust Boundary Enforcement:** Handled `trust_class: "untrusted_external"` at the Page runner entry boundary, immediately flagging `UNTRUSTED_EXTERNAL_INPUT` and setting recommendation to `"pause"`.
  3. **Genuine Two-Thesis Outcome Gate (T12):** Replaced synthetic value mutation with genuine heavy-tailed Pareto generation ($\hat{\alpha} \approx 1.8 \le 2.0$) and added Thesis 2 (Biotech Markov Turnaround with 75/25 stationary equilibrium), verifying two non-zero decision deltas naturally.
  4. **Staging & Distribution Inclusion:** Added `dlc-page.md` to `distribution.yaml` (`distribution_owned`) and `scripts/build_profile_staging.py` (`_ALLOWED_FILES`). Verified staging copy and manifest selection.
  5. **Recommendation Vocabulary Normalization:** Normalized `test_page_method_pack.py` to use `ALLOWED_COMMITTEE_RECOMMENDATIONS` natural language strings directly.
  6. **Permanent Mutation Test Suites (T27):** Authored `tests/mutation/test_model_thinking_mutations.py` testing formula kills, moment safety threshold mutation, Markov transposition/aperiodicity mutation, Bass capacity/discrete dynamics mutation, bandit draw-order mutation, and claim compiler supermajority/diversity mutation.
### Entry 16: Engineering Council Round 2 Audit Remediation & AST Source Mutation Engine
* **Task:** T12, T21, T22, T24, T27, T28, T29 (Codex Round 2 Release Blocker Resolution)
* **Defects Identified by Codex Round 2 & Executable Remediations:**
  1. **Strict Per-Model Input Trust Gating:**
     - *Issue:* Trust check relied on top-level flags or assumed trusted defaults.
     - *Fix:* `_run_page_method_pack()` in `runner.py` now scans every active model entry (`power_law`, `markov`, `bass`, `bandit`) for `input_trust_class` / `trust_class`. If any entry is missing, `untrusted_external`, or not in `{"synthetic_test", "user_verified", "verified_local"}`, it flags `UNTRUSTED_EXTERNAL_INPUT`, sets recommendation to `"pause"`, and sets `trust_status = "rejected"` without default assumption.
  2. **Canonical 6-String Closed Recommendation Contract:**
     - *Issue:* Permissive 10-value allowlist introduced vocabulary drift.
     - *Fix:* Unified `ALLOWED_COMMITTEE_RECOMMENDATIONS` and `COMMITTEE_PRIORITY_ORDER` strictly to the canonical 6 strings: `{"avoid margin", "pause", "watch", "hold current exposure", "trim to fractional Kelly", "increase exposure under this assumption set"}`.
  3. **T12 Real Page Execution on Committed Thesis Fixtures:**
     - *Issue:* Thesis 2 computed Markov output isolated from Page runner.
     - *Fix:* Committed valid synthetic fixtures `fixtures/valid/many_model/thesis_run_1_heavy_tail.json` and `fixtures/valid/many_model/thesis_run_2_markov_regime.json`. Updated `tests/distribution/test_outcome_gate.py` to execute `run_method_pack("thorp", case)`, `run_method_pack("page", case)`, and `run_committee(["thorp", "page"], case)` directly, mechanically proving decision deltas $> 0$.
  4. **Genuine AST Source-Level Mutation Engine:**
     - *Issue:* Mutation tests previously functioned as regression tests without executing mutated source bytecode.
     - *Fix:* Built `apply_source_mutation` in `tests/mutation/test_model_thinking_mutations.py` which dynamically rewrites AST source nodes of `power_law.py`, `markov.py`, `bass.py`, `bandits.py`, `compiler.py`, and `runner.py`, compiles isolated mutated modules into `sys.modules`, executes tests against mutated modules, and asserts 100% mutant kill rate across all 10 mutation targets.
  5. **Task List Synchronization & Clean Tree:**
     - *Issue:* Task list state headings were out of sync with summary table.
     - *Historical fix:* Reconciled all detailed task headings (`### T12`–`### T29`) to `- **State:** DONE` with explicit receipts. That pre-hardening checkpoint passed 329 tests; T31 later superseded it with the authoritative 338-test release-candidate run.
* **Agent Rule:** Always build genuine AST-rewriting source-level mutation tests to verify that every mathematical formula, boundary check, and trust gate cannot be mutated without failing test execution.

---

### Entry 17: Page Method Pack Input Schema Hardening & Exception Safety
* **Date:** 2026-09-02
* **Context:** Release hardening audit identified that non-object/malformed model inputs (e.g. `model_thinking_inputs = []`) raised unhandled `AttributeError` instead of returning a deterministic unavailable/pause result.
* **Obstacles & Resolutions:**
  1. **Non-Dict Envelope Handling:**
     - *Issue:* When `model_thinking_inputs` was passed as a `list`, `int`, `str`, or `bool`, calling `.get()` raised an `AttributeError`.
     - *Fix:* Added type verification `if not isinstance(raw_inputs, dict)` at the entry of `_run_page_method_pack()` in `runner.py`, safely returning `recommendation = "pause"`, `trust_status = "rejected"`, and `flags = ["SCHEMA_INVALID_MODEL_INPUTS"]`.
  2. **Schema & Model Entry Validation:**
     - *Issue:* Malformed model entries or invalid schema payloads with declared `contract_version: "nhi.model_input.v1"` could bypass schema verification.
     - *Fix:* Iterated over all active model keys, asserting `isinstance(entry, dict)` and invoking `validate_contract(entry)` when `contract_version` is present.
  3. **Calculation Exception Isolation:**
     - *Issue:* Internal numerical errors or malformed parameters could crash the runner.
     - *Fix:* Wrapped individual model calculation blocks in safe exception blocks that emit standard unavailability flags and fallback to safe watch/pause states.
  4. **Regression Test Suite:**
     - *Fix:* Added 9 dedicated parametrized regression tests in `test_page_runner_e2e.py` covering non-dict inputs (`[]`, `list`, `str`, `int`, `bool`), non-dict model entries, contract schema enum mismatches, and malformed parameter types.
* **Agent Rule:** Orchestration entry points must validate envelope types and schemas before accessing dictionary keys, ensuring that malformed inputs always produce deterministic `pause`/`unavailable` envelopes rather than unhandled process crashes.

---

### Entry 18: v0.2.0 Release Evidence Repair
* **Date:** 2026-09-02
* **Tasks:** T30–T32
* **Learning:** A green suite is not sufficient when its immutable verifier receipt is stale. Preserve the historical hash, record the current hash as a new release baseline, and use an explicit bounded waiver when prior RED ordering cannot be recreated honestly.
* **Verifier Orchestration Rule:** Staging tests and repository-wide scanners must execute serially. Running them concurrently can make the scanner correctly observe the staging test's temporary output and create a false release failure.
* **Current State:** Implementation complete; v0.2.0 release candidate has 338 passing tests. Publication remains pending T33–T34.

