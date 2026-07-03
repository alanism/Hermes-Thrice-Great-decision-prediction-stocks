# Agent failure log

## 2026-07-03 — Skill validator runtime mismatch

- Task: validate the `capital-research` skill.
- Failure: the generic workspace Python lacked the validator's YAML package.
- Evidence: `ModuleNotFoundError: No module named 'yaml'`.
- Resolution: run the same validator with the pinned Hermes 0.16.0 runtime; validation passed.
- Prevention: use the Hermes runtime for Hermes skill validation.
- Six-month retry: 2027-01-03.

## 2026-07-03 — Clean-checkout private-path false positive

- Task: run tests from a temporary clean clone.
- Failure: a containment assertion inspected the absolute Windows path and treated the operating-system `Local` directory as repository-private data.
- Resolution: inspect only the repository-relative fixture path.
- Prevention: containment assertions must normalize paths relative to the repository root.
- Six-month retry: 2027-01-03.
