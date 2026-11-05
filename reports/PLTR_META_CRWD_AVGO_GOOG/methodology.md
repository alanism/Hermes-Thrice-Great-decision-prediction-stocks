# Methodology and boundaries

## Snapshot and evidence classes

This is a public-evidence research illustration for PLTR, META, CRWD, AVGO and GOOG with an explicitly assumed **$1,000** budget. It contains no authenticated holdings or brokerage connection. Observations remain the **November 5, 2026** snapshot; history uses 501 completed adjusted closes / 500 returns through **November 4, 2026**. The partial November 5 session is excluded from historical calculations. Publication is not a data refresh.

The exact report labels are **measured / calculate / modeled / forecasted**. Observed provider quotes and screenshots are not resolved forecasts; reproducible arithmetic is not validated forward prediction. Source URLs and timestamps are inside the HTML and printed source ledger. Incomplete primary-release retrieval and conflicting macro-book quality remain disclosed.

## Actual financial execution

The displayed Sharpe, Kelly and convexity outputs came from the actual installed Capital Decision Lab v0.2.0 engines, frozen local source `330cdfee69f799f268c13005873bb77d8e7223e4`. The report work did not change that source. It exercised 35 analysis cases, with 35 observed calls to each of the three engines, across five stocks and two comparison portfolios. Seven base streams also passed isolated Hermes native dispatch and repeated identical CLI analysis. This does **not** establish dispatch from the user's current desktop profile.

The local verification rehashed 136 installed files and eight observed imported sources against that frozen source. Public metric values are retained without rounding in [metric-summary.csv](metric-summary.csv). Case/analysis hashes in the HTML bind the shown outputs to the retained local receipts. `execution-summary.json` is a selected public verification summary, not the entire raw execution archive. The local frozen-source commit is an audit identifier; this documentation publication does not claim to have published or deployed that plugin release.

### Historical Sharpe

Native definition: mean daily excess return divided by **population** daily standard deviation, multiplied by square root of 252. Annual constant cash assumptions of 0%, 3% and 5% are converted with `(1 + annual_assumption) ** (1/252) - 1`. These rates are modeled sensitivity inputs, **not measured Treasury yields**. Historical Sharpe is not a performance forecast or a serial-correlation-adjusted estimator. The earlier sample-volatility figures remain separately labeled.

### Conditional Kelly and convexity

Full details are in [finance-method-spec.json](finance-method-spec.json) and [model-definitions.json](model-definitions.json). The input model uses 4,000 joint moving-block bootstrap trials, a 252-session horizon, 21-session blocks and seed `20261105`. Common sampled blocks retain same-day cross-name dependence. This reuses in-sample history and assumes stationarity; empirical positive/negative frequencies are **not calibrated future stock win odds**.

Binary Kelly uses conditional mean positive/negative terminal payoffs. The quarter fraction, 50% confidence haircut, 30% standalone stock cap and unlevered portfolio-sleeve cap are illustrative model/analyst choices, **not user-approved risk policies**. Five standalone references are not an additive portfolio. Original capped-inverse-volatility and equal-dollar comparisons are not retrospectively renamed Kelly optimizations. The separate cash-retaining sleeve comparison is budget arithmetic, **not joint Kelly optimization**.

The native expected-log-growth kernel was additionally exercised on all retained trial outcomes for each stream. **Every uncapped full binary-Kelly fraction failed on at least one retained tail path.** Capped references passed those sampled domains; unseen tails, model error and optimality remain unproven. Borrowing or approved trades do not follow from any positive calculation.

Convexity compresses negative outcomes into bear and splits sorted positive outcomes into base/bull/moon by actual counts, preserving total empirical mass and mean. Its score is finite scenario asymmetry, **not option gamma**. Compressed bear-mean `max_loss` is neither the worst resampled trial nor a security's maximum possible loss. The conditional mean return column in the CSV is a model statistic, not a forecast or target return.

## Page models and simulated commentary

Actual power-law tail-fit, Markov and neutral allocation kernels were run upstream of the investor lenses. Applicability was screened; unavailable or inapplicable models were not presented as executed. Tail rejection, empirical uncertainty and the lack of independent model-authorized positive sizing remain visible.

All eight 200-word simulated investor essays were refreshed from the same nine-input financial-evidence packet. They are editorial analytical lenses, not statements by, endorsements from, or executable investment packs approved by those real people. The report preserves the equal-dollar portfolio's higher same-history Sharpe as counterevidence against the inverse-volatility illustration.

## Prediction markets and sources

The six Polymarket captures are actual retained browser screenshots, embedded unchanged. Each book has capture time, event horizon and resolution context. Raw Fed quotes were not silently normalized. The gasoline Yes-price total of 158.95% is incoherent as a direction distribution; no calibrated direction probabilities are inferred from it. AAA units and conversion assumptions remain explicit.

## Publication scope and verification

This folder publishes the finished HTML, an exported static PDF, a design specification, machine-readable metric/model summaries, selected verification and SHA-256 manifest. It deliberately excludes private `local/` records, account snapshots, credentials, machine-specific runtime files, provider response caches, the complete local test logs and the frozen plugin release archive. It is a report-publication bundle, **not a complete reproducible financial-engine source/data release**.

The HTML is self-contained with D3.js 7.9.2 and six embedded source screenshots. Opening it does not require a service, API token or CDN. GitHub may show HTML as source; download the file and open it in a browser. PDF is static: interactions and animation require HTML. Expanded disclosures, numeric/text presence, actual page geometry and visual samples are checked after PDF export; this is not a claim of PDF/A, PDF/UA, comprehensive assistive-technology support or a financial audit.

No brokerage integration, order, money movement, authenticated investment approval, live-profile install, public plugin deployment, hackathon submission or organizer contact is part of this publication.
