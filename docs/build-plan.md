# Many-Model Thinking Extension — Authoritative Build Plan

Status: implementation complete; ship-now release sprint T30-T34 approved, 2026-09-02
Execution queue: [`docs/tasks_list.md`](tasks_list.md)  
Canonical adversarial register: [`docs/council/risk_review.md`](council/risk_review.md)

This document replaces the missing/superseded draft summarized in `docs/council/review_packet.md`. Council reviews and `docs/council/plan-revisions.md` are evidence, not competing specifications. If they conflict with this file, this file governs.

## 1. Outcome

Build a local-first Scott Page-inspired analysis path that improves a stock-exposure decision by identifying when a thesis relies on an invalid tail assumption, an unstable regime model, an adoption assumption, or an under-explored information source. The extension must change a machine-readable decision permission or one of the existing six recommendation outcomes on at least one of two representative theses. Better prose alone is not success.

The completed user path is:

```text
verified local case + approved model inputs
  -> deterministic/fixed-seed model receipts
  -> typed claim projection
  -> deterministic claim compiler
  -> executable page method pack
  -> existing risk/recommendation precedence
  -> existing hash-bound human authorization
```

The extension never trades, contacts a broker, silently changes an assumption, or records a decision without the existing authorization contract.

### Success metric

Before broad expansion, two local thesis runs compare baseline versus Page-enabled behavior. A decision-relevant delta is either:

1. a changed value within the existing recommendation vocabulary; or
2. a newly binding, machine-readable veto that changes which downstream calculations or actions are permitted.

Pure wording, additional charts, or a different simulated voice do not count. If both thesis runs have zero decision-relevant delta, the completion branch is power-law-only and the other model, ensemble, Page-pack, and Committee tasks are marked `CUT` as defined in `tasks_list.md`.

## 2. Non-negotiable repository constraints

- The agent explains and orchestrates; fixed Python calculates.
- Runtime calculation code uses only the Python standard library. Neither lock file changes.
- Python support remains `>=3.11,<3.14`; same-version, separate-process replay must be byte-identical.
- Real portfolio and thesis data stays under gitignored `local/`. Committed fixtures are synthetic.
- Unavailable or untrusted inputs produce typed unavailable results; the engine never invents facts.
- Existing canonical JSON and SHA-256 helpers are reused.
- Page model receipts use decision-analysis evidence atoms, not source-level `evidence-item.v1` documents.
- Page analysis is upstream of existing Kelly, convexity, margin, model-health, recommendation, and authorization logic. It does not duplicate them.
- Margin survival remains the highest-priority recommendation constraint.
- Every production slice follows strict Red/Green TDD. Tests and fixtures are frozen before implementation; an implementer cannot weaken them.
- Existing harness configuration is immutable. New enforcement is added test-first; existing rules are never relaxed to pass.

## 3. Repository truth that the build may rely on

| Concern | Verified interface |
|---|---|
| CLI entry | `capital_decision_lab.plugin.commands:main` in `pyproject.toml` |
| Single method invocation | `capital method run --pack <id> --case <path>` |
| Committee invocation | `capital method committee --packs <ids...> --case <path>` |
| Method registry | `PACKS` in `methods/packs.py` |
| Method execution | `run_method_pack` in `methods/runner.py` |
| Committee execution | `run_committee` in `methods/runner.py` |
| Kelly | `calculations/allocation.py::kelly` and `analyze_kelly` |
| Canonicalization | `contracts/canonical.py` |
| Model-output atom | `$defs.evidence_atom` in `decision-analysis.v1.schema.json` |
| Distribution allowlist | `distribution.yaml::distribution_owned` |
| Private-data check | `scripts/check_staged_private_data.py` |

There will be no fictional `capital model-thinking run` command. The executable integration is `PACKS["page"]`, reached through the existing method commands and `capital analyze-position --method page`.

Root `dlc-*` files are agent-facing simulated voices. They are not the executable method-pack registry. The build creates both an executable `page` method pack and a bounded `dlc-page` interpretation voice, with those roles explicitly separated.

## 4. Adversarial corrections adopted

The earlier materials were directionally useful but contained unsafe or non-executable assumptions. The build adopts these corrections:

1. **No heterogeneous raw voting.** Markov, power-law, Bass, and bandit outputs are not predictions of the same quantity. The Diversity Prediction identity applies only to comparable numeric predictions of the same target under the stated squared-error/mean definitions. The compiler groups only normalized records sharing a `claim_id`; unrelated model outputs remain separate diagnostics.
2. **Power-law notation is explicit.** V1 supports a continuous density with `p(x) proportional to x^-alpha`. Under that convention, the mean is finite only for `alpha > 2` and variance only for `alpha > 3`. A CCDF exponent is rejected rather than silently interpreted.
3. **A log-log line is not proof.** The power-law engine is a bounded statistical diagnostic. “Not rejected under this diagnostic” is not “the data are a power law.” The implementation follows a named, tested continuous-tail procedure and reports its limitations.
4. **Kelly is not attributed to Page.** An undefined first moment creates a product safety veto on exposure increases when the Kelly probability/payoff inputs depend on that invalid tail model. It does not prove every binary-event Kelly calculation is mathematically undefined. Infinite variance blocks variance-dependent metrics; it does not by itself block Kelly.
5. **Markov orientation is explicit.** V1 uses row-stochastic `P[from_state][to_state]` and row-vector stationarity. The Page column-vector convention is documented as the transpose. Unlabeled orientation is rejected.
6. **Fixedness is an assumption, not observable from one matrix.** The engine checks finite dimensions, probabilities, row sums, irreducibility, and aperiodicity. A trusted `transition_rule_fixed` assertion is recorded as an assumption and limitation.
7. **Deterministic dynamics are calculated.** Markov and Bass numeric outputs are `calculated`; fixed-seed bandit simulations are `modeled`; decision implications are `forecast`.
8. **The “5–7 model sweet spot” is not a router invariant.** It is removed unless a primary source and its conditions are recorded. V1 has four models because of product scope and distinct decision questions.
9. **Committee strings are a closed interface.** Unknown recommendation text is rejected; the current `recommendations[0]` fallback is removed before Page joins Committee Mode.
10. **Trust is separate from provenance.** `input_trust_class` is model-input metadata, not a new `provenance_class` value.

Primary statistical grounding for the power-law diagnostic is [Clauset, Shalizi, and Newman, *Power-Law Distributions in Empirical Data*](https://arxiv.org/abs/0706.1062) (SIAM Review 2009). Page/Hong diversity results are explanatory context only; they do not define compiler mechanics or authorize cross-target voting.

## 5. Decisions frozen for v1

| Decision | Choice |
|---|---|
| Product scope | Prove a decision delta before broad build; zero delta completes as power-law-only |
| V1 models | Power-law, Markov, Bass diffusion, and Page-grounded bandit variants |
| Cut models | SIR, Schelling, Blotto, Polya, and NK; no dormant scaffolding ships |
| Ensemble | Deterministic compiler over typed, same-`claim_id` records |
| Robust conclusion | At least 2 applicable independent families and support from `max(2, ceil(2A/3))` of `A` applicable independent families; any binding veto prevents robust-positive |
| Correlation | Declared correlated models do not count as independent support |
| Threshold ownership | Versioned engine constants; no runtime agent-selected threshold |
| Seed UX | Derive from canonical validated input plus model ID; record it; no routine CLI seed flag |
| Model routing | Deterministic applicability rules; irrelevant models are not forced to fill a quota |
| Insufficient diversity | Emit `insufficient_distinct_models`; a single model may return a diagnostic but never an ensemble-robust claim |
| Decision hook | Wired in v1; no analysis-only deferral |
| Committee vocabulary | Existing six strings only; boundary validation replaces fallback |
| Threat scope | Browser, scrape, social, OCR, paste, and external retrieval are attacker-controlled by default |
| Privacy boundary | Existing ingest/extract/confirm quarantine plus typed trust gate and physical calculation-layer no-egress |
| Test policy | Strict recorded RED; no test-after compensation |
| Context ceiling | At most 6,000 added loaded tokens for a representative Page run; references load only when selected |
| Waivers | Written owner, affected gate, accepted risk, expiry/removal condition; silent skip fails; zero-delta branch is not waivable |

## 6. Contracts and boundaries

### 6.1 Model input envelope

Add `nhi.model_input.v1` with:

- `model_id`, `model_version`, `model_family`
- model-specific typed parameters
- `input_refs` and immutable input hashes
- `input_trust_class`: `synthetic_test`, `user_verified`, `verified_local`, or `untrusted_external`
- `claim_specs`: bounded identifiers and applicability rules; no arbitrary conclusion prose
- explicit units, orientation, horizon, and caps where relevant

Only `synthetic_test`, `user_verified`, and `verified_local` may enter calculations. External narrative can propose a typed input, but user confirmation must change its trust class before computation. Booleans are rejected as numbers; all numbers must be finite.

### 6.2 Model result envelope

Add `nhi.model_result.v1` with:

- result/model/family/version identifiers
- canonical input hash
- `data`: named decision-analysis evidence atoms
- metadata: algorithm version, parameters, seed or `not_applicable`, caps, iterations/trials, runtime policy
- limitations and shared unavailable reason codes
- canonical hash

Every stochastic model uses a local `random.Random(derived_seed)` and a frozen draw-order specification. Pure deterministic functions do not accept a meaningless seed.

### 6.3 Claim IR and ensemble result

Each applicable model result is projected by engine code into bounded claim records:

```text
claim_id
direction = supports | contradicts | neutral | unavailable
model_id
model_family
receipt_hash
applicable
correlation_group
binding_veto
condition_code
```

Add `nhi.ensemble_result.v1`. Required fields include `aggregated_by: "engine"`, contributing receipt hashes, applicable family count, threshold constant/version, `correlated_models`, robust/conditional/disputed claims, binding vetoes, limitations, and canonical hash. Free-text fields are bounded; engine verdicts and conditions use enums/reason codes.

The compiler never averages heterogeneous outputs. The Diversity Prediction identity gets a separate golden test using comparable scalar predictions; it is not the implementation of the claim compiler.

### 6.4 Page method pack

`PACKS["page"]` is the executable interface. `run_method_pack("page", case_bundle)` validates a `method_inputs.page` payload, runs applicable model engines, compiles claim receipts, and maps the result into a normal `nhi.method_pack_result.v1`.

Recommendation precedence is:

1. `avoid margin` when existing margin survival binds;
2. `pause` for untrusted required inputs, an unavailable required diagnostic, or a binding safety veto;
3. `watch` for material unresolved disagreement or downside without a valid sizing basis;
4. `hold current exposure` when informative but not resizing evidence;
5. `trim to fractional Kelly` only through the existing Kelly/risk constraints;
6. `increase exposure under this assumption set` only when the existing decision path permits it, the relevant claim is robust-positive, and no veto binds.

All outputs remain model-implied and require the existing separate user authorization.

## 7. V1 model catalog

### 7.1 Power-law diagnostic — first vertical slice

Decision question: do supplied positive continuous observations support use of finite-moment assumptions?

- Continuous density exponent convention only.
- V1 requires a trusted, explicit `xmin`; it does not search for one. It accepts 50–10,000 observations in the tail (`x >= xmin`) and rejects nonpositive/nonfinite data.
- Continuous maximum-likelihood estimate: `alpha = 1 + n / sum(log(x / xmin))`.
- Goodness-of-fit uses the one-sample KS distance against the fitted continuous power-law CDF and 250 canonically seeded parametric-bootstrap replicates. Each replicate re-estimates `alpha` at the same `xmin`. `p >= 0.10` means only `not_rejected_by_diagnostic`; lower values mean `rejected_by_diagnostic`.
- Numeric assertions use an explicit per-test tolerance, with `1e-10` as the default. The observation cap and bootstrap count are fixed for v1 and cannot be tuned by an implementer.
- Reports `alpha`, `xmin`, tail count, KS statistic, diagnostic p-value, `power_law_not_rejected`, `mean_defined`, and `variance_defined`.
- “Not rejected” never becomes “proven.” Unsupported/discrete/ambiguous exponent inputs return unavailable.
- Machine policy: `alpha <= 2` blocks moment-dependent positive exposure changes; `alpha <= 3` blocks variance-dependent metrics. Independently supplied bounded binary Kelly inputs are not automatically invalidated by variance alone.

### 7.2 Markov regime diagnostic

Decision question: under a trusted fixed transition rule, what is the stationary regime mix and is convergence justified?

- Row-stochastic matrix with 2–64 named states and explicit `row_from_state` orientation.
- Checks bounded finite dimension, finite probabilities, row sums, irreducibility, and aperiodicity.
- Requires a trusted `transition_rule_fixed` assumption and records it.
- Emits stationary distribution only when conditions hold; reducible, periodic, absorbing, transposed, or untrusted-rule fixtures return typed unavailable results.
- Row sums use tolerance `1e-12`. Stationarity uses uniform initialization, L1 delta `<=1e-12`, and at most 100,000 iterations. Golden fixture: the grounded two-state example yields 75/25 within `1e-10`.

### 7.3 Bass diffusion diagnostic

Decision question: how do innovation/broadcast and imitation assumptions change an adoption trajectory?

- Discrete-time equation `new = (p + q * adopters / market) * remaining`, with `p >= 0`, `q >= 0`, and `p + q <= 1` so one step cannot adopt more than the remaining population.
- Market potential is finite and in `(0, 1e9]`; initial adopters are in `[0, market]`; horizon is an integer in `[1, 10_000]`.
- Checks non-negativity, monotonic cumulative adoption, and population conservation within tolerance.
- Deterministic; no seed; numeric outputs are `calculated`.

### 7.4 Bandit information-value simulation

Decision question: which research option balances immediate payoff with information gain under supplied synthetic/verified reward assumptions?

- V1 uses 2–64 Bernoulli arms with verified probabilities in `[0,1]`, horizon `[1,100_000]`, deterministic lowest-index tie breaking, and three variants: greedy, sample-then-greedy, and adaptive epsilon.
- UCB1, Thompson sampling, and Gittins computation are excluded from v1.
- Sample-then-greedy requires 1–1,000 initial pulls per arm and cannot exceed the horizon. Adaptive epsilon uses `max(epsilon_min, epsilon_0 / sqrt(t + 1))`, with `0 <= epsilon_min <= epsilon_0 <= 1`.
- Per round, the frozen RNG order is exploration draw when applicable, exploratory arm draw when applicable, then one Bernoulli reward draw for the selected arm. The seed is derived from the canonical validated input plus model ID.
- Reports pulls, rewards, regret, selected policy, and seed as `modeled`; it never directly changes exposure.

## 8. Security architecture

The lethal-trifecta defense is structural:

- Private data remains local.
- External text remains untrusted data and cannot become calculation parameters without typed confirmation.
- Calculation modules have no network or subprocess/file-fetch behavior.
- The compiler consumes schemas and enums, not external prose.
- Model/ensemble free text is length/pattern bounded and cannot carry executable instructions.
- Injection-present and injection-absent runs with identical numeric inputs must produce identical canonical model output.
- Static checks reject `socket`, `urllib`, HTTP clients, subprocess invocation, dynamic imports, and non-stdlib imports in the new calculation package.
- The existing staged-private-data scanner is part of every integration/release gate, not a final checklist note.

Gemini and DeepSeek tasks receive only public repository material, synthetic fixtures, or explicitly redacted task-local packets. If the execution environment cannot guarantee that boundary, the task routes to Sol. No external model receives real portfolio/thesis data.

## 9. Execution phases and gates

Task-level details, heroes, models, editable scopes, and commands are in `docs/tasks_list.md`.

### Phase A — Freeze truth and establish baseline

Tasks T00–T05. Install the existing pinned development environment outside the source tree, capture Python/test count/runtime, map interfaces, freeze the customer outcome, threat model, and TDD ledger.

Gate: existing full suite is green. If it is red, feature work stops and the baseline fault is isolated without changing the harness.

### Phase B — Contracts and enforcement first

Tasks T06–T07. Write failing schema/trust/reason-code/canonicalization tests, freeze their hashes, then implement only enough shared contract support to pass.

Gate: targeted and full suites green; separate-process canonical replay matches; schema and validator mutants are killed; frozen test hashes unchanged.

### Phase C — Power-law vertical slice and outcome gate

Tasks T08–T12. Build the statistical diagnostic and downstream safety policy test-first, run through the real method path, then compare two local theses.

Gate: at least one machine-readable decision delta unlocks expansion. Zero delta marks T13–T24 `CUT` and completes a power-law-only product through the adapted release tasks.

### Phase D — Remaining approved models

Tasks T13–T18. Markov, Bass, and bandits are independent Red/Green slices. They may be implemented in parallel only after their verifier tasks freeze disjoint tests and fixtures.

Gate per model: rejection matrix, replay where stochastic, standard-library/no-egress checks, killed mutant, targeted/full suite green.

### Phase E — Typed claim compiler and Page integration

Tasks T19–T24. Build same-claim aggregation, the Page method pack, and the Committee vocabulary boundary.

Gate: no heterogeneous voting; no freehand LLM aggregation; `page` runs through the real CLI; unknown recommendation strings are rejected; default-cap run is at most five seconds.

### Phase F — Agent surface and distribution

Tasks T25–T26. Add a thin skill, lazy model references, and a non-executable `dlc-page` interpretation voice. Register all shipped paths and remove superseded guidance.

Gate: all documented commands execute unchanged; loaded context delta is at most 6,000 tokens; the voice contains no computation; Page pack and DLC roles cannot be confused.

### Phase G — Independent attack and release proof

Tasks T27–T29. Run injection, trust, egress, path, nonfinite, replay, mutation, performance, distribution, private-data, CLI, and full-regression gates. Remove temporary scaffolding whose removal triggers have fired.

Gate: every task is `DONE`, `CUT` by the outcome rule, or has a valid written waiver; no untracked private/generated artifacts; no unexplained changes; final full suite remains green.

## 10. Evidence and build ledger

Each task receipt records:

- task ID, state, hero, model, and agent/session identifier
- command, exit code, elapsed time, and concise failure/success evidence
- input/test/fixture hashes
- allowed and actual changed paths
- RED failure proving missing behavior
- GREEN targeted/full-suite results and test count
- mutation killed
- risk IDs retired or residual risk accepted
- waiver owner/expiry when applicable

Valid states are:

```text
PENDING -> READY -> IN_PROGRESS -> RED_RECORDED -> GREEN_VERIFIED -> DONE
```

`CUT` is allowed only through T12's automatic zero-delta branch. `BLOCKED` names the exact missing dependency or receipt. Implementers cannot edit frozen tests/fixtures; a wrong specification returns to its verifier.

## 11. Definition of done

The extension is complete only when:

- the T01 baseline and final full suite are green with test count unchanged or increased;
- every implemented behavior has prior valid RED evidence and at least one killed relevant mutant;
- canonical output replays byte-identically in separate processes on the recorded Python version;
- the power-law safety hook changes permissions as specified and does not overclaim statistical certainty;
- the expansion branch, if taken, ships exactly the four approved model families and the typed claim compiler;
- `capital method run --pack page` and `capital analyze-position --method page` succeed on synthetic golden cases;
- Committee rejects unknown recommendation strings and retains user authorization;
- no new runtime dependency, calculation-layer egress, private committed data, or lock/harness change exists;
- distribution registration, context budget, performance budget, and staged-private-data checks pass;
- Page interpretation is clearly separated from existing Hermes Kelly/margin logic and from simulated voice output;
- no unfinished placeholder marker, fictional interface, stale open question, or cut-model scaffolding remains in shipped guidance.
- the current release-verifier hashes are recorded without rewriting the historical T21 receipt; any missing prior-RED evidence has a named, expiring waiver;
- the authoritative release count is consistent in the task list, retrospective, learning log, and release receipt;
- `distribution.yaml::version`, the immutable Git tag, and the published release identifier all equal `0.2.0` / `v0.2.0`;
- a fresh checkout of `v0.2.0` passes the release smoke and staging-install validation.

## 12. Risk-retirement map

`docs/council/risk_review.md` remains the canonical detailed register. This map prevents its findings from becoming detached review prose.

| Risk IDs | Retired by | Required proof |
|---|---|---|
| MR-01, MR-04, MR-09 | T02,T06,T07,T23,T24 | exact schema/CLI/pack map; correct atom contract; closed Committee boundary |
| MR-02, MR-07, MR-15 | T01,T05,T06 and every Red/Green pair | green baseline; valid prior RED; frozen hashes; full-suite regression; killed mutants |
| MR-03, MR-11, MR-27 | T07–T09,T13–T20 | derived/recorded seeds only where stochastic; fixed draw order; canonical replay; fixed threshold constants |
| MR-05, MR-10, MR-30 | T19–T22 | deterministic same-claim compiler; correlation handling; two-family minimum; real Page consumer |
| MR-06, MR-08, MR-14, MR-29 | T08–T18 | bounded model contracts; grounded golden/adversarial tests; corrected moment thresholds; no unsupported attribution |
| MR-12, MR-13, MR-16, MR-17, MR-26 | T04,T06,T07,T19,T23,T27 | trust class; bounded text/reasons; no egress; injection invariance; shared reason vocabulary |
| MR-18, MR-20 | T03,T12 | measurable customer outcome; two-thesis receipt; automatic zero-delta cut |
| MR-21, MR-28, MR-32 | T19,T25,T28 | context ceiling; no skill-side computation; bounded agent-facing failures |
| MR-22, MR-23, MR-24, MR-25 | T02,T26–T29 | stdlib scanner; distribution coverage; staged-private-data command; repository corrections retained |
| MR-19, MR-31 | T20–T22,T28 | real CLI smoke and <=5-second default-cap execution |

No risk is closed by documentation alone when the register calls for a mechanical gate. Residual or waived risks remain visible in the build ledger.

## 13. Explicitly deferred work

SIR, Schelling, Blotto, Polya, NK, UCB1, Thompson sampling, Gittins computation, generalized discrete power-law fitting, cross-version byte identity, broker integration, automated trading, and distributed execution are not v1. A future proposal must name a validated thesis question, add a customer-outcome test, and repeat the contract-first Red/Green process. No placeholder modules or unused schema fields are created now.

## 14. Ship-now release sprint

The implementation is complete and the current full suite is green, but publication is blocked by stale release evidence: T21 records an obsolete frozen hash and T28-era prose mixes 329 and 338 tests. Tasks T30-T34 are the only authorized pre-release work. No feature expansion, calculation refactor, schema redesign, or adjacent cleanup is permitted.

### 14.1 Release decision

- **Release version:** bump `distribution.yaml` from `0.1.0` to `0.2.0` because Page is a backward-compatible feature expansion.
- **Git tag:** `v0.2.0`. The existing `v0.1.0-cli-mvp` tag is retained. Never move, replace, or force-update either tag.
- **Release branch:** `main`; publication uses ordinary fast-forward pushes to `origin` only.
- **Release artifact:** the deny-by-default staged Hermes profile plus its generated manifest, built from the exact tagged commit.
- **Failure policy:** any failed binary gate returns the active task to `BLOCKED`; do not weaken tests, rewrite a tag, force-push, or publish an unverified artifact. After a published defect, patch forward with a new version.

### 14.2 Frozen-test lineage decision

The historical T21 hash `F89DA724...` does not describe the current expanded verifier file. It remains historical evidence for the original T21 slice and must not be relabeled as unchanged. T30 records the current `tests/methods/test_page_runner_e2e.py` hash `315C6C27912D20BCD77206D103F14CEF40F191D4815B45E744DC438AE98BDB7B` as a new release-remediation verifier baseline.

Because the malformed-input implementation already existed before those extra assertions were isolated as a new verifier slice, prior RED evidence cannot be recreated honestly. T30 therefore records waiver `WV-PAGE-001`, limited to test-order provenance—not behavior, security, or test failures. The waiver expires at the earlier of 2026-10-02 or the next behavior change under `capital_decision_lab/methods/runner.py`. Its compensating controls are source-level trust-boundary mutation, independent code review, the immutable current hash, the 338-test suite, and a fresh-tag smoke test.

### 14.3 Release gates

T30-T34 execute serially. The release is shipped only when all gates are true:

1. Current verifier, outcome, mutation, project, and lock hashes are captured in one release receipt.
2. The targeted Page, Committee, outcome, mutation, distribution, private-data, and full suites pass from a clean tree.
3. Exactly 338 or more tests are collected; all authoritative documents report the observed count, never a copied expectation.
4. The staging manifest contains `dlc-page.md`, the Many-Model skill, schemas, fixtures, and plugin modules, and excludes `docs`, `tests`, `local`, credentials, and generated caches.
5. `git diff --check` is clean; lock hashes remain unchanged; no runtime dependency is added.
6. The release commit is tagged once as `v0.2.0`, pushed without force, and verified by remote ref lookup.
7. A fresh checkout of `v0.2.0` passes the release smoke and install-source validation.

Task ownership, intelligence levels, model routing, exact receipts, and editable scopes are defined in `docs/tasks_list.md`.

Release-governor routing override: by explicit user direction on 2026-09-02, every T30-T34 task previously assigned to Gemini or DeepSeek executes on `luna`. This changes T31 and T32's deployment model only; their difficulty classification, hero ownership, independent verification, containment rules, and binary gates remain unchanged. I5 tasks remain on `sol`.
