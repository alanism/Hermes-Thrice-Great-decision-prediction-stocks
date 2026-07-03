from __future__ import annotations

import importlib.util
import shutil
from pathlib import Path

from capital_decision_lab.privacy import containment


ROOT = Path(__file__).resolve().parents[2]
BUILDER_PATH = ROOT / "scripts" / "build_profile_staging.py"


def _builder():
    assert BUILDER_PATH.is_file(), "RED: staging builder does not exist"
    spec = importlib.util.spec_from_file_location("build_profile_staging", BUILDER_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_staging_is_deny_by_default(tmp_path: Path) -> None:
    module = _builder()
    output = tmp_path / "profile"
    result = module.build_staging(ROOT, output)

    assert result["success"] is True
    assert (output / "distribution.yaml").is_file()
    for forbidden in ("docs", "tests", ".git", "local", "tmp", "logs"):
        assert not (output / forbidden).exists()


def test_repository_root_is_not_an_install_payload() -> None:
    module = _builder()
    result = module.validate_install_source(ROOT)
    assert result == {
        "allowed": False,
        "issues": [{"code": "STAGING_SOURCE_ROOT_FORBIDDEN"}],
    }


def test_approved_dist_location_can_be_generated() -> None:
    module = _builder()
    output = ROOT / "dist" / "policy-test-profile"
    manifest = output.parent / f"{output.name}.manifest.json"
    shutil.rmtree(output, ignore_errors=True)
    manifest.unlink(missing_ok=True)
    try:
        result = module.build_staging(ROOT, output)
        assert result["success"] is True
        assert module.validate_install_source(output) == {"allowed": True, "issues": []}
    finally:
        shutil.rmtree(output, ignore_errors=True)
        manifest.unlink(missing_ok=True)


def test_containment_rejects_escape() -> None:
    result = containment.validate_contained_path(ROOT, ROOT / ".." / "outside.json")
    assert result["allowed"] is False
    assert result["issues"] == [{"code": "PATH_ESCAPE_FORBIDDEN"}]


def test_containment_rejects_reparse_traversal(monkeypatch) -> None:
    monkeypatch.setattr(
        containment,
        "_is_reparse_point",
        lambda path: path.name.casefold() == "schemas",
    )
    result = containment.validate_contained_path(
        ROOT, ROOT / "schemas" / "decision-case.v1.schema.json"
    )
    assert result["allowed"] is False
    assert result["issues"] == [{"code": "REPARSE_POINT_FORBIDDEN"}]
