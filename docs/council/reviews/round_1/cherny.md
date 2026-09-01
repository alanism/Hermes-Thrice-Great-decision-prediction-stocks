# Council Round 1 — Blind Adversarial Review
## [C] Boris Cherny — Type-Driven Orchestrator

**Operating question:** "How would this work if I gave the agent maximum autonomy, a high-level goal, and a deterministic verifier to iterate against?"

**Verdict up front:** The plan treats the implementing agent as a junior who must be told every function signature, while simultaneously withholding the three facts the agent cannot possibly invent (the real CLI surface, the real method-pack mechanism, the real ensemble aggregator). It micromanages the easy parts and under-specifies the hard parts — the exact inversion of what produces good agentic outcomes. I verified the repo directly: the plan's largest "open questions" are answerable in five minutes of reading, and every one of them left open becomes a hallucination opportunity for an autonomous executor.

---

## Key Risks

**R1. Open questions are fake unknowns — the repo already answers them. (Highest severity.)**
I checked the actual code:
- `plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py:138` — the CLI is argparse with `capital method run --pack <id> --case <path>` and `capital method committee --packs <list> --case <path>`. The plan invents `capital model-thinking run` and "capital method run --name page" — neither exists and the real flag is `--pack`, not `--name`.
- `methods/packs.py` — method packs are a **declarative Python dict** (`PACKS`), not markdown files. `dlc-thorp`-style markdown files are agent-facing voice prompts; the *engine-side* pack is a dict entry with `calculation_modules: ["kelly", ...]` consumed by `methods/runner.py`.
- `methods/runner.py:21-87` — `run_method_pack` dispatches on **hard-coded `elif pack_id ==` branches**. Adding a "page" pack means editing this function. The plan never names `runner.py` or `commands.py` as artifacts to touch.
- Kelly is located: `calculations/allocation.py:41` (`kelly`, `fractional_kelly`, `allocation.kelly.v1` formula_ref). The open question "Kelly implementation location" is already resolved and the review packet even says so — yet the plan text still lists it as open.

*Binary gate G1:* Every open question in §8.3 is replaced by a repo-cited answer with file:line, or is explicitly marked `HUMAN_DECISION` with a default. Pass condition: zero questions of the form "check X to see how Y works" remain; every question is either answered with a citation or answered with a chosen default.

**R2. The skill will be written against an interface that does not exist.**
Artifact 17 hard-codes `capital model-thinking run --models <list> --seed <int>` in the skill workflow — but there is no registered subcommand for it anywhere in `commands.py`. An autonomous agent that writes the skill in Phase 2 and the CLI glue (unspecified) in Phase 2-or-3 will either (a) iterate against a failing command with no spec for how to fix it, or (b) quietly rename things and drift from the plan. *Binary gate G2:* Before any SKILL.md is written, a `capital model-thinking run`-equivalent subcommand exists in `commands.py` with a passing test in `tests/cli/`, and the SKILL.md text quotes exactly the implemented invocation string. Verifier: `python -m ... commands.py` dry-run returns status ok, plus a grep that the SKILL.md command string equals the registered parser string.

**R3. Phase 2/3 gates are vibes, not verifiers.**
"All new calculation modules import and pass unit tests" is deterministic — good. But "Many-Model Thinking skill loads without error in Hermes agent," "dlc-page loads correctly in Hermes agent," "Committee Mode can run multiple DLCs including page" have **no command attached**. An agent cannot iterate against "loads without error." Each needs a scripted check: frontmatter parse, distribution.yaml membership, `capital method run --pack page --case <fixture>` returning status 0, and `capital method committee --packs page thorp --case <fixture>` returning a valid `committee_result.v1` document. *Binary gate G3:* every phase-gate line is either a shell command with expected exit code, or deleted.

**R4. Committee Mode compatibility is undefined against the actual comparison semantics.**
`runner.py:run_committee` compares the string value of `model_implied_recommendation` against a fixed priority list `["avoid margin", "pause", "trim to fractional Kelly", "watch", "hold current exposure", "increase exposure under this assumption set"]`. If dlc-page emits a novel recommendation string ("run ensemble, disagreement is high"), it falls out of the priority list and synthesis silently degrades to `recommendations[0]` — an arbitrary, undocumented result. This is the classic interface-boundary failure: the plan says "compatible with Committee Mode" without defining the contract (allowed recommendation vocabulary, or a schema change to committee-result). *Binary gate G4:* There exists a test `tests/methods/test_committee_page.py` running `run_committee(["page","thorp","mauboussin"], fixture)` asserting `agreement`/`disagreement` fields are computed and `hermes_synthesis` ∈ the documented priority vocabulary. Either the page pack emits within the vocabulary or the vocabulary extension is specified.

**R5. No artifact produces an ensemble result.**
The schema `ensemble-result.v1.schema.json` (Artifact 19) defines robust/condition-dependent/disagreement conclusions — but **no calculation module is specified to build it**. Nothing computes "≥ N models agree," nothing correlates models (grounding item 8 says flag correlated models — no artifact does that), nothing maps 8 model outputs into the schema. The schema will be validated only as "valid JSON Schema," i.e., a dead document. *Binary gate G5:* A new artifact `calculations/model_thinking/ensemble.py` with `build_ensemble_result(model_outputs: list[dict], threshold: int) -> ensemble-result dict` plus a round-trip test `test_ensemble.py` that (1) runs ≥2 models on a fixture, (2) builds the result, (3) validates it against the schema with a jsonschema-free stdlib validator or the repo's existing contract-validation pattern. Phase 2 gate passes only if that test passes.

**R6. Fixture expected-values depend on an undecided algorithm — the verifier is not yet deterministic.**
Artifact 3 leaves "MLE vs regression on log-log" open; Artifact 2 leaves convergence tolerance semantics open. These choices change the *bytes* of the output, so `fixtures/valid/model_thinking/power_law_fixed.json` cannot be authored until the choice is fixed — meaning the Phase 1 closed-loop target (fixture diff / known-case assertion) does not exist at planning time. A Cherny-style agent needs its target materialized before coding. *Binary gate G6:* For each of the 8 models, the plan names the exact algorithm (e.g., "Clauset MLE with x_min scan", "power iteration with row-stochastic start vector = uniform") and one golden-value test with a hand-computed expected number. Pass condition: the golden test exists and fails-red/passes-green deterministically.

**R7. Internal contradiction: seed discipline.**
Artifact 13 (Blotto) says "no seed needed" and tags `calculated`, while Phase 1-2 boilerplate says "Every output records the seed (even if None)." Fine if intentional — but then the determinism test for Blotto must assert *absence* of the seed field or `seed: null`, and the plan doesn't say which. Similarly Markov power iteration has no randomness, so a `seed` param there is a lie in the interface. Small thing, but every interface lie multiplies for 8 parallel agents. *Binary gate G7:* A one-row table in the plan: model → deterministic-without-seed | seeded-stochastic | hybrid — and the seed field contract for each. Grep-able.

**R8. Regressions checked only at Phase 4.**
The full existing suite is not a gate until Artifact 28. An agent that breaks `analyze.py` in Phase 2 won't discover it for two phases. Cheap fix: every phase gate includes "existing test suite green" — it's one command. *Binary gate G8:* Each phase's gate list contains "full `pytest` run: 0 failures, count unchanged-or-grown," verified per phase, not at the end.

**R9. No stdlib-only mechanical verifier despite being a named risk.**
Risk register says "CI check if possible." This is trivially mechanical: enumerate imports in new modules, assert subset of stdlib. Undecided verifiers breed "trust me" audits. *Binary gate G9:* A committed script `scripts/check_stdlib_only.py` that fails (exit 1) on any non-stdlib import under `calculations/model_thinking/`; phase 2 gate includes running it.

---

## Architecture Critique

**Effort is inverted relative to risk.** The plan spends 300+ words specifying `__init__.py`, Euler step size, and tolerance=1e-10 on modules an agent will nail in one pass with a good test file — that is micromanagement, and per my operating experience it knocks the model off-distribution for zero gain. Meanwhile the genuinely hard integration points — `runner.py` dispatch, `commands.py` subcommand registration, `methods/packs.py` PACKS entry shape, `committee-result` vocabulary, the ensemble aggregator — get zero lines. *Binary gate G10:* Every artifact that edits an existing shared file (`runner.py`, `commands.py`, `packs.py`, `decision-prediction/SKILL.md`, `config.yaml`, `distribution.yaml`, `SOUL.md`) carries a diff-shaped spec (which function/section, what contract change) — currently zero of seven do.

**Artifact 22 conflates two different things.** The repo has (a) markdown DLC voice files at repo root (`dlc-thorp` etc., agent-facing prompt persona) and (b) engine-side method packs (`PACKS` dict, deterministic). `dlc-page` per the audit is a voice file; per Phase 3's gate ("output conforms to ensemble-result schema") it must also be an engine pack. Pick one, name both artifacts if both are needed: `dlc-page/` voice file + `PACKS["page"]` entry + `runner.py` branch. *Binary gate G11:* Artifact 22 is split into 22a (voice DLC file, frontmatter spec) and 22b (PACKS entry + runner branch, dict-shaped spec with required_inputs / calculation_modules enumerated), each with its own verifier.

**Phase ordering is mostly right but two inversions exist.** (1) SKILL.md (Artifact 17) depends on a CLI that the plan schedules for "Phase 2 or 3" — inside the same phase as the skill itself, unresolvable. (2) The schema (Artifact 19) precedes the aggregator that produces its instances (which doesn't exist at all — R5). *Binary gate G12:* Dependency graph amended: CLI subcommand → SKILL.md; ensemble.py → schema fixture validation.

**Parallelization is left on the table.** The eight model modules are embarrassingly parallel (independent files, independent tests, independent fixtures); the plan sequences them as one blob. With worktrees + a claimable task list, Phase 1+2 core math is a 8-agent map-reduce. The plan gives no per-task claim convention (PROJECT_TASKS.md-style) and no collision surface analysis. *Binary gate G13:* Each of the 8 model tasks is stated as a self-contained claimable unit with its own gate (module + test + fixture + golden value), no shared-file edits, so two agents can run concurrently with zero merge conflicts.

**Nothing feeds agent-learned corrections back into shared memory.** This repo's analog of CLAUDE.md is SOUL.md + audit-report conventions. During an autonomous build, corrections ("packs are dicts not markdown", "the flag is --pack") should be appended to the audit report so a *second* agent doesn't re-hallucinate. *Binary gate G14:* Plan adds a standing instruction: every discovered convention correction during implementation is appended to `docs/audit-report.md` §Convention Summary with file:line citation in the same commit.

---

## Missing Specifications

- **M1 (R2/G2):** the actual CLI subcommand shape: subparser names, required args, JSON output envelope (must match `_base()` pattern in commands.py:305-316 with status/issues semantics — exit 0 ok, 3 blocked, 2 failed).
- **M2 (R4/G4):** Committee vocabulary contract for dlc-page: which of the six fixed recommendation strings the page pack may emit, or an explicit extension of `runner.py`'s priority list with tests.
- **M3 (R5/G5):** `ensemble.py` aggregator: input shape (list of model-output dicts), threshold semantics (from open question — default: ≥2 of N, floor 2, ceiling 5-7 per grounding item 8), correlation flagging rule, output key mapping to schema properties.
- **M4 (R1):** PACKS["page"] full dict shape: display_name, required_inputs, preferred_sources, workflow_steps, mini_loop_rules, calculation_modules (exact module names e.g. `["markov","power_law","sir",...]` — note existing entries use short names, so the runner's calculation_modules names must be mapped; the mapping function is unspecified today), rubric_dimensions, recommendation_modifiers, limitations.
- **M5 (R6/G6):** exact algorithms per model (Markov start vector + stopping rule; power-law method + x_min policy; SIR difference-equation discretization per grounding item 3 — note the plan's Euler choice contradicts the NotebookLM grounding that says "discrete-time difference equations"; Schelling relocation order; bandit variant set — grounding says greedy/sample-then-greedy/adaptive-ε, but plan Artifact 16 says UCB1/Thompson: **contradiction with grounding, resolve it**).
- **M6:** fixture file contract: is each fixture an *input case + expected output* or an evidence-atom instance? Currently ambiguous ("matching evidence-item schema" — but model outputs are dicts of atoms, not a single atom). Gate: one sentence per fixture stating its JSON shape and which test consumes it.
- **M7:** `distribution.yaml` membership: new files must be added to distribution-owned list (audit §3 says distribution.yaml enumerates skills, schemas, fixtures, plugins — the plan's Artifact 24 only mentions config.yaml). Gate: distribution.yaml diff enumerated per new path.
- **M8:** executor configuration: per my rule 8, the plan should state the implementing agent runs on the most capable model at maximum effort, and that scaffolding added "for today's model" carries an unshipping note (rule 10). Gate: one line in the plan header.

---

## Recommended Task Gate Updates

Reorder and gate per phase (every gate is a command with exit-code semantics):

1. **Phase 0.5 (new): Interface Grounding.** Replace §8.3 open questions with cited answers (G1). Artifacts: none; deliverable is an amended plan + audit-report addendum. This phase must complete before any code.
2. **Phase 1 (models 1-3 + tests + fixtures):** add G6 (golden-value tests), G7 (seed contract table), G8 (existing suite green), G9 (stdlib check script runs clean). Drop per-function micromanagement specs (tolerance values, step sizes) into the test files' assertions — let the agent choose implementation details as long as the golden values hold.
3. **Phase 2 split:**
   - **2a (parallel, worktree-claimable):** 5 remaining models + tests + fixtures, each an isolated task (G13).
   - **2b (serial, shared-file):** `commands.py` subcommand (G2 verifier: CLI test green) → `ensemble.py` + round-trip schema test (G5) → schema file → PACKS["page"] + runner branch (G11b). Each 2b step leaves a verifiable state: a green named test.
4. **Phase 3:** SKILL.md + references written only against the *implemented* command string (grep-verify, G2); voice DLC + committee test (G4); decision-prediction SKILL.md diff enumerated line-by-line.
5. **Phase 4:** registration diff per M7; final gate = full pytest + stdlib script + committee CLI on a fixture + deterministic rerun check (run one model twice, assert byte-identical canonical_hash). Add a standing G14 memory-append rule.

---

## Questions for the Human Governor

1. **Q1 (R1):** May the implementing agent resolve open questions by reading the repo itself (my preference — Q&A before code), or must the plan be pre-resolved by a human? Binary: plan-amendment phase exists vs. questions left open.
2. **Q2 (R5):** Is an ensemble aggregator (a deterministic module that fuses model outputs into robust/condition-dependent/disagreement conclusions) in scope? The PRD's ensemble-result schema implies it, but no artifact builds it. Binary: add `ensemble.py` artifact or descope the schema.
3. **Q3 (R4):** Should dlc-page's recommendation vocabulary extend the existing six-string Committee priority list, or emit within it? This is a design decision with schema ripple. Binary: extend list (amend runner + tests) vs. constrain to existing vocabulary.
4. **Q4 (M5):** Grounding doc says bandit variants are greedy / sample-then-greedy / adaptive-ε; the plan says UCB1/Thompson. Which wins — Page's NotebookLM grounding or the plan author's choice? Binary: one of the two, named in the plan.
5. **Q5 (R8):** Are you willing to accept per-phase full-suite runs as gates (adds ~minutes per phase) in exchange for catching regressions immediately? Binary: per-phase suite gate on/off.
6. **Q6 (M7):** Confirm `distribution.yaml` edits are authorized — the plan currently doesn't list the file, but audit says it governs what ships with the profile. Binary: distribution.yaml is an editable artifact or read-only constraint.

---

*Reviewed blind per packet; all file:line claims verified against the working tree at C:\Users\alani\Hermes-Thrice-Great-decision-prediction-stocks on review date. Security boundaries deferred to Carlini; product value deferred to Taylor.*
