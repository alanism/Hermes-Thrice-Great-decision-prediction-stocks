# Confirmation Pairing

`capital confirmation apply --queue <path> --responses <folder>` creates an
auditable pairing artifact. Matching uses this strict order:

1. exact request ID
2. source extraction ID
3. source artifact hash

Multiple matches are rejected as ambiguous. A response carrying a source hash
that differs from its request is rejected as stale. Pairing records retain the
match method, action, source identities, unresolved requests, and discarded
extractions.

Analyze-position performs the same pairing automatically for response files in
its host-input folder. It promotes confirmed or corrected bundles, excludes
discarded bundles, and pauses while any deferred or unanswered request remains.
