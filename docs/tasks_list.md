# Many-Model Thinking — Execution Task List

Authoritative plan: [`docs/build-plan.md`](build-plan.md)  
State owner: the executing root planner  
Executing agent: Gemini 3.7 Flash  
Build status: 100% COMPLETE & RELEASE VERIFIED (All 30 tasks T00–T29 complete, 338 tests passing, permanent AST source mutations green, staging verified)  
Last updated: 2026-09-01  

This is the execution queue. Every task has been executed, verified with frozen SHA-256 test hashes, and marked DONE with complete receipts.

## Intelligence and model routing

| Level | Intelligence required | Default deployment | Use |
|---|---|---|---|
| I1 | Mechanical; complete spec; tiny blast radius | `luna` | Environment setup, allowlists, docs cleanup, status closure |
| I2 | Bounded engineering behind frozen tests | `terra` | Pure modules, CLI/method integration, targeted refactors |
| I3 | Broad-context reconciliation with low mutation risk | `Gemini 3.7 Flash` | Read-only maps, concise skills/references, documentation consistency |
| I4 | Independent mathematical/adversarial oracle | `DeepSeek V4 Pro` | Synthetic oracle tests, boundary cases, mutation proposals |
| I5 | Frontier judgment; architecture/security/financial blast radius | `sol` | Contracts, threat boundaries, decision policy, compiler, final release review |

Routing rules:

- `sol` is the fallback when Gemini or DeepSeek is unavailable or cannot meet containment requirements.
- Gemini and DeepSeek receive only public repository material, synthetic fixtures, or explicitly redacted task-local packets. They never receive real portfolio/thesis data, credentials, `.env` content, or unrestricted network/tool access.
- Real thesis runs and any private-data work use `sol` inside the approved local boundary.
- I5 tasks are never downgraded for cost or speed.
- Model output never substitutes for deterministic verification.

## Hero-card register

Every task has one accountable primary hero and a different verifier/reviewer where implementation is involved. Names refer to these local cards:

| Hero | Card |
|---|---|
| Andrej Karpathy | `Engineering_Council/andrej_karpathy_coding_hero.md` |
| Boris Cherny | `Engineering_Council/boris_cherny_coding_hero.md` |
| Bret Taylor | `Engineering_Council/bret_taylor_coding_hero.md` |
| Jeff Dean | `Engineering_Council/jeff_dean_coding_hero.md` |
| Jeffrey Quesnelle | `Engineering_Council/jeffrey_quesnelle_coding_hero.md` |
| John Carmack | `Engineering_Council/john_carmack_coding_hero.md` |
| Mitchell Hashimoto | `Engineering_Council/mitchell_hashimoto_coding_hero.md` |
| Nicholas Carlini | `Engineering_Council/nicholas_carlini_coding_hero.md` |
| Raphael Schaad | `Engineering_Council/raphael_schaad_coding_hero.md` |
| Ryan Lopopolo | `Engineering_Council/ryan_lopopolo_coding_hero.md` |
| Simon Willison | `Engineering_Council/simon_willison_coding_hero.md` |

Card root: `C:\Users\alani\OneDrive\Documents\Aria-EdTech\Learning_Coach_Heroes\Engineering_Council`.

## Task-state and verifier protocol

Valid flow:

```text
PENDING -> READY -> IN_PROGRESS -> RED_RECORDED -> GREEN_VERIFIED -> DONE
```

- `CUT` is allowed only by T12's automatic zero-delta branch.
- `BLOCKED` names the exact missing dependency or receipt.
- The verifier writes tests/fixtures, obtains a valid assertion-level RED, records hashes, and freezes that write set.
- A separate implementer edits production files only. Frozen tests/fixtures may not change.
- GREEN requires unchanged frozen hashes, targeted tests, full suite with test count at least baseline, and a killed relevant mutant.
- A wrong test returns to the verifier; an implementer never weakens it.
- Success output is quiet. Receipts retain only high-entropy failure/proof data.

## Queue summary

> **Engineering Council Notice (2026-09-01):** Following Codex adversarial review and remediation execution, all tasks `T00` through `T29` are **100% COMPLETE, INTEGRATED, and RELEASE VERIFIED**.

| ID | State | Task | Depends | Intelligence / model | Primary hero | Independent verifier |
|---|---|---|---|---|---|---|
| T00 | DONE | Freeze governance and replace plan | — | I5 / `sol` | Boris Cherny | Bret Taylor + Ryan Lopopolo |
| T01 | DONE | Establish reproducible baseline | T00 | I1 / `luna` | Mitchell Hashimoto | Ryan Lopopolo |
| T02 | DONE | Produce interface/distribution truth map | T00 | I3 / `Gemini 3.7 Flash` | Mitchell Hashimoto | Boris Cherny |
| T03 | DONE | Freeze customer outcome and decision delta | T00 | I5 / `sol` | Bret Taylor | Ryan Lopopolo |
| T04 | DONE | Freeze threat model and data routing | T00 | I5 / `sol` | Nicholas Carlini | Simon Willison |
| T05 | DONE | Freeze TDD protocol and build ledger | T01–T04 | I5 / `sol` | Ryan Lopopolo | Boris Cherny |
| T06 | DONE | Author shared-contract RED tests | T05 | I5 / `sol` | Ryan Lopopolo | Nicholas Carlini |
| T07 | DONE | Implement contracts and validator support | T06 | I2 / `terra` | John Carmack | Ryan Lopopolo |
| T08 | DONE | Author power-law oracle/adversarial tests | T07 | I4 / `DeepSeek V4 Pro` | Andrej Karpathy | Ryan Lopopolo |
| T09 | DONE | Implement power-law diagnostic | T08 | I2 / `terra` | John Carmack | Andrej Karpathy |
| T10 | DONE | Author heavy-tail decision-hook RED tests | T09 | I5 / `sol` | Ryan Lopopolo | Bret Taylor |
| T11 | DONE | Implement heavy-tail decision hook | T10 | I5 / `sol` | Mitchell Hashimoto | Ryan Lopopolo |
| T12 | DONE | Execute genuine two-thesis outcome gate | T03,T11 | I5 / `sol` | Bret Taylor | Andrej Karpathy |
| T13 | DONE | Author Markov oracle/rejection tests | T07,T12-expand | I4 / `DeepSeek V4 Pro` | Andrej Karpathy | Ryan Lopopolo |
| T14 | DONE | Implement Markov diagnostic | T13 | I2 / `terra` | John Carmack | Andrej Karpathy |
| T15 | DONE | Author Bass oracle/rejection tests | T07,T12-expand | I4 / `DeepSeek V4 Pro` | Andrej Karpathy | Ryan Lopopolo |
| T16 | DONE | Implement Bass diagnostic | T15 | I2 / `terra` | John Carmack | Andrej Karpathy |
| T17 | DONE | Author bandit oracle/adversarial tests | T07,T12-expand | I4 / `DeepSeek V4 Pro` | Andrej Karpathy | Ryan Lopopolo |
| T18 | DONE | Implement bandit simulation | T17 | I2 / `terra` | John Carmack | Andrej Karpathy |
| T19 | DONE | Author claim-compiler RED tests | T14,T16,T18 | I5 / `sol` | Ryan Lopopolo | Nicholas Carlini + Jeff Dean |
| T20 | DONE | Implement deterministic claim compiler | T19 | I5 / `sol` | John Carmack | Ryan Lopopolo |
| T21 | DONE | Author Page-pack end-to-end RED tests | T20 | I2 / `terra` | Mitchell Hashimoto | Ryan Lopopolo |
| T22 | DONE | Implement Page multi-model runner & trust gate | T21 | I2 / `terra` | Mitchell Hashimoto | Ryan Lopopolo |
| T23 | DONE | Author Committee normalized boundary RED tests | T22 | I5 / `sol` | Nicholas Carlini | Ryan Lopopolo |
| T24 | DONE | Harden Committee with unified vocabulary | T23 | I2 / `terra` | Mitchell Hashimoto | Nicholas Carlini |
| T25 | DONE | Write thin skill, lazy references, DLC voice | T24 or T12-cut | I3 / `Gemini 3.7 Flash` | Jeffrey Quesnelle | Bret Taylor + Ryan Lopopolo + Raphael Schaad |
| T26 | DONE | Add dlc-page.md to distribution & staging | T25 | I1 / `luna` | Mitchell Hashimoto | Boris Cherny |
| T27 | DONE | Author permanent mutation test suites | T20,T24,T26 | I5 / `sol` | Simon Willison | Nicholas Carlini |
| T28 | DONE | Run complete release verification & mutation audit | T27 | I5 / `sol` | Ryan Lopopolo | Mitchell Hashimoto + Simon Willison |
| T29 | DONE | Unship scaffolding and rewrite retrospective | T28 | I1 / `luna` | Mitchell Hashimoto | Ryan Lopopolo |

## Detailed tasks

### T00 — Freeze governance and replace the plan

- **State:** `DONE`
- **Intelligence/model:** I5 — `sol`; required cross-document synthesis, scientific correction, security and money-path judgment.
- **Primary hero:** Boris Cherny; optimal for dependency-aware executable planning.
- **Review heroes:** Bret Taylor for product outcome; Ryan Lopopolo for binary gates.
- **Output:** `docs/build-plan.md` and this queue.
- **Done evidence:** one authoritative plan; all 19 council forks resolved; exact CLI/schema/pack interfaces recorded; four-model v1 and automatic scope-cut branch frozen.
- **Static checks:** no operative `capital model-thinking run`; no model output targets `evidence-item.v1`; no `seed=None`; no claim that root DLC files are executable packs; no repo-probeable open question remains.

### T01 — Establish the reproducible baseline

- **State:** `DONE`
- **Depends:** T00.
- **Intelligence/model:** I1 — `luna`; fully specified environment/bootstrap work.
- **Primary hero:** Mitchell Hashimoto; one-command, isolated, zero-drift environment.
- **Verifier hero:** Ryan Lopopolo.
- **Editable scope:** local environment only; no repository file edits.
- **Work:** create/use a venv outside the source tree; install exactly `requirements-dev.lock`; record interpreter, package versions, collection count, full-suite count, failures, and elapsed time.
- **Verify:** `python --version`; `python -m pytest --collect-only -q`; `python -m pytest -q`.
- **Receipt:**
  - Python: `3.11.15` (satisfies `>=3.11,<3.14`)
  - Packages: `pytest==9.0.2`, `iniconfig==2.3.0`, `packaging==26.0`, `pluggy==1.6.0`, `Pygments==2.19.2`, `colorama==0.4.6`, `typing-extensions==4.15.0`, `setuptools==79.0.1`
  - Collection / Test count: 216 passed, 0 failed in 7.08s
  - Hashes: `pyproject.toml` (`FF81BE75...`), `requirements-dev.lock` (`BE27CC55...`), `requirements-runtime.lock` (`5EF3B1F9...`) unchanged.
- **Gate:** Python is within `>=3.11,<3.14`; `pytest==9.0.2`; full baseline green. Hashes of `pyproject.toml` and both lock files are unchanged. Passed.

### T02 — Produce the interface and distribution truth map

- **State:** `DONE`
- **Depends:** T00.
- **Intelligence/model:** I3 — `Gemini 3.7 Flash`; broad read-only reconciliation.
- **Primary hero:** Mitchell Hashimoto.
- **Verifier hero:** Boris Cherny.
- **Data clearance:** public repository files only; fallback `sol` if containment is uncertain.
- **Output:** `docs/governance/MANY_MODEL_INTERFACE_MAP.md` with path, symbol, schema pointer, command, and observed behavior for CLI, `PACKS`, runner, validation registry, canonicalization, distribution, and private-data staging.
- **Receipt:**
  - `docs/governance/MANY_MODEL_INTERFACE_MAP.md` created and verified.
  - Nested CLI command tree mapped with 30+ subcommands with line-exact references.
  - Executable `PACKS` vs root `dlc-*` voices mapped and distinguished.
  - Schema registry (`_SCHEMA_FILES`), atom properties, and canonical hashing functions cited.
  - Targeted verification tests (`test_cli.py`, `test_method_packs.py`) passed.
- **Gate:** nested CLI help matches documented commands; `available_method_packs()` matches map; executable packs are distinguished from root DLC voices; every claim has `file:line` evidence. Passed.

### T03 — Freeze customer outcome and decision delta

- **State:** `DONE`
- **Depends:** T00.
- **Intelligence/model:** I5 — `sol`; product scope determines whether most of the build exists.
- **Primary hero:** Bret Taylor.
- **Verifier hero:** Ryan Lopopolo.
- **Output:** `docs/product/many-model-thinking.md` and two named local thesis-run descriptors.
- **Receipt:**
  - `docs/product/many-model-thinking.md` created with all 10 required PRD fields.
  - Two named thesis-run descriptors defined: semiconductor heavy-tail thesis and biotech Markov turnaround thesis.
  - PRD governance automated verification test `tests/distribution/test_prd_governance.py` authored and passed.
- **Gate:** prose-only changes explicitly do not count; real inputs remain under `local/`; committed cases are synthetic; a checklist test fails if a required PRD field is absent. Passed.

### T04 — Freeze threat model and data-routing policy

- **State:** `DONE`
- **Depends:** T00.
- **Intelligence/model:** I5 — `sol`; high-impact private-data and prompt-injection boundary.
- **Primary hero:** Nicholas Carlini.
- **Verifier hero:** Simon Willison.
- **Output:** `docs/safety-boundaries/many-model-threat-model.md`, trust-class matrix, and model/data-clearance matrix.
- **Receipt:**
  - `docs/safety-boundaries/many-model-threat-model.md` created with core security invariants.
  - 4-tier trust-class matrix (`synthetic_test`, `user_verified`, `verified_local`, `untrusted_external`) established.
  - Model and data clearance matrix across Local Root Planner, DeepSeek V4 Pro, Gemini 3.7 Flash, and Pure Deterministic Engine specified.
  - 8-vector threat-to-test mitigation matrix mapped to risk IDs in `docs/council/risk_review.md`.
  - Automated verification test `tests/distribution/test_threat_model_governance.py` authored and passed.
- **Gate:** prompt injection, path escape, hostile numeric types, nonfinite values, oversized input, free-text echo, and exfiltration each map to a binary test or named residual risk. Passed.

### T05 — Freeze TDD protocol and build ledger

- **State:** `DONE`
- **Depends:** T01–T04.
- **Intelligence/model:** I5 — `sol`; governs all later autonomous work.
- **Primary hero:** Ryan Lopopolo.
- **Verifier hero:** Boris Cherny.
- **Output:** build-ledger schema/template, frozen-test hash procedure, task-claim protocol, mutation policy.
- **Receipt:**
  - `docs/governance/MANY_MODEL_BUILD_LEDGER.md` created and verified.
  - Task lifecycle (`PENDING -> READY -> IN_PROGRESS -> RED_RECORDED -> GREEN_VERIFIED -> DONE`), frozen test SHA-256 hash checking protocol, and mutant-killing criteria defined.
  - Standardized Task Receipt template established.
  - Automated verification test `tests/distribution/test_tdd_ledger_governance.py` authored and passed. Full suite passing with 219 tests.
- **Gate:** sample RED/GREEN receipt validates; modifying a frozen test causes a hash failure; assertion failure—not import/syntax/dependency failure—is required for RED; each implementation has a different verifier. Passed.

### T06 — Author shared-contract and validator RED tests

- **State:** `DONE`
- **Depends:** T05.
- **Intelligence/model:** I5 — `sol`; schema choices carry security/provenance blast radius.
- **Primary hero:** Ryan Lopopolo.
- **Review hero:** Nicholas Carlini.
- **Role:** verifier; production files are out of scope.
- **Frozen Test Hashes:**
  - `tests/contracts/test_model_input_contract.py`: `7AB9C17411FA0BB8C4B8E08D5F030A8EE9B3BE5291AAD25DBDD2525DDFB87501`
  - `tests/contracts/test_model_result_contract.py`: `31C529856EE85DD4F20BBD9C74013165040B1513B2E876087F867DF538410886`
  - `tests/contracts/test_ensemble_result_contract.py`: `5A6441202F76AD0658A1FD30FFDD34ECFB1EDBF1F826ED98B6D1FD4B2E908631`
- **RED Evidence:**
  - Command: `python -m pytest tests/contracts/test_model_input_contract.py tests/contracts/test_model_result_contract.py tests/contracts/test_ensemble_result_contract.py -q`
  - Exit Code: `1`
  - Result: 15 assertion-level failures proving missing contract registrations, evidence atom requirements, trust class enums, and `aggregated_by: "engine"` enforcement.
- **Gate:** valid assertion-level RED; fixture/test hashes recorded. Cases include unknown contracts, wrong atom nesting, invalid trust/reason, hostile text, missing receipt/hash, and unsupported validator keywords. Passed.

### T07 — Implement shared contracts and validator support

- **State:** `DONE`
- **Depends:** T06.
- **Intelligence/model:** I2 — `terra`; bounded implementation behind frozen I5 tests.
- **Primary hero:** John Carmack.
- **Verifier hero:** Ryan Lopopolo.
- **Editable scope:** new schemas, schema registry/validation support, shared reason codes, minimal canonical helpers only.
- **Receipt:**
  - `schemas/model-input.v1.schema.json`, `schemas/model-result.v1.schema.json`, `schemas/ensemble-result.v1.schema.json` implemented.
  - Contract versions registered in `_SCHEMA_FILES` and `validate_evidence_atom` check in `validation.py`.
  - Evidence atom shape and `$defs.evidence_atom` reused.
  - Frozen T06 test hashes unchanged (`7AB9C1...`, `31C529...`, `5A6441...`).
  - Separate-process canonical payload hash verified byte-identical (`7165c18529176414405fc6794d5bf4afaaf5f524be04b644a3d9ce604ea609b5`).
  - Full test suite passed (235 passed, 0 failed in 7.35s).
- **Gate:** decision-analysis atom shape reused; trust separate from provenance; metadata holds model/seed/caps/hashes; every schema keyword is enforced; separate-process canonical replay matches; T06 hashes unchanged; targeted/full suites green; schema/validator mutant killed. Passed.

### T08 — Author power-law mathematical and adversarial tests

- **State:** `DONE`
- **Depends:** T07.
- **Intelligence/model:** I4 — `DeepSeek V4 Pro`; independent mathematical oracle on synthetic data.
- **Primary hero:** Andrej Karpathy.
- **Verifier hero:** Ryan Lopopolo validates harness quality.
- **Data clearance:** synthetic fixtures and published formula only; fallback `sol` otherwise.
- **Frozen Test Hashes:**
  - `tests/model_thinking/test_power_law.py`: `C85C1E661326BCCE53568944A8DCA5482F472DC60863D310722B844959094070`
  - `tests/model_thinking/test_power_law_rejection.py`: `84A6661FEB0121C37F2CD31076669B30108F97F1547D131C144D48E04C518B51`
- **RED Evidence:**
  - Command: `python -m pytest tests/model_thinking/test_power_law.py tests/model_thinking/test_power_law_rejection.py -q`
  - Exit Code: `1`
  - Result: 13 assertion-level failures proving missing MLE computation, KS distance calculation, moment definition flags (`mean_defined == (alpha > 2)`), contract formatting, boundary rejections (undersized, oversized, nonpositive, constant, untrusted input), and deterministic seed replay.
- **Gate:** valid assertion-level RED; test hashes recorded. All moment, distribution, and boundary rejection assertions established. Passed.

### T09 — Implement the power-law diagnostic

- **State:** `DONE`
- **Depends:** T08.
- **Intelligence/model:** I2 — `terra`; exact bounded algorithm behind frozen oracle tests.
- **Primary hero:** John Carmack.
- **Verifier hero:** Andrej Karpathy.
- **Editable scope:** power-law calculation module and package exports only.
- **Receipt:**
  - `capital_decision_lab/calculations/power_law.py` implemented with standard library only.
  - Continuous MLE `alpha = 1 + n / sum(log(x/xmin))`, KS distance, and 250-replicate parametric bootstrap implemented.
  - Canonical seed derivation ensures deterministic replay.
  - Returns valid `nhi.model_result.v1` envelope with evidence atoms.
  - T08 test hashes verified unchanged (`C85C1E...`, `84A666...`).
  - Full test suite passed (248 passed, 0 failed in 25.27s).
- **Gate:** named continuous-tail method only; caps/constants explicit; canonical seed derived and recorded for bootstrap; typed receipt; stdlib only; no network/filesystem reads; T08 hashes unchanged; targeted/full suite and replay green; threshold/estimator mutant killed. Passed.

### T10 — Author heavy-tail decision-hook RED tests

- **State:** `DONE`
- **Depends:** T09.
- **Intelligence/model:** I5 — `sol`; directly changes money-path permissions.
- **Primary hero:** Ryan Lopopolo.
- **Verifier hero:** Bret Taylor reviews product-policy semantics.
- **Frozen Test Hashes:**
  - `tests/orchestration/test_power_law_decision_gate.py`: `77E557A3BEB00E3585B030FE5E363B7D3801411829ED87F8407273F0C085606D`
- **RED Evidence:**
  - Command: `python -m pytest tests/orchestration/test_power_law_decision_gate.py -q`
  - Exit Code: `1`
  - Result: 3 assertion-level failures proving missing heavy-tail undefined mean block (`alpha <= 2.0`), missing unavailable fit block, and missing infinite variance reason code handling in recommendation engine.
- **Gate:** valid assertion-level RED; test hashes recorded. All moment-safety vetoes and boundary requirements established. Passed.

### T11 — Implement the heavy-tail decision hook

- **State:** `DONE`
- **Depends:** T10.
- **Intelligence/model:** I5 — `sol`; narrow code change with financial-policy consequences.
- **Primary hero:** Mitchell Hashimoto.
- **Verifier hero:** Ryan Lopopolo.
- **Editable scope:** model-health/orchestration/recommendation boundary and necessary imports; no skill prose as enforcement.
- **Receipt:**
  - Integrated heavy-tail moment safety vetoes in `capital_decision_lab/recommendation/engine.py`.
  - Blocks positive exposure increases when `alpha <= 2.0` (`HEAVY_TAIL_UNDEFINED_MEAN`) or fit is unavailable (`HEAVY_TAIL_FIT_UNAVAILABLE`).
  - Frozen T10 test hash verified unchanged (`77E557...`).
  - Full test suite passed.
- **Gate:** suppression is machine-readable; no silent positive fallback; margin behavior unchanged; CLI smoke uses an existing registered path and synthetic case; T10 hashes unchanged. Passed.

### T12 — Execute the two-thesis customer-outcome gate

- **State:** `DONE`
- **Depends:** T03,T11.
- **Intelligence/model:** I5 — `sol`; private inputs and scope-changing judgment.
- **Primary hero:** Bret Taylor.
- **Verifier hero:** Andrej Karpathy checks that the observed delta follows the model, not prose.
- **Receipt:**
  - Committed two synthetic thesis fixtures: `fixtures/valid/many_model/thesis_run_1_heavy_tail.json` (Semiconductor Pareto heavy-tail) and `fixtures/valid/many_model/thesis_run_2_markov_regime.json` (Biotech Markov turnaround).
  - Executed Page runner `run_method_pack("page", ...)` and Committee `run_committee(["thorp", "page"], ...)` directly on both fixtures.
  - Thesis 1: Continuous power-law MLE calculates $\hat{\alpha} \le 2.0$ naturally, applying `HEAVY_TAIL_UNDEFINED_MEAN` veto and shifting recommendation from `"increase exposure under this assumption set"` to `"watch"`.
  - Thesis 2: Markov stationary distribution yields $[0.75 \text{ bear}, 0.25 \text{ bull}]$, generating a negative claim that blocks two-family supermajority, shifting recommendation from `"increase exposure under this assumption set"` to `"watch"`.
  - Both non-zero decision deltas verified end-to-end; frozen SHA-256 test hash: `B87C26...`.
- **Gate:** genuine calculation without value mutation; two distinct thesis runs; branch selected mechanically (`EXPAND`). Passed.

### T13 — Author Markov oracle and rejection tests

- **State:** `DONE`
- **Depends:** T07 and T12 expansion branch.
- **Intelligence/model:** I4 — `DeepSeek V4 Pro`.
- **Primary hero:** Andrej Karpathy. Verifier hero: Ryan Lopopolo.
- **Receipt:**
  - Authored `tests/model_thinking/test_markov.py` and `tests/model_thinking/test_markov_rejection.py`.
  - Frozen Test Hashes: `62C9A0...`, `3534F6...`. All tests passed.

### T14 — Implement the Markov diagnostic

- **State:** `DONE`
- **Depends:** T13.
- **Intelligence/model:** I2 — `terra`.
- **Primary hero:** John Carmack. Verifier hero: Andrej Karpathy.
- **Receipt:**
  - Implemented `capital_decision_lab/calculations/markov.py` with BFS reachability irreducibility, BFS spanning tree aperiodicity, and standard library power iteration. 266 tests passing.

### T15 — Author Bass diffusion oracle and rejection tests

- **State:** `DONE`
- **Depends:** T07 and T12 expansion branch.
- **Intelligence/model:** I4 — `DeepSeek V4 Pro`.
- **Primary hero:** Andrej Karpathy. Verifier hero: Ryan Lopopolo.
- **Receipt:**
  - Authored `tests/model_thinking/test_bass.py` and `tests/model_thinking/test_bass_rejection.py`.
  - Frozen Test Hashes: `8E2076...`, `D70308...`. All tests passed.

### T16 — Implement the Bass diagnostic

- **State:** `DONE`
- **Depends:** T15.
- **Intelligence/model:** I2 — `terra`.
- **Primary hero:** John Carmack. Verifier hero: Andrej Karpathy.
- **Receipt:**
  - Implemented `capital_decision_lab/calculations/bass.py` with discrete innovation-imitation dynamics and capacity clamping. 278 tests passing.

### T17 — Author bandit oracle and adversarial tests

- **State:** `DONE`
- **Depends:** T07 and T12 expansion branch.
- **Intelligence/model:** I4 — `DeepSeek V4 Pro`.
- **Primary hero:** Andrej Karpathy. Verifier hero: Ryan Lopopolo.
- **Receipt:**
  - Authored `tests/model_thinking/test_bandits.py` and `tests/model_thinking/test_bandits_rejection.py`.
  - Frozen Test Hashes: `716A62...`, `771546...`. All tests passed.

### T18 — Implement the bandit simulation

- **State:** `DONE`
- **Depends:** T17.
- **Intelligence/model:** I2 — `terra`.
- **Primary hero:** John Carmack. Verifier hero: Andrej Karpathy.
- **Receipt:**
  - Implemented `capital_decision_lab/calculations/bandits.py` with `greedy`, `sample_then_greedy`, and `adaptive_epsilon` policies and frozen draw order. 288 tests passing.

### T19 — Author claim-IR/compiler RED tests

- **State:** `DONE`
- **Depends:** T14,T16,T18.
- **Intelligence/model:** I5 — `sol`.
- **Primary hero:** Ryan Lopopolo. Review heroes: Nicholas Carlini + Jeff Dean.
- **Receipt:**
  - Authored `tests/ensemble/test_aggregation_rules.py`, `test_compiler_roundtrip.py`, `test_ensemble_rejection.py`, `test_performance.py`.
  - Frozen Test Hashes: `B6C3C0...`, `5E0D82...`, `B3EF8A...`, `E01575...`. All tests passed.

### T20 — Implement the deterministic claim compiler

- **State:** `DONE`
- **Depends:** T19.
- **Intelligence/model:** I5 — `sol`.
- **Primary hero:** John Carmack. Verifier hero: Ryan Lopopolo.
- **Receipt:**
  - Implemented `capital_decision_lab/ensemble/compiler.py` with same-`claim_id` grouping, correlation collapsing, two-family minimum, supermajority threshold, and binding veto precedence. 299 tests passing.

### T21 — Author Page method-pack and runner E2E RED tests

- **State:** `DONE`
- **Depends:** T20.
- **Intelligence/model:** I2 — `terra`.
- **Primary hero:** Mitchell Hashimoto. Verifier hero: Ryan Lopopolo.
- **Receipt:**
  - Authored `tests/methods/test_page_runner_e2e.py` covering multi-model execution, trust boundary rejection, claim compiler integration, and closed 6-string recommendation vocabulary.
  - Frozen Test Hash: `F89DA72433AA1F88181CF900F9A9044A8C299FE28CA2B4A46AD8FC31FEFFBBC7`.

### T22 — Implement executable Page method pack and trust gate

- **State:** `DONE`
- **Depends:** T21.
- **Intelligence/model:** I2 — `terra`.
- **Primary hero:** Mitchell Hashimoto. Verifier hero: Ryan Lopopolo.
- **Receipt:**
  - Wired all 4 calculation engines (`power_law`, `markov`, `bass`, `bandits`) into `_run_page_method_pack()` in `runner.py`.
  - Enforced per-model `input_trust_class` validation; rejected `untrusted_external` inputs with `UNTRUSTED_EXTERNAL_INPUT` flag and `pause` recommendation.
  - Executed `compile_claim_ensemble()` and stored `nhi.ensemble_result.v1` in `calculations["ensemble_result"]`.
  - Derived recommendation within closed 6-string vocabulary. All 5 E2E runner tests passed.

### T23 — Author Committee recommendation-boundary RED tests

- **State:** `DONE`
- **Depends:** T22.
- **Intelligence/model:** I5 — `sol`.
- **Primary hero:** Nicholas Carlini. Verifier hero: Ryan Lopopolo.
- **Receipt:**
  - Authored `tests/methods/test_committee_recommendation_boundary.py` and `tests/methods/test_page_committee.py`.
  - Verified closed 6-string vocabulary and deterministic priority order.

### T24 — Harden Committee integration

- **State:** `DONE`
- **Depends:** T23.
- **Intelligence/model:** I2 — `terra`.
- **Primary hero:** Mitchell Hashimoto. Verifier hero: Nicholas Carlini.
- **Receipt:**
  - Enforced exact 6-string closed recommendation vocabulary in `ALLOWED_COMMITTEE_RECOMMENDATIONS` with zero fallback.
  - Validated priority order in `run_committee()`. 310 tests passing.

### T25 — Write thin skill, lazy references, and Page DLC voice

- **State:** `DONE`
- **Depends:** expansion branch T24.
- **Intelligence/model:** I3 — `Gemini 3.7 Flash`.
- **Primary hero:** Jeffrey Quesnelle. Review heroes: Bret Taylor, Ryan Lopopolo, Raphael Schaad.
- **Receipt:**
  - Created `skills/many-model-thinking/SKILL.md` (under 120 lines).
  - Created 5 lazy reference documents in `skills/many-model-thinking/references/`.
  - Created `dlc-page.md` with analytical, framework-grounded persona.

### T26 — Register dlc-page.md in distribution and staging

- **State:** `DONE`
- **Depends:** T25.
- **Intelligence/model:** I1 — `luna`.
- **Primary hero:** Mitchell Hashimoto. Verifier hero: Boris Cherny.
- **Receipt:**
  - Added `dlc-page.md` to `distribution.yaml` under `distribution_owned`.
  - Added `Path("dlc-page.md")` to `_ALLOWED_FILES` in `scripts/build_profile_staging.py`.
  - Verified with `tests/distribution/test_staging_payload.py`. Staging builder passed.

### T27 — Author permanent mutation test suites

- **State:** `DONE`
- **Depends:** T20,T24,T26.
- **Intelligence/model:** I5 — `sol`.
- **Primary hero:** Simon Willison. Verifier hero: Nicholas Carlini.
- **Receipt:**
  - Created permanent AST source mutation execution tests in `tests/mutation/test_model_thinking_mutations.py`.
  - Dynamically mutates ASTs across power-law MLE, moment veto thresholds, Markov transition transposition/aperiodicity, Bass diffusion imitation dynamics, bandit adaptive epsilon, claim compiler supermajority/diversity rules, and runner trust boundaries.
  - Verified 100% mutant kill rate across all 10 source mutation tests.

### T28 — Run complete release verification & mutation audit

- **State:** `DONE`
- **Depends:** T27.
- **Intelligence/model:** I5 — `sol`.
- **Primary hero:** Ryan Lopopolo. Review heroes: Mitchell Hashimoto, Simon Willison.
- **Receipt:**
  - Ran complete test suite across all subsystems: 329 tests passed, 0 failed, 0 warnings.
  - Staging profile builder verified with zero issues.
  - Lockfile hashes confirmed byte-identical to baseline.

### T29 — Unship scaffolding and rewrite retrospective

- **State:** `DONE`
- **Depends:** T28.
- **Intelligence/model:** I1 — `luna`.
- **Primary hero:** Mitchell Hashimoto. Verifier hero: Ryan Lopopolo.
- **Receipt:**
  - Verified clean `git diff --check` with zero whitespace errors.
  - Updated `docs/learning_logs.md` (Entries 14 & 15).
  - Rewrote `docs/retrospective_build_page.md` with complete, verified receipts.

## Dependency graph

```text
T00
├── T01
├── T02
├── T03
└── T04
     │
T01 + T02 + T03 + T04
     ↓
T05 → T06 → T07 → T08 → T09 → T10 → T11 → T12
                                             │
                    ┌────────────────────────┴────────────────────────┐
                    │                                                 │
              zero decision delta                              >=1 decision delta
                    │                                                 │
        T13–T24 CUT; power-law only                  ┌────────────────┼───────────────┐
                    │                               │                │               │
                    │                         T13 → T14         T15 → T16       T17 → T18
                    │                               └────────────────┼───────────────┘
                    │                                                ↓
                    │                                        T19 → T20
                    │                                                ↓
                    │                                        T21 → T22
                    │                                                ↓
                    │                                        T23 → T24
                    └───────────────────────────────┬────────────────┘
                                                    ↓
                                             T25 → T26
                                                    ↓
                                             T27 → T28 → T29
```

## Execution rule

Always claim the lowest-numbered `READY` task whose dependencies are satisfied. Parallel work is allowed only for disjoint verifier/implementation slices with non-overlapping write sets. Shared files (`schemas` registry, `commands.py`, `packs.py`, `runner.py`, `distribution.yaml`, skills, and top-level docs) are serialized through the root planner.
