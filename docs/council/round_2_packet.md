# Round 2 Cross-Examination Packet — Merged & Anonymized Round 1 Findings

Reviewers were: A (harness/gates lens), B (decomposition/verifier lens), C (adversarial/security lens), D (numerical/runtime lens), E (lethal-trifecta/composition lens), F (product-outcome lens). Each reviewed the build plan blind.

## Merged findings (deduplicated, anonymized)

### Consensus findings (3+ reviewers)
**M1. Wrong/underspecified schema target** (A, C, E)
Plan cites `evidence-item.v1.schema.json` for conformance; that schema requires source-ref/timestamp fields model outputs can't have. Real atom shape is `$defs.atom` in `bayesian-update.v1`/`decision-analysis.v1`. Also proposed: add `input_trust_class` to provenance enum so attacker-controlled evidence is distinguishable downstream.

**M2. Green-then-Red test ordering; no eval-tamper defense** (A, B, D, E)
Every phase artifact lists tests as depending on the calculation module — no failing-test-first artifact anywhere. No mutation check or independent verifier despite `tests/mutation/` existing. Self-grading eval risk: same agent writes implementation and tests.

**M3. `seed=None` default contradicts repo's required-seed convention** (A, C, D)
`simulation.py` requires a keyword-only int seed; the plan defaults all stochastic functions to `seed=None`, making C4 ("every number reproducible from inputs+seed") untestable. D additionally flags: deterministic functions (Markov, power-law, SIR base) accept a seed no RNG consumes — a lie in the signature. Hostile/typed seeds (strings, bool) silently change semantics; seed flows into canonical_hash.

**M4. Open questions are fake unknowns — answerable by repo probes** (A, B, D)
Kelly lives at `allocation.py:41` (`kelly()`, `fractional_kelly()`); CLI registry is `plugin/commands.py`; packs are a PACKS dict in `methods/packs.py`; real invocation is `capital method run --pack`. B: Artifact 17 hard-codes `capital model-thinking run`, a subcommand that does not exist. Leaving these "open" forces the implementing agent to hallucinate interfaces.

**M5. Ensemble aggregation has no computation site** (B, C, A)
Schema (`ensemble-result.v1`) is specified but no module builds/validates instances. If the LLM judges "robust conclusions," the flagship feature violates the never-compute-freehand rule and canonical_hash becomes provenance theater. A: step 8 of the skill is a direct LLM→final-artifact pipeline; must be a deterministic compiler over an Ensemble IR.

**M6. Committee Mode mechanics undefined but used as a Phase 3 acceptance gate** (B, E, C)
`runner.py` has a fixed six-string recommendation vocabulary; novel dlc-page strings silently degrade to `recommendations[0]`. Unmechanized claim cannot be gated.

**M7. All-valid fixtures; zero adversarial fixtures** (C, E, D)
`fixtures/adversarial/` is an existing repo convention (10 fixtures). Plan tests only the average case: missing non-stochastic Markov rows, cyclic chains, gamma=0 SIR, NK n overflow, injected-evidence, non-finite inputs.

**M8. Input validation is prose, not tests** (C, D)
"Every 'validates input' AC is a sentence, not a test." The eight new modules never mandate the existing `simulation.py` rejection pattern (isfinite, bool exclusion, unavailable_result fallback). Unbounded dimensions (NK n, Markov matrix size, Schelling grid, SIR days, bandit horizon) capped "in documentation" — control-by-doc is prompt-security.

**M9. Spec contradictions vs grounding doc** (D, B)
Markov: plan implements only power iteration; grounding requires all four Page convergence conditions (finite, fixed, ergodic, non-cyclic) — cyclic/reducible chains can silently fabricate a stationary distribution. SIR: plan says Euler Δt=1; grounding specifies discrete difference equations — and Euler goes negative at large β, violating conservation; rounding rule undefined. Polya: plan's single-trial signature contradicts grounded multi-trial-spread deliverable. Bandits: plan names UCB1/Thompson; grounding specifies greedy / sample-then-greedy / adaptive-ε. Thompson sampling names no stdlib Beta draw. Blotto "purely combinatorial" hides C(W+N−1,N−1) enumeration blowup. Schelling omits relocation-order seeding.

**M10. Scope exceeds demonstrated outcome** (F, E)
F: no named customer outcome anywhere in the plan; ensemble output has no wired decision hook (nothing consumes ensemble-result.v1; no spec for how robust/disagreement changes the Buy/Hold/Trim verdict); AI-Tourism veto on SIR, Bass, Blotto, NK — Page's own 5–7 sweet spot argues ≤4 decision-relevant models; no smoke test / end-to-end moment of value; no human has ever run a Page ensemble on a real thesis (2-4-10 violation). E concurs: 8 reference files + skill + DLC threaten byte-exact cache prefix; no token budget.

**M11. Determinism never defined** (D, A)
No bit-exact vs tolerance policy; no CPython version pin; canonical_hash float serialization unspecified. Acceptance criteria mix binary checks with aspirational vibes ("useful guidance", "clear explanation").

### Single-reviewer findings (preserve, do not average away)
- **A (harness)**: token-efficiency of agent-facing error messages unspecified; 12 named binary gates (G-SCHEMA-1…G-TOKEN-1) proposed.
- **B (decomposition)**: full existing test suite only gated at Phase 4 — regressions caught two phases late; phase 2 should split for parallel worktree execution; interface-grounding phase needed before skill authoring.
- **C (security)**: injection loop — untrusted extracted evidence becomes numeric parameters, engine output feeds back into agent context as "validated" conclusions; no rule governs which provenance_class values may populate engine parameters. Free-text condition/point_of_contention fields in ensemble schema are an unbounded injection echo channel back into Committee Mode context.
- **D (runtime)**: α≤2 gate is prose in the router skill, not machine-readable schema data — downstream Kelly/Sharpe invalidity is not compiler-enforced.
- **E (composition)**: grounding doc is an LLM transcript cited as authority; computable claims (75/25 equilibrium, Diversity Prediction Theorem, V≥1−1/R0) are testable but never tested; "5–7 sweet spot" hard-coded into router guidance without primary-source verification.
- **F (product)**: no named customer outcome; 2-4-10 validation absent.

## Instructions for Round 2
You previously reviewed blind. Now judge the merged findings: (1) which objections are strongest and MUST be enforced as gates; (2) which are wrong or over-weighted, with reasoning; (3) what is still missing; (4) what the human governor must decide. Then produce your final prioritized risk register with columns: | Risk | Severity | Evidence | Prevention | Task Gate Check | Blocks Build? |.
