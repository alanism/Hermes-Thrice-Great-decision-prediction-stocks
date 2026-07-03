# Hermes Research Run

Hermes Desktop calls:

```text
capital research run --case <path> --host-inputs <folder>
```

For an orchestration case bundle, this is an alias of `capital
analyze-position`. Hermes provides capability-response documents or previously
normalized extraction bundles in the host-input folder. Supported source types
are Polymarket, X/Twitter, Reddit, portfolio tables, broker margin captures, and
manual notes.

Capability responses retain retrieval method, capture time, source reference,
content hash, confidence, and limitations. The workflow does not fetch a new
source itself and does not connect to an account or execution venue.

Older readiness-only research documents continue through the existing
readiness path so the host bridge remains backward compatible.
