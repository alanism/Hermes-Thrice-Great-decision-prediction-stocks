from __future__ import annotations

import importlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _scanner():
    return importlib.import_module("capital_decision_lab.privacy.scanner")


def test_domain_terms_and_references_are_detected() -> None:
    scanner = _scanner()
    vocabulary = scanner.scan_text("A learner report", policy="domain")
    reference = scanner.scan_text(
        "from ucc.contracts import receipt", policy="domain", suffix=".py"
    )
    assert vocabulary[0]["code"] == "DOMAIN_VOCABULARY_FORBIDDEN"
    assert reference[0]["code"] == "DOMAIN_REFERENCE_FORBIDDEN"


def test_domain_path_reference_is_detected_outside_python() -> None:
    issues = _scanner().scan_text(
        '{"schema_ref":"../ucc/schemas/receipt.json"}',
        policy="domain",
        suffix=".json",
    )
    assert any(item["code"] == "DOMAIN_REFERENCE_FORBIDDEN" for item in issues)


def test_marked_adversarial_fixture_proves_detection() -> None:
    fixture = ROOT / "fixtures" / "adversarial" / "domain-leak.json"
    assert fixture.is_file()
    issues = _scanner().scan_path(fixture, include_adversarial=True)
    assert any(item["code"] == "DOMAIN_VOCABULARY_FORBIDDEN" for item in issues)


def test_valid_scopes_are_clear_and_policy_definitions_are_exempt() -> None:
    issues = _scanner().scan_repository(ROOT, policy="domain")
    assert issues == []


def test_root_readme_exemption_does_not_exempt_runtime_content(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("UCC learner disclaimer", encoding="utf-8")
    runtime = tmp_path / "plugins" / "probe" / "module.py"
    runtime.parent.mkdir(parents=True)
    runtime.write_text('label = "UCC learner"\n', encoding="utf-8")
    issues = _scanner().scan_repository(tmp_path, policy="domain")
    assert issues
    assert all(Path(item["path"]).name == "module.py" for item in issues)
