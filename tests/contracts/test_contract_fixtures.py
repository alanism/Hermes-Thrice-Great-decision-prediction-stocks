from __future__ import annotations

import json
from pathlib import Path

from capital_decision_lab.contracts import validation


ROOT = Path(__file__).resolve().parents[2]
VALID_ROOT = ROOT / "fixtures" / "valid" / "contracts"
ADVERSARIAL_ROOT = ROOT / "fixtures" / "adversarial" / "contracts"


def test_schema_loader_resolves_all_contract_versions() -> None:
    versions = validation.supported_contract_versions()
    assert versions == (
        "nhi.assumption_register.v1",
        "nhi.decision_analysis.v1",
        "nhi.decision_authorization.v1",
        "nhi.decision_case.v1",
        "nhi.decision_comparison.v1",
        "nhi.decision_ledger.v1",
        "nhi.decision_proposal.v1",
    )
    for version in versions:
        schema = validation.load_schema(version)
        assert schema["properties"]["contract_version"]["const"] == version


def test_all_valid_contract_fixtures_pass() -> None:
    fixtures = sorted(VALID_ROOT.glob("*.json"))
    assert len(fixtures) == 7
    for path in fixtures:
        document = json.loads(path.read_text(encoding="utf-8"))
        assert validation.validate_contract(document) == [], path.name


def test_all_adversarial_contract_fixtures_fail_with_expected_code() -> None:
    fixtures = sorted(ADVERSARIAL_ROOT.glob("*.json"))
    assert len(fixtures) >= 5
    for path in fixtures:
        fixture = json.loads(path.read_text(encoding="utf-8"))
        issues = validation.validate_contract(fixture["document"])
        assert fixture["expected_issue_code"] in {item["code"] for item in issues}, path.name

