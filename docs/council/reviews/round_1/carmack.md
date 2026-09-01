# Round 1 Blind Adversarial Review — [J] John Carmack, Runtime Truth Engineer

Operating question: **"Could the compiler have caught this before it ever ran?"**
Scope: functional purity of the planned model engine, numerical-correctness landmines, assert-as-contract design limits, interface obviousness, stdlib-only discipline without heroics, back-of-envelope performance. Security threat modeling deferred to Carlini; roadmap to Taylor.

---

## Key Risks

1. **Phantom seed parameters on deterministic functions (compiler-visible design rot).**
   `markov.stationary_distribution(..., seed=None)`, `power_law_check(..., seed=None)`, `sir_model(..., seed=None)` are fully deterministic algorithms — power iteration, MLE fit, Euler stepping draw no randomness. A `seed` parameter that is accepted, recorded, and never consumed is a lie in the signature: it teaches callers that seeding matters where it doesn't, and it invites a future maintainer to "use" the seed somewhere mid-stream, destroying the input→output contract. Every RNG-touching module must declare its stream; every non-RNG module must not accept a seed at all.
   **Gate G-J1:** No calculation module may accept a `seed` argument unless a named RNG stream consumes it; `assert seed_is_used or seed is None` in the module's own test. Binary: seed param present on a function whose test proves zero RNG calls → FAIL.

2. **Cross-platform/version determinism is claimed but never defined.**
   Acceptance criterion "same inputs + seed → same output" is asserted in prose, not mechanically. `random.Random(seed)` (Mersenne Twister) and `gauss()` draw sequences are stable within a CPython version but not contractually guaranteed across versions; `math.fsum`/`statistics.fmean` accumulation order matters. The repo's existing pattern (simulation.py, `random.Random(seed)`) is good, but the plan must pin: (a) target CPython version in metadata, (b) bit-exact vs. tolerance compare for tests, (c) canonical serialization before hashing (canonical_hash on dicts with float values is only stable if floats are serialized identically — sort keys, fixed float repr).
   **Gate G-J2:** Determinism test = full-output byte/hash equality (`first == second` like test_seeded_monte_carlo.py) for every model, plus a metadata field `python_runtime` or a pinned-version note. Binary: any model whose determinism test uses `pytest.approx` instead of exact equality on the seeded path → FAIL.

3. **SIR Euler with Δt = 1 day will violate the plan's own conservation acceptance criterion.**
   Explicit Euler at step size 1 with β·Δt not small produces overshoot: S(t+1) < 0 or I(t+1) < 0 is routine for β near or above 1 with a large infected fraction. Plan demands "conserves population (S+I+R = constant)" AND integer S/I/R outputs AND "matches known analytical approximations." These three cannot all hold with naive Euler + rounding. Fractional Euler results cast to `int` silently break conservation and peak-day correctness.
   **Gate G-J3:** Every SIR/Bass step asserts `0 <= S, I, R` before recording; if any would go negative, the module returns `unavailable_result` with reason "parameters outside stable Euler domain (beta*step too large)" — matching the repo's existing `unavailable_result` pattern. Binary: a fixture with β ≥ 1, population ≥ 10⁴, 60 days must either converge with conservation invariant exactly (S+I+R == population at every recorded step) or return `unavailable` — never silently clamp. Also: specify the rounding rule (floor of cumulative fractional counts, not per-step rounding).

4. **NK landscape 2ⁿ blowup has no machine-enforced cap.**
   Plan says "n kept small for feasibility" (Artifact 15). "Kept small" is a human-discipline contract, which Carmack's rule #3 says don't build. `nk_landscape(n=30)` produces 2³⁰ genotypes — OOM or a multi-hour hang, and the fitness table itself is n·2^(K+1) uniform draws. An assert on entry is free.
   **Gate G-J4:** `assert isinstance(n, int) and 0 <= n <= MAX_N and 0 <= k < n` with `MAX_N = 20` (2²⁰ = 1,048,576 genotypes; with K+1 draws per bit ≈ 2⁶ ≈ 67M RNG calls ≈ a few seconds — still acceptable; beyond that refuse with `unavailable`). Binary: n=21 returns `unavailable_result`, not a hang. Document RNG-consumption order (bit index → dependent-bit choice → configuration table) explicitly so the seed→landscape mapping is spec-stable.

5. **Power-law check mixes randomness, statistics, and gates without pinning any of them.**
   Artifact 3 leaves the fitting method an open question (MLE vs. log-log regression), yet `ks_statistic` and `ps_value` in the output contract depend entirely on that choice (KS p-values require a bootstrap — which RNG stream? how many resamples?). And the grounded rule "α ≤ 2 ⇒ mean/variance undefined ⇒ Kelly/Sharpe invalid" is currently only a *router-skill prose rule*. Prose is not a compiler. The flag must be a field the schema validates and downstream engines must read, not a suggestion the LLM may ignore.
   **Gate G-J5a:** Fitting method and bootstrap count are named constants in the module (`_FITTING_METHOD`, `_BOOTSTRAP_ROUNDS`), with the RNG stream derived from `seed` and documented. Binary: two runs, same seed, same data → identical `ks_statistic`, `ps_value`, `alpha_estimate` bit-for-bit.
   **Gate G-J5b:** Output atom carries `alpha <= 2` → field `heavy_tail_gates: ["mean", "variance", "kelly", "sharpe"]` as machine-readable data; schema requires it. Binary: ensemble schema rejects an atom lacking the gate field when `is_power_likely` is true.

6. **Markov convergence conditions are grounded (4 Page conditions) but the plan implements only power iteration.**
   Power iteration on a periodic (cyclic) or reducible chain can oscillate forever or converge to a non-stationary artifact; the plan's open question "should we detect and report non-ergodic chains?" must be answered YES before Phase 1 code, not after. Detecting reducibility/periodicity in pure Python is cheap (reachability via closure over the transition graph; periodicity via gcd of return times or a power-of-M check on the boolean adjacency).
   **Gate G-J6:** Module detects and reports `ergodic`, `reducible`, or `cyclic` classification as a machine-readable field; non-convergent cases return `unavailable_result` with the reason. `max_iterations` exhaustion is a reported status, not a silently stale vector. Binary: a 3-state deterministic cycle fixture must return `cyclic`/`unavailable`, not a fabricated distribution.

7. **Schelling: "seed the initial placement AND relocation order" (grounding doc) is absent from Artifact 12's spec.**
   The spec says only "random for agent placement if needed." Relocation order and vacancy choice both consume the RNG stream; an unspecified order makes two "deterministic" implementations diverge. Also no cap on grid_size or steps, and no terminal condition distinction ("converged" vs. "hit step limit") — a segregation index reported at step-limit is not an equilibrium and must not be labeled the same.
   **Gate G-J7:** Spec names the RNG consumption order (placement → per-step relocation scan order → vacancy pick); `assert 0 < grid_size <= 128` and `0 < steps <= 1000`; output field `terminated_reason: converged | step_limit`. Binary: fixture with heterogeneous tolerances reproduces the macro≠micro gap (>realized segregation vs. T) or the fixture is rewritten.

8. **Thompson sampling has no stdlib Beta sampler — spec hand-waves it.**
   stdlib `random` offers gauss, uniform, expovariate, betavariate (actually `random.betavariate` exists — verify and pin it); if used, its algorithm (Cheng's) is version-stable but must be named. If the plan's `thompson_sampling_bandit(arm_alpha_beta, horizon, seed)` intends `random.betavariate`, say so in the spec; if it intends a hand-rolled sampler, that is a heroics violation — use stdlib. Regret computation needs a specified oracle (true means known → regret = H·max_mean − reward).
   **Gate G-J8:** Spec names the exact stdlib draw for each stochastic model (betavariate, gauss, uniform) and the regret oracle. Binary: bandit determinism test passes bit-exact and regret ≥ 0 for all fixtures.

9. **Blotto "purely combinatorial, no seed" hides a combinatorial blowup.**
   Number of allocations of W troops across N battlefields is C(W+N−1, N−1); enumerating the "payoff matrix" for W=50, N=8 is ~10⁹ rows. Either the interface is two-strategy comparison (cheap, pure) or full enumeration (infeasible) — the spec conflates them and labels output "calculated" (calculated = deterministic math, fine) but the acceptance criteria don't cap W and N.
   **Gate G-J9:** `assert N <= 16 and total_troops_a + total_troops_b <= 400` for pairwise payoff; full-strategy-space enumeration gets its own capped function (or is excluded). Binary: oversized input returns `unavailable_result`, not a loop that eats the machine.

10. **Polya "multi-trial spread is the deliverable" (grounding doc) but Artifact 14's signature is single-trial.**
    `polya_process(initial_a, initial_b, steps, seed=None)` returns one run's sequence and final proportion. The grounded finding — uniform spread of terminal proportions across trials IS the output — needs a `trials` parameter and per-trial seed derivation (`seed + trial_index` or a stream object), specified now, or two implementers will derive child seeds differently and fixtures will disagree.
    **Gate G-J10:** Spec states child-seed derivation rule for all multi-trial models (Polya, bandit ensembles, power-law bootstrap). Binary: fixture pins one derivation and a test asserts `trials=3` output equals three single-trial runs with derived seeds.

---

## Architecture Critique

- **Good: the repo's existing purity pattern is exactly right and the plan should copy it verbatim.** `simulation.py` demonstrates the house style: pure module-level functions, explicit keyword-only args, validity gate returning `unavailable_result` (never raising on bad input mid-compute), `random.Random(seed)` local instance (no global state, no module-level RNG — no tendrils), metadata with seed/parameters/input_hashes/limitations. New modules that follow this are compiler-verifiable by construction. The plan references the pattern but does not make "matches simulation.py structural template" an acceptance criterion per artifact. It should.
- **Bad: one `model_thinking/` subpackage with 8 heterogeneous modules is fine, but the plan gives none of them a shared contract.** Each artifact re-specifies "output evidence-atoms dictionary with seed, provenance_class" in prose. That's eight chances to drift. One `model_thinking/atoms.py` helper (like `_modeled` in simulation.py) with a fixed atom constructor — inputs, unit, formula_ref, limitations, provenance_class, seed — makes conformance structural rather than per-author discipline. Missing from the plan; add as Artifact 1.5.
- **Interface obviousness fails the Train Wreck Test in two places.** (a) The CLI invocation is still an open question (`capital model-thinking run` vs. alternatives) while Phase 2's skill already hard-codes one spelling in its workflow step 7 — if the CLI lands differently, the skill text is wrong on day one. Resolve the CLI question *before* writing Artifact 17, not after. (b) `power_law_check(data, seed=None)` returning `ps_value` — Page's convention vs. standard KS p-value semantics needs a `formula_ref` and a limitation string, or users will read p > 0.05 as "proven power law," which it is not.
- **Schema: `additionalProperties: false` on ensemble-result is the right compiler-style move; carry it down to the per-model atoms too.** If the atom schema rejects unknown fields, drift in the 8 modules is caught at validation time — the closest thing to a compiler this repo has.
- **Paralysis-by-Purity self-check (deliberate):** the plan is NOT over-pure — it reuses the existing simulation/evidence infrastructure instead of rebuilding it, keeps stdlib-only without hand-rolling statistics, and stages Phase 1 (3 models) before committing to 8. That's the right pragmatic shape. Do not "fix" it by demanding typed dataclasses or a numeric-stability framework; the pure-function + unavailable-result + assert-caps pattern is sufficient for a research tool. The one purity demand I'd soften: per-model deterministic bit-exactness fixtures should not block Phase gates when a model's *documented tolerance class* (e.g., iterative convergence to 1e-10) is what varies — pin the *iteration count and tolerance in output*, compare values with a stated tolerance there, and keep bit-exactness only for the RNG stream and control flow.

---

## Missing Specifications

1. **Float tolerance and serialization policy.** Which comparisons are bit-exact vs. `abs_tol`? How are floats canonicalized before `canonical_sha256`? (Existing repo code computes hashes over parameter dicts — dict ordering and float repr must be pinned.) Not specified anywhere in the plan.
2. **Assert/limit table per module.** One place listing every design-limit assert: MAX_N (NK) = 20, grid ≤ 128 (Schelling), horizon cap (bandits), troops cap (Blotto), iteration_count cap (already exists: ≤ 1_000_000 in simulation.py — copy it), Markov max_iterations = 1000, tolerance = 1e-10. Asserts are active comments; they should be enumerated in the plan, not improvised by implementers.
3. **Ensemble performance envelope.** Back-of-envelope: 7 models × (MC-heavy ones at ~10⁴ trials × ~50 steps) ≈ a few million RNG calls ≈ 1–3 s in pure Python — fine. But: ensemble × multi-seed sweep (Page's rerun-the-tape discipline) multiplies linearly; a 7-model × 20-seed sweep is ~1 minute. The plan should state a budget (e.g., "single ensemble run ≤ 5 s at default caps") and cap Monte-Carlo-style sub-models accordingly, so the router skill can promise interactive latency.
4. **Markov input convention.** Grounding doc uses Page's row/column convention (columns = t, rows = t+1); Artifact 2 says "each row sums to 1.0" (standard convention). These differ. Pick one, state it in the function docstring, and put a transposition note in the reference file — otherwise agent and engine will disagree on a transposed matrix and produce a plausible-looking wrong equilibrium.
5. **Integer vs. float SIR/Bass state.** Spec output says `{"S": int, "I": int, "R": int}` but Euler produces fractions. Define: track floats internally, report `floor` of cumulative counts with conservation re-verified post-rounding, or report floats and drop the int claim. Currently contradictory.
6. **Mutation-test coverage requirement for new models.** tests/mutation/test_formula_mutations.py exists and kills sign/direction mutations. The plan's Phase 2 test artifact (Artifact 20) doesn't require mutation tests for the 8 new models. Each model needs at least one sign-flip and one off-by-one mutation killed, or the test suite is a smoke test pretending to be a proof.
7. **Ensemble correlated-model flagging is grounded (Section 9 of grounding doc) but absent from the schema spec.** `explicit_disagreements` exists; `correlated_models` (shared-framework flag) does not. Add a required field or the Diversity Prediction Theorem's failure mode (a) is unrepresentable in the schema.

---

## Recommended Task Gate Updates

| Gate | Binary criterion | Where |
|------|-----------------|-------|
| G-J1 | No unused `seed` parameter on any calculation function; tests prove RNG usage or absence | Phase 1 & 2 all model artifacts |
| G-J2 | Determinism tests are exact-equality on full output (matching test_seeded_monte_carlo.py pattern); CPython version pinned in metadata or CI matrix | Phase 1 gate |
| G-J3 | SIR/Bass fixtures include an unstable-domain case that returns `unavailable_result`; conservation invariant asserted per step; rounding rule documented | Artifact 4 / test_sir.py |
| G-J4 | NK: `assert n <= 20, k < n`; n=21 → `unavailable_result`; RNG consumption order documented | Artifact 15 |
| G-J5a/b | Power-law: fitting method + bootstrap count named constants; α≤2 emits machine-readable gate fields validated by schema | Artifact 3, 19 |
| G-J6 | Markov: chain classification field (`ergodic`/`reducible`/`cyclic`); cyclic fixture returns `unavailable`; Page vs. standard matrix convention stated | Artifact 2 |
| G-J7 | Schelling: RNG order, caps (grid ≤ 128, steps ≤ 1000), `terminated_reason` field | Artifact 12 |
| G-J8 | Bandits: named stdlib draws; regret ≥ 0 asserted in tests; regret oracle defined | Artifact 16 |
| G-J9 | Blotto: input caps asserted; enumeration vs. pairwise split into two named functions | Artifact 13 |
| G-J10 | Multi-trial child-seed derivation rule stated once, tested once | Artifacts 14, 16 |
| G-J11 | Shared atom-constructor helper (`atoms.py`) exists before any model module; all atoms pass `validate_evidence_atom` | New Artifact 1.5, before Artifact 2 |
| G-J12 | CLI name resolved *before* Artifact 17 is written; skill text matches the implemented command | Phase 2 ordering |
| G-J13 | Per-model mutation tests (≥1 sign-flip killed each) added to Artifact 20 acceptance criteria | Phase 2 gate |
| G-J14 | Performance budget stated (single ensemble run ≤ 5 s at default caps) and enforced by a timing test with generous CI headroom | Phase 2 gate |

---

## Questions for the Human Governor

1. **Determinism class policy:** Is bit-exact reproducibility across *CPython versions* a hard requirement (then we pin the runtime and document it), or only within one version (then tests assert exact equality and we note the caveat in docs)? This decides how much energy G-J2 consumes.
2. **NK cap value:** Is n ≤ 20 acceptable for the decision use-cases you foresee, or does the router need landscapes only up to n ≈ 12 for interactivity? (Lower cap = faster ensemble sweeps.)
3. **Markov convention:** Adopt Page's row/column convention verbatim for didactic fidelity, or the standard row-stochastic convention for interop with any future data pipelines? One must win; both cannot coexist.
4. **SIR fidelity vs. honesty:** When Euler at Δt=1 is unstable, do you want (a) `unavailable` (honest, my recommendation), (b) automatic sub-stepping (Δt = 1/k until stable, still deterministic, slightly more code), or (c) RK4? (b) is ~20 lines and keeps the "1 day" mental model; my recommendation is (b) with (a) as the cap fallback.
5. **Ensemble latency budget:** Is a ≤ 5 s single-run budget (my back-of-envelope says it's achievable with the caps above) the right number for the interactive router, or should sweeps be batch-mode only?
6. **Blotto scope:** Do you need full mixed-strategy analysis (infeasible exactly in stdlib; would need sampling → becomes `modeled` not `calculated`), or is pairwise payoff + underdog-concentration analysis (cheap, pure) enough for Phase 2? The provenance label flips depending on your answer.
