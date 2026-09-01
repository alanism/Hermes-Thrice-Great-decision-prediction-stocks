# [T] Bret Taylor — Round 2 Cross-Examination (Product-Outcome Lens)

**Reviewer F.** Judging the merged packet M1–M11 through one question: *does this build a machine that produces happy customers, or a machine that produces artifacts?*

---

## 1. Strongest findings — MUST be enforced as gates

**M10 is the spine; everything else is scaffolding around it.** I raised it blind (as did E) and the merged packet confirms it: no named customer outcome, no wired decision hook, no smoke test, no human validation run. Concretely, I enforce:

- **G1 — Customer-outcome PRD** (user, job, metric) before Phase 1. "Defends against single-model fallacy" is internal storytelling (Rule 11), not an outcome.
- **G2 — 2-thesis validation run** on real TRACKED.md theses before Phase 2. If the verdict-delta is zero, the honest build is the power-law gate alone. This is the 2 in 2-4-10, and it is cheap — throwaway script, not 28 artifacts.
- **G4 — Decision-consumption contract.** An `ensemble-result.v1` with no consumer is a museum piece. Name the artifact/field it changes or cut the ensemble layer.
- **G5 — End-to-end smoke test** as the moment of value, run at every phase gate.

**M5 (ensemble aggregation has no computation site) is the second must-enforce.** E and A are right that an LLM assembling the flagship output makes canonical_hash provenance theater. From my seat the sharper framing: an LLM-computed ensemble result is a *hidden design decision machine* — the consumer contract (G4) is meaningless if the thing it consumes is regenerated differently each run. Deterministic compiler over an Ensemble IR. Gate: build/validate an `ensemble-result.v1` instance in a test, not in prose.

**M2 (green-then-Red; no eval-tamper defense) — enforce.** Same agent writing implementation and tests is the internal equivalent of grade-your-own-homework. Failing-test-first artifact + mutation check or independent verifier. Binary.

**M4 (fake unknowns, hallucinated subcommands).** "Answerable by repo probes" means the plan lets the implementing agent invent interfaces — that is Rule 12's forbidden hidden design decision, laundered through an "Open Questions" section. Enforce: every open question resolved by probe or deleted; Artifact 17's `capital model-thinking run` fixed to the real `capital method run --pack`.

**M8 (validation as prose, not tests).** Enforce the `simulation.py` rejection pattern (isfinite, bool exclusion, unavailable_result) as mandated tests per module, and dimension caps as runtime checks. "Capped in documentation" is prompt-security, and from the customer side an unbounded run is a hang — the user never gets their verdict.

## 2. Wrong or over-weighted

- **M1 (schema target) — right diagnosis, wrong weight as a top gate.** It is a lookup fix, not an architectural risk: point conformance at `$defs.atom`, decide `input_trust_class`, done in an afternoon. Enforce it, but it does not belong in the top tier alongside M5/M10. Also flag: renaming the enum is a spec edit, not a security control — it only matters if the *engine layer actually refuses* attacker-class inputs (see C's single-reviewer finding, which I promote to enforced).
- **M3 (seed=None) — over-weighted as written.** Real issue, real reproducibility gate (C4 untestable otherwise; seeded floats entering canonical_hash is a genuine determinism hole per M11). But the hostile-seed semantics sub-point (string/bool seeds) is an edge case nobody's customer hits; fold it into a typed-seed contract and stop. Severity: medium, one gate, not three.
- **M9 (spec contradictions) — substantially correct but padded.** The Markov convergence conditions, SIR Euler-negative problem, and bandit algorithm mismatch are real build-blocking spec errors and must be fixed against the grounding doc. But Polya multi-trial and Blotto enumeration blowup are *consequences of the scope problem* (M10/R3): if we cut SIR/Bass/Blotto/NK, half of M9 evaporates. Fix the spec errors for the models we keep; don't polish the syllabus.
- **M7 (adversarial fixtures) — right instinct, over-weighted at 10 fixtures for 8 pedagogical models.** Adversarial fixtures earn their cost where money is computed (power-law gate, bandits, injected evidence). After the M10 scope cut, this is a handful of tests, not a fixture program.
- **M11 (determinism) — the bit-exact/tolerance policy and version pin are enforceable and cheap; the "aspirational vibes" critique is fair but is really the same complaint as M8 (prose instead of binary). Merge into one gate.

## 3. Still missing

1. **Injection loop governance** (C, single-reviewer). Untrusted extracted evidence becomes numeric parameters that feed back into agent context as "validated" conclusions — with no rule on which provenance classes may populate engine parameters, and free-text ensemble fields as an unbounded echo channel. I under-weighted this in Round 1; it is a customer-trust failure (garbage verdicts that look authoritative), and I adopt C's fix as a gate. M1's `input_trust_class` is the *label*; C's rule is the *enforcement*. Both needed.
2. **Machine-readable α≤2 gate** (D). The power-law gate is the one model I'd defend as unambiguously wired to a real decision — so its invalidity signal must be schema data, not router prose. Downstream Kelly/Sharpe refusal must be compiler-enforced. This is G6 in my Round 1 list; it survives the scope cut.
3. **Correlated-models constraint** (my Round 1 architecture critique, absent from the merge). Router rule: ensembles span ≥2 distinct model families with a correlation flag. After cutting SIR+Bass-family overlap this matters *more*, not less — with 4 models, two correlated ones are half the ensemble and disagreement is theater.
4. **Early full-suite regression gate** (B). Existing tests only gated at Phase 4 means regressions surface two phases late. Cheap: run the suite at every phase gate alongside G5.
5. **Primary-source check on the "5–7 sweet spot"** (E) — agreed; if we cite a number as a build constraint we test it or delete it. Also the token/cache budget (E): 8 reference files + skill + DLC threatens the byte-exact prefix; set a token budget gate.

## 4. Human governor decisions

1. **The moment.** What question do you expect to ask that the Kelly/convexity/margin loop answers badly? Honest answer "none yet" ⇒ cut to the power-law gate and stop. That is a legitimate outcome, not a failure.
2. **Where you'll read it.** If the ensemble output has no landing spot in your pre-trade ritual, G4 cannot pass and we build a museum. Name the surface.
3. **Scope trade.** One artifact ("power-law tail check flags Kelly/Sharpe invalidity") vs. 28 artifacts (full 8-model Page ensemble). Money-equivalent exchange says deliver the first, earn the second.
4. **Pedagogy as a declared goal.** If the repo is meant to embody Page's toolkit as education, re-plan it honestly as education — different gates, no decision-consumption contract required, AI-Tourism veto withdrawn.
5. **Seed contract:** confirm bit-exact determinism is actually required for the ensemble layer (C4 says yes; if not, scope the pin out) — this decides how heavy M3/M11 enforcement is.

---

# Round 3 — Final Risk Register

Binary executable gates only. Ordering: customer outcome first, correctness of the money path second, mechanism third.

| Risk | Severity | Evidence | Prevention | Task Gate Check | Blocks Build? |
|---|---|---|---|---|---|
| No named customer outcome; ensemble output consumed by nothing | CRITICAL | M10 (F,E); plan has no user-outcome metric, no consumer of `ensemble-result.v1` | Customer-outcome PRD (user/job/metric) + decision-consumption contract naming the consuming artifact and verdict-field semantics | G1: PRD exists w/ metric baselined at 0; G4: consumer + field mapping written before schema work | YES — Phase 1 |
| Ensemble result computed freehand by LLM (provenance theater) | CRITICAL | M5 (B,C,A): no computation site for `ensemble-result.v1`; skill step 8 is LLM→final-artifact | Deterministic compiler over Ensemble IR; schema instance built+validated in test | G5: test builds a valid ensemble-result.v1 from fixture IR; no LLM in the path | YES — Phase 2 |
| No human validation before 28 artifacts exist | CRITICAL | M10/R4: all validation synthetic; zero design-partner exposure | 2-thesis run on real TRACKED.md theses, verdict-delta documented by human | G2: 2 runs recorded w/ deltas; zero delta ⇒ scope cut to power-law gate | YES — Phase 2 |
| No end-to-end moment of value; unit tests pass while no decision changes | HIGH | M10/R5; all phase gates internal (imports, pytest) | Golden-path smoke test: thesis → ensemble → consumed output, run every phase | G5b: smoke test binary in every phase gate | YES — all phases |
| Spec contradicts grounding doc (Markov convergence, SIR Euler-negative, bandit algorithms) | HIGH | M9 (D,B); grounding requires 4 convergence conditions, discrete SIR equations, greedy/adaptive-ε | Spec conformance pass against grounding doc for models that survive the scope cut | G6: per-model conformance checklist checked, contradictions resolved in writing | YES — Phase 2 |
| Wrong schema target; untrusted evidence indistinguishable in engine params | HIGH | M1 (A,C,E); C's injection loop finding | Conformance target = `$defs.atom`; `input_trust_class` in enum AND engine layer rejects attacker-class params; free-text ensemble fields length-bounded | G7: schema conformance test passes; engine-rejection test for untrusted-class params passes | YES — Phase 2 |
| Tests written after implementation; self-graded evals | HIGH | M2 (A,B,D,E); no failing-test-first artifact; `tests/mutation/` unused | Failing-test-first artifact per phase; mutation check or independent verifier | G8: red-first artifact present; ≥1 mutation survives naive test suite in CI log | YES — each phase |
| Fake open questions force interface hallucination | HIGH | M4 (A,B,D); Artifact 17's nonexistent `capital model-thinking run` | Probe-answered spec: `allocation.py:41`, `plugin/commands.py`, `capital method run --pack` | G9: zero TBD/implicit-default entries; Artifact 17 command matches registry | YES — Phase 1 |
| Input validation is prose; unbounded dimensions hang the run | HIGH | M8 (C,D) | `simulation.py` rejection pattern (isfinite, bool-exclusion, unavailable_result) mandated per module; runtime caps on NK n, Markov size, SIR days, bandit horizon | G10: per-module rejection tests exist and pass; cap-violation input returns typed error | YES — Phase 2 |
| α≤2 invalidity is router prose, not schema data; Kelly/Sharpe silently valid | HIGH | D single-reviewer; M9 | α gate as machine-readable schema field; downstream refusal is compiler-enforced | G11: schema asserts α≤2; Kelly test fails when fed α=2.5 result | YES — Phase 2 |
| Correlated ensembles are the path of least resistance | MEDIUM | Round 1 architecture critique; grounding §9 marginal-returns collapse | Router rule: ≥2 distinct model families per ensemble + correlation flag | G12: router rejects single-family ensemble w/ test | YES — Phase 2 |
| `seed=None` default breaks reproducibility (C4); seeded floats into canonical_hash | MEDIUM | M3 (A,C,D) | Keyword-only int seed required everywhere; typed-seed contract; deterministic float serialization pinned | G13: two identical runs produce byte-identical artifact + hash | YES — Phase 2 |
| No determinism/version policy; aspirational ACs | MEDIUM | M11 (D,A) | CPython pin; bit-exact vs tolerance policy per check; ACs rewritten binary | G14: policy doc + every AC binary-checkable | YES — Phase 1 |
| Regression caught two phases late | MEDIUM | B single-reviewer | Full existing suite at every phase gate, not Phase 4 | G15: suite green in each phase gate log | YES — all phases |
| Pedagogical models shipped without decision mandate (SIR, Bass, Blotto, NK) | MEDIUM | M10/R3; Page 5–7 sweet spot (E: verify primary source) | Cut to ≤4 decision-relevant models, or each survivor names a real thesis question | G3: scope cut executed or per-model justification accepted | YES — Phase 2 |
| Context bloat breaks byte-exact cache prefix | LOW | E single-reviewer | Token budget for skill+references+DLC | G16: budget measured under limit | NO — Phase 3 |
| Adversarial fixtures absent | LOW (post-scope-cut) | M7 (C,E,D) | Adversarial fixtures for money-path models only (power-law, bandits, injected evidence) | G17: adversarial fixture suite green | NO — Phase 2 exit |

**Governor gates that block everything:** G1 (PRD), G2 (2-thesis run). If G2 shows zero verdict-delta, the correct deliverable is G11 (power-law gate) alone — one artifact, one real metric — and the plan is rewritten, not resumed.
