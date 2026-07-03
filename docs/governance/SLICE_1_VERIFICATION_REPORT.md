# Slice 1 Verification Report

Status: **PASS — recorded before Slice 2 implementation and before first commit**

Repository: `C:\Users\alani\OneDrive\Documents\Aria-EdTech\Hermes-Projects\capital-decision-lab`

## 1. Git status summary

The repository is initialized on `main` and has no commits. All intended source files are untracked (`??`); no files are staged. Generated `.venv/` and `dist/` content is ignored and absent from `git status`.

## 2. Full Slice 1 source tree

This tree excludes `.git/`, `.venv/`, generated `dist/`, and this report itself.

```text
capital-decision-lab/
├── .env.EXAMPLE
├── .gitignore
├── LICENSE
├── README.md
├── SOUL.md
├── config.yaml
├── distribution.yaml
├── pyproject.toml
├── requirements-dev.lock
├── requirements-runtime.lock
├── docs/
│   ├── architecture/
│   │   ├── contract-flow.md
│   │   └── system-boundary.md
│   ├── finance-math/
│   │   ├── formula-specification.md
│   │   └── simulation-method.md
│   ├── governance/
│   │   ├── provenance-policy.md
│   │   └── tdd-policy.md
│   ├── product/
│   │   └── cli-mvp.md
│   └── safety-boundaries/
│       ├── comparison-only-policy.md
│       ├── no-model-created-facts.md
│       └── private-data-policy.md
├── fixtures/
│   ├── adversarial/
│   │   ├── authorization-mismatch.json
│   │   ├── domain-leak.json
│   │   ├── insufficient-inputs.json
│   │   ├── invalid-probabilities.json
│   │   └── path-escape.json
│   ├── mutation/
│   │   └── formula-mutations.json
│   └── valid/
│       ├── alternative-comparison.json
│       ├── authorized-decision.json
│       ├── seeded-simulation.json
│       └── single-alternative.json
├── local/
│   └── README.md
├── plugins/
│   └── capital-decision-lab/
│       ├── __init__.py
│       ├── plugin.yaml
│       └── capital_decision_lab/
│           ├── __init__.py
│           ├── calculations/
│           │   ├── __init__.py
│           │   ├── allocation.py
│           │   ├── returns.py
│           │   ├── risk.py
│           │   └── simulation.py
│           ├── contracts/
│           │   ├── __init__.py
│           │   ├── authorization.py
│           │   ├── canonical.py
│           │   ├── ledger.py
│           │   └── validation.py
│           ├── orchestration/
│           │   ├── __init__.py
│           │   ├── analyze.py
│           │   ├── compare.py
│           │   └── record.py
│           ├── plugin/
│           │   ├── __init__.py
│           │   └── commands.py
│           ├── privacy/
│           │   ├── __init__.py
│           │   ├── containment.py
│           │   └── scanner.py
│           └── reporting/
│               ├── __init__.py
│               └── comparison.py
├── schemas/
│   ├── assumption-register.v1.schema.json
│   ├── decision-analysis.v1.schema.json
│   ├── decision-authorization.v1.schema.json
│   ├── decision-case.v1.schema.json
│   ├── decision-comparison.v1.schema.json
│   ├── decision-ledger.v1.schema.json
│   └── decision-proposal.v1.schema.json
├── scripts/
│   ├── build_profile_staging.py
│   └── check_staged_private_data.py
├── skills/
│   └── README.md
└── tests/
    ├── contracts/
    │   ├── test_analysis_contract.py
    │   ├── test_case_contract.py
    │   ├── test_ledger_contract.py
    │   └── test_proposal_authorization_separation.py
    ├── distribution/
    │   ├── forbidden_vocabulary.json
    │   ├── test_advice_language.py
    │   ├── test_cli.py
    │   ├── test_domain_anti_leakage.py
    │   ├── test_private_data_exclusion.py
    │   └── test_staging_payload.py
    ├── formulas/
    │   ├── test_allocation.py
    │   ├── test_returns.py
    │   └── test_risk.py
    ├── mutation/
    │   ├── test_formula_mutations.py
    │   └── test_policy_mutations.py
    └── simulation/
        └── test_seeded_monte_carlo.py
```

## 3. Exact passing test command

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

## 4. Passing test summary

```text
...........................                                              [100%]
```

Result: **27 passed**, exit code `0`.

## 5. Initial RED evidence

After provisioning the isolated pinned dev environment, the initial policy command was:

```powershell
.\.venv\Scripts\python.exe -m pytest tests\distribution\test_staging_payload.py tests\distribution\test_private_data_exclusion.py tests\distribution\test_domain_anti_leakage.py tests\distribution\test_advice_language.py -q
```

It produced **10 expected failures**:

1. `test_staging_is_deny_by_default` — staging builder absent.
2. `test_repository_root_is_not_an_install_payload` — staging builder absent.
3. `test_local_path_is_rejected_by_scanner` — runtime scanner absent.
4. `test_private_sentinel_never_enters_staging` — staging builder absent.
5. `test_only_local_readme_is_trackable` — ignore policy absent.
6. `test_domain_terms_and_references_are_detected` — runtime scanner absent.
7. `test_marked_adversarial_fixture_proves_detection` — hostile fixture absent.
8. `test_valid_scopes_are_clear_and_policy_definitions_are_exempt` — runtime scanner absent.
9. `test_advice_and_execution_language_is_detected` — runtime scanner absent.
10. `test_conservative_comparison_language_is_allowed` — runtime scanner absent.

These failures were replaced by the minimum containment, scanner, staging, and doctor behavior. Later edge tests also captured RED for approved `dist/` generation, exemption placement, path-reference scanning, and Hermes CLI registration before their fixes.

## 6. `local/` verification

`local/` contains only tracked-intended `README.md`. `.gitignore` ignores `local/*` and explicitly re-allows only `local/README.md`. Private sentinel files created by tests are removed in `finally` blocks.

## 7. Generated `dist/` verification

`dist/` is ignored by `.gitignore`. `git check-ignore` reports the `dist/` rule for the generated payload. Current generated content is:

```text
dist/
├── hermes-thrice-great-nhi-profile/
└── hermes-thrice-great-nhi-profile.manifest.json
```

The payload and hash inventory are generated artifacts, not source authority. Private-data and domain/advice scans returned no issues.

## 8. Source-repository isolation

`git status --short` and `git diff --stat` in the existing education-focused repository both returned no output. No file there was modified, moved, renamed, imported, or vendored.

## 9. Deferred behavior verification

- Calculation and simulation modules contain only deferral docstrings.
- Formula and simulation test modules contain only explicit deferred-slice markers.
- Proposal and authorization exist only as separate schema boundaries; no creation or transition behavior exists.
- The ledger module contains no append or write implementation.
- Analysis, comparison, and record orchestration modules contain no executable behavior.
- Deferred CLI commands return `CLI_FEATURE_DEFERRED` without side effects.

## 10. Runtime dependency verification

`pyproject.toml` declares `dependencies = []`; `requirements-runtime.lock` states that v1 uses the Python standard library only. Runtime import roots are standard-library modules plus package-relative modules:

```text
__future__, argparse, collections, importlib, json, os, pathlib, re, sys
```

`setuptools==79.0.1` is pinned as a build backend, not a runtime dependency. Pinned pytest packages exist only in the dev lock.

## 11. `capital doctor` output

```json
{"command":"capital doctor","distribution_id":"hermes-thrice-great-nhi","expected_hermes_version":"0.16.0","installed_hermes_version":"0.16.0","issues":[],"model_calls":0,"network_attempts":0,"profile":"nhi","status":"ok"}
```

## 12. Known limitations and deferred work

- Contract schemas are structural placeholders pending Slice 2 validation rules.
- No general contract loader, schema validator, evidence-atom validator, or canonical contract hash API exists.
- No finance formulas or seeded simulation execution exists.
- No analysis, comparison, proposal creation, authorization creation, or ledger-write workflow exists.
- `validate`, `analyze`, `compare`, and `record` remain deferred CLI surfaces.
- No live data, external services, cloud synchronization, telemetry, or transaction execution exists.
- The repository has not yet been committed or installed as a Hermes profile.

