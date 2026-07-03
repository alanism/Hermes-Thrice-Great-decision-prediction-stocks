from __future__ import annotations

import importlib
import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _scanner():
    return importlib.import_module("capital_decision_lab.privacy.scanner")


def _builder():
    path = ROOT / "scripts" / "build_profile_staging.py"
    assert path.is_file(), "RED: staging builder does not exist"
    spec = importlib.util.spec_from_file_location("build_profile_staging", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_local_path_is_rejected_by_scanner(tmp_path: Path) -> None:
    private = tmp_path / "local" / "case.json"
    private.parent.mkdir()
    private.write_text('{"private_sentinel":"never-stage"}', encoding="utf-8")

    issues = _scanner().scan_path(private, repository_root=tmp_path)
    assert [item["code"] for item in issues] == ["PRIVATE_PATH_FORBIDDEN"]


def test_private_sentinel_never_enters_staging(tmp_path: Path) -> None:
    sentinel = ROOT / "local" / "private-sentinel.json"
    sentinel.parent.mkdir(exist_ok=True)
    sentinel.write_text('{"private_sentinel":"never-stage"}', encoding="utf-8")
    try:
        output = tmp_path / "profile"
        result = _builder().build_staging(ROOT, output)
        assert result["success"] is True
        assert "never-stage" not in "".join(
            path.read_text(encoding="utf-8", errors="ignore")
            for path in output.rglob("*")
            if path.is_file()
        )
    finally:
        sentinel.unlink(missing_ok=True)


def test_only_local_readme_is_trackable() -> None:
    ignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
    assert "local/*" in ignore
    assert "!local/README.md" in ignore
