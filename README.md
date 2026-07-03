# Hermes Thrice Great NHI — Investment
### Operator's Manual — Capital Decision Lab

---
Hermes Thrice Great NHI Investment turns a user’s real portfolio, thesis, and messy evidence from Polymarket, X/Twitter, Reddit, filings, screenshots, and local sources into a structured belief-update workflow.

Hermes verifies the evidence, classifies it as Measured / Calculated / Modeled / Forecast, updates Bayesian probabilities, then recalculates Kelly sizing, convexity, margin safety, and model health through selected method packs like Thorp, Mauboussin, Shkreli, Laffont or Committee Mode.

The result is a local, self-directed capital research operator that tells the user what the model implies — add, trim, hold, hedge, avoid margin, watch, or reject — and records the decision so future outcomes can be calibrated against the original belief.

**You install this through Hermes agent.**


## 0. Read This First

This manual explains **Hermes Thrice Great NHI Investment**, a self-directed capital research system built as an extension of the Hermes agent. It takes messy real-world evidence — your portfolio, your thesis, market data, social sentiment, prediction markets, filings — and turns it into a structured, disciplined decision process built on three pillars:

1. **Kelly Criterion** — how much exposure your edge actually justifies.
2. **Convexity / Asymmetry** — whether your upside is worth your downside.
3. **Margin Safety** — whether you can survive being wrong before you're proven right.

You do not need to know any of the math behind these three ideas. The system runs them in fixed, deterministic Python — not inside a language model's head — so the same inputs always produce the same outputs, every time, with no guessing and no drift. Your job is to supply honest beliefs and real evidence. The system's job is to update those beliefs correctly, calculate the consequences precisely, and show you what they imply.

**What changed in this version:** the tool used to be a pure calculator — you typed in assumptions, it did arithmetic. It now also *gathers and organizes evidence* (your portfolio, market data, social sentiment, prediction markets, filings), *updates your probability estimates* using that evidence, and *produces a model-implied recommendation* — increase, decrease, hold, hedge, watch, pause, reject, or record no action.

**What has not changed:** the tool still does not execute trades. It does not place orders. It does not move money. Every recommendation ends with you — the user — authorizing what actually gets recorded as a decision. Hermes researches, models, recommends, and records. It does not act on your behalf.

---

## 1. The Pipeline, In One Picture

```
portfolio + thesis + evidence
   → belief update
   → Kelly sizing
   → convexity analysis
   → margin survival
   → model-implied recommendation
   → user-authorized decision record
```

Nine questions this pipeline is built to answer:

1. What do I own right now?
2. What do I believe about this position?
3. What evidence supports or weakens that belief?
4. How should my probabilities update?
5. What does Kelly imply about position size?
6. Is the upside convex enough to justify the downside?
7. Can I survive the margin and drawdown path?
8. Should the model imply add, trim, hold, hedge, watch, or reject?
9. What should be recorded for future calibration?

This is not a portfolio tracker and it is not a signal service. It is a **capital decision lab** — a workflow that forces your beliefs to meet real evidence before your money does.

---

## 2. Why "Non-Human Intelligence"?

Language models are good at language. They are not naturally reliable at arithmetic under pressure, and they get worse at it the longer a conversation runs. Ask an LLM to freehand a Kelly fraction, a margin call price, or a Bayesian update, and you're trusting a word-predictor to do something that has one correct answer.

Hermes Thrice Great NHI takes the math *out* of the language model entirely. Every calculation — belief updates, Kelly sizing, convexity scoring, margin stress tests — runs through a fixed, standard-library Python engine, not a guess. The "NHI" name is a deliberate reminder: this part of the system is not a mind estimating an answer. It is a calculator that happens to sit inside a conversational agent. Same inputs, same outputs, every time, and every output is traceable back to the exact evidence and formula that produced it.

---

## 3. The Four Layers of Evidence

Everything the system touches — every number, every claim, every conclusion — gets sorted into one of four layers. Understanding these four layers is the single most useful thing you can learn about how this tool thinks, because it's the difference between "the model said so" and "here's exactly why."

### Measured
Something observed or retrieved directly from a source: your portfolio holdings, your cash balance, your margin used, a Polymarket price, a post on X, a Reddit thread, a line from an SEC filing, a number read off a broker screenshot. **Measured does not mean true** — it means "this was retrieved from somewhere and can be traced back to it." A screenshot can still be misread. A Reddit post can still be wrong. Measured is the raw material, not the verdict.

### Calculated
Deterministic math run on measured or assumed inputs: a Kelly fraction, an expected value, a margin call price, a liquidation buffer, a convexity score. **Calculated means the formula is exact and repeatable** — the same inputs will always produce the same output, and you can check the arithmetic yourself if you want to.

### Modeled
An inference or interpretation built from evidence and assumptions, rather than a direct observation: how credible a source is, how relevant a piece of evidence is to your thesis, how crowded a trade looks, how much two sources are just echoing each other. **Modeled means "this is the system's best interpretation," not a fact.** It's labeled as such so you never mistake an inference for a measurement.

### Forecast
A forward-looking belief or decision implication: your updated probability of the bull case, your updated Kelly-implied exposure, the model-implied recommendation itself. **Forecast means "this is what the evidence and rules imply about the future," under the assumptions you supplied and approved.** It is never presented as certainty.

Every recommendation Hermes produces can be traced back through these four layers to the original measured evidence. If you ever want to know *why* the system believes what it believes, you can always walk the chain backward.

---

## 4. The Three Master Disciplines, In Plain English

### 4.1 Kelly Criterion — "How much should I actually risk?"

Imagine a weighted coin that comes up heads 60% of the time, and heads means you double your stake. That's a good bet — but how much of your money should you actually put on it? All-in is reckless: a 60% edge still means you lose 40% of the time, and one bad flip with everything on the table ends the game. Betting almost nothing wastes most of your edge.

The Kelly Criterion answers exactly this question: **given a real edge, what fraction of your capital grows it fastest over time without risking ruin?** Developed at Bell Labs in 1956, it has one property that makes it different from every other sizing method — bet more than Kelly says, and your long-run growth rate goes *down*, not up, because the extra volatility eats your compounding. Kelly isn't a risk limit invented by a compliance department. It's a mathematical fact about how volatility and compounding interact.

**What the tool does with this:** you (or the belief-update stage below) supply a win probability and a payoff ratio. The system returns the Kelly fraction implied by those numbers, along with half-Kelly and quarter-Kelly equivalents, because almost every serious practitioner deliberately under-bets full Kelly to protect against the very real chance their edge estimate is wrong.

### 4.2 Convexity / Asymmetry — "Is my upside worth my downside?"

The wrong first question about a trade is "will it go up or down." The right first question is: **if I'm right, how much do I make — if I'm wrong, how much do I lose — and are those two numbers even close to the same size?**

A trade with 10% possible upside and 40% possible downside is bad even if you're right most of the time, because one loss erases many wins. A trade with 40% possible upside and 10% possible downside is attractive even if you're only right half the time, because your wins pay for your losses several times over. That lopsidedness is **convexity**, or plainly, **asymmetry**.

**What the tool does with this:** you give it your upside scenario and downside scenario (with probabilities if you have them), and it calculates the upside/downside multiple, the probability-weighted expected value, the breakeven probability, and a convexity score. It won't tell you what ratio is "good enough" — that's your call — but it makes sure you're deciding based on the real number, not a vibe.

### 4.3 Margin Safety — "Can I survive being wrong before I'm right?"

Borrowing to invest multiplies gains and losses equally, but it does not affect survival symmetrically. A cash position that drops 50% is still yours to hold and wait out. A leveraged position that drops far enough triggers a **margin call** — the broker forces you to deposit more cash or liquidates the position for you, often at the worst possible moment, locking in the loss permanently. Being early and being wrong look identical the instant a margin call fires.

**What the tool does with this:** you give it your account's margin terms — equity, borrowed amount, maintenance requirement — and it stress-tests the position against a menu of drawdowns (10%, 20%, 30%, 50%, or custom), returning the exact price that triggers a margin call and how much buffer you have before that happens. In this system, **margin safety can override Kelly.** If Kelly math says 7% exposure is optimal but a 30% decline would trigger a dangerous margin condition, the model-implied exposure gets capped below Kelly, and the recommendation says exactly why.

---

## 5. Three Investment Traditions Behind the System

Hermes Thrice Great NHI doesn't invent its own investing philosophy from scratch. It draws on three well-documented research traditions, offered as selectable "method packs" rather than baked into one confused style. You can run any one of them, or run all three at once and see where they disagree.

### 5.1 The Thorp Tradition — Hedge First, Size Second, Survive Always

**Edward O. Thorp** is the founding figure of quantitative investing, and the reason Kelly sizing has a real-world track record at all. He started in casinos: in the early 1960s he mathematically proved blackjack could be beaten through card counting, sized his bets with the (then-obscure) Kelly Criterion, and published the results in *Beat the Dealer* (1962) — the first book to demonstrate a casino game could be beaten by a disciplined player. Casinos changed the rules of blackjack in response.

He then pointed the same toolkit at Wall Street. His first major market edge came from stock purchase warrants, which he found were routinely mispriced relative to the stock they were tied to. He never took a naked directional bet on that mispricing — he built a **market-neutral hedge**, long the underpriced side and short the overpriced side, so the position didn't need him to guess market direction at all. That hedge-first discipline is the origin of the tool's convexity module: convexity isn't just measured, in this tradition it's *constructed*.

Knowing the edge was only half the job. Thorp adapted Kelly sizing into a practical trading rule and discovered something the formula doesn't say on its own: full Kelly is mathematically optimal but produces drawdowns most humans can't stomach without abandoning the system. His answer was **fractional Kelly** — trading at half or a quarter of what full Kelly recommends, and capping leverage at roughly 2× no matter what the raw math implied. He also described the **"avalanche effect"**: when a shorted, overpriced leg of a hedge declined, it released margin that could be redeployed into new positions without fresh cash — compounding capital efficiency, but only within the leverage caps Kelly math allowed.

The result, through his fund Princeton/Newport Partners: roughly 19–20% annualized returns from 1969 to 1988, with 227 of 230 months profitable and the worst single month's drawdown under 1%. That record is a useful contrast to Long-Term Capital Management, a fund staffed by Nobel laureates who understood the same math extremely well and still collapsed in 1998 — because their leverage sizing ignored the survivability question Kelly and margin math both force you to confront. Being right about the math and sizing correctly are two different skills, and the second one determines whether you're still playing the game in ten years.

**What this pack emphasizes in the tool:** hedged, market-neutral thesis construction, aggressive fractional-Kelly discipline, hard leverage caps, and a three-question model-health check — did it work in the past, is it working now, will it keep working — used to tell the difference between a normal losing streak and a broken edge.

### 5.2 The Mauboussin Tradition — Anchor to Base Rates, Then Update

**Michael Mauboussin's** work starts from an uncomfortable observation: as investors get more skilled on average, luck — not skill — increasingly decides short-term outcomes, because the skill gap between competitors shrinks even as the luck gap stays wide. His answer is to anchor every forecast to an **outside view**: instead of building a forecast from company-specific detail and gut feel (the "inside view," which reliably produces overconfidence), start from the base rate of a whole reference class of similar situations, and treat company-specific evidence as a Bayesian update *on top of* that base rate — never as a replacement for it.

He pairs this with **reverse-engineering the market's own expectations**: instead of building a valuation from scratch, start with the current price and solve backward for what growth, margins, and competitive-advantage duration the market is already assuming. That reframes every investment question from "what's this worth" to "can this company actually clear the bar the market has already set for it."

Mauboussin is also explicit about where this framework breaks: strict base-rate discipline would have told you to bet against almost every truly transformative company in history, because transformative outcomes are by definition outside the historical reference class. His resolution is that base rates are the *prior*, not the ceiling — exceptional evidence can update it, but the base case should never quietly become the outlier case.

**What this pack emphasizes in the tool:** grounding your prior probability in a real reference class before any evidence updates it, reverse-engineering what the current price already assumes, and tracking your own forecast accuracy over time (a "Brier score") so your calibration — not just your win rate — improves.

### 5.3 The Contrarian Filings Tradition — Primary Sources Over Narrative

The third tradition starts from a simple rule: **read the filings yourself, before you read anyone's opinion about them.** Its workflow goes directly to SEC 10-K and 10-Q filings rather than secondary financial media, calculates a company's core numbers by hand — market cap, cash, debt, and enterprise value (the real price tag of a business once you account for what you're inheriting and what you're acquiring) — and builds cash-flow projections from that primary-source foundation rather than a headline growth number.

Its signature move is the same reverse-engineering idea as above, applied more mechanically: plug the current stock price into your own cash-flow model and adjust the assumptions until the model matches the market price. Whatever assumptions it takes to get there are exactly what the market is betting on. If those assumptions are absurd — permanent 40% growth with no new competition ever showing up — that's a warning sign the price is disconnected from the business. If the assumptions are unreasonably pessimistic for a fundamentally sound company, that's the opposite signal. This tradition also draws a hard line against re-evaluating a thesis just because a price moved — it re-evaluates only when new fundamental evidence arrives (a filing, an earnings call, a trial result), which is the difference this tradition draws between being *wrong* and being *early*.

**What this pack emphasizes in the tool:** filings-first evidence, enterprise-value-based analysis, reverse-engineered market expectations, and strict discipline about what counts as a reason to change your mind.

### 5.4 Running Them Together — Committee Mode

Because these three traditions can genuinely disagree, the system supports running all of them on the same thesis and comparing the results directly rather than blending them into one muddy answer. A Committee Mode run might come back looking like: the hedge-and-survival lens says trim because Kelly and margin math both bind; the base-rate lens says watch because the moonshot scenario isn't supported as a base case; the filings lens says hold because the market's implied expectations aren't excessive relative to the company's cash and assets. The system's synthesis names the disagreement explicitly rather than picking a winner for you.

---

## 6. How It Works, Step by Step

### Step 1 — Portfolio
You give Hermes your current holdings — a broker screenshot, a CSV export, a pasted table, or manual entry. It extracts ticker, shares, price, market value, cash, margin used, borrowed amount, maintenance margin, and position weight. If any field can't be verified with confidence, Hermes asks you to confirm or correct it before moving on.

### Step 2 — Thesis
You state what you believe, in your own words — "I own this because I think the upside is convex due to X, Y, Z, and I'm considering adding, but I want to know if margin risk makes that a bad idea." Hermes turns this into structured assumptions: target asset, time horizon, bear/base/bull/moonshot scenarios and their probabilities and payoffs, key catalysts, kill conditions (the specific evidence that would prove the thesis wrong), a max exposure cap, and your confidence level. You can edit any of this before it's used.

### Step 3 — Evidence Gathering
Hermes can gather or accept evidence from Polymarket, X/Twitter, Reddit, financial news, SEC/EDGAR filings, company investor relations pages, broker screens, screenshots, or your own manual notes. Every piece of evidence is recorded with its source, retrieval method, timestamp, and a confidence rating — nothing is quietly assumed to be reliable.

### Step 4 — Confirmation Queue
Anything extracted from a screenshot, OCR, or a low-confidence source gets queued for you to confirm, correct, discard, or defer. **Only evidence you've confirmed, corrected, or that came from a high-reliability source can affect a belief update.** This exists specifically to stop an OCR misread or a bad screenshot from silently changing a recommendation.

### Step 5 — Evidence Synthesis
Hermes combines everything into a small set of readable pressures: bullish pressure, bearish pressure, volatility pressure, crowding pressure (is everyone already in this trade), source diversity, and a contradiction score for when your sources disagree with each other. Each pressure is scored with its own confidence and stated limitations.

### Step 6 — Bayesian Belief Update
This is the Model layer in action: your prior belief, combined with the weight and reliability of the new evidence, produces a posterior belief. For example: a prior bull probability of 32%, updated by evidence with a likelihood ratio of 1.18, becomes a posterior of roughly 36%. **This update never silently overwrites your thesis.** Hermes proposes the update; you approve, reject, modify, or leave it pending.

### Step 7 — Kelly Sizing
Using the updated probability, Hermes calculates full, half, quarter, and capped Kelly exposure, the resulting change in capital at risk, and an overbet warning if your current position already exceeds what your own updated beliefs justify.

### Step 8 — Convexity Analysis
Hermes checks whether the asymmetry of the position still justifies the risk under the updated beliefs — upside/downside multiple, probability-weighted expected value, breakeven probability, and how much of the potential outcome space sits in the tail.

### Step 9 — Margin Safety
Current equity, borrowed amount, margin ratio, estimated margin call price, liquidation buffer, and a full stress table across drawdown scenarios. As noted above, this step can cap what Kelly alone would otherwise allow.

### Step 10 — Model Health
Hermes tracks whether the thesis itself still looks healthy — healthy, watch, degrading, broken, or unavailable — based on evidence contradictions, how much the apparent edge has compressed, whether realized drawdown matches what was expected, margin stress, and whether any kill conditions have been triggered. This is the mechanism for telling **bad luck** apart from a **broken thesis** apart from **edge compression** apart from **margin-driven danger** — four very different problems that feel identical from the inside if you're not tracking them separately.

### Step 11 — Recommendation
Hermes produces a model-implied recommendation — increase exposure, trim to fractional Kelly, hold, avoid margin, reduce margin, hedge, watch, pause, reject the thesis, or record no action — along with the specific Kelly, convexity, margin, evidence, and model-health reasons behind it, plus its confidence and limitations.

### Step 12 — Decision Record
**Hermes does not turn a recommendation into a decision on its own.** You authorize the final record — accept, modify, reject, record no action, or record a watch trigger for the future. The decision record stores a traceable snapshot of the portfolio, evidence, belief update, Kelly analysis, convexity analysis, margin analysis, recommendation, and your authorization, timestamped, forming a local decision journal you can use later to check your own calibration.

---

## 7. Method Packs

Method packs are selectable research lenses layered on top of the same core engine:

- **Core Pack** — the fast, general-purpose path: portfolio → thesis → evidence → Bayesian update → Kelly → convexity → margin → recommendation.
- **Thorp Pack** — emphasizes hedged structures, aggressive fractional-Kelly discipline, hard leverage caps, and capital recycling.
- **Mauboussin Pack** — emphasizes base-rate anchoring, reverse-DCF market-implied expectations, expected-value framing, and a running decision journal for calibration.
- **Contrarian Filings Pack** — emphasizes primary-source filings, enterprise-value analysis, and reverse-engineered market expectations, especially for deep single-name research.
- **Committee Mode** — runs multiple packs on the same thesis and surfaces where they agree and disagree, rather than forcing a single answer.

---

## 8. What This Tool Is Deliberately Not

To be unambiguous, in this version as much as the last:

- It is **not** financial advice. Every recommendation is explicitly a model-implied output under the assumptions and evidence you approved — not a directive.
- It does **not** connect to any brokerage account for trading purposes, and it does **not** execute trades of any kind, under any circumstances.
- It **does** gather public and user-supplied evidence — filings, prediction markets, social sentiment, portfolio screenshots — strictly to inform the belief-update step. This is read-only research, gated by your confirmation before it can change anything, never live order execution.
- It does **not** silently act on your behalf. Every belief update, every Kelly change, every recommendation requires your review, and every decision record requires your explicit authorization before it's saved.
- It does **not** predict the future with certainty. It calculates the mechanical consequences of the beliefs and evidence you and it jointly assembled. Every forward-looking number is labeled as a forecast, not a fact.
- All runtime data — your real portfolio, your real evidence, your real decisions — stays local. It is never committed to shared source control; only synthetic fixture data is used for testing.

The tool's entire value rests on one property: **it never lets you fool yourself about what your own beliefs and evidence actually imply.** It cannot do that if it starts guessing at prices, executing trades, or softening a bad stress-test result to make a thesis feel better than it is.

---

## 9. Frequently Asked Questions

**"Do I need to understand any of the underlying formulas to use this?"**
No. State your holdings and your thesis in plain language; confirm the evidence the system finds; approve or adjust the belief update it proposes. The Kelly, convexity, and margin math runs underneath without you ever needing to touch it.

**"What if I don't have a confirmable win probability?"**
Then you likely don't have a quantifiable edge yet, and the system will say so rather than manufacture false confidence. Treat any output built on a rough guess as provisional, and lean toward the more conservative fractional-Kelly sizing until your confidence — and your evidence — improve.

**"Why does the system ask me to confirm things it already extracted?"**
Because screenshots get misread, OCR makes mistakes, and a wrong number silently flowing into a belief update would produce a confidently wrong recommendation. The confirmation queue exists specifically to prevent that failure mode.

**"Can the different method packs actually disagree with each other?"**
Yes, by design. Committee Mode exists because Thorp, Mauboussin, and the contrarian filings tradition ask genuinely different questions of the same evidence. Watching them disagree is often more useful than any single answer.

**"What happens if I never authorize a decision record?"**
Nothing gets saved as a decision. Recommendations without authorization simply expire as unrecorded analysis — the system never assumes silence means approval.

---

## 10. Glossary

| Term | Plain-English Meaning |
|---|---|
| **Kelly Criterion** | A formula for sizing a bet or position so that long-run growth is maximized without risking ruin. |
| **Full Kelly** | The mathematically optimal exposure size implied by a given edge. |
| **Fractional Kelly** (half, quarter, capped) | Deliberately sizing below full Kelly to protect against the near-certainty that your edge estimate is somewhat wrong. |
| **Convexity / Asymmetry** | The relationship between a position's potential upside and its potential downside. |
| **Expected Value (EV)** | The probability-weighted average outcome of a set of scenarios. |
| **Margin Lending** | Borrowing from a broker, using your position as collateral, to increase exposure. |
| **Maintenance Margin** | The minimum equity percentage a broker requires you to hold in a leveraged account. |
| **Margin Call** | A broker's demand for more cash or collateral when equity falls below the maintenance requirement, often resulting in forced liquidation. |
| **Bayesian Updating** | A disciplined method for revising a probability estimate as new evidence arrives, weighted by how reliable that evidence has been. |
| **Prior / Posterior** | Your probability estimate before new evidence (prior) versus after it's been incorporated (posterior). |
| **Likelihood Ratio** | How much more (or less) likely a piece of evidence makes one belief versus the alternative. |
| **Base Rate / Outside View** | The historical frequency of an outcome across a whole reference class of similar situations, used as a starting anchor before specifics are added. |
| **Reverse DCF / Market-Implied Expectations** | Starting from the current price and solving backward for what growth, margin, or advantage-duration assumptions would justify it. |
| **Enterprise Value (EV)** | Market cap minus cash plus debt — the real acquisition price of a business. |
| **Market-Neutral Hedge** | A position structured so profit doesn't depend on predicting market direction, but on a pricing relationship between two linked assets. |
| **Avalanche Effect** | Redeploying margin freed up by a winning hedge into new positions, compounding capital efficiency without adding fresh cash. |
| **Model Health** | A running assessment of whether a thesis is healthy, on watch, degrading, or broken, based on evidence and performance versus expectations. |
| **Kill Condition** | A piece of evidence specified in advance that, if it occurs, is agreed to invalidate the thesis. |
| **Decision Record** | A timestamped, traceable log of the portfolio state, evidence, belief update, analysis, recommendation, and your authorization at the moment a decision was made. |
| **Brier Score** | A measure of forecast calibration — how closely your stated probabilities matched what actually happened over time. |
| **Measured / Calculated / Modeled / Forecast** | The four-layer classification the system applies to every number and claim it produces (see Section 3). |

---

*Hermes Thrice Great NHI — the calculation stays deterministic, the evidence stays traceable, and the decision stays yours.*
