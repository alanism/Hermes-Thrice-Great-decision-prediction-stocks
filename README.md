# Hermes Thrice Great NHI — Investment

## Educational use and privacy

Decision ≥ Prediction is educational research and decision support. It presents evidence, exposure, assumptions and scenarios so users make their own decisions and predictions. It does not provide portfolio advisory, prescribe trades or allocations, or issue Buy/Hold/Add/Trim/Sell instructions. Older engine/schema names containing “recommendation” describe model artifacts, not personal advice; the dot reporting flow must not present them as recommended actions.

For optional portfolio context, recommend a redacted CSV or screenshot with names, account numbers and other identifiers removed before sharing. Keep only necessary holdings/exposure fields and the as-of date; verify extracted values. The project creator is not an intended recipient of inputs or outputs. The selected agent, model, storage or hosting provider may process or retain data under its own policies. Verify the actual workflow and destination; this documentation does not guarantee that all deployments are local-only or that a creator can never receive data. Do not upload private data to GitHub, public hosting or a new provider without required permission.

## First report with OAI Dot

Start with one ticker and a public-data-only [first report](docs/reports/FIRST-REPORT-WITH-DOT.md). The reusable [HTML template](templates/stock-report/Stock-Report-Web-Template.html) and [authoring guide](docs/reports/HTML-REPORT-GUIDE.md) provide the editorial report, eight investor lenses plus Page, Business Model Canvas, Seven Powers and final generated sketchnote. This is an authoring scaffold, not a completed report or installed automation; browser and new-user acceptance remain unverified.

## Platform onboarding and verified scope

For first-use setup with dot, Meta Muse AI, Grok Bot, Claude Cloud or Hermes, read the [platform onboarding guides](docs/platforms/README.md) and [customer setup manual](docs/Decision-Prediction-onboard-setup.md). These explain available investor-inspired lenses, separate analysis and risk preferences, evidence gates, verified versus conditional capabilities, and opt-in review schedules.

The guides are source documentation, not a native integration or installer. The current staging allowlist excludes these guides and the eight original investor cards; automatic installed-profile discovery needs separate implementation and tests. See the [full-report completeness gate](docs/Decision-Prediction-onboard-setup.md#full-report-completeness-gate) before claiming the whole workflow was applied.

**A deterministic capital-decision engine that plugs into your Hermes agent — Kelly sizing, convexity, and margin-safety math, run by fixed Python, not a language model's guess.**

This repo is not a standalone app. It's an **extension for the [Hermes](https://hermes-agent.nousresearch.com) desktop agent from Nous Research** (and, untested but supported in principle, the OpenClaw agent harness or any CLI-driven Hermes session). You talk to it in plain language through your agent; underneath, every number — Kelly fraction, margin call price, convexity score — is computed by a fixed standard-library Python engine, so the same inputs always produce the same output. No drift, no re-derivation, no "the model felt like 15% this time."

It turns your real portfolio, your thesis, and messy real-world evidence — Polymarket, X/Twitter, Reddit, SEC filings, broker screenshots — into a structured belief-update workflow, then hands that off to a **DLC investor hero** (or several at once) to structure simulated analytical perspectives inspired by repository playbooks, with deterministic calculations kept separate. The named people and firms do not participate or endorse the output.

> **New here? Read [START_HERE.md](START_HERE.md)** — the operational guide: what you do manually (portfolio screenshots/CSV), optional scheduling patterns (only when explicitly chosen and verified), and the artifact conventions.

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

### Step 3 — Verify capabilities, then request one public-data report

Open or supply the source repository in the authorized host and read the relevant [platform guide](docs/platforms/README.md). Verify file discovery, Python version, reviewed runtime/adapter, permitted commands, source access and private artifact delivery before saying they work. Opening a folder does not prove installation or automatic execution.

Start with the [one-ticker public-data flow](docs/reports/FIRST-REPORT-WITH-DOT.md). Introduce redacted portfolio context only if desired. If a runtime or source is unavailable, deliver clearly scoped qualitative research with its missing calculations stated.

Compatibility is host-specific. Historical adapter verification does not establish a current Hermes desktop installation, fresh-user onboarding, CLI/OpenClaw integration, or portable runtime. See the [verification scope](docs/Decision-Prediction-onboard-setup.md#source-identity-and-verification-scope).

---

## 2. What This Actually Is

Two things stacked together:

1. **A deterministic Python tool.** Belief updates, Kelly sizing, convexity scoring, and margin stress tests all run through fixed, repeatable arithmetic — not a language model freehanding math. Every output traces back to the exact evidence and formula that produced it.
2. **An AI harness on top of it.** Your Hermes agent handles the parts language models are actually good at — reading a broker screenshot, pulling a Reddit thread, summarizing a filing, holding a conversation about your thesis — and hands the numbers off to the Python engine the moment real math is required.

The agent talks. The tool calculates. They don't trade places.

It is **not** a portfolio tracker, a signal service, or a trade-execution tool. It never connects to a brokerage, never places an order, and never moves money. It researches, models, and presents decision-support evidence — you authorize what gets recorded as a decision.

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
| **Measured** | A dated, traceable observation with required verification. Screenshot transcriptions remain Observed transcription · unconfirmed until exact extraction is genuinely confirmed. |
| **Calculated** | Deterministic math on measured/assumed inputs (Kelly fraction, EV, margin call price). Exact and repeatable. |
| **Modeled** | An inference or interpretation (source credibility, thesis crowding). The system's best read, not a fact. |
| **Forecast** | A forward-looking implication (updated probability, model-implied recommendation). Never presented as certainty. |

The three math disciplines underneath the whole thing:

- **Kelly Criterion** — a model-dependent long-run growth calculation under specified assumptions; it does not guarantee avoiding ruin or establish a suitable allocation.
- **Convexity / Asymmetry** — is the upside, if you're right, actually worth the downside if you're wrong.
- **Margin Safety** — can you survive being wrong before you're proven right; this can override Kelly outright.

---

## 4. DLC Investor Heroes

The narrative cards provide simulated research perspectives, not authenticated real-person views, independent votes or eight executable engines. Read the [exact card inventory and disclaimers](docs/platforms/common.md#the-lens-inventory). Check the runtime’s actual executable method catalog separately.

| DLC | Lens |
|---|---|
| `dlc` | Legacy duplicate of the Thorp card at the reviewed version; not a separate ninth original perspective. |
| `dlc-thorp` | Edward Thorp — hedge-first construction, aggressive fractional-Kelly discipline, hard leverage caps, model-health checks. |
| `dlc-mauboussin` | Michael Mauboussin — base-rate anchoring, reverse-engineering what the current price already assumes, forecast-calibration tracking. |
| `dlc-page.md` | Scott Page — Many-Model Thinking, multi-model ensemble aggregation, power-law fat-tail diagnostics, Markov regimes, Bass diffusion, and multi-armed bandits. |
| `dlc-munger-buffett` | Munger & Buffett — quality-and-moat-first value investing, circle of competence, long-horizon compounding over short-term edge. |
| `dlc-laffont` | Thomas and Philippe Laffont / Coatue — concentrated, high-conviction growth/tech investing built around durable secular trends. |
| `dlc-Galloway` | Scott Galloway — brand, platform-power, and market-structure lens on valuation, skeptical of narrative-driven pricing. |
| `dlc-Gerstner` | Brad Gerstner / Altimeter: technology adoption, crossover investing and expectations priced into growth. |
| `dlc-shkreli` | Martin Shkreli — aggressive, filings-first biotech/pharma catalyst analysis; short-horizon, event-driven. |
| `dlc-camillo` | Social Arbitrage framework — reading consumer/cultural sentiment shifts before they show up in earnings. |

A focused lens response is a labeled partial view. A full report retains all eight original perspectives plus Page and their strongest disagreements. The read-only adapter does not expose arbitrary method execution; only claim a pack ran when an actual invocation and retained result prove it.

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

The repository design uses `local/` and `.gitignore` for private runtime files; public commits should contain only synthetic or authorized public inputs. Git ignore rules do not prevent model/API transmission, hosting-provider retention or deliberate file sharing. Inspect the actual host, permissions and data destination before using sensitive data.

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

**What happens if I never authorize a decision record?** No authorized local decision-ledger record should be created by that workflow. This does not erase source files, generated reports, shell logs or host/model-provider retention; inspect the selected environment’s policies. Unrecorded model analysis is not portfolio advice.

---

## License

See [LICENSE](./LICENSE) — Fair Source.

