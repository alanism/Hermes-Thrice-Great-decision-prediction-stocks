from __future__ import annotations

import ast
import json
from pathlib import Path

from capital_decision_lab.calculations import allocation, convexity, margin
from capital_decision_lab.contracts.validation import validate_evidence_atom
from capital_decision_lab.privacy.scanner import scan_text


ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "fixtures" / "valid" / "stock-exposure"


def _fixture(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def test_stock_engine_outputs_preserve_language_and_provenance_gates() -> None:
    results = [
        allocation.analyze_kelly(_fixture("kelly-stock-thesis.json")["inputs"]),
        convexity.analyze_convexity(_fixture("convex-upside-stock.json")["inputs"]),
        margin.analyze_margin(_fixture("margin-danger.json")["inputs"]),
    ]
    for result in results:
        assert all(validate_evidence_atom(atom) == [] for atom in result.values())
        serialized = json.dumps(result, sort_keys=True)
        assert scan_text(serialized, policy="domain", suffix=".json") == []
        assert scan_text(serialized, policy="advice", suffix=".json") == []


def test_network_imports_are_confined_to_connector_boundary() -> None:
    network_modules = {"requests", "httpx", "socket", "urllib", "websocket"}
    violations: list[str] = []
    runtime = ROOT / "plugins" / "capital-decision-lab" / "capital_decision_lab"
    for path in runtime.rglob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names = {alias.name.split(".")[0] for alias in node.names}
                if names & network_modules and "connectors" not in path.parts:
                    violations.append(str(path))
            elif isinstance(node, ast.ImportFrom) and node.module:
                name = node.module.split(".")[0]
                if name in network_modules and "connectors" not in path.parts:
                    violations.append(str(path))
    assert violations == []


def test_stock_fixtures_are_synthetic_and_outside_private_storage() -> None:
    for path in FIXTURES.glob("*.json"):
        relative = path.relative_to(ROOT)
        assert "local" not in {part.casefold() for part in relative.parts}
        assert _fixture(path.name)["fixture_class"] == "valid_synthetic_stock_exposure"


def test_hermes_profile_does_not_globally_disable_connector_tools() -> None:
    config = (ROOT / "config.yaml").read_text(encoding="utf-8")
    assert 'disabled_toolsets: ["*"]' not in config
    assert "platform_toolsets:\n  cli: []" not in config.replace("\r\n", "\n")
