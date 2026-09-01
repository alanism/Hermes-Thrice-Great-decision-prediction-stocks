# Codebase Audit Report for Hermes-Thrice-Great Decision Prediction Stocks

## Overview
This report documents the existing structure, conventions, and patterns of the Hermes-Thrice-Great decision-prediction-stocks repository as of the audit date. It serves as the foundation for planning the Many-Model Thinking extension.

## Repository Layout
```
.
├── .env.EXAMPLE
├── .gitignore
├── config.yaml
├── design/
│   ├── DESIGN-Creative Giants.md
│   ├── DESIGN-Ease Health.md
│   └── DESIGN-Monocle.md
├── distribution.yaml
├── dlc (core)
├── dlc-camillo
├── dlc-Galloway
├── dlc-Gerstner
├── dlc-laffont
├── dlc-mauboussin
├── dlc-munger-buffett
├── dlc-shkreli
├── dlc-thorp
├── docs/
│   ├── architecture/
│   ├── connectors/
│   ├── evidence/
│   ├── finance-math/
│   ├── governance/
│   ├── host/
│   ├── method-packs/
│   ├── product/
│   ├── safety-boundaries/
│   └── workflows/
├── fixtures/
├── local/
├── plugins/
│   └── capital-decision-lab/
├── pyproject.toml
├── README.md
├── requirements-dev.lock
├── requirements-runtime.lock
├── schemas/
├── scripts/
├── skills/
│   ├── capital-research/
│   ├── decision-prediction/
│   ├── polymarket-macro-scan/
│   └── stock-portfolio-artifacts/
├── SOUL.md
├── START_HERE.md
└── tests/
```

## Detailed File Analysis

### 1. README.md & START_HERE.md
- **Purpose**: Onboarding and operational guide.
- **Patterns**: 
  - Clear separation of concerns: "The agent talks. The tool calculates."
  - Evidence layer tagging (Measured, Calculated, Modeled, Forecast).
  - DLC investor hero packs as selectable research lenses.
  - Committee Mode for explicit disagreement.
- **Integration Constraints**: 
  - New capabilities must honor the deterministic engine contract.
  - All math must remain in fixed Python (stdlib only).
  - Real data stays under `local/` (gitignored).

### 2. SOUL.md
- **Purpose**: Agent behavior/persona definition.
- **Content**: 
  - Operate as a self-directed capital research assistant.
  - Preserve source provenance.
  - Treat evidence classes as distinct.
  - Never invent financial facts or claim certainty.
  - Require explicit hash-bound human authorization before recommendations become decision records.
- **Integration Constraints**: 
  - Many-Model Thinking must align with these behavioral tenets.
  - Outputs must preserve evidence-layer tagging.

### 3. config.yaml & distribution.yaml
- **config.yaml**: 
  - Minimal runtime configuration (agent disabled_toolsets, platform_toolsets, plugins, mcp_servers).
  - Plugins array currently empty; skills are likely auto-loaded from `skills/` directory.
- **distribution.yaml**: 
  - Defines distribution-owned files: SOUL.md, config.yaml, .env.EXAMPLE, skills, schemas, fixtures/valid, plugins/capital-decision-lab.
  - Indicates what gets packaged with the Hermes profile.

### 4. skills/capital-research/SKILL.md
- **Purpose**: Guide user from portfolio/thesis through evidence gathering to authorization-gated local record.
- **Frontmatter Format**: 
  ```yaml
  ---
  name: capital-research
  description: Guide a user from portfolio and thesis through evidence gathering, Bayesian updates, Kelly sizing, convexity, margin safety, model health, a model-implied recommendation, and an authorization-gated local record. Use for stock exposure research, portfolio review, source investigation, or recommendation workflows in Capital Decision Lab.
  ---
  ```
- **Workflow Steps** (numbered 1-13):
  1. Validate/import portfolio with `capital portfolio`.
  2. Structure thesis as pending assumptions.
  3. Gather evidence via connectors (prefer API > browser > scrape > screenshot > paste > file import > manual entry).
  4. Use `capital host ingest` then `capital host extract`.
  5. Use `capital host confirm` for screenshots/OCR/low-confidence.
  6. Preserve provenance (URL, method, time, raw hash, confidence, status, limitations).
  7. Run `capital research run --case <path> --host-inputs <folder>`.
  8. Synthesize evidence and apply thesis-specific sensitivity rules.
  9. Produce bounded belief update and pending assumption proposal.
  10. Apply only approved updates.
  11. Recalculate Kelly, convexity, margin safety, model health.
  12. Produce model-implied recommendation (margin danger overrides Kelly).
  13. Record after separate hash-bound human authorization.
- **Patterns**: 
  - Clear separation between agent-led steps (1-6, 8-9) and engine-led steps (7, 11-12).
  - Authorization-gated recording.
  - Evidence provenance preservation.
- **Integration Constraints for Many-Model Thinking**:
  - New skill must follow same frontmatter format.
  - Must integrate with existing host commands (`capital host ingest/extract/confirm`).
  - Must produce evidence-atoms with proper provenance_class.
  - Must call `capital research run` or equivalent to trigger engine.
  - Output must be compatible with existing decision-analysis schema.

### 5. skills/decision-prediction/SKILL.md
- **Purpose**: Decision > Prediction stock analysis (single ticker/portfolio) with Thorpe evidence discipline and token metrology.
- **Key Sections**:
  - Evidence hierarchy non-negotiable (measured > calculated > modeled > forecast > narrative > unknown).
  - Never invent financial facts; invalid domains → `unavailable` with reason.
  - Kelly is a reference, not instruction; margin danger overrides Kelly.
  - Only `user_verified` evidence updates Bayesian beliefs; cap max change per update.
- **Workflow** (single stock):
  1. Capture & preserve provenance (screenshots, portfolio, Polymarket/X, options chain; require user confirmation for screenshot-derived values).
  2. Metrology first (token_meter) to ground image bytes before LLM call.
  3. Cache architecture (byte-exact prefix: SYSTEM, FILINGS, FINANCE-MATH, DLC prompt, DYNAMIC).
  4. Engines to run (from capital-decision-lab docs): Formula spec, Kelly, Convexity, Margin, Simulation.
  5. Bayesian discipline (prior odds, likelihood ratio, posterior; source quality scales weight).
  6. Image & cost optimization (prefer 3 images or stitched composite; downscale to 720p).
  7. Reporting (Monocle artifact anatomy; required sections when engines run).
  8. Verification & logging (ls -lh, wc -l, update token cost analysis, log to usage_log.csv).
- **Patterns**: 
  - Token metrology and prompt caching critical for cost control.
  - Strict ordering of cache prefixes (byte-exact).
  - Engines produce labeled atoms; DLC voices rendered as stylized simulated commentary.
- **Integration Constraints**:
  - Many-Model Thinking skill must output evidence-atoms consumable by this skill's reporting section.
  - Must follow cache architecture if adding new dynamic content.
  - Must label outputs with appropriate evidence layer (likely Modeled or Forecast depending on determinism).

### 6. skills/polymarket-macro-scan/SKILL.md & skills/stock-portfolio-artifacts/SKILL.md
- **Purpose**: 
  - Polymarket macro scan: biweekly scan of Polymarket categories.
  - Stock portfolio artifacts: manage local artifact storage and generation.
- **Patterns**: 
  - Both define CLI commands and workflows for automated tasks.
  - Stock portfolio artifacts skill creates `~/stock portfolio analyst artifacts/` folder and handles screenshot/CSV imports.
- **Integration Constraints**: 
  - Many-Model Thinking should not interfere with existing cron jobs or artifact workflows.
  - May want to add new artifact sections for model-thinking outputs.

### 7. plugins/capital-decision-lab/
- **Structure**: 
  - Modular Python package with clear separation of concerns:
    - `calculations/`: allocation, convexity, margin, returns, risk, simulation (all stdlib-only deterministic math).
    - `connectors/`: various data source connectors (filings, local file, manual input, polymarket, reddit, screenshot, web, x_twitter) + registry.
    - `contracts/`: authorization, canonical, ledger, validation.
    - `evidence/`: bayesian, common, event_market, proposals, sensitivity, social, synthesis, validation.
    - `host/`: artifacts, bridge, confirmation, confirmation_queue, extractors (broker_margin, common, manual_note, polymarket, portfolio_table, reddit, x_twitter), miniloops.
    - `methods/`: packs, runner.
    - `orchestration/`: analyze, compare, record, research_run.
    - `privacy/`: containment, scanner.
    - `recommendation/`: engine, health, records.
    - `reporting/`: comparison.
    - `research/`: loop, portfolio, thesis.
- **Key Files Examined**:
  - `plugins/capital-decision-lab/plugin.yaml`: defines plugin name, version, description, kind: standalone.
  - `plugins/capital-decision-lab/capital_decision_lab/orchestration/analyze.py`: entry point for analysis orchestration (exists per file listing, though earlier read failed; likely present).
  - Calculation files (convexity.py, margin.py, etc.) show deterministic Python implementations using only standard library.
  - Evidence layer handling: seen in `evidence/` modules where atoms are constructed with provenance_class.
- **Patterns**:
  - All math in `calculations/` is deterministic, standard-library only, seeded where appropriate (simulation.py).
  - Engine outputs are evidence-atoms with `provenance_class` set to `calculated` or `modeled` or `forecast`.
  - Host orchestrates flow: research → ingest/extract → evidence synthesis → calculations → recommendation → recording.
  - Plugins are registered via `plugin.yaml` and loaded by Hermes agent.
- **Integration Constraints for Many-Model Thinking Engine**:
  - New models must live under `plugins/capital-decision-lab/capital_decision_lab/calculations/` or a new subpackage (e.g., `model_thinking/`).
  - Must be deterministic, standard-library only, accept `--seed` argument, and record seed in output.
  - Must output evidence-atoms with proper `provenance_class` (likely `modeled` for simulations, `forecast` for implications).
  - Must integrate with host orchestrator (likely via `methods/packs.py` or similar).
  - Must not change existing lock files (requirements-*.lock).
  - Must reuse existing Kelly/convexity/margin math where applicable (e.g., for position sizing within new models).

### 8. DLC Packs (dlc, dlc-camillo, etc.)
- **Format**: 
  - Each DLC is a markdown file with YAML frontmatter (`--- name: ... description: ... ---`) followed by structured content.
  - Examples: `dlc-thorp` contains Ed Thorp's investment methodology workflow, Kelly criterion implementation, portfolio construction, etc.
  - DLCs define an investor's analytical style, prompts, and connection to the engine.
  - Committee Mode runs multiple DLCs and states disagreement explicitly.
- **Patterns**:
  - Frontmatter metadata includes `name` and `description`.
  - Content includes workflow mermaid diagrams, step-by-step sections, quantitative references.
  - DLCs are referenced by name in skills (e.g., decision-prediction skill lists DLC voices).
- **Integration Constraints for `dlc-page`**:
  - New DLC must follow same frontmatter format.
  - Must define Scott Page's Many-Model Thinking lens: refusal of single-model answers, distributional assumption checks, ensemble execution, disagreement reporting.
  - Must be compatible with Committee Mode (i.e., output must be consumable by disagreement comparison logic).
  - Should reference the new model-thinking engine for computations.

### 9. schemas/
- **Format**: JSON Schema (draft 2020-12) defining contracts for evidence, assumptions, decisions, etc.
- **Key Schemas**:
  - `decision-analysis.v1.schema.json`: top-level analysis contract with `evidence_atom` definitions.
  - `evidence-item.v1.schema.json`: defines `provenance_class` enum (measured, assumed, calculated, modeled, forecast, decided, unavailable).
  - `method-pack.v1.schema.json`, `method-pack-result.v1.schema.json`: likely for DLC packs.
  - Many others for bayesian updates, confirmation pairing, event market signals, etc.
- **Patterns**:
  - Strict typing, no additionalProperties, required fields.
  - Evidence atoms contain `value` (any), `provenance_class`, optional `unit`, `input_refs`, `formula_ref`, `limitations`, `reason`.
  - `canonical_hash` (SHA-256) used for immutability and provenance.
- **Integration Constraints**:
  - Many-Model Thinking outputs must conform to `evidence-item.v1.schema.json`.
  - New schemas may be needed for ensemble results (robust conclusions, condition-dependent conclusions, explicit disagreements) but should follow same patterns.
  - If extending decision-analysis schema, must maintain backward compatibility.

### 10. fixtures/
- **Structure**:
  - `fixtures/valid/`: synthetic test data for valid cases (evidence, contracts, guided research, portfolios, etc.).
  - `fixtures/adversarial/`: test data for error conditions and edge cases.
- **Patterns**:
  - Fixtures are JSON files matching the relevant schemas.
  - Used in unit tests to verify contract compliance and engine behavior.
- **Integration Constraints**:
  - Many-Model Thinking must have synthetic fixtures for testing.
  - Fixtures must be committed; real data never committed (stays in `local/`).

### 11. tests/
- **Structure**: Mirroring source code layout (unit tests for formulas, connectors, contracts, evidence, hosting, methods, mutation, orchestration, recommendation, research, simulation).
- **Patterns**:
  - Uses pytest (likely) based on test file naming and imports.
  - Determinism tests: seeded simulations produce same output given same seed.
  - Contract validation tests: ensure outputs adhere to schemas.
- **Integration Constraints**:
  - New unit tests required for model-thinking engine.
  - Must follow existing test patterns (e.g., `tests/formulas/test_*.py`).
  - Must verify determinism and seed handling.

### 12. scripts/
- **Contents**: 
  - `build_profile_staging.py`, `check_staged_private_data.py`.
- **Patterns**:
  - Setup/utility scripts for Hermes profile management.
  - Likely invoked during installation or CI.
- **Integration Constraints**:
  - Many-Model Thinking may require updates to these scripts if new dependencies or config steps are added (but per C1, no stdlib-only engine should not need new dependencies).

### 13. local/
- **Purpose**: Local-only runtime data (real portfolio data, evidence, decision records) — gitignored.
- **Patterns**:
  - `local/README.md` likely explains usage.
  - Ensures security model: data never leaves user's machine without explicit authorization.
- **Integration Constraints**:
  - Many-Model Thinking must respect this boundary; no real data leakage into committed fixtures or code.

### 14. design/
- **Contents**: DESIGN-*.md style references (Monocle, Creative Giants, Ease Health) for artifact styling.
- **Patterns**:
  - CSS variable definitions for colors, fonts, borders.
  - Used by skills to generate HTML artifacts.
- **Integration Constraints**:
  - Many-Model Thinking artifact sections should use existing design system or extend it following same patterns.

## Convention Summary

### Skill Conventions
- **Frontmatter**: YAML block with `name:` and `description:`.
- **Workflow**: Numbered steps, clear separation of agent vs engine responsibilities.
- **Commands**: Use `capital <verb>` CLI pattern (e.g., `capital portfolio`, `capital host ingest`, `capital research run`).
- **Evidence Handling**: Preserve provenance (URL, method, time, raw hash, confidence, status, limitations).
- **Authorization**: Separate hash-bound human authorization before recording decisions.
- **Output**: Compatible with decision-analysis schema; evidence-atoms labeled with provenance_class.

### Engine Conventions
- **Location**: `plugins/capital-decision-lab/capital_decision_lab/calculations/`.
- **Determinism**: Python standard library only; seeded simulations record seed.
- **Output**: Evidence-atoms with `provenance_class` set appropriately (`calculated`, `modeled`, `forecast`).
- **Reuse**: Extend existing math (Kelly, convexity, margin) rather than duplicate.
- **Dependency Policy**: No changes to lock files; no non-stdlib dependencies for deterministic engine.

### DLC Pack Conventions
- **Frontmatter**: YAML with `name:` and `description:`.
- **Content**: Workflow description, step-by-step methodology, quantitative references.
- **Committee Mode**: Outputs must be comparable for explicit disagreement reporting.
- **Integration**: Referenced by name in skills; agent invokes DLC prompts.

### Schema Conventions
- **Format**: JSON Schema draft 2020-12.
- **Evidence Atom**: `provenance_class` enum, `input_refs`, `formula_ref`, `limitations`, `reason`.
- **Immutability**: `canonical_hash` (SHA-256) for change detection.
- **Extension**: Follow same patterns; maintain backward compatibility.

### Test Conventions
- **Fixtures**: Synthetic JSON matching schemas, stored under `fixtures/valid/` or `fixtures/adversarial/`.
- **Determinism Tests**: Verify same seed → same output.
- **Contract Tests**: Validate output against schemas.

## Reusable Components Identified
- **Kelly Criterion Logic**: Already present in skills/decision-prediction (referenced) and likely in engine (though no kelly.py file found; may be embedded elsewhere). Should verify if engine has Kelly implementation; if not, may need to add or reference existing.
- **Convexity Scoring**: `plugins/capital-decision-lab/capital_decision_lab/calculations/convexity.py` — can be extended for new concavity/convexity models.
- **Margin Safety**: `plugins/capital-decision-lab/capital_decision_lab/calculations/margin.py`.
- **Simulation Framework**: `plugins/capital-decision-lab/capital_decision_lab/calculations/simulation.py` — provides seeded Monte Carlo baseline; new models (Markov, SIR, etc.) can follow similar pattern.
- **Evidence Atom Construction**: `plugins/capital-decision-lab/capital_decision_lab/evidence/` modules.
- **Host Orchestration**: `plugins/capital-decision-lab/capital_decision_lab/orchestration/` — analyze.py, research_run.py likely coordinate workflow.
- **CLI Command Pattern**: Defined in `plugins/capital-decision-lab/plugin/commands.py` (not examined but inferred).
- **Cache Architecture**: Byte-exact prefix ordering critical for prompt caching (from decision-prediction skill).
- **Design System**: DESIGN-*.md files for artifact styling.

## Risks & Unknowns from Preliminary Review
- **Kelly Implementation Location**: No `kelly.py` file found in calculations; Kelly logic may be in `decision-prediction` skill or elsewhere. Need to locate to avoid duplication.
- **Engine Entry Point**: Exact mechanism for invoking calculations from skills (e.g., `capital research run`) needs confirmation.
- **DLC Pack Invocation**: How DLC prompts are integrated with engine (likely via `methods/packs.py`).
- **Committee Mode Mechanics**: How disagreement is computed and reported; needed for dlc-page design.
- **Schema for Ensemble Results**: No existing schema for many-model outputs; must design new schema or extend existing ones.
- **Seed Disclosure Convention**: How seeds are reported in outputs; need to verify existing simulation seed handling.
- **Non-Stdlib Dependency Ban**: Must ensure all new model code uses only Python standard library.

## Conclusion
The codebase follows clear, consistent conventions for skills, deterministic engine, DLC packs, and schemas. The Many-Model Thinking extension can be integrated by adhering to these patterns, particularly:
- Creating a new skill under `skills/many-model-thinking/` with proper frontmatter and workflow.
- Adding deterministic models under `plugins/capital-decision-lab/capital_decision_lab/calculations/model_thinking/` (or similar).
- Defining a new DLC pack `dlc-page` following existing DLC format.
- Creating new schemas for ensemble results under `schemas/`.
- Adding synthetic fixtures and unit tests.
- Ensuring all math remains standard-library only and deterministic.
- Reusing existing Kelly/convexity/margin logic where applicable.
- Preserving evidence-layer tagging and provenance requirements.
- Maintaining compatibility with Committee Mode and existing artifact reporting.

Next steps: produce build plan, open questions log, and risk register based on this audit.