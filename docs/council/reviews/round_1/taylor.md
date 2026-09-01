# [T] Bret Taylor — Product Machine Builder — Round 1 Blind Adversarial Review

**Persona:** Bret Taylor. **Operating question:** "Does this move a metric?"
**Document under review:** `docs/build-plan.md` (Many-Model Thinking extension).
**Lens:** customer outcomes, not technical milestones. Code is disposable; the PRD and the customer's job-to-be-done are the durable assets. AI Tourism is a veto.

---

## Key Risks

**R1 — No named customer outcome anywhere in the plan (BLOCKER).**
The build plan is 33KB of artifacts, interfaces, fixtures, and gates, and not one line states what the user can do after this build that they cannot do today. The user of this repo is a single person running a Thorp-style barbell loop: drop screenshots in, ask "analyze GOOG," read a Monocle report with a Buy/Hold/Trim/Add/Sell verdict already produced by Kelly, Sharpe/Sortino, convexity, margin safety, and seeded Monte Carlo, then optionally stress it through an 8-voice investor hero panel. That loop already produces a verdict. The plan never answers: what decision does the ensemble change, and what metric does it move (verdict reversal rate? thesis-kill rate? time-to-confidence)? "Defends against single-model fallacy" is internal storytelling, not an outcome. A machine that produces happy customers is measured by the customer's next action — this plan measures itself by artifacts shipped.

**R2 — The ensemble output has no wired decision hook (BLOCKER).**
Trace the actual flow: `capital model-thinking run` → ensemble-result JSON (robust / condition-dependent / explicit-disagreement) → …then what? The plan's own skill workflow says "recalculate Kelly, convexity, margin safety, model health" and "produce a model-implied recommendation. Let margin danger override Kelly" — but the Monocle report's 13 sections, the verdict enum, and the margin-danger-override logic are NOT in scope. There is no specified artifact that consumes the ensemble result. A robust_conclusion that never touches the Verdict section is a museum piece. The user does nothing differently because the ensemble ran. This is the definition of output that doesn't change behavior.

**R3 — AI-Tourism veto on 5 of the 8 models (VETO recommended).**
Page's own grounding doc says the ensemble sweet spot is **5–7 models** and that marginal benefit falls off after that — but look at what the 8 are doing for a capital-decision user:
- **Justified by the decision loop:** power_law (gates Kelly/Sharpe validity when α≤2 — this is a real input to an existing engine), Schelling-like path-dependence intuition via Polya (path dependence → position sizing under increasing returns), bandits (explore/exploit ≈ add-to-winner vs. rebalance decisions).
- **Tourism:** SIR (epidemic spread of *disease* — the reference file stretches to "spread of information," which is Bass's job anyway), Bass (new product adoption — the user has no new-product decision), Blotto (zero-sum multi-front allocation — the portfolio is not a zero-sum game), NK landscapes (genotype fitness — cute, unusable), Markov (market regimes is plausible but is not specified against a real regime question).
SIR, Bass, Blotto, NK = 4 full M/L-complexity artifacts, each with tests and fixtures, justified by "Page teaches it." That is building the syllabus, not the product. Page's diversity mechanism needs models that *disagree about the user's thesis*, not models that check every pedagogical box.

**R4 — No human has ever run a Page ensemble on a real thesis here (2-4-10 violation).**
The plan's validation is entirely synthetic: fixtures, unit tests, schema conformance. Zero design-partner exposure. Per the 2-4-10 rule, before this much code exists there should be at least 2 real uses: take 2 real tracked theses (from TRACKED.md), run the 3 highest-value models by hand or via throwaway script, and see whether robust/disagreement structure actually changes the verdict the existing engines produced. If it doesn't, the correct build is the power-law gate alone — one file, one real metric (Kelly-invalidated flags raised). The plan inverts this: it builds 28 artifacts and leaves customer truth to "final validation" (a pytest run).

**R5 — Smoke test absence: no single end-to-end moment of value defined.**
Every phase gate is internal ("imports successfully," "tests pass," "schema is valid JSON Schema," "skill loads without error"). Nowhere does the plan say the sentence: *the user asks "analyze NVDA", and the Monocle report now contains a Many-Model section showing one robust conclusion, one condition-dependent split, and one explicit disagreement that the user weighs before deciding.* There is no integration/smoke test artifact, no golden end-to-end fixture from thesis → ensemble → consumed output. Unit tests passing while the feature changes no decision is a fully possible terminal state of this plan.

---

## Architecture Critique

- **The scope is a curriculum, not a product.** 8 models × (module + tests + fixtures) + router skill + 8 reference files + DLC pack + schema + registration + docs = the shape of "digitize the textbook." Taylor test: could we ship the *one* outcome (distributional-assumption gating of Kelly + a 3-model disagreement readout) in a fifth of the artifacts and learn from the user? Yes. Then build more only if the user reaches for it. Do not digitize the Yellow Pages — disassemble the Lego set and keep the two bricks that hold weight.
- **The ensemble layer is specified before its consumer.** `ensemble-result.v1` is designed "standalone" with an open question about whether it should feed decision-analysis. That's the architecture deciding backwards: define what the Verdict/engines section consumes, then shape the schema. An output contract with no consumer contract is where orphaned schemas are born.
- **Correlated-models risk is acknowledged (grounding §9, risk register) but not architected against.** If the router lets the user pick any N models, the likeliest real usage is correlated ones (SIR+Bass are the same difference-equation family; the grounding doc itself says marginal returns collapse past 5–7). Ensembles fail when mistakes are correlated — this plan makes correlated ensembles the path of least resistance. Diversity should be a router constraint, not a documentation note.
- **Committee Mode integration is an open question driving a Phase 3 gate.** "Committee Mode can run multiple DLCs including page and report disagreements" is an acceptance criterion whose mechanism the plan admits it doesn't know. That's a hidden design decision — the exact thing Rule 12 forbids. Resolve the mechanism before writing dlc-page, or cut dlc-page from this plan.
- **Duplicative surface:** a `skills/many-model-thinking` router AND a `dlc-page` lens pack both encode "when to use which model" and "refuse single-model answers." Two homes for one behavior = drift. Pick one (the DLC lens, which sits where the user already gets verdicts), and let the skill be a thin CLI shim.

---

## Missing Specifications

1. **The moment of value (smoke test).** One end-to-end golden path: input = a real (synthetic-body) thesis from the tracked universe; expected output = a named artifact section containing ≥1 robust conclusion, ≥1 condition-dependent split, ≥1 explicit disagreement, and the resulting change (or explicit no-change) to the verdict inputs. Binary: this smoke test passes or the build isn't done.
2. **Decision-consumption contract.** Which existing artifact/schema ingests ensemble results, and what field of the verdict changes. Binary: spec'd or cut the ensemble layer.
3. **The user-outcome metric.** Define it before Phase 1 (candidates: number of verdicts where the ensemble changed the decision input; count of Kelly-invalidated theses caught by the power-law gate). Binary: metric defined and baselined at zero, or no build.
4. **Model-selection diversity constraint.** Router rule: an ensemble must span ≥2 distinct model families (e.g., not SIR+Bass together) and report a correlation flag. Binary gate.
5. **Human-validated precedent.** Two documented manual/throwaway runs of a 3-model ensemble on real TRACKED.md theses, with the verdict-delta recorded, before Phase 2 is authorized. Binary gate.
6. **Power-law gate behavior spec.** α≤2 → what exactly happens downstream today: does the existing Kelly/Sharpe calculation refuse, degrade, or annotate? The plan says "hard router rule" but the consumer-side behavior is undefined. Binary.

---

## Recommended Task Gate Updates

| # | Gate (binary) | Blocks |
|---|---|---|
| G1 | **Customer-outcome PRD exists**: one page naming the user, the job, and the metric the ensemble moves. Fail = no Phase 1. | Phase 1 |
| G2 | **2-thesis validation run**: 2 real TRACKED.md theses, 3-model throwaway ensemble, verdict-delta documented by a human. Fail (no delta) = cut scope to power-law gate only. | Phase 1 completion |
| G3 | **Scope cut executed**: SIR, Bass, Blotto, NK removed from Phase 2 (or individually justified with a named real thesis question each). 8 models → ≤4. | Phase 2 |
| G4 | **Decision-consumption contract written**: ensemble-result consumer identified (Monocle engines/verdict section), fields mapped, verdict-change semantics defined. | Phase 2 (schema) |
| G5 | **End-to-end smoke test artifact added**: golden path thesis → ensemble → consumed output, run in every phase gate. | All phase gates |
| G6 | **Committee Mode mechanism resolved or dlc-page cut**: no Phase 3 work begins on an unknown invocation mechanism. | Phase 3 |
| G7 | **Diversity router rule shipped**: min families per ensemble + correlated-model flag, with a test. | Phase 2 |

---

## Questions for the Human Governor

1. **Name the moment.** Since building this, what question do you expect to ask that the current Kelly/convexity/margin loop answers badly? If the honest answer is "I don't know yet, Page's book was interesting," that is AI Tourism and we should cut to the power-law gate and stop.
2. **Will you read it?** The ensemble output lands where — in the Monocle report, in chat, nowhere yet? If nowhere, we're building a museum exhibit. Where would you actually look before a Buy/Hold/Trim/Add/Sell?
3. **Would you trade a demo for a decision?** I can deliver, in ~one artifact, "power-law tail check that flags when Kelly/Sharpe are invalid for your positions" — a real, wired outcome. The full 8-model Page ensemble is 28 artifacts. Which do you want, in which order? (Exchange of value, not enthusiasm, is the signal.)
4. **Was there a thesis where you felt the existing engines were overconfident?** If yes, give me that thesis — it becomes the 2-thesis validation run (G2) and the smoke test's golden path.
5. **Is the pedagogical value itself a goal?** If you explicitly want the repo to embody Page's full toolkit as a learning artifact, say so and we'll plan it honestly as education, not as decision infrastructure — different gates, different success criteria.

---

*Every objection above maps to a binary gate G1–G7. Recommend: do not proceed to Phase 1 until G1 passes; expect G2 to cut the scope by half or more.*
