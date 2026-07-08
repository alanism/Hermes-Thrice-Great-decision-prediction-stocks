# Hermes Thrice Great NHI — Investment

**A deterministic capital-decision engine that plugs into your Hermes agent — Kelly sizing, convexity, and margin-safety math, run by fixed Python, not a language model's guess.**

This repo is not a standalone app. It's an **extension for the [Hermes](https://hermes-agent.nousresearch.com) desktop agent from Nous Research** (and, untested but supported in principle, the OpenClaw agent harness or any CLI-driven Hermes session). You talk to it in plain language through your agent; underneath, every number — Kelly fraction, margin call price, convexity score — is computed by a fixed standard-library Python engine, so the same inputs always produce the same output. No drift, no re-derivation, no "the model felt like 15% this time."

It turns your real portfolio, your thesis, and messy real-world evidence — Polymarket, X/Twitter, Reddit, SEC filings, broker screenshots — into a structured belief-update workflow, then hands that off to a **DLC investor hero** (or several at once) to do the analysis and quant math the way that investor actually thinks.

---

## 1. Quick Start

### Step 1 — Install Hermes (Nous Research's desktop agent)
Download the Hermes desktop app: **https://hermes-agent.nousresearch.com**

If you want a walkthrough, this setup guide covers install end-to-end:
**[Hermes install/setup guide (YouTube)](https://youtu.be/EJm8Ka-gVOc?si=crIgF9-_LtpDqbF-)**

### Step 2 — Clone this repo
Once Hermes is installed, open a terminal and run:

```bash
gh repo clone alanism/Hermes-Thrice-Great-decision-prediction-stocks
```

### Step 3 — Point Hermes at it
Open the cloned folder as a working directory in Hermes (or your CLI/OpenClaw session), and start a conversation. Hermes reads the repo's `SOUL.md` and `config.yaml` for how to behave, and calls into the deterministic Python tools under the hood — you don't run the math yourself.

That's it. From here, everything happens by talking to your agent: describe your portfolio, state your thesis, and let the pipeline run.

> **Compatibility note:** built and tested against the Hermes desktop app. CLI-terminal use and the OpenClaw agent harness *should* work the same way (Hermes just needs shell/file access to this repo), but neither has been tested yet by me. If you try it on either, I'd genuinely like to hear how it goes — open an issue.

---

## 2. What This Actually Is

Two things stacked together:

1. **A deterministic Python tool.** Belief updates, Kelly sizing, convexity scoring, and margin stress tests all run through fixed, repeatable arithmetic — not a language model freehanding math. Every output traces back to the exact evidence and formula that produced it.
2. **An AI harness on top of it.** Your Hermes agent handles the parts language models are actually good at — reading a broker screenshot, pulling a Reddit thread, summarizing a filing, holding a conversation about your thesis — and hands the numbers off to the Python engine the moment real math is required.

The agent talks. The tool calculates. They don't trade places.

It is **not** a portfolio tracker, a signal service, or a trade-execution tool. It never connects to a brokerage, never places an order, and never moves money. It researches, models, and recommends — you authorize what gets recorded as a decision.

---

## 3. The Pipeline

```
portfolio + thesis + evidence
   → belief update
   → Kelly sizing
   → convexity analysis
   → margin survival
   → model-implied recommendation
   → user-authorized decision record
```

Every number the pipeline produces is tagged with one of four evidence layers, so you can always tell the difference between an observation and a guess:

| Layer | Meaning |
|---|---|
| **Measured** | Retrieved directly from a source (a holding, a price, a filing line, a screenshot). Traceable, not necessarily true. |
| **Calculated** | Deterministic math on measured/assumed inputs (Kelly fraction, EV, margin call price). Exact and repeatable. |
| **Modeled** | An inference or interpretation (source credibility, thesis crowding). The system's best read, not a fact. |
| **Forecast** | A forward-looking implication (updated probability, model-implied recommendation). Never presented as certainty. |

The three math disciplines underneath the whole thing:

- **Kelly Criterion** — given a real edge, what fraction of capital grows it fastest without risking ruin.
- **Convexity / Asymmetry** — is the upside, if you're right, actually worth the downside if you're wrong.
- **Margin Safety** — can you survive being wrong before you're proven right; this can override Kelly outright.

---

## 4. DLC Investor Heroes

Method packs are selectable research lenses on top of the same core engine — each one runs the same evidence through a different investor's actual analytical style, so you can see where they'd agree and where they'd genuinely fight about your thesis.

| DLC | Lens |
|---|---|
| `dlc` (Core) | General-purpose path: portfolio → thesis → evidence → belief update → Kelly → convexity → margin → recommendation. |
| `dlc-thorp` | Edward Thorp — hedge-first construction, aggressive fractional-Kelly discipline, hard leverage caps, model-health checks. |
| `dlc-mauboussin` | Michael Mauboussin — base-rate anchoring, reverse-engineering what the current price already assumes, forecast-calibration tracking. |
| `dlc-munger-buffett` | Munger & Buffett — quality-and-moat-first value investing, circle of competence, long-horizon compounding over short-term edge. |
| `dlc-laffont` | Philippe Laffont (Coatue) — concentrated, high-conviction growth/tech investing built around durable secular trends. |
| `dlc-galloway` | Scott Galloway — brand, platform-power, and market-structure lens on valuation, skeptical of narrative-driven pricing. |
| `dlc-gerstner` | Corporate turnaround / operational-value lens — is the business itself being fixed, or is the story just getting better. |
| `dlc-shkreli` | Martin Shkreli — aggressive, filings-first biotech/pharma catalyst analysis; short-horizon, event-driven. |
| `dlc-camillo` | Social Arbitrage framework — reading consumer/cultural sentiment shifts before they show up in earnings. |

Run one pack for a fast answer, or run **Committee Mode** to fire several at once and get the disagreement stated explicitly rather than blended into a false consensus.

---

## 5. Repo Layout

```
skills/capital-research/     Hermes-facing skill definitions and source extractors
plugins/capital-decision-lab/  Core deterministic engine
schemas/                      Evidence, thesis, and decision-record schemas
scripts/                       Setup and utility scripts
fixtures/                      Synthetic test data (no real portfolio data is ever committed)
docs/                         Method-pack writeups and operator's manual
local/                        Your real, local-only runtime data — never pushed to source control
dlc*/                          DLC investor hero packs (see table above)
SOUL.md                        Agent behavior/persona definition read by Hermes
config.yaml                    Runtime configuration
```

All real portfolio data, evidence, and decision records stay local under `local/` and are `.gitignore`d — only synthetic fixtures are ever committed.

---

## 6. What This Deliberately Does Not Do

- **No financial advice.** Every output is a model-implied result under the assumptions and evidence you approved — never a directive.
- **No trading.** It doesn't connect to a brokerage, place an order, or move money, under any circumstance.
- **No silent action.** Every belief update, Kelly change, and recommendation requires your review; every decision record requires your explicit authorization before it's saved.
- **No false certainty.** Every forward-looking number is labeled a forecast, not a fact.

---

## 7. FAQ

**Do I need to understand the math to use this?** No. Describe your holdings and thesis in plain language to your agent; confirm the evidence it finds; approve or adjust the belief update. Kelly, convexity, and margin math run underneath without you touching them.

**Does this work outside the Hermes desktop app?** In principle, yes — anything that gives an agent CLI/file access to this repo (a terminal session, the OpenClaw harness) should be able to drive it the same way. This hasn't been tested yet outside the Hermes desktop app; feedback via issues is welcome.

**Can the DLC packs disagree with each other?** Yes, by design — that's what Committee Mode is for.

**What happens if I never authorize a decision record?** Nothing gets saved. Recommendations without authorization simply expire as unrecorded analysis.

---

## License

See [LICENSE](./LICENSE) — Fair Source.
