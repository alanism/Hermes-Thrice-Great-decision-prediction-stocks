from __future__ import annotations

import importlib


def _scanner():
    return importlib.import_module("capital_decision_lab.privacy.scanner")


def test_advice_and_execution_language_is_detected() -> None:
    issues = _scanner().scan_text(
        "This is a guaranteed buy signal and you should buy.", policy="advice"
    )
    assert {item["match"].lower() for item in issues} >= {
        "guaranteed",
        "buy signal",
        "should buy",
    }


def test_conservative_comparison_language_is_allowed() -> None:
    text = (
        "Under the supplied assumptions, this calculated result is a modeled "
        "estimate for a user-selected exposure. Unavailable due to insufficient "
        "inputs. Comparison only, not financial advice."
    )
    assert _scanner().scan_text(text, policy="advice") == []

