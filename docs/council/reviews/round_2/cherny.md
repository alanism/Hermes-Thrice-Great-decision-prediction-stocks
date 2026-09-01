# Council Round 2+3 — [C] Boris Cherny (Decomposition / Verifier Lens)

**Operating question:** "How would this work if I gave the agent maximum autonomy, a high-level goal, and a deterministic verifier to iterate against?"

---

## Round 2 — Judgment of Merged Findings M1–M11

### 1. Strongest — MUST be enforced as binary gates

**M4 (fake unknowns).** This is my R1 from Round 1 and it remains the single highest-leverage fix. Every open question the repo can answer is a hallucination invitation for an autonomous executor. It costs one "interface grounding" phase to fix and nothing to enforce: zero "check X to see how Y" strings may survive in the plan. Must enforce. (Gate G1 / RG-04.)

**M2 (no red-first artifact; self-grading eval).** A verifier that was written by the same agent after the implementation is not a verifier — it's a rubber stamp. Tests that depend on the calculation module and never exist in a failing state cannot prove anything. The repo already has `tests/mutation/`; not using it is free rigor left on the table. Must enforce: every Phase-1/2 gate requires a demonstrated failing-then-passing test (red→green captured in CI log or gate output), and at least one mutation check per module family. (Gates RG-02, RG-07.)

**M3 (seed discipline contradiction).** The signature is the contract for 8 parallel agents; a `seed=None` default that breaks C4 reproducibility is an interface lie that multiplies across every worktree. The signature must be `seed: int` required (no default), with `bool` excluded and `str` rejected — exactly the `simulation.py` pattern. Deterministic functions must not accept a seed at all. Must enforce. (RG-01, RG-03.)

**M5 (ensemble has no computation site).** A schema with no producer is a dead document, and the only way it gets "produced" in practice is LLM freehand — which then feeds `canonical_hash` provenance theater. This is my R5 and it is the flagship feature. Must enforce: `ensemble.py` aggregator exists, is deterministic, and a round-trip test validates its output against the schema before Phase 2 closes. (RG-06.)

**M8 (validation is prose, not tests).** "Validates input" as a sentence is unverifiable — an agent cannot iterate against it. Caps "in documentation" are prompt-security, not gates. Every validation AC becomes a named test with an expected rejection; every dimension bound becomes an assertion. Must enforce. (RG-05.)

**M11 (determinism never defined).** C4 ("every number reproducible") is untestable without a bit-exact-vs-tolerance policy, a CPython pin, and a float-serialization rule for `canonical_hash`. The cheapest gate: run one model twice, assert byte-identical hash — but the hash itself is undefined until serialization is pinned. Must enforce. (RG-08.)

### 2. Wrong or over-weighted — with reasoning

**M1 (schema target) — half right, over-weighted.** The file-name error is real but trivially mechanical (grep-able). The `input_trust_class` provenance extension is Carlini's turf — I defer. Enforce the schema-target correction as a gate; do not let the provenance-design work block the math phases.

**M6 (Committee Mode mechanics) — real, but solvable in one decision, not a phase of work.** The six-string vocabulary either constrains dlc-page's output or gets extended with tests. I'd constrain to the existing vocabulary — a novel recommendation string from a stochastic voice model is exactly the kind of unbounded surface that degrades the comparison silently. Gate it (test asserts synthesis ∈ vocabulary); don't over-engineer a new contract type.

**M9 (spec contradictions vs grounding) — partially over-weighted.** The Markov convergence-conditions and SIR discretization contradictions are genuine and must be resolved (Euler going negative is a golden-value-test failure waiting to happen). But listing Polya signature wording and Blotto enumeration blowup at the same severity is averaging away signal: the Blotto blowup is a scope/performance note, not a correctness gate, and Schelling relocation-order is a seed-contract detail already covered by M3. Enforce the algorithm-naming gate per model (my G6); treat the rest as notes inside it.

**M10 (scope/customer outcome) — real but not my dimension and partially unenforceable as a binary gate.** "No named customer outcome" is a product judgment; I defer to F. The enforceable slice: no smoke test / end-to-end moment of value, and unbounded context cost. I'd gate "one end-to-end CLI run producing a valid ensemble-result from a fixture" — that's binary. The 5–7-model sweet spot question is a governor decision, not a gate.

### 3. Still missing

- **Single-reviewer C's injection loop** (untrusted evidence → numeric parameters → engine output → agent context) is not a merged finding, and it's the scariest thing in the packet. I don't own security architecture — Carlini does — but I note it must survive into the register even though it's not consensus, and its gate belongs to him (provenance_class allow-list for engine parameters). Do not average it away.
- **Stdlib-only mechanical check** (my G9): the register says "CI check if possible" — that's a decision, not a risk. `scripts/check_stdlib_only.py` is trivially mechanical. Missing from the merged set.
- **Per-phase full-suite gate** (my G8/R8): merged into M2 partially, but the specific point — full existing suite gated at Phase 4 means regressions age two phases — deserves its own line. One command per phase.
- **distribution.yaml / registration diff** (my M7 from Round 1): the plan ships files without enumerating where they're registered. Missing from merged findings entirely.
- **Shared-memory loop** (my G14): discovered corrections appended to the audit report in the same commit, so a second agent doesn't re-hallucinate "packs are dicts, the flag is --pack."

### 4. Human governor decisions (must not be resolved by the agent)

1. **Bandit variants:** grounding says greedy / sample-then-greedy / adaptive-ε; plan says UCB1/Thompson. Grounding wins by default, but it changes fixtures and golden values — governor calls it.
2. **Ensemble scope:** add the aggregator module (my recommendation) or descope ensemble-result.v1. The PRD implies it; shipping a schema without a producer is worse than not shipping it.
3. **Committee vocabulary:** constrain dlc-page to the existing six strings vs. extend `runner.py`'s priority list. Recommend constrain.
4. **Model count:** 8 models vs Page's own 5–7 sweet spot (F's AI-Tourism veto). If the ensemble's value depends on model diversity, 4 decision-relevant models may beat 8 decorated ones. This reshapes every downstream artifact — decide before Phase 1.
5. **M9 discretization:** grounding's discrete difference equations vs plan's Euler for SIR. Recommend grounding (Euler violates conservation at large β; a conservation test is then a free golden gate).
6. **Executor config:** confirm implementing agent runs most-capable model at maximum effort, and any scaffolding added "for today's model" carries an unshipping note.

---

## Round 3 — Final Risk Register

| Risk | Severity | Evidence | Prevention | Task Gate Check | Blocks Build? |
|---|---|---|---|---|---|
| RG-01: `seed=None` defaults break reproducibility contract C4; deterministic fns accept unused seed (signature lie) | Critical | M3 (A,C,D); `simulation.py` keyword-required seed; seed flows into canonical_hash | Required `seed: int` keyword, bool/str rejected; deterministic modules take no seed param; seed-contract table per model | Run module twice with same seed → identical canonical_hash; call with `seed=True`/`"42"` → raises | YES |
| RG-02: Green-then-red test ordering; same agent writes impl + tests; no mutation check despite `tests/mutation/` existing | Critical | M2 (A,B,D,E); no failing-test-first artifact in any phase | Every test artifact authored before impl; red→green captured; ≥1 mutation survives per module family | Gate log shows a failing test run followed by passing run; mutation check script exit 0 | YES |
| RG-03: Ensemble result has no deterministic computation site → LLM freehand flagship output; canonical_hash is provenance theater | Critical | M5 (B,C,A); schema ensemble-result.v1 has no producer | `calculations/model_thinking/ensemble.py` aggregator + round-trip test vs schema; LLM may draft conclusions text only after numeric core exists | `pytest tests/.../test_ensemble.py` green; output validates against schema | YES |
| RG-04: Open questions answerable from repo left "open" → implementing agent hallucinates interfaces | Critical | M4 (A,B,D); `allocation.py:41`, `plugin/commands.py`, `methods/packs.py`; Artifact 17 invents `capital model-thinking run` | Phase 0.5 Interface Grounding: every open question → file:line citation or HUMAN_DECISION | `grep -E "check .* to (see|determine)" plan.md` → 0 hits | YES |
| RG-05: Input validation is prose; unbounded dims (NK n, Markov size, Schelling grid, SIR days, bandit horizon); no `simulation.py` rejection pattern | High | M8 (C,D); caps "in documentation" | Each validation AC → named test with expected raise; dimension caps as constants asserted in tests | Validation test suite green; each cap has an asserting test | YES |
| RG-06: Determinism undefined (bit-exact vs tolerance, no CPython pin, float serialization for canonical_hash) | High | M11 (D,A) | Pin CPython version; define exact float serialization for hash; tolerance policy per test class | Determinism doc section exists; double-run byte-identical hash test green | YES |
| RG-07: Full existing suite only gated at Phase 4 → regressions age two phases | High | M2 + B single-finding | Per-phase gate: full `pytest` green, count unchanged-or-grown | Each phase gate log shows suite run: 0 failures | YES |
| RG-08: Plan/grounding contradictions (SIR Euler vs difference equations; Markov missing 4 convergence conditions; bandit variant mismatch) | High | M9 (D,B); grounding doc cited | Governor resolves each; grounding wins by default; golden-value tests encode the resolved algorithm | One named golden test per model, hand-computed expected value | YES (SIR/Markov) |
| RG-09: Wrong schema target (evidence-item.v1 vs `$defs.atom`); fixtures reference schema outputs can't satisfy | Medium | M1 (A,C,E) | Point conformance at `$defs.atom` in bayesian-update.v1/decision-analysis.v1 | Fixture validates against corrected schema path | YES |
| RG-10: Committee Mode vocabulary mismatch → silent degradation to `recommendations[0]` | Medium | M6 (B,E,C); `runner.py` six-string list | dlc-page constrained to existing vocabulary (or governor-approved extension + tests) | `test_committee_page.py`: synthesis ∈ vocabulary | NO (post-core) |
| RG-11: All-valid fixtures; zero adversarial fixtures despite `fixtures/adversarial/` convention (10 existing) | Medium | M7 (C,E,D) | ≥1 adversarial fixture per module family: missing rows, cyclic chains, gamma=0, overflow, injected evidence, non-finite | Adversarial suite green (rejections asserted) | NO (pre-ship) |
| RG-12: Non-stdlib imports creep into new modules; verifier left "CI if possible" | Medium | B Round-1 G9 | `scripts/check_stdlib_only.py` committed | Script exit 0 over `calculations/model_thinking/` | NO (pre-merge) |
| RG-13: New files not registered in distribution.yaml → ships broken | Medium | B Round-1 M7 | Registration diff enumerated per new path | distribution.yaml contains every new path; grep check | NO (pre-merge) |
| RG-14: Injection loop (untrusted evidence → params → output → agent context); free-text ensemble fields as echo channel | High | C single-finding | Carlini-owned: provenance_class allow-list for engine parameters; bound/strip free-text fields | (Carlini's gate — attestable test on parameter provenance) | YES (Carlini call) |
| RG-15: Scope bloat: 8 models vs 5–7 sweet spot; no end-to-end smoke test; no token budget | Medium | M10 (F,E) | Governor decides model count; one end-to-end CLI run on fixture produces valid ensemble-result | `capital method committee` on fixture exits 0 with valid output | NO (governor) |
| RG-16: Agent-learned corrections not fed to shared memory → second agent re-hallucinates | Low | B Round-1 G14 | Standing rule: corrections appended to audit report §Convention Summary same commit, file:line | Audit report grows during build; grep for new citations | NO |

**Governor decisions outstanding (block their linked gates, not the build):** bandit variant set (RG-08), ensemble scope (RG-03), committee vocabulary (RG-10), model count (RG-15), SIR discretization (RG-08), provenance allow-list design (RG-14).

---
*Deferred: security architecture to Carlini (RG-14), empirical validation rigor to Willison (RG-02 golden values), operational registration discipline to Hashimoto (RG-13). All file:line claims carried from my Round 1 working-tree verification.*
