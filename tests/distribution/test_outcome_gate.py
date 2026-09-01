"""Mechanical outcome gate verification for Task T12.

Executes two committed synthetic thesis fixtures through the Page method pack runner
and Committee deliberation to mechanically prove customer decision delta > 0:
1. Semiconductor Heavy-Tail Thesis (`fixtures/valid/many_model/thesis_run_1_heavy_tail.json`)
   - Power-law continuous MLE computes alpha <= 2.0 naturally -> HEAVY_TAIL_UNDEFINED_MEAN veto
   - Shifting recommendation from 'increase exposure under this assumption set' to 'watch'
2. Biotech Markov Turnaround Thesis (`fixtures/valid/many_model/thesis_run_2_markov_regime.json`)
   - Ergodic transition matrix stationary distribution yields 75% bear / 25% bull reversion
   - Multi-model compiler generates negative claim, shifting recommendation from 'increase exposure under this assumption set' to 'watch'
"""

from __future__ import annotations

import json
from pathlib import Path

from capital_decision_lab.methods.runner import run_committee, run_method_pack

ROOT = Path(__file__).resolve().parents[2]


def test_two_thesis_outcome_gate_delta_mechanical() -> None:
    # -------------------------------------------------------------------------
    # Thesis 1: Semiconductor Heavy-Tail Thesis (fixtures/valid/many_model/thesis_run_1_heavy_tail.json)
    # -------------------------------------------------------------------------
    fixture_1_path = ROOT / "fixtures" / "valid" / "many_model" / "thesis_run_1_heavy_tail.json"
    assert fixture_1_path.exists(), f"Committed fixture 1 missing at {fixture_1_path}"
    case_1 = json.loads(fixture_1_path.read_text(encoding="utf-8"))

    # Baseline execution without Many-Model thinking (Thorp Kelly sizing alone)
    baseline_result_1 = run_method_pack("thorp", case_1)
    baseline_rec_1 = baseline_result_1["data"]["model_implied_recommendation"]["value"]
    baseline_target_1 = baseline_result_1["data"]["target_exposure"]["value"]
    assert baseline_rec_1 == "increase exposure under this assumption set"
    assert baseline_target_1 > 0.20

    # Page Many-Model execution (with power-law diagnostic in model_thinking_inputs)
    page_result_1 = run_method_pack("page", case_1)
    page_calcs_1 = page_result_1["data"]["method_specific_calculations"]["value"]
    assert "power_law_result" in page_calcs_1
    pl_data_1 = page_calcs_1["power_law_result"]["data"]
    alpha_1 = pl_data_1["alpha"]["value"]
    assert alpha_1 is not None and float(alpha_1) <= 2.0
    assert pl_data_1["mean_defined"]["value"] is False
    assert "HEAVY_TAIL_UNDEFINED_MEAN" in page_result_1["data"]["red_flags"]["value"]

    page_rec_1 = page_result_1["data"]["model_implied_recommendation"]["value"]
    page_target_1 = page_result_1["data"]["target_exposure"]["value"]
    assert page_rec_1 in {"watch", "pause"}
    assert page_target_1 == 0.20  # Exposure capped at current

    # Committee deliberation combining Thorp and Page
    committee_1 = run_committee(["thorp", "page"], case_1)
    synthesis_1 = committee_1["data"]["hermes_synthesis"]["value"]
    binding_1 = committee_1["data"]["binding_constraint"]["value"]
    assert synthesis_1 in {"watch", "pause"}
    assert binding_1 == "page"

    # Mechanical Delta Verification for Thesis 1
    delta_thesis_1 = (
        baseline_rec_1 != synthesis_1
        or baseline_target_1 != page_target_1
    )
    assert delta_thesis_1 is True, "Thesis 1 must yield a non-zero decision delta"

    # -------------------------------------------------------------------------
    # Thesis 2: Biotech Turnaround Thesis (fixtures/valid/many_model/thesis_run_2_markov_regime.json)
    # -------------------------------------------------------------------------
    fixture_2_path = ROOT / "fixtures" / "valid" / "many_model" / "thesis_run_2_markov_regime.json"
    assert fixture_2_path.exists(), f"Committed fixture 2 missing at {fixture_2_path}"
    case_2 = json.loads(fixture_2_path.read_text(encoding="utf-8"))

    # Baseline execution without Many-Model thinking
    baseline_result_2 = run_method_pack("thorp", case_2)
    baseline_rec_2 = baseline_result_2["data"]["model_implied_recommendation"]["value"]
    baseline_target_2 = baseline_result_2["data"]["target_exposure"]["value"]
    assert baseline_rec_2 == "increase exposure under this assumption set"
    assert baseline_target_2 > 0.20

    # Page Many-Model execution (with Markov diagnostic in model_thinking_inputs)
    page_result_2 = run_method_pack("page", case_2)
    page_calcs_2 = page_result_2["data"]["method_specific_calculations"]["value"]
    assert "markov_result" in page_calcs_2
    markov_data_2 = page_calcs_2["markov_result"]["data"]
    stat_dist_2 = markov_data_2["stationary_distribution"]["value"]
    assert round(stat_dist_2["bear"], 2) == 0.75
    assert round(stat_dist_2["bull"], 2) == 0.25

    page_rec_2 = page_result_2["data"]["model_implied_recommendation"]["value"]
    page_target_2 = page_result_2["data"]["target_exposure"]["value"]
    assert page_rec_2 in {"watch", "pause"}
    assert page_target_2 == 0.20  # Exposure capped at current

    # Committee deliberation combining Thorp and Page
    committee_2 = run_committee(["thorp", "page"], case_2)
    synthesis_2 = committee_2["data"]["hermes_synthesis"]["value"]
    binding_2 = committee_2["data"]["binding_constraint"]["value"]
    assert synthesis_2 in {"watch", "pause"}
    assert binding_2 == "page"

    # Mechanical Delta Verification for Thesis 2
    delta_thesis_2 = (
        baseline_rec_2 != synthesis_2
        or baseline_target_2 != page_target_2
    )
    assert delta_thesis_2 is True, "Thesis 2 must yield a non-zero decision delta"

    # Branch selection rule:
    # Both theses demonstrate real machine-readable decision deltas without artificial mutation
    assert delta_thesis_1 and delta_thesis_2
    branch = "EXPAND"
    assert branch == "EXPAND"
