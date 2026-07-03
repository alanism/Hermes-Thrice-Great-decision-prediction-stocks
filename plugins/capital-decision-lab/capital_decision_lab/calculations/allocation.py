"""Kelly-based exposure calculations from explicit supplied inputs."""

from __future__ import annotations

import math

from capital_decision_lab.contracts.validation import unavailable_result


def _atom(value: float, formula_ref: str, refs: list[str]) -> dict:
    return {
        "value": value,
        "provenance_class": "calculated",
        "unit": "capital fraction",
        "input_refs": refs,
        "formula_ref": formula_ref,
        "limitations": ["Depends entirely on supplied probability and odds"],
    }


def _base(probability: float, net_odds: float) -> tuple[float | None, str | None]:
    if (
        not isinstance(probability, (int, float))
        or isinstance(probability, bool)
        or not math.isfinite(float(probability))
        or probability < 0
        or probability > 1
    ):
        return None, "probability must be between zero and one"
    if (
        not isinstance(net_odds, (int, float))
        or isinstance(net_odds, bool)
        or not math.isfinite(float(net_odds))
        or net_odds <= 0
    ):
        return None, "net odds must be greater than zero"
    loss_probability = 1.0 - float(probability)
    return (float(net_odds) * float(probability) - loss_probability) / float(net_odds), None


def kelly(probability: float, net_odds: float) -> dict:
    value, reason = _base(probability, net_odds)
    if reason:
        return unavailable_result(reason, unit="capital fraction", input_refs=["win_probability", "net_odds"])
    return _atom(value, "allocation.kelly.v1", ["win_probability", "net_odds"])


def fractional_kelly(probability: float, net_odds: float, fraction: float) -> dict:
    value, reason = _base(probability, net_odds)
    if reason:
        return unavailable_result(reason, unit="capital fraction", input_refs=["win_probability", "net_odds", "kelly_fraction"])
    if (
        not isinstance(fraction, (int, float))
        or isinstance(fraction, bool)
        or not math.isfinite(float(fraction))
        or not 0 < fraction <= 1
    ):
        return unavailable_result("fraction must be greater than zero and at most one", unit="capital fraction", input_refs=["kelly_fraction"])
    return _atom(value * float(fraction), "allocation.fractional_kelly.v1", ["win_probability", "net_odds", "kelly_fraction"])


def capped_fractional_kelly(
    probability: float,
    net_odds: float,
    fraction: float,
    exposure_cap: float,
) -> dict:
    fractional = fractional_kelly(probability, net_odds, fraction)
    if fractional["provenance_class"] == "unavailable":
        return fractional
    if (
        not isinstance(exposure_cap, (int, float))
        or isinstance(exposure_cap, bool)
        or not math.isfinite(float(exposure_cap))
        or not 0 <= exposure_cap <= 1
    ):
        return unavailable_result("exposure cap must be between zero and one", unit="capital fraction", input_refs=["exposure_cap"])
    value = min(max(float(fractional["value"]), 0.0), float(exposure_cap))
    return _atom(
        value,
        "allocation.capped_fractional_kelly.v1",
        ["win_probability", "net_odds", "kelly_fraction", "exposure_cap"],
    )
