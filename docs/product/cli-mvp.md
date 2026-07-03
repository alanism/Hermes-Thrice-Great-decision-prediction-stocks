# CLI MVP

The public command namespace is `capital`.

```text
capital doctor
capital validate --synthetic
capital analyze --case <path>
capital compare --case <path>
capital record --analysis <path> --authorization <path>
```

All five commands are active. `analyze` and `compare` read contained files below `local/`. `record` resolves a separate proposal through the authorization document, validates proposal and analysis hashes, and appends atomically to `local/ledger/decision-ledger.json`. Replaying an identical authorization is idempotent; a conflicting replay is rejected.
