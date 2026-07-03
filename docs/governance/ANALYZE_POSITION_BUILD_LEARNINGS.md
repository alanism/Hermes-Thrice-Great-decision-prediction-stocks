# Analyze Position Build Learnings

## Phase 1 — Workflow contract

- Went well: a single orchestrator could reuse the shipped extraction,
  synthesis, analysis, health, and recommendation components.
- Failure observed: the first RED run failed at import because the orchestrator
  intentionally did not exist.
- Mitigation: tests fixed blocker precedence and the twelve-section report
  before production code was introduced.

## Phase 2 — Engine integration

- Went well: confirmation eligibility provided one gate for every source.
- Failure observed: a nominally approved proposal without a proposed assumption
  was invalid, and the stock-focused Kelly input needed its paired loss
  probability updated with win probability.
- Mitigation: tests use complete proposals; approved probability changes update
  the paired value atomically, while pending proposals remain inert.
- Failure observed: extractor direction fields use `direction_candidate`, not a
  derived direction.
- Mitigation: routing tests now exercise the actual host contract field.

## Phase 3 — CLI and containment

- Went well: both command forms share one implementation and path validation.
- Failure observed: the alias correctly failed its RED test as an unknown CLI
  action.
- Mitigation: alias equivalence and out-of-root rejection are permanent tests.

## Six-month retry note

Re-test whether host-provided confirmations can be paired automatically in one
folder without weakening hash binding. It remains deferred because the current
slice accepts confirmed bundles and must not invent confirmation intent.
