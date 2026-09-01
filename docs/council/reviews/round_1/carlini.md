# Round 1 Adversarial Review — [N] Nicholas Carlini, Adversarial Reductionist

**Operating question:** "If an attacker controls one external input to this system, can they hijack the agent's control flow?"

**Scope note:** Local research tool, no persistence beyond hash-bound human-authorized records, no autonomous trading. Per my cost-to-attack release valve, I am *not* demanding Docker/VM sandboxing or credential isolation here — attack reward is low and the authorization gate already caps blast radius. What I *do* demand is that the deterministic engine hard-fail structurally on hostile inputs, because the plan currently has the LLM standing on the trust boundary with nothing deterministic behind it. Every objection below is a binary gate: pass or fail, no vibes.

---

## Key Risks

**R1 — The trust boundary is enforced by prompt, not by architecture. (SEVERITY: HIGH)**
The plan's central safety claim for the new skill is: *"Never instructs agent to compute simulations freehand (enforced in description)"* (Artifact 17). "Enforced in description" is an oxymoron — a YAML `description:` field is prompt text, and prompt text is not a security mechanism. My card is explicit: *"If you're trusting the model to 'be safe,' you've already lost."* The real control-flow hijack path is:

1. Skill workflow step 3 instructs the agent to gather evidence via browser/scrape/OCR/paste connectors (attacker-controllable if the agent reads a hostile web page, a scraped filing, an X post).
2. That untrusted text becomes model parameters (a transition matrix, a population count, a seed, a beta/gamma pair).
3. The LLM — whose context now contains attacker text interleaved with instructions — decides how to format the CLI call to `capital model-thinking run`.

Nothing in the plan specifies a deterministic layer between "extracted text" and "engine argument." The existing engine pattern (validated in `calculations/simulation.py` — isinstance checks, bool exclusion, `math.isfinite`, probability sum tolerance, `unavailable_result` fallback) *is* the right architecture; the plan never mandates it for the eight new modules. Each of the 8 model artifacts says only "Validates inputs" as an acceptance criterion — one sentence, no spec, no test enumeration.

**Binary gate:** Every `model_thinking/*.py` module MUST reject, with `unavailable_result` (not exception-crash, not clamping), any input that is: non-numeric, `bool`, NaN, ±inf, out-of-declared range, wrong shape/dimension, or above a declared size cap — and MUST have a per-rejection-class unit test proving it. Gate fails if any of the 8 modules lacks the full rejection matrix.

**R2 — Attacker-controlled resource exhaustion via unbounded dimensions. (SEVERITY: MEDIUM-HIGH)**
Concrete instances the plan leaves open:
- Markov: "square matrix" — of any size. A hostile page could yield a 10,000×10,000 matrix; power iteration is O(k·n²).
- NK landscape: "n kept small for feasibility" (Artifact 15) and "Limit n≤10 **in documentation and reference files**" (Risk Register). That's control-by-documentation — exactly the "prompt wording as security" failure. The agent reading a hostile input can propose n=24 (16M genotypes × 2^k fitness evals each) and the engine will happily hang the machine.
- Schelling: `grid_size`, `steps` unbounded. SIR: `days` unbounded. Bandits: `horizon` unbounded.

**Binary gate:** Each module declares a hardcoded maximum (e.g., n≤10 for NK, matrix dim ≤ 64, grid ≤ 200×200, days ≤ 3650, horizon ≤ 10^6) and raises `unavailable_result("INPUT_EXCEEDS_LIMIT")` above it. The limit lives in the .py file, not in a reference markdown.

**R3 — `seed` handling is unspecified and partially breaks the C4 determinism contract. (SEVERITY: MEDIUM)**
- Artifacts accept `seed=None` while claiming "Deterministic: same inputs + seed → same output." For stochastic models (Polya, Thompson, Schelling placement, bandits), `seed=None` means unseeded `random` → non-reproducible output → C4 violated silently. `simulation.py` (the house pattern) requires `seed: int` as a keyword-only argument — the new modules diverge from the only working precedent in the repo.
- Seed type/width is unspecified. `random.Random(x)` will happily accept strings, tuples, or `True` (which equals seed 1). A hostile or malformed seed is a silent semantics change, not a crash.
- The seed flows *out* into evidence atoms and into `canonical_hash` inputs. An attacker who controls the seed controls reproducibility claims — a forged provenance channel.

**Binary gate:** All stochastic modules take `seed: int` (keyword-only, required, `isinstance(seed, int) and not isinstance(seed, bool)` validated, range-checked), mirroring `simulation.py`. `seed=None` is rejected with `unavailable_result`, not defaulted to system entropy. Gate fails if any stochastic module accepts None.

**R4 — Skill-as-injection-surface: extracted evidence text is never structurally separated from instructions. (SEVERITY: HIGH)**
The skill workflow (Artifact 17) reproduces the capital-research flow: ingest → `capital host extract` → analyze. That flow was built for *narrative* evidence, where an LLM reading attacker text is an accepted cost (bounded by the authorization gate). The new flow is different: the same attacker text becomes *numeric model parameters* that feed a deterministic engine whose output is then fed back into the agent's context as "robust conclusions." That closes an injection loop: hostile page → hostile parameters → engine output → agent believes the engine "validated" the content. Validation of *shape* is not validation of *provenance*. The plan has no rule stating which provenance classes of evidence may populate which model parameters.

**Binary gate:** The engine's CLI layer (`capital model-thinking run`) MUST accept parameters only from structured host-extract fields and MUST embed each parameter's `input_refs` + provenance in the output metadata (the repo already does this — `simulation.py` records `input_hashes`). Evidence atoms with `provenance_class` in {unknown, narrative, unavailable} MUST be rejected as model parameters with `unavailable_result("UNTRUSTED_PARAMETER_SOURCE")`. The skill prompt may *say* this too, but the gate is on the engine.

**R5 — Ensemble aggregation ("robust conclusions") has no specified computation site. (SEVERITY: HIGH)**
Artifact 19 defines `robust_conclusions` as "conclusions supported by ≥ threshold models" — but nowhere does the plan say *who computes* the support count. If the LLM reads 5–7 model outputs and freehands the robust/disagreement classification, then: (a) the "never compute freehand" hard rule is violated by the flagship feature, (b) the count is attacker-influencable via any single model's parameters (my Rule 9: never trust model self-correction — same logic applies to agent judgment), and (c) `canonical_hash` over an LLM-judged result is provenance theater.

**Binary gate:** A deterministic engine function (e.g., `model_thinking/ensemble.py: aggregate(results, threshold)`) MUST compute robust/condition-dependent/disagreement classification from the raw evidence atoms, with its own unit tests, and the ensemble-result schema MUST require an `aggregated_by: "engine"` field. If the plan keeps aggregation in agent judgment, the gate fails.

**R6 — Free-text string fields in the ensemble schema are an injection channel back into agent context. (SEVERITY: MEDIUM)**
`condition` (string) and `point_of_contention` (string) in Artifact 19 are unconstrained free text inside a schema whose consumers are LLMs (Committee Mode compares DLC outputs). If any contributing model's parameters were attacker-influenced, those strings are the echo channel that re-arms the injection after the engine has reduced everything else to validated numbers. This is my Rule 2 (instruction/data confusion) — the schema is the compiler boundary, and it currently permits raw prose in it.

**Binary gate:** Schema MUST bound these fields (max length, and either enum-of-condition-slots or a pattern), and the deterministic aggregator MUST derive `point_of_contention` from a fixed vocabulary (e.g., field name + model ids), not from model output prose. Failing that, the fields must be marked `provenance_class: "modeled"` and carry `input_refs` — but bounded-vocabulary is the pass condition.

**R7 — Adversarial fixtures are completely absent from the plan. (SEVERITY: MEDIUM)**
The repo has a working pattern: `fixtures/adversarial/` with 10 fixtures covering invalid probabilities, path escape, missing provenance, authorization mismatch. The plan specifies `fixtures/valid/model_thinking/` for all new models and *zero* adversarial fixtures. Per my Rule 4, you never test security against the average case; per my Rule 7, red-team inputs are how you find the rejection matrix gaps. This is the cheapest, highest-yield fix in this review.

**Binary gate:** For each of the 8 new models, ≥4 adversarial fixtures MUST be committed under `fixtures/adversarial/model_thinking/` covering: (1) NaN/inf, (2) wrong shape/type, (3) over-limit dimension, (4) bool-as-number or seed abuse. Gate = fixtures exist AND each is wired to a test asserting `unavailable_result`.

---

## Architecture Critique

- **The good news, stated precisely:** the repo's existing engine layer already implements my Structured Output Compiler pattern correctly — LLM produces intent → CLI → deterministic Python → validated evidence atoms → schema with `canonical_hash` → hash-bound human authorization for anything that persists. `privacy/containment.py` even does real reparse-point-aware path containment. This plan is extending an architecture that already has the right spine. My objections are about the new modules not inheriting the spine, not about the spine itself.
- **The plan's failure mode is uniform:** every security-relevant property in it ("validates input", "enforced in description", "kept small in documentation", "verify local/ boundary is respected") is expressed as a *sentence* rather than as a *test*. Sentences are prompts. Prompts are not security. Convert each sentence into an executable assertion and the plan becomes acceptable.
- **Division of labor:** Cherny owns whether the gate ordering is right; I only note that Phase 1's acceptance gate ("all unit tests pass") contains no adversarial-case requirement, so a Phase 1 implementation could pass its own gate while accepting every hostile input in R1–R3. The gate itself is structurally insufficient, independent of ordering.
- **The ensemble feature is the one genuinely new trust-boundary shape** in this plan (many engine outputs → single conclusion object consumed by agent + Committee Mode). Everything else is pattern-following. That's where architectural attention belongs, and it's currently the least-specified artifact (threshold open, aggregator unspecified, free-text fields unbounded).

## Missing Specifications

1. A written **input validation contract** for `model_thinking/` (accepted types, isfinite requirement, bool exclusion, range and size caps, rejection mechanism = `unavailable_result` with stable reason codes) — one document, referenced by all 8 artifacts.
2. **Seed specification**: type, required-ness, range, and the rule that a stochastic model without a seed is a hard error, not a default.
3. **Parameter provenance rule**: which `provenance_class` values are admissible as engine parameters (R4).
4. **Aggregation ownership**: who computes robust conclusions, and proof it's deterministic (R5).
5. **Size-limit table**: per-model hardcoded maxima with the exact rejection code (R2).
6. **Injection-test suite**: adversarial fixtures enumerated per model (R7) — the plan has a Risk Register row for "non-stdlib dependency" but none for hostile inputs; that asymmetry is the tell that threat modeling wasn't done.
7. **local/ boundary enforcement for model runs**: the plan's Phase 4 says "Check that real data boundary is respected" — a checklist sentence. The repo has `scripts/check_staged_private_data.py`; the gate should be "script runs clean and is wired into the Phase 4 validation command," not "checked."

## Recommended Task Gate Updates

| # | Gate (binary) | Blocks |
|---|---|---|
| G1 | All 8 modules implement the full input rejection matrix (type, bool, NaN/inf, shape, size cap, provenance-class) with per-class unit tests | Phases 1–2 exit |
| G2 | Per-model hardcoded size limits live in code; doc-only limits fail the gate | Phases 1–2 exit |
| G3 | Stochastic modules require typed int seed (no None, no bool); determinism tests pin (inputs+seed) → byte-identical output | Phases 1–2 exit |
| G4 | `ensemble.py` deterministic aggregator exists, tested, and `ensemble-result.v1` requires `aggregated_by: "engine"` | Phase 2 exit |
| G5 | `condition`/`point_of_contention` bounded (length + vocabulary or pattern) in schema | Phase 2 exit |
| G6 | ≥4 adversarial fixtures per model under `fixtures/adversarial/model_thinking/`, wired to tests | Phase 2 exit |
| G7 | Phase 4 validation command includes `check_staged_private_data.py` clean run | Phase 4 exit |
| G8 | Engine rejects model parameters whose provenance_class is untrusted, with stable reason code | Phase 2 exit |

Cost-to-attack check: all eight gates are test-writing and a few dozen lines of validation — hours, not weeks. For a local research tool this is the entire justified spend; I explicitly do **not** gate on sandboxing, network egress controls, or red-team CTF infrastructure here.

## Questions for the Human Governor

1. **Aggregation authority:** do you accept that "robust conclusions" must be computed by the engine, even if the LLM's synthesized narrative reads better? (This is a UX-vs-integrity tradeoff only you can price.)
2. **Threat model scope:** should evidence gathered by the browser/scrape connectors be treated as attacker-controllable by default (my assumption), or do you operate in a trusted-corpus mode where pages are pre-vetted? This sets whether G8 is a must or a nice-to-have.
3. **Seed policy:** should seeds be user-visible and user-chosen (reproducibility-first, as Page's practice implies), or engine-generated and merely *recorded*? Attacker-chosen seeds allow targeted reproducibility fraud; recorded-only seeds are the safer default.
4. **Size limits:** are my proposed caps (NK n≤10, matrix ≤64, etc.) acceptable operating ranges for your actual research use, or do you need larger regimes (which would move limits from hardcoded to config-file, with the config itself outside the trust boundary)?
