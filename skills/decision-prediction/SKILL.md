---
name: decision-prediction
description: Use for Decision > Prediction stock analysis.
---

# Decision > Prediction — Thorpe + Capital Decision Lab

Single-stock and portfolio research under the Hermes Thorpe evidence discipline, with calibrated token metrology.

## When to use

- User requests `Decision > Prediction` stock analysis (single ticker or portfolio)
- GOOG-style requests: filings + earnings + X sentiment + Porter/Helmer/BMC + Polymarket + options + barbell + DLC
- Any request that needs `capital-decision-lab` engines or `token_meter` cost tracking

## Core principles

1. Evidence hierarchy is non-negotiable: **measured > calculated > modeled > forecast > narrative > unknown**. Label every number.
2. Never invent financial facts. Never claim brokerage access. Invalid domains → `unavailable` with reason.
3. Kelly is a reference, not an instruction. Margin danger overrides Kelly.
4. Only `user_verified` evidence updates Bayesian beliefs; cap max change per update.

## Workflow — Single stock (e.g., GOOG)

### 1. Capture & preserve provenance
- Screenshots + position: record price, shares, cost, % return, file hash, capture time.
- Portfolio + margin: equity, margin used, maintenance, withdrawable — each as measured atom.
- Polymarket / X: snapshot title, odds, volume, resolution rules, capture time, verification status.
- Options chain: strikes, breakeven, ask, expiry — measured at a time.
- Require **user confirmation** for screenshot-derived values before they become `measured`.

### 2. Metrology first (token_meter)
```
~/.hermes/profiles/thorpe/workspace/token_meter/token_meter.py
~/.hermes/profiles/thorpe/workspace/token_meter/measure_real.py → measure_snapshot.json
~/.hermes/profiles/thorpe/workspace/token_meter/usage_log.csv  (append-only)
```
- Run `measure_real.py` to ground image bytes (real `ls -lh`) before estimating.
- Estimate CORE vs EXPANDED vs ENGINES+DLC before the LLM call — fill `PRICING` dict.

### 3. Cache architecture (byte-exact prefix — do not reorder)
```
[1] SYSTEM  ~2.8k — soul.md + D>P Phase 1-3 + framework definitions + finance-math spec excerpts — TTL ∞
[2] FILINGS ~141k/ticker — 10-K+10-Q+earnings, normalized whitespace, fixed section order, sha256-hashed — TTL 90d
[3] FINANCE-MATH specs ~1.27k — formula-spec, kelly, convexity, margin, simulation — TTL ∞ (cacheable static)
[4] DLC prompt ~1.2k — 8 lenses frozen text — semi-cacheable
[5] DYNAMIC 22–49k — images (base64) + Polymarket JSON + options + X + question — NEVER cached
```
- Anthropic: `cache_control: ephemeral` on [1]+[2]+[3], 4 breakpoints max, 90% read discount. Use `anthropic-beta: extended-cache-ttl-2025-04-11` for 1hr.
- OpenAI: auto after 1,024 tok, 50% discount — no code.
- Gemini: `caches.create cachedContent`, 1hr default, 75% discount.
- Never put `Question:` before filings. Never inline dynamic text with filings.

### 4. Engines to run (from capital-decision-lab/docs/finance-math/)

| Engine | Doc file | Supply | Key formulas | Output |
|---|---|---|---|---|
| **Formula spec** | `formula-specification.md` | Periodic returns OR supplied vol/drawdown | ROI, CAGR, pop σ, downside σ, drawdown (positive), VaR/ES sorted, Sharpe/Sortino/Calmar annualised by √(periods) | Atoms with input refs + limitations |
| **Kelly** | `kelly-criterion.md` | p,q, g>0, l<0, haircut, fraction, cap | `edge=p·g+q·l`, `full_kelly=−edge/(g·l)`, `confidence_adjusted=full·haircut`, `fractional=adj·fraction`, `capped=min(max(frac,0),cap)` + `Σ p·log(1+ex·payoff)` | Negative edge → 0+warning; bad inputs → unavailable |
| **Convexity** | `convexity-upside.md` | Bear/base/bull/moon prices→payoffs + probs | `up/down = bull/|bear|`, `breakeven=|bear|/(bull+|bear|)`, `weighted_up/down`, `convexity=weighted_up/|weighted_down|` | EV, expected return, skew, max loss; ratio unavailable if downside 0 |
| **Margin** | `margin-safety.md` | MV, borrowed, maintenance | `equity=MV−borrowed`, `margin_ratio=eq/MV`, `LTV=borrowed/MV`, `required=maint·MV`, `call=borrowed/(shares·(1−maint))`, `buffer=price−call` + stress rows | Stressed MV/equity/ratio/threshold — labeled as stress, not brokerage truth |
| **Simulation** | `simulation-method.md` | μ, σ, seed, iters, distribution | Seeded normal Monte Carlo, bounded at −1.0, deterministic given seed | P5/P50/P95, mean terminal, loss prob |

### 5. Bayesian discipline
- Prior odds `prior/(1−prior)`, likelihood ratio (bounded), posterior `odds/(1+odds)` — per `bayesian-belief-updates.md`.
- Source quality scales weight; low-liquidity/noisy/contradictory → less weight.
- Need matching thesis sensitivity rule to set direction; need `user_verified` to apply.

### 6. Image & cost optimization
- Prefer **3 images** (position + 1W + 1Y) or a **stitched composite** over 17 loose files. Saves 22.4k tok / $0.067 per stock on Sonnet — more than a Flash run.
- Downscale to 720p (`sips -Z 1280` / `magick -resize 1280x`) before base64 (−30% to −60% vision).
- Batch Porter + Helmer + BMC + Bayesian/Kelly/convexity/margin/simulation + DLC in **one call** sharing one filings prefix — second call repays filings.

### 7. Reporting (Monocle)
- Full artifact anatomy (skeleton, 13-section order, sidebar blocks, inline-SVG chart functions, evidence-labeling conventions): `references/monocle-report-anatomy.md`. Working HTML example: `~/Downloads/GOOG_Monocle_Report_Sanitized_Example.html`.
- Template: `Documents/Vibe Code/Design-md collection/DESIGN-Monocle.md` (`--color-newsprint-cream #fdfcf3`, `--color-signal-yellow #ffc500`, Plantin headlines, 0 radius, hairlines not shadows, 3-col grid).
- Required sections when engines run: **Engines** (formula-spec), **Convexity** (four scenarios + 5 ratios), **Simulation** (seeded P5/P50/P95), updated **Sharpe/Kelly** per `kelly-criterion.md`, updated **Margin** per `margin-safety.md`, **DLC** (8 simulated lenses, labeled not attributed), **Metrology** (CORE vs EXPANDED vs ENGINES+DLC with cache).
- DLC voices: `dlc-Galloway, Gerstner, camillo, laffont, mauboussin, munger-buffett, shkreli, thorp` — render as stylized, simulated commentary with disclaimer; no pack files assumed on disk.

### 8. Verification & logging
- After rendering HTML, `ls -lh` + `wc -l` the outputs; open in preview to confirm.
- Update `GOOG_Token_Cost_Analysis.md` in `~/Downloads` with engine+DLC delta (+~2.47k input cacheable, +~6.1k output) and revised 20-stock warm costs.
- Log to `usage_log.csv`: timestamp, ticker, provider, input/cached/output, cost_usd, saving_pct. Wire `response.usage.cached_tokens` for measured (not estimated) next row.

## Prompt-cache quick reference

| Provider | Read discount | TTL | Enable |
|---|---|---|---|
| Anthropic Claude | 90% | 5 min (1 hr with `extended-cache-ttl` beta) | `cache_control: ephemeral` on static blocks |
| OpenAI GPT-4o | 50% | 5–10 min auto | Automatic ≥1,024 tok |
| Gemini 2.5 | 75% | 1 hr (up to 24 hr) | `caches.create` |
| muse-spark / DeepSeek | ~50% | variable | Auto |

## Pitfalls

- Reordering prefix busts cache (byte-exact). Dynamic block must be last.
- Finance-math specs look small (~1.27k) but output adds ~6.1k — budget output, not just input.
- `unavailable` is correct behavior — never substitute a number when domain invalid.
- Vault/secrets never go in prompts — keep `config.yaml` api_key out of cache-busting.
