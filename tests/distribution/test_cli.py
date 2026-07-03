from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

from capital_decision_lab.plugin.commands import doctor


ROOT = Path(__file__).resolve().parents[2]


def test_doctor_accepts_exact_runtime_version() -> None:
    exit_code, result = doctor(lambda _: "0.16.0")
    assert exit_code == 0
    assert result["status"] == "ok"
    assert result["expected_hermes_version"] == "0.16.0"


def test_doctor_rejects_runtime_version_mismatch() -> None:
    exit_code, result = doctor(lambda _: "0.16.1")
    assert exit_code == 2
    assert result["issues"] == [{"code": "HERMES_VERSION_MISMATCH"}]
    assert result["installed_hermes_version"] == "0.16.1"


def test_plugin_registers_capital_cli_with_hermes_context() -> None:
    plugin_root = ROOT / "plugins" / "capital-decision-lab"
    spec = importlib.util.spec_from_file_location(
        "capital_decision_plugin",
        plugin_root / "__init__.py",
        submodule_search_locations=[str(plugin_root)],
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    calls = []

    class Context:
        def register_cli_command(self, **kwargs):
            calls.append(kwargs)

    module.register(Context())
    assert len(calls) == 1
    assert calls[0]["name"] == "capital"
    assert callable(calls[0]["setup_fn"])
    assert callable(calls[0]["handler_fn"])
