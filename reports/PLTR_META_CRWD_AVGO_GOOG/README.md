# Five stocks · one hypothetical $1,000 research budget

**Snapshot: November 5, 2026. Publication: November 6, 2026.** Completed adjusted-price history ends November 4. This is a public-evidence research illustration, not actual holdings, an executable order, calibrated stock forecasts or investment approval.

## Read the report

- **[PDF report](PLTR_META_CRWD_AVGO_GOOG_Monocle_Report.pdf)** — static A4 evidence edition, with financial tables, all eight essays, expanded ledgers and six actual Polymarket captures.
- **[Interactive HTML report](PLTR_META_CRWD_AVGO_GOOG_Monocle_Report.html)** — download and open in a browser. Single offline file, with five D3 figures, date/macro inspection, replay/pause and reduced-motion support. GitHub's file view may show source instead of executing HTML.

Both editions contain the actual plugin's **historical Sharpe, conditional Kelly and scenario-convexity calculations**. In the PDF, the main five-stock numeric table is on **page 6** under **“Run the engine. Then challenge its assumptions.”** The HTML has the same section at `#finance`. Raw full fractions are not approved leverage; every full binary-Kelly reference failed at least one retained full-path log domain.

## Supporting files

| File | Purpose |
|---|---|
| [design.md](design.md) | Implemented editorial layout, tokens, interaction, print and evidence rules; links to the existing three repository design references |
| [tokens.json](tokens.json), [tailwind.theme.json](tailwind.theme.json) | Machine-readable exports of the design specification |
| [methodology.md](methodology.md) | Snapshot, native-engine execution, model assumptions, Page/lens wiring and publication limitations |
| [finance-method-spec.json](finance-method-spec.json) | Predeclared calculation/input/authority policy |
| [model-definitions.json](model-definitions.json) | Actual bootstrap, payoff compression and exposure-reference parameters |
| [metric-summary.csv](metric-summary.csv) | Unrounded native metrics for five stocks plus equal-dollar and inverse-volatility comparison portfolios |
| [execution-summary.json](execution-summary.json) | Selected source/receipt/domain verification, stripped of machine-specific paths; not the complete raw case archive |
| [verification.json](verification.json) | Verification of this exact publication, separate from historical engine/report regression results |
| [manifest.json](manifest.json) | Byte sizes and SHA-256 hashes for the report bundle; the manifest excludes its own hash |
| [D3-LICENSE.txt](D3-LICENSE.txt) | License for the embedded D3.js 7.9.2 library |

## Read the calculations correctly

- Sharpe uses population daily volatility, 252 sessions/year and declared 0% / 3% / 5% constant cash benchmarks—not retrieved Treasury yields.
- Kelly and convexity reuse a conditional in-sample historical-resampling model. They are not calibrated forward probabilities or a validated independent edge.
- Quarter Kelly, a 50% confidence haircut and exposure caps are **unapproved illustrative model choices**. Five standalone references cannot be combined as portfolio weights.
- The cash-retaining sleeve comparison is **not joint Kelly optimization**. The original inverse-volatility weights remain a separate risk-only illustration.
- Convexity score is finite scenario asymmetry, **not option gamma**. Compressed bear loss is not a worst trial or maximum possible loss.
- The eight investor takes are **simulated analytical lenses**, not real investor statements or endorsements.

## Scope

Public files only. No private `local/` folder, brokerage/account data, credentials, provider caches, full local test logs or machine-specific runtime environment are included. This publication does not install or deploy a plugin, publish the separate frozen plugin release, place trades, or submit anything to hackathon organizers. See [methodology.md](methodology.md) for the boundaries and missing coverage.

PDF is static; the HTML is the interactive edition. Tagged output is not a claim of PDF/UA or comprehensive screen-reader conformance. Printing an HTML preview alone was not treated as proof of PDF pagination: the exported PDF was separately checked.
