# Risk Register for Many-Model Thinking Extension

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Repo conventions differ from assumptions in this PRD (e.g., SKILL.md format) | Low | High | Audit phase gates the plan; plan must follow observed conventions, not this PRD's guesses |
| Seeded multi-trial outputs complicate the "same inputs → same output" brand | Medium | Medium | Plan must define seed-disclosure + cross-seed-variance-as-Forecast convention |
| Overlap between new concavity/convexity model and existing convexity scoring | Low | Medium | Audit must map the overlap; plan specifies extend-vs-reuse |
| Standard-library-only math limits fidelity (e.g., power-law fitting) | Medium | Low | Plan documents approximations and their determinism/accuracy tradeoffs |
| Committee Mode integration complexity | Low | High | Audit must verify how DLC packs are invoked before designing dlc-page |
| Deterministic engine accidentally gains non-stdlib dependency | Low | High | All new model code explicitly restricted to stdlib; consider adding CI check if possible |
| Skill/engine version drift (skill expects engine functions that don't exist) | Low | Medium | Implement engine first, then skill; add integration tests |
| Output schema conflicts with existing decision-analysis | Low | Medium | Design ensemble-result schema to be complementary, not conflicting; test integration with Monocle report |
| User confusion between Many-Model Thinking and existing DLCs | Low | Low | Clear documentation and naming; dlc-page has distinct purpose (ensemble vs single lens) |
| Performance issues with NK landscape (2^n complexity) | Low | Low | Limit n to feasible size (e.g., n≤10) in documentation and reference files; note computational limits |
| Determinism broken by implicit ordering (e.g., dict iteration pre-Python 3.7) | Low | Medium | Use sorted() or OrderedDict where order matters; document Python version requirement |
| Seed handling inconsistency (some models use seed, others don't) | Low | Low | Enforce seed parameter in all model functions; record seed even if None |
| Evidence layer mislabeling (e.g., calling stochastic output "calculated") | Low | Medium | Follow established pattern: deterministic math = "calculated", simulations = "modeled", forecasts = "forecast" |
| Provenance chain broken in ensemble synthesis | Low | High | Ensemble-result schema must preserve input_refs and canonical_hash from model outputs |
| CLI command conflicts with existing capital commands | Low | Medium | Choose verb-noun pattern that doesn't clash (e.g., `capital model-thinking run` is likely safe) |
| Reference file proliferation causing skill bloat | Low | Low | Keep reference files concise; consider consolidating if too many |
| DLC pack output not consumable by Committee Mode | Low | High | Examine existing DLC output format before designing dlc-page; ensure compatibility |
| Unit tests fail due to non-determinism in test environment | Low | Medium | Control random seeds in tests; isolate stdlib randomness |
| Fixtures become outdated as implementation evolves | Low | Low | Treat fixtures as living documents; update when implementation changes |
| Documentation lags behind implementation | Low | Medium | Update docs as part of each phase's acceptance criteria |
| Performance regression in existing engine due to new imports | Low | Low | Lazy import models only when needed; benchmark if concerned |
| License incompatibility with new code | Low | High | Ensure all new code follows same Fair Source license as existing repo |
| User expects financial advice from model outputs | Low | High | Clear disclaimers in skill and DLC that outputs are model-implied under assumptions, not advice |
| Margin danger override logic not extended to new models | Low | Medium | Ensure skill workflow includes margin check after model-thinking engine, before recommendation |