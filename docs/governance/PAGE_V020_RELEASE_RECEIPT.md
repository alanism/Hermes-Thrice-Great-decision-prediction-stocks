# Page v0.2.0 Release Receipt

Status: RELEASED — v0.2.0
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

- Model: `luna` (explicit user override)
- Primary hero: Ryan Lopopolo
- Independent verifier: Nicholas Carlini
- Frozen-hash replay: all six recorded verifier/project/lock hashes matched
- Targeted release selection: 43 tests passed (Page runner, method pack, Committee, outcome, AST mutations, adversarial security, distribution, and staging)
- Adversarial probes: five malformed/untrusted envelopes returned deterministic `pause`, emitted the expected schema/trust flag, invoked power-law calculation zero times, and raised no exception
- Collection: 338 tests
- Full suite: 338 passed in the final serial run
- Product/test changes: none

One invalid verification attempt ran the staging tests and full repository scanner concurrently. The scanner correctly observed the staging test's temporary `dist/policy-test-profile` while it was being written and failed `test_domain_anti_leakage`. After the targeted run completed, the temporary tree was absent. The full suite was rerun serially from the same commit and passed. This is recorded as verifier orchestration error, not product evidence, and staging/scanner release commands are serial from this point forward.

T31 result: `GREEN_VERIFIED` → `DONE`.

## T32 — Version and documentation reconciliation

- Model: `luna` (explicit user override)
- Primary hero: Raphael Schaad
- Independent verifier: Ryan Lopopolo
- Distribution version changed from `0.1.0` to `0.2.0`
- Authoritative release-candidate count: 338 tests
- Historical 329 count retained only where labeled pre-hardening/historical
- Historical T21 hash retained only where labeled historical; current release baseline remains `315C6C27912D20BCD77206D103F14CEF40F191D4815B45E744DC438AE98BDB7B`
- Status normalized to `RELEASE CANDIDATE`; no document claims v0.2.0 was published

Verification: `git diff --check` clean after formatting normalization; all stale 329 references explicitly historical; no obsolete release claim remains; full 338-test suite passed; collected count 338.

T32 result: `GREEN_VERIFIED` → `DONE`.

## T33 — Release-candidate certification

- Candidate commit: `f9784b7eb768284df031371e19517baa3c48f307`
- Model: `sol`
- Primary hero: Simon Willison
- Independent verifiers: Mitchell Hashimoto and Ryan Lopopolo
- Start/end repository state: clean
- Lock/project hashes: unchanged from T30
- Targeted release tests: 43 passed
- Full suite: 338 passed; collection: 338
- Adversarial/no-egress/private-data/distribution tests: passed
- Staged profile: 207 files, version `0.2.0`
- Required staged paths missing: 0
- Forbidden staged paths/files: 0
- Private-data scan: success, zero issues
- Install-source validation: allowed, zero issues
- Staging manifest SHA-256: `77798AED40607A89F05B35799F0935CB354FF1CB1C52893485E3A77C2D660D03`
- CLI/Committee smokes: both committed synthetic thesis fixtures returned `watch`; user authorization remained required
- Temporary certification profile: removed after manifest verification

The first CLI smoke used repository `local/` as the containment root for a committed fixture outside that directory and correctly failed `PATH_ESCAPE_FORBIDDEN`. The corrected smoke used the fixture directory as the explicit containment root and passed both cases. This was a verifier invocation error, not a product failure.

T33 result: `GREEN_VERIFIED` → `DONE`; independent decision: `GO` for publication.

## T34 — Publication and fresh-tag smoke

- Model: `sol`
- Primary hero: Mitchell Hashimoto
- Independent verifiers: Ryan Lopopolo and Bret Taylor
- Release source: the commit peeled from annotated tag `v0.2.0`
- Publication method: ordinary fast-forward push of `main` plus one new annotated tag; no force, tag movement, deletion, or history rewrite
- Candidate manifest SHA-256: `77798AED40607A89F05B35799F0935CB354FF1CB1C52893485E3A77C2D660D03`
- Required post-tag proof: remote branch/tag object IDs, fresh-clone install-source validation, Page/Committee/outcome smoke, and clean local tree

The immutable tag identifies the released source. Exact release/tag objects and the remote fresh-clone proof are recorded in the post-publication receipt on `main`; that evidence commit intentionally follows the release tag and does not move it.

T34 result: `GREEN_VERIFIED` → `DONE`; v0.2.0 released.
