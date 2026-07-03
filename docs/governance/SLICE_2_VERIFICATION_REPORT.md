# Slice 2 Verification Report

Status: **PASS — Contract Validation and Provenance Atoms**

## RED evidence

The focused contract command initially produced `13 failed, 7 passed`. Exact details are recorded in `SLICE_2_RED_REPORT.md`.

## Implemented boundary

- Seven version-allowlisted schemas load from the local profile using the Python standard library.
- A deterministic schema subset validates types, required properties, constants, enums, patterns, arrays, additional properties, local references, and conditional branches used by the contracts.
- Decision analysis and comparison content requires evidence atoms.
- Evidence atoms require `value` and one allowed `provenance_class`; optional metadata includes `unit`, `input_refs`, `formula_ref`, and `limitations`.
- Unavailable atoms require a nonempty reason and a null value.
- Canonical JSON uses sorted keys, compact separators, UTF-8 text, and non-finite-number rejection.
- SHA-256 hashes are stable across object-key order and change with semantic values.
- Proposal and authorization remain separate schemas. Authorization requires proposal and analysis hash references.

## GREEN evidence

Focused command:

```powershell
.\.venv\Scripts\python.exe -m pytest tests\contracts -q
```

Focused result: `20 passed` before final acceptance additions.

Complete command:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Complete result: `44 passed`.

The generated profile was rebuilt. All seven staged valid contract fixtures passed validation using the staged package and staged schemas. Private-data and domain/advice scans returned no issues. `capital doctor` continued to report exact Hermes compatibility at `0.16.0`.

## Preserved exclusions

No finance formulas, simulation execution, comparison orchestration, proposal creation, authorization creation, ledger append, live data, external integration, or shared package exists. Runtime dependencies remain empty and implementation imports remain standard-library-only.

