# NotebookLM Grounding — Scott E Page Notebook (083ca6cf-8d45-4a1b-a7b8-c80f82f9faf9)

Queried via `notebooklm ask` (conversation b879514b), 7 rounds, 2026-09-01.
These notes ground the math and skill design for the Many-Model Thinking extension. Each claim traces to the notebook's answer (sources: Model Thinking course, Complexity lectures, Miller & Page textbook, Page's talks).

## 1. Markov (stationary distribution)
- Formulation: transition matrix M, entry P(A,B); Page's convention: columns = distribution at t, rows = distribution at t+1.
- Convergence (Perron–Frobenius / Markov Convergence Theorem) requires FOUR conditions: (1) finite states, (2) fixed transition rule, (3) ergodicity, (4) non-cyclic.
- Stationary distribution: solve p* = M p*. Two-state example (engaged/bored): 90% stay engaged, 30% of bored become engaged → equilibrium 75/25.
- **Decision insight**: long-run outcomes independent of initial state/history. One-off state interventions wash out; only changing the transition probabilities changes the equilibrium.
- Engine note: check all four convergence conditions, not just ergodicity; report non-convergence as `unavailable` with reason.

## 2. Power-law vs normal
- Diagnostic: log-log plot of event size vs probability. Straight line = power law p(x)=Cx^(-a). Initially straight then curving downward = lognormal/exponential.
- Domains: normal (heights, test scores, daily sales — independent additive events); power-law (city sizes, firm sizes, book sales, war casualties — positive feedback).
- Decision impact: normal → 95% within ±2σ, mean representative. Power-law with a ≤ 2 → NO convergent mean, infinite variance. Assuming normality in a power-law domain catastrophically underestimates extremes.
- Heuristic Page stresses: Rule of 72 (compounding → inequality). Periods to double ≈ 72/R.
- Engine note: report alpha estimate, tail classification, and EXPLICITLY flag when mean/variance are not well-defined (a ≤ 2) — downstream Kelly/Sharpe math is invalid there.

## 3. Spreading models (SIR / Bass)
- Page teaches DISCRETE-TIME difference equations (not just continuous ODEs):
  - S(t+1) = S − P_contact·P_spread·(I/N)·S
  - I(t+1) = I + P_contact·P_spread·(I/N)·S − P_recover·I
  - R(t+1) = R + P_recover·I
  - β = P_contact·P_spread, γ = P_recover
- R0 = β/γ = (P_contact·P_spread)/P_recover. R0 > 1 spreads; R0 < 1 dissipates. Vaccination threshold V ≥ 1 − 1/R0.
- Bass diffusion: I(t+1) = I + p·S + q·(I/N)·S, where p = P_broad (innovation/broadcast), q = P_diffuse (imitation). High q → S-shaped curve (seed influencers); high p → r-shaped (mass advertising).
- **Decision insight**: R0 is a contextual tipping point; target individual parameters rather than treating the system as uncontrollable.

## 4. Schelling segregation
- Setup: two agent types on M×M grid with vacancies; each agent checks its Moore neighborhood (8 adjacent squares); relocates to a random vacant square if same-type % < personal tolerance T_i.
- Cascades via "genesis tips" (new arrival pushes a resident below threshold) and "exodus tips" (departure lowers remaining residents' ratio).
- **Core lesson**: macro outcomes ≠ micro tolerances. T = 30% tolerance agents end up in ~70–72% same-type neighborhoods. Heterogeneous thresholds make tipping more likely but prevent 100% segregation (tolerant border agents stay put).
- Engine note: seed the initial placement AND relocation order; report tolerance distribution and realized segregation index, not just the final grid.

## 5. Colonel Blotto
- Setup: two players allocate fixed budgets W_A, W_B across N battlefields simultaneously; higher allocation wins each front; majority of fronts wins the game.
- No pure-strategy equilibrium — any predictable allocation is exploitable → mixed strategies required.
- **Underdog insight**: W_A < W_B can win by conceding selected fronts (zero allocation) and concentrating on a majority of the rest. As N grows, the resource-rich player's advantage shrinks (over-dispersion).
- Applies to: zero-sum multi-front resource allocation — marketing across regions, legal defenses, portfolio attention allocation.

## 6. Polya process / path dependence
- Urn rule: start (1 white, 1 gray); draw one, return it PLUS another of the same color.
- Equilibrium: uniform over final proportions — after 1000 periods, 40% white is as probable as 2%. Path decides the attractor.
- Page's taxonomy: outcome path dependence (t+1 shaped by history) vs equilibrium path dependence (the steady state itself depends on the path). Increasing returns (positive feedback) drives both; balancing (negative feedback) processes show outcome path dependence but converge to symmetric 50-50 (no equilibrium path dependence).
- Engine note: run multi-trial with seed; report the spread of terminal proportions across trials — the uniform spread IS the finding.

## 7. Bandits / explore-exploit
- Explore-exploit tradeoff: each pull = immediate payoff (exploit) + data (explore).
- Gittins index = expected immediate reward + discounted expected value of future rewards under optimal subsequent play given new information. Optimal = pull largest Gittins index.
- Heuristics Page contrasts: greedy (myopic, ignores information value) vs sample-then-greedy (M trials per arm, then exploit best) vs adaptive exploration rate (trial chunks proportional to success rates).
- **Decision insight**: pull the arm with best payoff+information-value combination, not highest immediate payoff. Organizations chronically under-explore.

## 8. NK / rugged landscapes
- Solution s ∈ {0,1}^N. Fitness V(s) = Σ V_i(s_i, {s_ik}) where {s_ik} = K randomly chosen other bits; each V_i drawn uniformly for each of 2^(K+1) configurations.
- K=0 → smooth single-peak "Mount Fuji" (hill-climbing works). K=N−1 → fully random, maximally rugged.
- Local peak: all single-flip neighbors lower. Higher K → higher global peak (synergies) but exponentially more local optima.
- Dancing landscape: OTHER actors' moves shift your landscape's peaks (co-evolution).
- **Decision insight**: stable rugged problems → deep centralized long-term investment; dancing landscapes → rapid decentralized adaptation. Escaping local optima requires cognitive diversity (diverse encodings + diverse search heuristics).

## 9. The ensemble argument (Diversity Prediction Theorem)
- Identity: **Crowd/Ensemble Error = Average Error − Diversity of Predictions.** Ensemble error ≤ average individual model error, always.
- Ensembles fail when: (a) model mistakes are CORRELATED (shared frameworks → shared blind spots), (b) models share a structural bias (amplified by averaging), (c) attribute correlations limit true model diversity — **marginal benefit falls off after ~5–7 models**.
- Page's rules: avoid single-model hubris; treat models as a latticework crisscrossing the possibility space; do NOT settle for raw voting/averaging — deep deliberation on where models overlap and DIVERGE, using contradictions to expose hidden assumptions.

## 10. Concavity/convexity, betting, simulation discipline
- Concave = diminishing returns → risk aversion; convex = accelerating returns → risk-seeking. K=0 concave structure → smooth landscape; interdependency ruggedizes.
- Page's sources do NOT mention Kelly sizing — do not attribute Kelly to Page. Related Page result: in negative-EV games, ONE large bet beats many small bets (maximizes P(profit) before the law of large numbers locks in aggregate loss).
- Simulation discipline: PRNGs must be tied to a FIXED SEED so simulations are fully repeatable; anomalies are traced by "rerunning the tape" from the same initial state.
- Qualitative vs quantitative rules: Stakes Rule (heuristics for low stakes, formal optimization for high stakes); Granularity Rule (quantitative for big-data prediction, simple models for core dynamics); Multi-Lens Blend (big data + thick data).

## Implications for the build plan / skill (grounded corrections)
1. **Markov convergence check**: test all four Page conditions (finite, fixed, ergodic, non-cyclic), not just power-iteration convergence.
2. **Power-law check must gate downstream math**: if tail classification says a ≤ 2, flag that mean/variance-based engines (Sharpe, Kelly) are not well-defined — this becomes a hard router rule in the skill.
3. **SIR/Bass in discrete-time difference-equation form** with Page's P_contact/P_spread/P_recover parameterization (more interpretable for decision work than raw β/γ); report R0 and the V ≥ 1−1/R0 threshold.
4. **Schelling**: seed placement + relocation order; heterogeneous tolerances; report realized segregation vs individual tolerance — the macro≠micro gap is the output.
5. **Blotto**: mixed strategies only; include the underdog concentration analysis as a named output.
6. **Polya**: distinguish outcome vs equilibrium path dependence; multi-trial spread is the deliverable.
7. **Bandits**: offer greedy / sample-then-greedy / adaptive-ε variants per Page; Gittins index mentioned conceptually, not required.
8. **Ensemble synthesis**: 5–7 models is the evidence-backed sweet spot; disagreement ≠ noise, it's the mechanism (diversity term of the theorem). Correlated models must be flagged.
9. **Skill must NOT attribute Kelly to Page**; the negative-EV single-large-bet result is Page's own adjacent insight and may be reported as such.
10. **All stochastic models fixed-seed** — now directly grounded in Page's own simulation discipline, strengthening constraint C4.
