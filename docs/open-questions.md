# Open Questions Log for Many-Model Thinking Extension

| Question | Context | Proposed Resolution |
|----------|---------|---------------------|
| Kelly implementation location | No `kelly.py` found in calculations; referenced in decision-prediction skill | Locate Kelly logic (may be in decision-prediction skill or elsewhere) to avoid duplication or determine if engine needs Kelly module |
| Exact CLI command pattern | How to invoke calculations from skills? (e.g., `capital research run` vs `capital run model-thinking`) | Examine existing orchestration/analyze.py or similar to determine pattern |
| DLC pack invocation mechanism | How are DLC packs invoked by the agent? | Check methods/packs.py or hosting logic to see how `dlc-thorp` etc. are called |
| Committee Mode disagreement mechanics | How is disagreement computed and reported between DLCs? | Examine method-pack-result schema and hosting logic for comparison |
| Ensemble result threshold | How many models must agree for a "robust conclusion"? | Propose: ≥2 models for small ensembles, majority for larger; human-tunable via skill reference |
| Model selection automation | How does skill decide which models to run based on thesis? | Provide reference files with clear criteria; skill does not auto-select, user specifies via `--models` flag |
| Seed disclosure convention | How are seeds reported in outputs for reproducibility? | Follow simulation.py pattern: include `seed` field in every evidence-atom output |
| Non-stdlib dependency verification | How to ensure no accidental non-stdlib dependencies creep in? | Add CI check or rely on stdlib-only audit during implementation |
| DLc-page output format | Should dlc-page output extend decision-analysis or use standalone ensemble-result schema? | Start with standalone schema; can integrate later if needed for Monocle report |
| Reference file location | Should model reference files be in skills/ or docs/? | Follow capital-research pattern: put in `skills/many-model-thinking/references/` |
| Plugin registration mechanism | Are skills auto-loaded from `skills/` directory or registered via config.yaml? | Examine distribution.yaml and plugin loading code to determine |