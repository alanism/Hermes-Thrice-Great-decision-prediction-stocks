# Council Synthesis — Verified & Conformed into the Build Plan

Status: the three-round adversarial council review (6 personas × 3 rounds) is COMPLETE. Canonical merged register: `docs/council/risk_review.md` (32 merged risks MR-01..MR-32, 24 blocking, 8 minority-preserved). This file records the revisions applied to `docs/build-plan.md` as a result.

## Applied revisions (supersede prior plan text where they conflict)

### R-A. Schema citation correction (MR-01) — replaces Artifact 19's conformance clause
- Ensemble atoms conform to **`$defs.atom` in `bayesian-update.v1.schema.json` / `decision-analysis.v1.schema.json`** — NOT `evidence-item.v1.schema.json`.
- Provenance enum extended with **`input_trust_class`** (Carlini R-B): schema data, not prompt wording.
- Gate: jsonschema.validate on fixture atoms; no `evidence-item.v1` reference remains.

### R-B. Ensemble compiler (MR-05) — replaces Artifact 19's "designed to work with"
- New Artifact: `model_thinking/ensemble.py: aggregate(results, threshold)` — deterministic compiler over typed Ensemble IR; `aggregated_by: "engine"` required field; threshold = human-owned named constant with golden-file drift test; LLM may draft conclusion prose only after the numeric core exists.
- `correlated_models` required field (MR-30); ≥2-distinct-families router rule.
- Free-text `condition`/`point_of_contention` fields: schema `maxLength` + enum/pattern bounds (MR-13).

### R-C. Seed contract (MR-03)
- Stochastic entrypoints: **keyword-only `seed: int` required** (None → `unavailable_result`); deterministic modules take NO seed parameter; one RNG-draw-order table per stochastic model.
- Gate: AST lint fails on `seed=None`; hostile typed seeds rejected; two-process same-seed replay byte-compares.

### R-D. Red/Green + mutation (MR-02, MR-15)
- Every new test authored before its module; committed RED log predates module commit; ≥1 mutant killed per test class; full `pytest` green + count-unchanged-or-grown is a precondition of EVERY phase transition.

### R-E. Phase 0 interface grounding (MR-04) — replaces "Open Questions" phase-0 posture
- All repo-probeable items resolved NOW: Kelly = `allocation.py:41`; CLI registry = `plugin/commands.py`; real invocation = `capital method run --pack`; packs = PACKS dict in `methods/packs.py`.
- Artifact 17's `capital model-thinking run` hallucinated subcommand is DELETED; skill references only registry-verified commands.
- Remaining open questions are HUMAN_DECISIONs (see risk_review.md Governor table).

### R-F. Grounding contradictions resolved (MR-08) — grounded corrections now mandatory
- Markov: all four Page convergence conditions implemented as rejections; matrix convention stated in docstring AND tested with transposed fixture.
- SIR: discrete difference equations (grounding), per-step conservation/non-negativity assertion; SIR honesty policy per Governor Decision 16.
- Polya: multi-trial signature (spread is the deliverable).
- Bandits: greedy / sample-then-greedy / adaptive-ε (grounding), `betavariate` named for Thompson.
- Blotto: scope decided per Governor Decision 17 (pairwise vs enumeration).
- Grounding doc wins conflicts unless governor overrides in writing (Decision 7).

### R-G. Money-path gates (MR-12, MR-14, MR-16, MR-17)
- Engine rejects parameters with provenance_class ∈ {unknown, narrative, unavailable} → `unavailable_result("UNTRUSTED_PARAMETER_SOURCE")` (MR-12).
- `power_law_check` emits machine-readable veto (`mean_variance_defined: false`); orchestration test proves Kelly/Sharpe suppressed on that flag (MR-14).
- Egress scanner test over `calculations/` — zero socket/urllib/http/requests (MR-16, Willison minority).
- Injection-refusal e2e test — injected evidence never reaches privileged computation; output byte-identical with/without (MR-17, Willison minority).

### R-H. Scope cut pending governor decision (MR-18, MR-20)
- Customer-outcome PRD (user/job/metric baselined at 0) required before Phase 1; 2-thesis human validation run before Phase 2; zero verdict-delta ⇒ build stops and re-plans to the power-law gate alone (Taylor G2 branch — hard stop, not council-waivable).
- Model count is Governor Decision 4 (≤4 decision-relevant recommended; model count becomes a named constant, never router prose).

### R-I. Phase gate order (supersedes plan's per-phase acceptance gates)
- Phase 0 grounding (MR-04 blocks all authoring) → Phase 1 exit (MR-01,02,03,06,07,11,12,14,15,16,17,22,26,27) → Phase 2 exit (MR-05,08,10,13,19,20,21,23,29,30,31,32) → Phase 3 precondition (MR-09 mechanizable-or-cut, MR-28 no-compute-steps) → Phase 4 (MR-24 wired private-data script + re-checks).

### R-J. Standards & hygiene
- `check_stdlib_only.py` committed; planted-import red run (MR-22).
- Shared reason-code enum for all `unavailable_result` codes (MR-26).
- Seed + aggregation threshold fixed defaults or human-supplied, recorded in ledger — never agent-chosen (MR-27).
- CPython version pin + one shared canonical JSON serializer + stated rounding policy (MR-11).
- `distribution.yaml` must register every new path (MR-23).
- `scripts/check_staged_private_data.py` wired into Phase 4 validation command (MR-24).
- Audit report grows with `file:line` corrections during the build (MR-25).
- Perf budget: ensemble run ≤5s at default caps (MR-31).
- Grounding-claims fixtures: 75/25 equilibrium, Diversity identity, V≥1−1/R0 bit-exact (MR-29); non-computable router claims need primary-source citations.

### R-K. Waiver protocol (adopted from Willison Q-W7)
- Recorded waiver = governor initials + one sentence accepted risk in the ledger. Silent skipping = phase failure. MR-16/MR-17 waivable only under explicit trusted-corpus ruling (Decisions 8/9).

## Human Governor Decisions required before Phase 1
See `docs/council/risk_review.md` § Human Governor Decisions (19 items). Highest-leverage: #1 ensemble compiler scope, #4 model-count scope cut, #8 lethal-trifecta ruling, #15 PRD/2-thesis gate. Decisions 4 and 15 can re-plan the build entirely.
