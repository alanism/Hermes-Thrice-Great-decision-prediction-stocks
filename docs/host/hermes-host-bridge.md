# Hermes Host Bridge

Hermes Desktop is the capability host. Capital Decision Lab is the local reasoning engine. The host may provide browser pages, URL responses, selected text, screenshots, OCR, authenticated-session responses, local file choices, clipboard text, and user confirmations.

The bridge separates five contracts: capability request, capability response, local source artifact, source-specific extraction result, and human confirmation. A generic response is provenance-complete but cannot update beliefs until a source adapter emits an extraction result.

Runtime artifacts and extracted records belong under local user storage. They must not enter Git or distribution staging.
