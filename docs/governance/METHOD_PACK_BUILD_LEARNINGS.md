# Method Pack Build Learnings

## Phase 1 — Boundary

- Went well: the existing analysis document is a sufficient shared substrate.
- Failure observed: the RED suite failed at the absent method package, proving
  no hidden implementation already satisfied the contract.
- Mitigation: packs are overlays and contain no duplicated finance formulas.

## Phase 2 — Pack behavior

- Went well: provenance atoms represent every method-specific result.
- Failure observed: process methods can disagree without a mathematically valid
  way to average their actions.
- Mitigation: committee synthesis selects the most conservative binding
  constraint and preserves every original pack result.

## Phase 3 — Interface

- Went well: standalone and analyze-position commands share one pack runner.
- Mitigation: unknown packs fail explicitly, Core remains the default, and all
  outputs remain pending user authorization.

## Six-month retry note

Re-test richer reverse-valuation and filing rubrics only when their required
inputs can be supplied without model-created facts or new runtime dependencies.
