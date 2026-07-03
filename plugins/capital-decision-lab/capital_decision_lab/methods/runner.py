"""Run method packs as deterministic overlays on the shared analysis substrate."""

from __future__ import annotations

from capital_decision_lab.contracts.canonical import canonical_sha256, contract_payload_hash
from capital_decision_lab.evidence.common import atom
from capital_decision_lab.orchestration.analyze import analyze_case

from .packs import PACKS


def available_method_packs() -> list[str]:
    return sorted(PACKS)


def _value(analysis: dict, name: str, default=0.0):
    value = analysis.get("data", {}).get(name, {}).get("value")
    return default if value is None else value


def run_method_pack(pack_id: str, case_bundle: dict, *, base_result: dict | None = None) -> dict:
    if pack_id not in PACKS or pack_id == "committee":
        raise ValueError("METHOD_PACK_UNKNOWN")
    case = case_bundle.get("decision_case", case_bundle)
    analysis = (base_result or {}).get("analysis") or analyze_case(case)
    portfolio = case_bundle.get("portfolio")
    thesis = case_bundle.get("thesis")
    missing = [name for name, value in (("portfolio", portfolio), ("thesis", thesis)) if not value]
    flags: list[str] = []
    modifiers = list(PACKS[pack_id]["recommendation_modifiers"])
    evidence_used: list[str] = []
    current = float((portfolio or {}).get("positions", [{}])[0].get("position_weight", 0.0))
    recommendation = "hold current exposure"
    confidence = float(case_bundle.get("method_inputs", {}).get("evidence_quality", 0.5))
    target = current
    calculations = {"shared_analysis_hash": analysis["canonical_hash"]}

    if pack_id == "thorp":
        full = float(_value(analysis, "full_kelly_fraction"))
        fraction = 0.25 if confidence < 0.4 else 0.5
        target = max(0.0, min(float(_value(analysis, "capped_exposure", full)), full * fraction))
        rows = _value(analysis, "margin_stress_table", []) or []
        margin_danger = float(_value(analysis, "liquidation_buffer_percent", 0.0)) <= 0 or any(row.get("maintenance_breach") for row in rows)
        if margin_danger:
            recommendation = "avoid margin"; flags.append("MARGIN_SURVIVAL_BINDING")
        elif target < current:
            recommendation = "trim to fractional Kelly"
        elif target > current:
            recommendation = "increase exposure under this assumption set"
        calculations.update({"full_kelly": full, "kelly_fraction_applied": fraction, "max_leverage": float(case_bundle.get("method_inputs", {}).get("max_leverage", 2.0))})
    elif pack_id == "mauboussin":
        probabilities = (thesis or {}).get("probabilities")
        if not isinstance(probabilities, dict) or any(not isinstance(value, (int, float)) for value in probabilities.values()):
            flags.append("NUMERICAL_PROBABILITIES_REQUIRED"); missing.append("numerical_probabilities"); recommendation = "pause"
        base_rate = case_bundle.get("method_inputs", {}).get("base_rate")
        user_probability = probabilities.get("bull") if isinstance(probabilities, dict) else None
        if isinstance(base_rate, (int, float)) and isinstance(user_probability, (int, float)) and user_probability - base_rate >= 0.15:
            flags.append("BASE_RATE_OVERCONFIDENCE"); recommendation = "watch"
        calculations.update({"base_rate": base_rate, "user_bull_probability": user_probability})
    elif pack_id == "contrarian_filings":
        filings = [item for item in case_bundle.get("filing_evidence", []) if item.get("source_type") == "filings" and item.get("verification_status") in {"auto_retrieved", "user_verified", "user_corrected"}]
        if not filings:
            flags.append("PRIMARY_FILINGS_REQUIRED"); missing.append("primary_filings"); recommendation = "watch"
        else:
            evidence_used.append("filings")
        calculations["verified_filing_count"] = len(filings)

    result = {
        "contract_version": "nhi.method_pack_result.v1",
        "result_id": f"method_result_{canonical_sha256([pack_id, contract_payload_hash(case_bundle)])[:16]}",
        "pack_id": pack_id, "pack_name": PACKS[pack_id]["display_name"],
        "case_hash": contract_payload_hash(case_bundle),
        "data": {
            "inputs_used": atom([name for name in ("portfolio", "thesis") if name not in missing], "calculated"),
            "missing_inputs": atom(sorted(set(missing)), "calculated"),
            "evidence_used": atom(evidence_used, "calculated"),
            "method_specific_calculations": atom(calculations, "calculated"),
            "red_flags": atom(flags, "modeled"), "recommendation_modifiers": atom(modifiers, "modeled"),
            "model_implied_recommendation": atom(recommendation, "modeled"),
            "target_exposure": atom(target, "modeled", unit="capital fraction"),
            "full_kelly": atom(float(_value(analysis, "full_kelly_fraction")), "calculated", unit="capital fraction"),
            "confidence": atom(confidence, "modeled", unit="score"),
        },
        "limitations": PACKS[pack_id]["limitations"], "required_user_authorization": True,
    }
    result["canonical_hash"] = contract_payload_hash(result)
    return result


def run_committee(pack_ids: list[str], case_bundle: dict) -> dict:
    if not pack_ids:
        raise ValueError("METHOD_PACKS_REQUIRED")
    results = [run_method_pack(pack_id, case_bundle) for pack_id in pack_ids]
    recommendations = [item["data"]["model_implied_recommendation"]["value"] for item in results]
    agreement = len(set(recommendations)) == 1
    priority = ["avoid margin", "pause", "trim to fractional Kelly", "watch", "hold current exposure", "increase exposure under this assumption set"]
    synthesis = next((item for item in priority if item in recommendations), recommendations[0])
    binding = next((item["pack_id"] for item in results if item["data"]["model_implied_recommendation"]["value"] == synthesis), results[0]["pack_id"])
    document = {
        "contract_version": "nhi.committee_result.v1", "committee_id": f"committee_{canonical_sha256([pack_ids, contract_payload_hash(case_bundle)])[:16]}",
        "pack_results": results,
        "data": {"agreement": atom(agreement, "calculated"), "disagreement": atom([] if agreement else recommendations, "calculated"),
                 "strongest_add_case": atom(next((item["pack_id"] for item in results if "increase exposure" in item["data"]["model_implied_recommendation"]["value"]), None), "modeled"),
                 "strongest_trim_case": atom(next((item["pack_id"] for item in results if item["data"]["model_implied_recommendation"]["value"] in {"avoid margin", "trim to fractional Kelly"}), None), "modeled"),
                 "strongest_hold_watch_case": atom(next((item["pack_id"] for item in results if item["data"]["model_implied_recommendation"]["value"] in {"hold current exposure", "watch"}), None), "modeled"),
                 "binding_constraint": atom(binding, "modeled"), "hermes_synthesis": atom(synthesis, "modeled")},
        "required_user_action": "Review the synthesis and explicitly authorize any decision record.",
        "required_user_authorization": True,
    }
    document["canonical_hash"] = contract_payload_hash(document)
    return document
