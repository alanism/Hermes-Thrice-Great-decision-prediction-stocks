from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_ledger_entry_requires_authorization_hash() -> None:
    schema = json.loads(
        (ROOT / "schemas" / "decision-ledger.v1.schema.json").read_text(encoding="utf-8")
    )
    entry = schema["properties"]["entries"]["items"]
    assert "authorization_hash" in entry["required"]


def test_no_ledger_append_or_write_behavior_exists() -> None:
    from capital_decision_lab.contracts import ledger

    assert not hasattr(ledger, "append_entry")
    assert not hasattr(ledger, "write_ledger")

