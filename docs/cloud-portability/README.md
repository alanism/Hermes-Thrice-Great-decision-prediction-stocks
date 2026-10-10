# Portable cloud installation (review candidate)

Decision ≥ Prediction provides educational research and hypothetical models. This is a **portable file bundle and generic-shell adapter**, used first in the selected OAI cloud workspace. It is not an installed native dot, Muse, Grok or Hermes integration. Python 3.11–3.13 and an explicitly selected persistent private directory are required. Linux/Python versions actually tested are recorded in VERIFICATION.md; other operating systems remain unverified.

## Fresh install, then relocate

From this checked-out implementation branch (or an approved release source):

```sh
python3 scripts/bootstrap_portable.py --destination /chosen/new/bundle
```

Choose an existing parent directory and a new bundle path outside this checkout. The installer uses only Python's standard library; it does not install packages, contact services, register native skills, create cron jobs or modify credentials. It refuses an existing destination, overlapping roots, missing required assets, symlink assets and upstream policy-scan failures. It preserves the existing Hermes staging allowlist unchanged and uses a separate explicit public-assets allowlist.

The returned manifest SHA-256 identifies the exact manifest. Keep that digest in an independent trusted record. All selected bytes are hashed. `source_base_commit` is the source checkout's base commit, not proof that uncommitted additions were released. A release commit must be verified separately.

Move the entire bundle to a new location if desired. From an unrelated working directory:

```sh
python3 -I /relocated/bundle/portable.py doctor
python3 -I /relocated/bundle/portable.py validate
python3 -I /relocated/bundle/portable.py analyze --fixture --file valid/mvp-case.json
python3 -I /relocated/bundle/portable.py compare --fixture --file valid/mvp-case.json
```

For authenticity as well as integrity, set `DECISION_MANIFEST_SHA256` to the installer-returned trusted digest before running. The launcher verifies all inventory hashes before importing bundle code. Without an independent pinned digest, an unsigned manifest detects accidental/tampered-file differences but cannot defeat replacement of both manifest and code. The Python interpreter, launcher invocation and local filesystem must themselves be trusted. No remote updater exists.

The whole bundle is self-contained for these offline actions: original engines, schemas, synthetic fixtures, all eight case-sensitive authored investor cards, Page, source skills and anatomy, onboarding guides, current educational policy and report template are included. Historical source instructions with Hermes-specific paths or prescriptive language are retained as source material, not automatically executed. `REPORT-POLICY.md` and this adapter's explicit paths govern the portable workflow.

## First synthetic report

Select or create a private directory using your normal host's controls first. This directory must already exist, be outside the bundle and checkout, and be an absolute path. The adapter never chooses a home directory or scans accounts.

```sh
python3 -I /relocated/bundle/portable.py demo --data-dir /chosen/private-data
```

The result is a **partial synthetic demonstration**, with a visibly fictional company, artificial assumptions and no live-provider calls. It exercises the renderer and bundled deterministic calculations, not financial-data acceptance. Eight simulated framework cards and Page, the complete anatomy checklist, nine-block BMC and Seven Powers are present. Missing real sources, generated sketchnote and browser visual review remain explicit open gates. A placeholder is never reported as an actual generated image. Read the retained report receipt and completeness sections.

A second run creates a new immutable revision. Stable report identity is `reports/workshop-cloud-synthetic/current.json`; it points to `versions/v000001/report.html` (then v000002), its exact input JSON and hash receipt. Hosts resolve this pointer to deliver the latest report. Earlier versions are retained; this does not create a decision ledger entry or human approval. No automatic publication or upload occurs.

## Explicit user-supplied inputs

`analyze`, `compare` and `import-portfolio` read only a relative file below either `--data-dir /chosen/private-data` or the bundled `--fixture` root. They reject absolute, traversal, foreign-drive and symlink paths. They do not invoke a shell or external timeout command. Inputs are size-limited; simulation work is bounded across all effective alternatives (32 alternatives maximum; 500,000 aggregate simulation steps). Report input has a separate bounded allowance for embedded PNG bytes. Financial schemas and calculation contracts remain unchanged.

```sh
python3 -I /relocated/bundle/portable.py analyze --data-dir /chosen/private-data --file cases/example.json
python3 -I /relocated/bundle/portable.py import-portfolio --data-dir /chosen/private-data --file redacted.csv
python3 -I /relocated/bundle/portable.py render --data-dir /chosen/private-data --file report-input.json --report-id example-company
```

Portfolio import is optional. The report ID must match the payload identity. Data directories inside a Git checkout are rejected to reduce accidental publication. CSV uses the original engine's required fields and capture timestamp; repeatability excludes that real import timestamp. Outputs remain Observed · unconfirmed. Verification claims inside raw imported JSON are retained as source content, not treated as a confirmation performed by this adapter. Neither schema validity nor redaction confirms the contents. The import command emits JSON to the invoking process; choose a trusted host and understand its logging/retention. The original engine has older recommendation schema names; this adapter does not expose recommendation, confirmation, record-decision, trading, brokerage or network commands.

## Host handoff and schedules

Read `host-capabilities.json`: it is a contract describing optional capabilities, not claims that these APIs exist on any named host. `doctor` distinguishes locally observed Python/file access from unimplemented browser, image, human-confirmation, delivery and scheduler capabilities. A host should map only tools actually available and authorized, keep evidence receipts and report unavailable capabilities.

`schedule-intent.example.json` is intentionally inactive. Agree exact schedule, timezone, tickers, source policy, private destination and retention before using an actually available host scheduler. Keep its confirmed setup receipt, then a separate first successful run receipt. A populated manifest does not create cron or prove recurring delivery.

## Recovery and boundaries

Writes use exclusive per-report locks, immutable version directories and an atomic current pointer. A process crash can leave `.write-lock` or an unreferenced version. Do not delete a lock while a writer is running. After checking no writer is active, inspect any pending directory and receipts, retain the last valid current pointer, and remove only the stale lock with user authorization where required. Rerun to create a new revision; do not overwrite a historical version. Filesystem durability, backups, permission enforcement and host retention are deployment responsibilities; local fsync cannot guarantee cloud-provider recovery.

No publisher endpoints, telemetry, API keys, paid calls or account discovery are implemented. This is a narrow code-level observation about this adapter, not a platform-wide noncollection guarantee. Private data must stay out of the bundle, repository, public reports and support messages.

## Resume this implementation

`tasks.json` is the canonical fixed ten-task board; `KANBAN.html` is its offline view. A task counts Done only with evidence, and independent review/publication are separate gates. Use `scripts/update_cloud_kanban.py` in the source checkout to update both. On resumption, read tasks, inspect git status, rerun affected checks, and verify remote refs before any authorized push. Do not inherit historical test counts. Keep review and publication open until their receipts exist.

### Publication checkpoint — 10 October 2026

Independent review passed the bounded synthetic/offline draft scope, including a separate rerun of all 37 tests, exact file-hash verification and report/image receipt checks. No critical, high or medium finding remained.

The remote branch `feat/oai-dot-portable-cloud-2026-10-10` was created at `c04f68eac43a1dd3f96b7b2bfe716d221f4f9915`. The subsequent tree-creation operation was explicitly cancelled before an implementation commit or pull request was created. The remote branch therefore still contains only the onboarding base, not this implementation. Publication is blocked pending fresh retry approval. Do not automatically repeat the cancelled operation.

On authorized resumption, first verify the branch still points to the expected base and that no implementation commit or PR appeared. Reconcile any changed remote state before writing. Use the refreshed reviewed file-hash manifest, create the implementation commit through the authenticated publication flow, open a stacked **draft** PR against `docs/platform-onboarding-2026-10-09`, and verify its remote commit and PR state. No merge or deployment is included. Full upstream pytest regression remains separately blocked on dependency-installation approval; browser and native-host acceptance remain open.
