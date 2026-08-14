# START HERE — Hermes Thrice Great · Decision > Prediction

The operational guide for the investment-reasoning system: a Hermes agent that applies Edward Thorp-style evidence discipline to a concentrated barbell portfolio (AI · defense · minerals & energy · fintech).

The system **never connects to your brokerage**. Portfolio data comes from screenshots/CSVs you drop into a folder — that is the whole security model. Data stays on your machine; the analyst reads it the way a human would.

## The loop

```mermaid
flowchart TB
    subgraph CAPTURE["Capture — recurring cadence"]
        PM["Polymarket macro scan<br/>every other Sat 22:00 local · China off-peak<br/>9 category pages → screenshots + Gamma API"]
        XS["X / Twitter sentiment<br/>biweekly · active once xurl is installed"]
        PS["Portfolio snapshot<br/>you drop screenshots / CSV exports<br/>portfolio screenshots and csv/ · no API, no login"]
    end

    PM --> KB[("Macro KB<br/>~/Documents/Polymarket-Scans/&lt;date&gt;/scan.md")]
    XS --> KB
    PS --> PD[("Portfolio state<br/>holdings · balance · as-of date")]

    KB -->|Bayesian priors| DP
    PD -->|position data| DP
    TM[("TRACKED.md<br/>owned + watchlist")] -->|scope| DP

    subgraph DP["Decision > Prediction — muse-spark-1.2-contributor"]
        EV["Evidence hierarchy<br/>measured → calculated → modeled → forecast → narrative"]
        EN["Engines<br/>Kelly · Sharpe/Sortino · convexity · margin · Monte Carlo"]
        V["Verdict<br/>Buy / Hold / Trim / Add / Sell"]
        HERO["Investor hero panel<br/>8 lenses · thesis stress-test<br/>Galloway · Gerstner · Camillo · Laffont ·<br/>Mauboussin · Munger/Buffett · Shkreli · Thorp"]
    end

    EV --> EN --> V
    V --> HERO

    DP --> ART[("Monocle report<br/>~/stock portfolio analyst artifacts/&lt;TICKER&gt;_Monocle_Report.html<br/>updated in place")]
    HERO --> DD[("Deep dive (optional)<br/>&lt;TICKER&gt;_DeepDive.html<br/>6-page McKinsey style · hero lens")]
    ART --> YOU["You read the verdict"]
    DD --> YOU
    YOU -->|new trades change holdings| PS
    YOU -->|macro heats up → trigger on demand| PM
    YOU -->|request deep dive on a key name| HERO
```

Three capture rhythms feed one analysis core, which produces two artifact types, and your decisions close the loop.

## What YOU do manually

1. **Drop portfolio snapshots** into `stock portfolio analyst artifacts/portfolio screenshots and csv/` — screenshots (Robinhood, Fidelity, etc.) and/or CSV exports. Newest wins; CSV beats screenshots. Everything is labeled as-of the snapshot date — data may be stale; that is expected and disclosed.
2. **Confirm values when asked** — a value only becomes `measured` after you verify it.
3. **(Optional) X sentiment:** install `xurl` and complete OAuth (`xurl auth oauth2`) outside the agent. Until then the X step is skipped gracefully.
4. **Keep `TRACKED.md` current** — PORTFOLIO (owned) + WATCHLIST (eyeing). This drives what gets refreshed.
5. **Ask in chat:** "analyze GOOG", "update my portfolio", "deep dive NVDA", "run the macro scan".

## What is automated

- **Polymarket macro scan** (live cron): every other Saturday, off-peak. A 12-day recency guard makes it biweekly and suppresses the scheduled run if you already triggered one on demand mid-week.
- **Artifact refresh** (planned): Sunday off-peak cron that updates every tracked ticker's artifact in place.
- **On-demand:** macro scan when things heat up; deep dives any time.

## Artifacts

- `~/stock portfolio analyst artifacts/<TICKER>_Monocle_Report.html` — standard report (13 sections: position, frameworks, Bayesian, Sharpe/Kelly, engines, convexity, simulation, margin, options, barbell, investor heroes, metrology, verdict).
- `~/stock portfolio analyst artifacts/<TICKER>_DeepDive.html` — optional 6-page McKinsey-style investor deep dive from the investor-hero lens.
- Both use the same DESIGN-*.md system (Monocle / Creative Giants / Ease Health) and are **overwritten in place — never archived**.

## Evidence & engines

- Evidence hierarchy (non-negotiable): **measured > calculated > modeled > forecast > narrative > unknown**. Every number is labeled.
- Engines (`plugins/capital-decision-lab`, deterministic Python): Kelly sizing (fractional + capped), Sharpe/Sortino/Calmar, convexity, margin safety, seeded Monte Carlo.
- Verdicts: Buy / Hold / Trim / Add / Sell — survivability first: *if the downside breaks the portfolio, the upside is irrelevant.*

## Repo layout

- `skills/` — Hermes skills: `decision-prediction` (process), `capital-research`, `polymarket-macro-scan`, `stock-portfolio-artifacts`.
- `design/` — DESIGN-*.md style references (Monocle, Creative Giants, Ease Health).
- `docs/` — architecture, evidence, finance-math specs, workflows, safety boundaries.
- `plugins/capital-decision-lab/` — the calculation engines.
- `schemas/`, `fixtures/`, `tests/` — contracts, test data, verification.

## First-time checklist (~10 minutes)

1. Clone this repo; open it as the Hermes working directory.
2. Create `~/stock portfolio analyst artifacts/` and its `portfolio screenshots and csv/` subfolder (see the `stock-portfolio-artifacts` skill).
3. Drop one portfolio screenshot or CSV into the folder.
4. In chat: "analyze <TICKER> from my portfolio folder".
5. Verify the values quoted — they become `measured` only after your confirmation.
6. Optional: install `xurl` for X sentiment; ask for the Sunday refresh cron once comfortable.
