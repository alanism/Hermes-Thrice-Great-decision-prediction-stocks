# Provenance policy

Every decision-content value emitted beneath an output `data` object must contain `value` and exactly one `provenance_class`:

- `measured`
- `assumed`
- `calculated`
- `modeled`
- `forecast`
- `decided`
- `unavailable`

Protocol metadata such as contract versions, identifiers, references, and canonical hashes is not decision content.

`forecast` is a forward-looking estimate under supplied assumptions, verified evidence, and explicit model rules. It is not a guarantee.
