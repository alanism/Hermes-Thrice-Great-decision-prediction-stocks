"""Build a fresh, deny-by-default Hermes profile staging tree."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PLUGIN_IMPORT_ROOT = REPO_ROOT / "plugins" / "capital-decision-lab"
if str(PLUGIN_IMPORT_ROOT) not in sys.path:
    sys.path.insert(0, str(PLUGIN_IMPORT_ROOT))

from capital_decision_lab.privacy.containment import validate_contained_path  # noqa: E402
from capital_decision_lab.privacy.scanner import scan_repository  # noqa: E402


_ALLOWED_FILES = (
    Path("distribution.yaml"), Path("SOUL.md"), Path("config.yaml"),
    Path(".env.EXAMPLE"),
)
_ALLOWED_DIRS = (
    Path("skills"), Path("schemas"), Path("fixtures/valid"),
    Path("plugins/capital-decision-lab"),
)
_FORBIDDEN_TOP_LEVEL = {
    ".git", ".venv", "docs", "local", "logs", "outputs", "tests", "tmp",
}


def _failure(code: str) -> dict:
    return {"success": False, "issues": [{"code": code}], "files": []}


def validate_install_source(path: Path) -> dict:
    root = Path(path)
    if (root / ".git").exists() or (root / "tests").exists() or (root / "docs").exists():
        return {"allowed": False, "issues": [{"code": "STAGING_SOURCE_ROOT_FORBIDDEN"}]}
    violations = sorted(name for name in _FORBIDDEN_TOP_LEVEL if (root / name).exists())
    if violations:
        return {"allowed": False, "issues": [{"code": "STAGING_PATH_FORBIDDEN"}]}
    return {"allowed": True, "issues": []}


def _copy_file(source_root: Path, output_root: Path, relative: Path) -> str:
    check = validate_contained_path(source_root, relative)
    if not check["allowed"]:
        raise ValueError(check["issues"][0]["code"])
    source = Path(check["resolved_path"])
    destination = output_root / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    return relative.as_posix()


def _selected_files(source_root: Path) -> list[Path]:
    selected = [item for item in _ALLOWED_FILES if (source_root / item).is_file()]
    for directory in _ALLOWED_DIRS:
        root = source_root / directory
        if root.is_dir():
            selected.extend(
                path.relative_to(source_root)
                for path in root.rglob("*")
                if path.is_file()
                and "__pycache__" not in {part.casefold() for part in path.parts}
                and path.suffix.casefold() != ".pyc"
            )
    return sorted(set(selected), key=lambda item: item.as_posix())


def build_staging(source: Path, output: Path) -> dict:
    source_root = Path(source).resolve(strict=True)
    output_root = Path(output).resolve(strict=False)
    try:
        output_relative = output_root.relative_to(source_root)
        approved_generated_output = (
            len(output_relative.parts) >= 2
            and output_relative.parts[0].casefold() == "dist"
        )
        if not approved_generated_output:
            return _failure("STAGING_SOURCE_OUTPUT_OVERLAP")
    except ValueError:
        pass
    if output_root.exists():
        return _failure("STAGING_OUTPUT_EXISTS")
    preflight = scan_repository(source_root, policy="domain") + scan_repository(source_root, policy="advice")
    if preflight:
        return {"success": False, "issues": preflight, "files": []}

    copied: list[str] = []
    try:
        output_root.mkdir(parents=True)
        for relative in _selected_files(source_root):
            if relative.parts[0].casefold() in _FORBIDDEN_TOP_LEVEL:
                raise ValueError("STAGING_PATH_FORBIDDEN")
            copied.append(_copy_file(source_root, output_root, relative))
    except (OSError, ValueError) as exc:
        if output_root.exists():
            shutil.rmtree(output_root)
        code = str(exc) if str(exc).isupper() else "STAGING_BUILD_FAILED"
        return _failure(code)

    postflight = scan_repository(output_root, policy="domain") + scan_repository(output_root, policy="advice")
    if postflight:
        shutil.rmtree(output_root)
        return {"success": False, "issues": postflight, "files": []}

    inventory = []
    for relative in copied:
        value = (output_root / relative).read_bytes()
        inventory.append({"path": relative, "sha256": hashlib.sha256(value).hexdigest()})
    manifest_path = output_root.parent / f"{output_root.name}.manifest.json"
    manifest_path.write_text(
        json.dumps({"distribution_id": "hermes-thrice-great-nhi", "files": inventory}, sort_keys=True, indent=2),
        encoding="utf-8",
    )
    return {"success": True, "issues": [], "files": copied, "manifest": str(manifest_path)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--validate-install-source", type=Path)
    args = parser.parse_args(argv)
    result = (
        validate_install_source(args.validate_install_source)
        if args.validate_install_source is not None
        else build_staging(args.source, args.output)
    )
    print(json.dumps(result, sort_keys=True))
    return 0 if result.get("success", result.get("allowed", False)) else 2


if __name__ == "__main__":
    raise SystemExit(main())
