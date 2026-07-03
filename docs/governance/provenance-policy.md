# Provenance policy

Every decision-content value emitted beneath an output `data` object must contain `value` and exactly one `provenance_class`:

- `measured`
- `assumed`
- `calculated`
- `modeled`
- `decided`
- `unavailable`

Protocol metadata such as contract versions, identifiers, references, and canonical hashes is not decision content.

