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
4. Preserve URL or artifact provenance, retrieval method and time, raw hash, confidence, status, and limitations.
5. Require confirmation for screenshot-derived values.
6. Run `capital research loop --case <path>` and resolve each returned block.
7. Synthesize evidence and apply only thesis-specific sensitivity rules.
8. Produce a bounded belief update and a pending assumption proposal.
9. Apply only approved updates to analysis.
10. Recalculate Kelly, convexity, margin safety, and model health.
11. Produce a model-implied recommendation. Let margin danger override Kelly.
12. Record only after a separate hash-bound human authorization.

Return `blocked_source_unavailable` when no connector succeeds. Ask the user when required facts or thesis-channel weights remain missing.

Never invent financial facts, claim certainty or account access, silently alter assumptions, or report transaction execution.
