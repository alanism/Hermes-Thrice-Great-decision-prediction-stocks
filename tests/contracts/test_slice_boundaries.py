from __future__ import annotations

import inspect

from capital_decision_lab.contracts import authorization, ledger
from capital_decision_lab.orchestration import analyze, compare, record


def _public_functions(module) -> list[str]:
    return [
        name
        for name, value in vars(module).items()
        if not name.startswith("_") and inspect.isfunction(value)
    ]


def test_blocked_runtime_modules_have_no_behavior() -> None:
    for module in (
        authorization,
        ledger,
        analyze,
        compare,
        record,
    ):
        assert _public_functions(module) == [], module.__name__
