# Page v0.2.0 Release Receipt

Status: T30 lineage frozen; T31 verification pending
Release branch: `main`
Release version/tag: `0.2.0` / `v0.2.0`
Receipt owner: root release planner

## T30 — Release lineage freeze

- Starting commit: `916b3419f7609e721fbba2aad28f16805813d00d`
- Starting worktree: clean (`git status --porcelain` returned zero entries)
- Runtime: Python `3.11.15`; pytest `9.0.2`
- Remote: `origin` → `https://github.com/alanism/Hermes-Thrice-Great-decision-prediction-stocks.git`
- Existing tag: `v0.1.0-cli-mvp`; `v0.2.0` absent
- Model: `sol`
- Primary hero: Ryan Lopopolo
- Independent reviewers: Boris Cherny and Simon Willison

### Frozen release hashes

| Artifact | SHA-256 |
|---|---|
| `tests/methods/test_page_runner_e2e.py` | `315C6C27912D20BCD77206D103F14CEF40F191D4815B45E744DC438AE98BDB7B` |
| `tests/distribution/test_outcome_gate.py` | `B87C26E437DA16DE8818A331C005765D1C1E3C9631D0D30A8F2DA203F0A441A7` |
| `tests/mutation/test_model_thinking_mutations.py` | `EC6339C22C98A7973C9FA90233B17AB8CA8A593335B8FDE928AA492D14DB4F46` |
| `pyproject.toml` | `FF81BE7583087F58EEFF1F17AB989BAB17C427D35B404535C022CBA29006104F` |
| `requirements-dev.lock` | `BE27CC557D70E0D5C6E0FC1BDD53E3E46A2192F46989DD9F57DE809B5EBFA2B4` |
| `requirements-runtime.lock` | `5EF3B1F93A7674042C9947C8A10E2D6EF83F5FD1EB450A84B7E8367CCEEBBAF4` |

### T21 lineage correction

The historical T21 hash `F89DA72433AA1F88181CF900F9A9044A8C299FE28CA2B4A46AD8FC31FEFFBBC7` covered the original Page verifier slice. It does not describe the expanded release-boundary verifier. The current immutable release baseline is `315C6C27912D20BCD77206D103F14CEF40F191D4815B45E744DC438AE98BDB7B`. No receipt claims those hashes are identical or that the historical test remained unchanged.

### WV-PAGE-001 — Prior-RED provenance waiver

- Owner: user-authorized release governor
- Scope: test-order provenance for malformed Page input assertions added after the corresponding boundary implementation
- Explicit exclusions: no behavior waiver; no security waiver; no failing-test waiver; no test-count waiver
- Reason: prior RED evidence cannot be recreated honestly after implementation
- Compensating controls: immutable current verifier hash; source-level trust-boundary mutation; independent adversarial review; full release suite; staged-profile validation; fresh-tag smoke
- Expiry: the earlier of `2026-10-02` or the next behavior change to `plugins/capital-decision-lab/capital_decision_lab/methods/runner.py`
- Decision: accepted for v0.2.0 release provenance only

T30 result: `GREEN_VERIFIED` → `DONE`.

## T31 — Independent verifier snapshot

Pending.

## T32 — Version and documentation reconciliation

Pending.

## T33 — Release-candidate certification

Pending.

## T34 — Publication and fresh-tag smoke

Pending.
