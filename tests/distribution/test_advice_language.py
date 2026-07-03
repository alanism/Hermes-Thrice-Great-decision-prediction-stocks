from __future__ import annotations

import importlib
from pathlib import Path


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


def test_root_readme_advice_disclaimer_exemption_is_narrow(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("recommend securities", encoding="utf-8")
    report = tmp_path / "reports" / "result.md"
    report.parent.mkdir()
    report.write_text("recommend securities", encoding="utf-8")
    issues = _scanner().scan_repository(tmp_path, policy="advice")
    assert issues
    assert all(Path(item["path"]).name == "result.md" for item in issues)


def test_stock_exposure_advice_phrases_are_detected() -> None:
    text = (
        "recommended position; optimal investment; the stock will rise; "
        "guaranteed upside; safe to use margin; recommended leverage"
    )
    matches = {item["match"].lower() for item in _scanner().scan_text(text, policy="advice")}
    assert {
        "recommended position",
        "optimal investment",
        "the stock will",
        "guaranteed upside",
        "safe to use margin",
        "recommended leverage",
    } <= matches


def test_self_directed_model_language_is_allowed() -> None:
    text = (
        "Kelly-implied exposure; model-implied sizing; posterior probability; "
        "reduce exposure under this assumption set; increase exposure under this assumption set; "
        "projected impact on Kelly; projected impact on convexity; projected impact on margin safety"
    )
    assert _scanner().scan_text(text, policy="advice") == []


def test_certainty_execution_and_connection_claims_are_blocked() -> None:
    text = (
        "cannot lose; sure thing; this will happen; the stock will go up; "
        "trade executed; order placed; brokerage connected; we bought; we sold; "
        "we execute trades for you; fiduciary guarantee; guaranteed profit"
    )
    matches = {item["match"].lower() for item in _scanner().scan_text(text, policy="advice")}
    assert {
        "cannot lose", "sure thing", "this will happen", "the stock will go up",
        "trade executed", "order placed", "brokerage connected", "we bought", "we sold",
        "we execute trades for you", "fiduciary guarantee", "guaranteed profit",
    } <= matches
