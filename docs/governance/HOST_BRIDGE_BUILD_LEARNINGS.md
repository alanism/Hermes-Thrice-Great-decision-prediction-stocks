# Host bridge build learnings

## Phase 1 — Host contract boundary (2026-07-04)

- RED evidence: 4 expected failures; every new document returned `CONTRACT_VERSION_UNKNOWN`.
- GREEN evidence: 4 tests passed after adding five allowlisted schemas.
- What went well: separate request, response, artifact, extraction, and confirmation identities prevented raw host payloads from being mistaken for verified evidence.
- What did not: the first schema draft exposed that artifact and request references need distinct shapes.
- Mitigation: keep reference objects contract-specific and validate canonical hashes at ingestion boundaries.
- Six-month retry: 2027-01-04.

## Phase 2 — Source-specific extraction (2026-07-04)

- RED evidence: collection failed because the host adapter package did not exist.
- GREEN evidence: 5 initial tests passed across Polymarket, X/Twitter, Reddit, portfolio, margin, manual-note, and correction flows.
- What went well: one shared extraction envelope kept retrieval provenance consistent while source adapters produced their existing domain contracts.
- What did not: normalized destination contracts differ materially; event snapshots, social batches, portfolios, and margin fields cannot share one document writer.
- Mitigation: share verification and references, keep field mapping source-specific, and require screenshots or confidence below 0.70 to enter confirmation.
- Six-month retry: 2027-01-04.

## Phase 3 — Host bridge CLI and readiness (2026-07-04)

- RED evidence: collection failed because no host bridge module or command tree existed.
- GREEN evidence: 4 tests passed for capabilities, ingest, extraction, confirmation, research-run readiness, and actionable failure prompts.
- What went well: generic responses retain provenance while remaining ineligible until a source adapter emits a validated extraction contract.
- What did not: command labels initially reused the older `research loop` name for `research run` output.
- Mitigation: derive command identity from the parsed action and test through the public CLI boundary.
- Six-month retry: 2027-01-04.

## Phase 4 — Host evidence recommendation gate (2026-07-04)

- RED evidence: 4 failures showed that recommendations ignored host extraction status, contradiction, and source-specific reason fields.
- GREEN evidence: 16 recommendation tests passed after adding host eligibility, contradiction downgrade, and five reason atoms.
- What went well: the existing margin override remained higher priority than evidence or Kelly changes.
- What did not: a provenance-complete host response was previously indistinguishable from source-extracted evidence at the recommendation boundary.
- Mitigation: inspect validated extraction contracts; unconfirmed screenshots force `pause`, and high contradiction forces `watch` unless a stronger safety block applies.
- Six-month retry: 2027-01-04.

## Phase 5 — Governance and distribution (2026-07-04)

- RED evidence: 1 of 192 full-suite tests failed because the exact schema manifest did not yet include the five host contracts. A separate field-confidence probe failed because only aggregate confidence was considered.
- GREEN evidence: 193 tests passed; staging succeeded with 171 files; the Hermes skill validator passed.
- What went well: existing containment and boundary scanners accepted the host bridge without weakening private-data or execution protections.
- What did not: schema-valid artifact metadata alone did not prove the local file hash, and low-confidence individual fields could initially bypass confirmation.
- Mitigation: validate contained artifact bytes against SHA-256 and use the minimum supplied field confidence in verification status.
- Six-month retry: 2027-01-04.
