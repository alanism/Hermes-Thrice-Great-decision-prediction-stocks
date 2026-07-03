# Confirmation Queue

`capital confirmation queue --case <path> --host-inputs <folder>` inspects
source-specific extraction bundles and emits one request for every unverified
extraction. Each request carries the extraction identity, source type, source
artifact hash, extracted fields, field confidence values, reason, allowed
actions, and creation time.

Hermes should present each request as: “I need confirmation before using this
evidence. Confirm, edit, discard, or defer?” Responses remain private runtime
artifacts in `local/` or another contained private path.

Confirm and correct resolve a request. Discard resolves it while excluding the
evidence. Defer keeps the request pending and blocks the recommendation.
