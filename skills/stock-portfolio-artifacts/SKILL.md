---
name: stock-portfolio-artifacts
description: "Use for stock analyst artifact storage and portfolio data."
---

# Stock Portfolio Analyst Artifacts

Conventions for storing and updating `Decision > Prediction` stock analyst HTML artifacts and sourcing portfolio data — no brokerage APIs, no logins.

## When to use

- Creating or updating a stock analyst HTML artifact (GOOG-style Monocle reports).
- Any portfolio-dependent analysis where holdings/balance were NOT supplied in chat.
- Setting up the periodic Sunday refresh job or iterating tracked companies.

## Folder conventions

- Artifacts root: `/Users/alannguyen/stock portfolio analyst artifacts/`
- Portfolio source data: `/Users/alannguyen/stock portfolio analyst artifacts/portfolio screenshots and csv/`
- Tracked companies manifest: `/Users/alannguyen/stock portfolio analyst artifacts/TRACKED.md`
- Root README.md explains the layout.

## Portfolio data sourcing (no APIs, no login)

1. When Alan needs portfolio-dependent math and did not paste data: look in `portfolio screenshots and csv/`.
2. Pick the newest snapshot (modification date, then date embedded in the filename). Prefer CSV over screenshots when both exist — structured beats OCR/vision.
3. Record the source file + date. Label all values as-of that date; add the stale disclaimer: "data as of <date> from <file>; calculations may be stale".
4. Empty or ancient folder? Tell Alan — never invent holdings. If the snapshot is older than ~2 weeks and the analysis is position-sensitive, flag it prominently.
5. Screenshots may be cropped/partial — cross-check the CSV when both exist.

## Artifact creation & update (update-in-place)

- Naming: `<TICKER>_Monocle_Report.html` in the artifacts root.
- When a ticker already has an artifact: EDIT it, do not regenerate from scratch. Overwrite the old file. Do NOT archive versions unless Alan asks.
- Update the delta, preserve the structure (13 sections per `decision-prediction` skill `references/monocle-report-anatomy.md`):
  - Update: position numbers, price block, margin, Polymarket odds tables, options chains, Bayesian posterior, verdict/TL;DR if the signal changed.
  - Preserve: framework tables (Porter/Helmer/BMC), narrative sections, chart scaffolding unless the data changed.
- First-time ticker: create fresh per the Monocle anatomy.

## Deep-dive artifact (optional — 6-page McKinsey style)

- Trigger: on request for a key position or watchlist name ("deep dive NVDA from the heroes"). Not part of the routine refresh.
- Naming: `<TICKER>_DeepDive.html` in the artifacts root — its own artifact, distinct from `<TICKER>_Monocle_Report.html`.
- Lens: written from the investor-hero panel (the same 8 simulated lenses as the Monocle report hero panel) — each page framed by a hero's discipline; hero quotes are simulated commentary, labeled, never attributed statements.
- Structure (6 pages):
  1. Executive summary — the ask and the answer
  2. Business & moat — Porter / Helmer / BMC
  3. Financial engine — returns, margins, capex, FCF
  4. Market & competition — TAM, share, substitutes
  5. Risk & scenario — downside, margin of safety, Kelly sizing
  6. Decision & action — verdict, triggers, position plan
- Design: same DESIGN-*.md set (Monocle / Creative Giants / Ease Health); use the same design family as the ticker's Monocle report for visual consistency.
- Storage + update: same as Monocle reports — overwrite in place, never archive.
- Evidence: same hierarchy (measured > calculated > modeled > forecast > narrative).

## Tracked companies (TRACKED.md)

- Two sections: PORTFOLIO (owned — sync with the screenshots/csv folder) and WATCHLIST (eyeing/following, no position yet).
- Add tickers when analysis starts; remove when no longer relevant; update "last confirmed" when a snapshot confirms the holding.
- This manifest drives the periodic refresh: PORTFOLIO names get full position-aware updates; WATCHLIST names get light "still worth watching?" updates.

## Periodic refresh (planned — Sunday off-peak cron)

Outline (attach this skill + `decision-prediction` + `polymarket-macro-scan`):
1. Read TRACKED.md; read the latest portfolio snapshot in `portfolio screenshots and csv/`.
2. Pull macro priors from `~/Documents/Polymarket-Scans/<latest>/scan.md` if fresh (<14 days).
3. Current prices: browser/web quote source (e.g. stockanalysis.com/stocks/<TICKER>) or the user's screenshots — never a brokerage API. Label "measured via web quote <date>".
4. For each tracked ticker: update the artifact in place (or create if missing). Overwrite.
5. Deliver a summary: what changed, which verdicts flipped.

Cadence: Sunday off-peak (22:00 local ≈ China late-night off-peak, matching the Polymarket scan slot). Not created yet — creating it is a decision point.

## Evidence discipline

- Holdings/balance = measured as-of the screenshot/CSV date; state the date in the artifact.
- Calculations = derived from that snapshot; may be stale — always include the disclaimer line.
- Web quotes = measured as-of fetch time (record it).
- Never claim brokerage access. The folder IS the data pipeline.

## Pitfalls

- Don't re-read the portfolio folder repeatedly inside one analysis — read once, use it.
- Don't archive old artifacts by default — overwrite.
- Don't invent holdings when the folder is empty or missing.
- CSV beats screenshots; newest wins.
- TRACKED.md drives WHAT to update; the folder drives the NUMBERS.
