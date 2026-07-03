---
name: capital-research
description: Guide a user from portfolio and thesis through evidence gathering, Bayesian updates, Kelly sizing, convexity, margin safety, model health, a model-implied recommendation, and an authorization-gated local record. Use for stock exposure research, portfolio review, source investigation, or recommendation workflows in Capital Decision Lab.
---

# Capital Research

Start by requesting the current portfolio snapshot, thesis, intended action, constraints, and available evidence.

Use this sequence:

1. Validate or import the portfolio with `capital portfolio`.
2. Structure the thesis as pending assumptions; never supply missing probabilities, prices, payoffs, or balances.
3. Gather evidence with available connectors. Prefer configured API, browser, scrape, screenshot, paste, file import, then manual entry.
4. Use `capital host ingest` for Hermes capability responses, then require `capital host extract` before analysis.
5. Use `capital host confirm` for screenshots, OCR, or low-confidence fields.
6. Preserve URL or artifact provenance, retrieval method and time, raw hash, confidence, status, and limitations.
7. Run `capital research run --case <path> --host-inputs <folder>` and resolve each returned block.
8. Synthesize evidence and apply only thesis-specific sensitivity rules.
9. Produce a bounded belief update and a pending assumption proposal.
10. Apply only approved updates to analysis.
11. Recalculate Kelly, convexity, margin safety, and model health.
12. Produce a model-implied recommendation. Let margin danger override Kelly.
13. Record only after a separate hash-bound human authorization.

Return `blocked_source_unavailable` when no connector succeeds. Ask the user when required facts or thesis-channel weights remain missing.

Never invent financial facts, claim certainty or account access, silently alter assumptions, or report transaction execution.
