# Analyze Position

`capital analyze-position --case <path> --host-inputs <folder>` runs a local,
deterministic position review. The case bundle supplies the decision case, a
human-confirmed thesis, the portfolio snapshot, and any assumption-update
proposal. The host folder supplies real artifacts captured or retrieved by
Hermes Desktop.

The workflow detects each source, invokes its dedicated extractor, and stops
when extracted fields still require human confirmation. Eligible evidence is
synthesized before the existing belief, Kelly, convexity, margin, model-health,
and recommendation components run. Only an assumption proposal whose
`approval_status` is `approved` can change analysis inputs.

When confirmation-response artifacts are present in the host-input folder, the
workflow pairs them automatically. Confirmed and corrected evidence can enter
synthesis; discarded evidence is excluded; deferred evidence remains visible
and keeps the workflow paused.

The result has twelve stable report sections: portfolio, thesis, gathered
evidence, pending confirmations, provenance-grouped results, Bayesian update,
Kelly impact, convexity impact, margin safety, model health, recommendation,
and required user action. The prepared decision record remains pending. This
command neither authorizes nor writes a decision.

All input paths must resolve beneath the configured private local root.
