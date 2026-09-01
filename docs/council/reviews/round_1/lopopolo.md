# Round 1 Blind Review — [R] Ryan Lopopolo, Harness Master

**Persona:** [L] Harness Master. **Operating question:** "What harness rule makes this failure class physically harder to repeat?"
**Scope:** `docs/build-plan.md` as a build plan for the Many-Model Thinking extension. Product value and aesthetics deferred. Every objection below is stated as a binary, mechanically executable task gate.

I verified plan claims against the actual tree before asserting anything. Three of the plan's own claims are **wrong against the repo as it exists today**, and the plan's gate structure is prose, not machinery. Those two facts drive most of this review.

---

## Key Risks

**R1 — CRITICAL: The plan's schema conformance target does not exist as the plan describes it.**
Artifacts 2, 3, 4, 19 all say "Output evidence-atoms conform to `evidence-item.v1.schema.json`." I read `schemas/evidence-item.v1.schema.json`: it is a **source-evidence item** contract requiring `source_ref`, `source_type`, `verification_status`, `timestamp`, `captured_at`, `direction`, `claim_tags`, `content`, `thesis_relevance`, `source_credibility` — none of which a Markov stationary distribution possesses. The actual evidence-atom shape lives in `$defs.atom` in `bayesian-update.v1.schema.json` and `decision-analysis.v1.schema.json` (`value`, `provenance_class`, `unit`, `input_refs`, `formula_ref`, `limitations`, `reason`), and that is what `calculations/simulation.py` actually emits. If the agent executes the plan as written, it will either (a) force model outputs into a contract they cannot satisfy, or (b) emit atoms that pass a *different* schema while the plan claims conformance — a silent spec drift that no reviewer catches because the plan cites the wrong file by name.
> **Binary gate:** `G-SCHEMA-1`: `python -c "import jsonschema; jsonschema.validate(<engine output fixture>, json.load(open('schemas/<declared-schema>')))"` must exit 0 for the *exact schema filename named in the artifact spec*, with the filename check enforced by a test that greps the build plan against `schemas/`. A schema filename cited in a spec that does not validate the output = gate fails. No partial credit.

**R2 — CRITICAL: The plan encodes test-after-code, which is the Red/Green inversion.**
Phase 1 artifact ordering is explicit: Artifact 2 (markov.py) → Artifact 5 (test_markov.py), and the dependency block says "**Tests depend on their respective calculation modules**." That is Green-then-Red. "A gate that only lives in documentation does not exist" — and this plan's *ordering itself* is documentation of a process that guarantees the failure class it claims to prevent: tests written against a finished implementation only restate what the implementation does. There is no failing-test-first artifact anywhere in the plan.
> **Binary gate:** `G-TDD-1`: per module, the CI job order is `pytest tests/formulas/test_<model>.py` → must exit non-zero on a repo state with no `model_thinking/<model>.py` (RED proof, logged), then implement, then `pytest` → zero. CI must record the RED artifact (the pre-implementation failing run output file). A phase whose tests only ever ran green = gate fails. Additionally, `G-TAMPER-1`: a CI step computes a hash of `tests/formulas/` + `fixtures/valid/model_thinking/` before and after the implementation job; any diff to test or fixture files inside the implementation job = gate fails (eval tamper detection).

**R3 — HIGH: `seed=None` default is a determinism escape hatch baked into every stochastic function signature.**
The plan specifies `stationary_distribution(..., seed=None)`, `power_law_check(data, seed=None)`, etc. The existing convention in `simulation.py` is the opposite: `seed: int` is **required**, validated (`isinstance(seed, int) and not isinstance(seed, bool)`), and recorded in `metadata`. `seed=None` in a stochastic model means the same CLI invocation produces different outputs on different days — exactly the failure C4 exists to kill, and the reproducibility acceptance criterion ("All numbers from engine are reproducible from (inputs + seed) alone") becomes untestable because the runner may silently fall back to entropy.
> **Binary gate:** `G-DET-1`: AST lint on `calculations/model_thinking/*.py` fails if any public function signature contains `seed=None`, or if `random.Random` is ever constructed with an argument that is not a literal-or-parameter `seed`. Second gate: `G-DET-2` — canonical replay: run each model twice in separate interpreter processes with the same `--seed` and byte-compare canonical JSON; any diff = gate fails. Reproducibility is a *test*, not an acceptance bullet.

**R4 — HIGH: The "open questions" are resolvable now, by the plan's own audit — this is spec ambiguity converted into deferred work.**
The plan asks "Kelly implementation location" as an open question. I located it: `calculations/allocation.py` — `kelly()`, `fractional_kelly()`, `capped_fractional_kelly()` at lines 41–68, with tests already in `tests/formulas/test_kelly_stock.py`. The open question is not an unknown; it is an un-executed grep. Similarly, "exact CLI invocation pattern" is discoverable from `plugin/commands.py` today. Every unresolved question that is answerable by reading the repo becomes an ambiguity an executing agent resolves *by guessing*, and each guess is a drift event with no interceptor.
> **Binary gate:** `G-SPEC-1`: the plan cannot be approved for Stage 4 while any open question is answerable by a mechanical repo probe. Gate check: a CI job runs the probes (grep for `def kelly`, parse `commands.py` command registry, parse `distribution.yaml`) and diffs its findings against the plan's open-questions table; any entry still marked open whose probe returned a determinate answer = gate fails. Ask the human only what cannot be probed (see Questions section).

**R5 — MEDIUM: Phase acceptance gates are prose, not executable predicates.**
"Repo remains in working state", "skill loads without error in Hermes agent", "Committee Mode can run multiple DLCs including page and report disagreements" — none of these is a command with an exit code. Per the non-negotiable: every phase gates on (a) schema-match, (b) unit tests, (c) end-to-end validation with real inputs. The plan has (b)-ish only, and no idempotency check, no canonical replay, no schema-validated e2e output, and no drift test anywhere.
> **Binary gate:** `G-E2E-1`: each phase's gate block must contain ≥3 commands with literal expected exit codes, including one that runs the engine twice and byte-compares outputs (idempotency) and one that validates output against the declared schema. A phase gate section containing only prose criteria = gate fails at review, before Stage 4.

---

## Architecture Critique

**A1 — No structured-output compiler pattern; the ensemble path is LLM→final-artifact.**
The most dangerous line in the plan is Skill step 8: "Synthesize model outputs and apply thesis-specific sensitivity rules" — i.e., the agent (an LLM) reads the ensemble engine output and writes `robust_conclusions` / `explicit_disagreements` directly into `ensemble-result.v1`. That is precisely the direct LLM→final-artifact pipeline I veto. The grounded math (Diversity Prediction Theorem: error = avg error − diversity; the "robust threshold") is *deterministic arithmetic over model outputs* — it belongs in a deterministic compiler, not in agent prose. Architecture required:
```
8 model modules → Ensemble IR (schema-tied) → deterministic ensemble compiler (robustness threshold, disagreement set, correlation flags) → IR round-trip/drift test → ensemble-result.v1 artifact
```
The plan has no Ensemble IR, no compiler module, no round-trip test. "Never accept a direct LLM→final-artifact pipeline" is not advisory here; it is the mechanism by which "disagreement is the signal" silently becomes "disagreement is whatever the model felt like saying."
> **Binary gate:** `G-COMPILER-1`: a `calculations/model_thinking/ensemble.py` (or equivalent) that consumes a list of model-atoms and deterministically emits robust/condition-dependent/disagreement sets per a *stated, constant* threshold — with the threshold as a named shared constant (not a tunable magic number inline) — plus a golden-file drift test: compiler(IR fixture) must byte-match the committed `ensemble_result_fixed.json`. No ensemble artifact may be emitted by any code path that is not this compiler. Gate: grep test asserts no other module imports the schema writer.

**A2 — Golden fixtures are hand-authored, not engine-emitted → fixture drift.**
Artifacts 8–10 and 21 say fixtures "contain known test case inputs and expected outputs" with no emission mechanism. Two failure classes: (a) an agent hand-writes expected outputs by mental math — hallucinated goldens that tests then "verify" against the implementation, laundering the hallucination into CI-passing evidence; (b) fixtures rot as the implementation evolves. The repo already has the pattern: `simulation.py` computes `input_hashes` via `canonical_sha256`.
> **Binary gate:** `G-GOLDEN-1`: every fixture under `fixtures/valid/model_thinking/` must be regenerated by a committed `--emit-fixture` mode of the engine itself (deterministic), and a CI job re-emits and diffs; any drift = gate fails. Hand-edited expected outputs in fixtures = eval tampering; covered by `G-TAMPER-1`.

**A3 — `provenance_class` labeling is decided per-model ad hoc.**
Blotto is "calculated", the rest "modeled" — the decision is inline in artifact specs with no stated *rule*. The repo rule exists (deterministic closed-form → calculated; anything drawing on `random` → modeled) but the plan never states it, so agents will re-derive it inconsistently, and a mislabel (stochastic output tagged "calculated") inflates the evidence hierarchy, which is a *governance* failure, not a cosmetic one.
> **Binary gate:** `G-PROV-1`: CI check — for each module in `model_thinking/`, if the module imports `random`, all emitted atoms' `provenance_class` ∈ {modeled, forecast}; if it does not, ∈ {calculated, unavailable}. Any violation = gate fails.

**A4 — Skill-driven routing ("never compute simulations freehand") is prompt-based enforcement, which does not count.**
The plan's one behavioral guard — "Hard rule: never compute simulations freehand" — lives in SKILL.md frontmatter and in dlc-page prose. Prompt wording does not count as a primary mechanism. The agent can reason about a Markov chain in its reply and the harness has no interceptor. Architecture-level control: the ensemble-result schema (and/or decision-analysis) should carry a `model_refs` field requiring `formula_ref` values that exist in a registry of committed engine functions; a conclusion atom whose numbers have no matching engine-run receipt (`canonical_hash` of inputs + seed present) is schema-invalid.
> **Binary gate:** `G-RECEIPT-1`: ensemble-result schema gains a required `engine_receipts` array; every substantive conclusion atom must reference a receipt whose `input_hash` matches `canonical_sha256` of the recorded inputs — validated by a CI job that re-runs the referenced inputs+seed and compares. Conclusion present, receipt missing/mismatched = gate fails. This makes freehand computation *physically unrepresentable in the artifact*, not merely forbidden in prose.

**A5 — NK landscape has no resource ceiling.**
`nk_landscape(n, k)` emitting all 2^n genotypes with n documented as "kept small" in prose is unbounded. One invocation with n=20 hangs the deterministic engine and poisons the "repo remains in working state" story.
> **Binary gate:** `G-LIMIT-1`: a shared-constant max (e.g., `MAX_NK_N = 10`) in a shared constants module; input validation returns `unavailable_result` (the existing convention from `contracts/validation.py`) above the ceiling; unit test asserts the ceiling path. No inline magic number.

**A6 — Committee Mode disagreement mechanics are still prose ("likely compares canonical_hash").**
"Likely" is not a spec. If dlc-page's disagreement payload shape is not *schema-defined against `committee-result.v1.schema.json`/`decision-comparison.v1.schema.json`* (both exist in `schemas/`, verified), the Committee integration is an integration test nobody can write.
> **Binary gate:** `G-COMMITTEE-1`: before Phase 3, a probe task must produce the exact comparison contract (which fields of two DLC outputs are diffed, by what deterministic rule) written into the build plan, verified by rendering two committed example outputs and diffing them mechanically. Unresolved after probe → escalate to human; dlc-page cannot start.

---

## Missing Specifications

1. **Non-ergodic / non-convergence path is unspecified per the repo's own convention.** The plan asks "should we detect non-ergodic chains?" as an open question; the grounding doc already answers it ("report non-convergence as `unavailable` with reason") and the repo provides `unavailable_result()` in `contracts/validation.py` (used throughout `simulation.py`). Spec it: non-ergodic, cyclic, non-fixed, or non-finite chain → atom with `provenance_class="unavailable"`, `reason` string naming the failed Page condition. **Gate `G-UNAVAIL-1`: for each of the four Page conditions, one adversarial fixture in `fixtures/adversarial/` and one unit test asserting the `unavailable` output with the correct `reason`.**
2. **Power-law α ≤ 2 downstream gate is a suggestion, not a contract.** The grounding says Kelly/Sharpe are undefined at α ≤ 2 and calls it a "hard router rule in skill" — that is prompt enforcement again. Spec it as engine output: `power_law_check` emits `mean_variance_defined: false` when α ≤ 2, and the ensemble compiler refuses (→ `unavailable` with reason) any downstream Kelly/Sharpe atom whose `input_refs` chain to a power-law run flagged undefined. **Gate `G-PLAW-1`: test that a Kelly atom chained to an α≤2 run cannot validate against the schema.**
3. **Seed disclosure convention incomplete.** `simulation.py` puts `seed` in `metadata`, not in atoms. The plan says "seed recorded in every output." Which — metadata or atom? Pick one, name the field, spec the schema. Ambiguity here makes `G-DET-2` untestable as written. **Gate: schema + test define exactly one canonical seed location.**
4. **Cross-seed variance ("modeled vs forecast" for multi-trial Polya).** The risk register flags it; the plan never resolves it. Spec: within-seed outputs = modeled; the *distribution across seeds* = forecast with `limitations` stating it. **Gate `G-PROV-2`: test asserts multi-trial spread atoms are tagged forecast, not modeled.**
5. **Robustness threshold must be a named constant, not an open question.** "≥2? majority?" as an open question means the compiler (per A1) cannot exist yet, which means the plan's Phase 2 cannot actually close. Spec the constant (e.g., `ENSEMBLE_ROBUST_MIN = 2`) in a shared-constants module, tunable only by a human commit. **Gate: constant exists, test asserts threshold behavior at n−1/n.**
6. **Correlated-model flagging is absent from the schema.** The grounding's failure modes (a)–(c) demand correlation flags; `ensemble-result` has no field for them. Without it, five models that are all lognormal-shaped will pass the robustness gate and the "disagreement is the signal" claim is false in the artifact. **Gate `G-CORR-1`: schema field + compiler rule + test that N same-family models are flagged.**
7. **Error messages are unspecified.** Every invalid input in the plan is "validates input" — no spec for what the agent-facing failure text looks like. The repo convention is `unavailable_result(reason, ...)` prose. Spec: every model module's validation failure returns `unavailable_result` with prose remediation naming the violated rule, never a stack trace. **Gate `G-ERR-1`: unit tests assert no traceback reaches output on each invalid-input class, and that `reason` names the exact violated invariant.**
8. **Token efficiency contract for the 8+1 skill files and 8 reference files.** SKILL.md as ToC is right, but no size budget is stated. **Gate `G-TOKEN-1`: `wc -l` on `skills/many-model-thinking/SKILL.md` ≤ the repo's existing largest SKILL.md (probe capital-research SKILL.md for the budget); each reference file ≤ stated cap. Over-budget = gate fails.** Scaffolding is temporary — mark the "8 reference files" as removable once engine `--help`/docstrings are sufficient, with a stated removal trigger.

## Recommended Task Gate Updates

Folding the above into the plan's phase gates as binary predicates:

| Gate | Predicate (exit-code enforceable) | Blocks |
|---|---|---|
| `G-SCHEMA-1` | Engine output fixture validates against the *exact schema filename cited in its artifact spec*; plan-to-schema filename cross-check passes | Phase 1, 2 |
| `G-TDD-1` | Per-module RED artifact (pre-implementation failing pytest log) exists and is committed before the module lands | Phase 1, 2 |
| `G-TAMPER-1` | Hash of `tests/` + `fixtures/` identical before/after implementation jobs; fixtures re-emittable by engine (`--emit-fixture`) with zero diff | All phases |
| `G-DET-1/2` | AST lint: no `seed=None` on stochastic entrypoints, no unsourced `random` use; two-process byte-identical replay on fixed seed | Phase 1, 2 |
| `G-PROV-1/2` | `random`-importing modules → atoms ∈ {modeled, forecast}; multi-trial spread → forecast; deterministic → calculated | Phase 1, 2, 3 |
| `G-COMPILER-1` | Ensemble artifact produced only by deterministic compiler; golden drift test byte-exact | Phase 2, 3 |
| `G-RECEIPT-1` | Conclusion atoms carry verifiable engine receipts (re-run + compare) | Phase 2, 3, 4 |
| `G-UNAVAIL-1` | One adversarial fixture + test per failed Page condition / α≤2 gate / NK ceiling | Phase 1, 2 |
| `G-E2E-1` | Each phase gate lists ≥3 commands with expected exit codes incl. idempotency + schema validation | All phases |
| `G-SPEC-1` | No open question remains that a mechanical repo probe answers (probe job diffs against open-questions table) | Stage 4 entry |
| `G-COMMITTEE-1` | dlc-page disagreement contract schema-verified against `committee-result.v1` / `decision-comparison.v1` before Phase 3 start | Phase 3 |
| `G-TOKEN-1` | SKILL.md/reference files within measured budgets; removal triggers stated for scaffolding | Phase 2, 4 |

Also reorder: **tests before modules in the artifact list**, fixtures emitted by engine, and replace "seed=None" throughout with required `seed: int` per `simulation.py`'s precedent.

## Questions for the Human Governor

1. **Ensemble artifact authority:** confirm that the deterministic ensemble compiler (A1) is in scope — it is the difference between "disagreement is the signal" being a property of the engine vs. an aspiration of the prompt. If out of scope for v1, Phase 2/3 must ship ensemble results as engine-run receipts *without* synthesized conclusions; the compiler is Phase 5.
2. **Robustness threshold value:** the constant must be human-set (I propose `= 2` minimum agreement for ≤7-model ensembles, but this is a judgment call on the analytical product, not a harness decision). Set it, commit it, own it.
3. **Seed UX:** require explicit `--seed` on every stochastic invocation (breaking change for any existing runner that omits it), or auto-derive `seed = canonical_sha256(inputs)` so it is reproducible *and* invisible to the user? The latter preserves C4 without UX cost — human call.
4. **Committee Mode contract ownership:** if the disagreement comparison rule is not mechanically derivable from `committee-result.v1.schema.json`, the human must define which fields two DLC outputs are diffed on — this is a spec hole no reviewer can fill without inventing product semantics (deferred to you per my card).
5. **Baseline state:** confirm the existing test suite is green today before Phase 1 (I did not run it; a red baseline would make `G-TDD-1` non-converging). `python -m pytest` once, by the governor or a Stage 4 probe, is the gate's precondition.

---

**Verdict as reviewer (advisory):** the plan is *not* executable as written — R1 (wrong schema cited), R2 (Green-before-Red ordering), and R4 (probes-answerable open questions) are hard stops. Fixable by folding the gate table above into the task definitions and re-cutting Phase 2 around the ensemble compiler.
