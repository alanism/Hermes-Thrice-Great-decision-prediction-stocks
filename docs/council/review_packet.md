# Review Packet: Many-Model Thinking Extension — Build Plan

## Problem & JTBD
The Hermes-Thrice-Great repo (`alanism/Hermes-Thrice-Great-decision-prediction-stocks`) is a deterministic capital-decision engine (Kelly sizing, convexity, margin safety, all stdlib Python) fronted by a Hermes agent. The user wants to add **Many-Model Thinking** (Scott Page's ensemble-of-formal-models method): a deterministic model engine (Markov, SIR/Bass, Schelling, Blotto, Polya, power-law, NK, bandits), a router skill, an ensemble-result schema, a `dlc-page` lens pack, Committee Mode integration, and registration/docs — WITHOUT building yet. The deliverable is a build plan document that a reviewer could execute.

## Key constraints (from PRD)
- C1: deterministic engine = Python stdlib only; no lock-file changes
- C2: no harness/fork changes; agent-facing behavior via skills/ files
- C3: real data stays under local/ (gitignored); only synthetic fixtures committed
- C4: every engine number reproducible from (inputs + seed) alone
- C5: no financial advice / no trading / no silent action
- C6: new capabilities respect existing decision-record authorization flow

## Grounding
Math grounded via NotebookLM "Scott E Page" notebook queries (7 rounds) — documented in `docs/grounding-scott-page-notebooklm.md`. Notable grounded facts: Markov needs all four convergence conditions (finite, fixed, ergodic, non-cyclic); power-law α≤2 ⇒ mean/variance undefined ⇒ Kelly/Sharpe invalid; SIR/Bass as discrete difference equations; ensemble sweet spot 5–7 models; Diversity Prediction Theorem (error = avg error − diversity).

## The plan under review (docs/build-plan.md, summary)
- Phase 0 (done): audit report; conventions extracted from actual repo files.
- Phase 1: `calculations/model_thinking/` with markov.py, power_law.py, sir.py + tests + fixtures.
- Phase 2: bass.py, schelling.py, blotto.py, polya.py, nk.py, bandits.py + tests/fixtures; `skills/many-model-thinking/` router skill + 8 reference files; `schemas/ensemble-result.v1.schema.json`.
- Phase 3: `dlc-page` pack; Committee Mode integration; decision-prediction SKILL.md updated.
- Phase 4: registration (config.yaml / distribution.yaml), docs/method-packs writeup, SOUL.md line, final validation.
- Each artifact has: target path, interface spec, dependencies, acceptance criteria, evidence-layer handling, S/M/L estimate, open questions.
- Full text: `docs/build-plan.md` (33KB). Audit: `docs/audit-report.md`. Open questions: `docs/open-questions.md`. Risk register: `docs/risk-register.md`.

## Known open questions (from plan, may be incomplete)
- Kelly logic location (found in allocation.py — plan needs to update)
- Exact CLI invocation pattern for engine
- DLC pack invocation mechanism
- Committee Mode disagreement mechanics
- Ensemble robust-conclusion threshold
- Plugin registration mechanism

## Evidence-layer conventions observed
- provenance_class enum: measured, assumed, calculated, modeled, forecast, decided, unavailable
- deterministic math → "calculated"; simulations → "modeled"; forward-looking → "forecast"
- canonical_hash (SHA-256) for immutability

## Task for reviewers
Blind adversarial review per your persona card. Categories: Core Risks, Hidden Assumptions, Failure Modes, Security Gaps, Test Gaps. Output sections: Key Risks / Architecture Critique / Missing Specifications / Recommended Task Gate Updates / Questions for the Human Governor.
