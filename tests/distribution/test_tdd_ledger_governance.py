"""Verification test for TDD ledger governance requirements in Task T05."""

from pathlib import Path


def test_tdd_ledger_protocol():
    ledger_path = Path(__file__).resolve().parents[2] / "docs" / "governance" / "MANY_MODEL_BUILD_LEDGER.md"
    assert ledger_path.is_file(), f"Build ledger missing at {ledger_path}"
    content = ledger_path.read_text(encoding="utf-8").lower()

    required_sections = [
        "task-claim & lifecycle protocol",
        "frozen-test hash procedure",
        "mutation testing policy",
        "build ledger task receipt schema",
    ]

    for section in required_sections:
        assert section in content, f"Missing required section {section}"

    required_keywords = [
        "red_recorded",
        "green_verified",
        "mutant killed",
        "frozen test hashes",
    ]
    for kw in required_keywords:
        assert kw in content, f"Missing required keyword {kw}"
