from __future__ import annotations

from pathlib import Path

from capital_decision_lab.methods.packs import PACKS
from capital_decision_lab.methods.runner import available_method_packs

ROOT = Path(__file__).resolve().parents[2]


def test_root_dlc_voices_are_not_executable_packs() -> None:
    packs = available_method_packs()
    # "page" is the executable method pack registered in code
    assert "page" in packs
    # Root DLC files like "dlc-page" or "dlc-contrarian" must never be registered as packs
    assert "dlc-page" not in packs
    assert "dlc-contrarian" not in packs


def test_page_pack_declarative_schema_and_steps() -> None:
    assert "page" in PACKS
    pack = PACKS["page"]
    required_keys = {"display_name", "description", "workflow_steps", "calculation_modules", "rubric_dimensions", "report_sections", "limitations"}
    assert required_keys.issubset(pack.keys())
    assert len(pack["workflow_steps"]) >= 4
    assert "power_law" in pack["calculation_modules"]
