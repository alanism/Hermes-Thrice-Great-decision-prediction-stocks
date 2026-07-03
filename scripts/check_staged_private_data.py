"""Reject private paths or sentinel content in a staged profile."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def check_staging(root: Path) -> dict:
    base = Path(root).resolve(strict=True)
    issues: list[dict] = []
    for path in sorted(base.rglob("*")):
        if any(part.casefold() == "local" for part in path.relative_to(base).parts):
            issues.append({"code": "PRIVATE_PATH_FORBIDDEN", "path": str(path)})
        if path.is_file():
            try:
                if "private_sentinel" in path.read_text(encoding="utf-8"):
                    issues.append({"code": "PRIVATE_SENTINEL_FORBIDDEN", "path": str(path)})
            except UnicodeDecodeError:
                continue
    return {"success": not issues, "issues": issues}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    result = check_staging(args.root)
    print(json.dumps(result, sort_keys=True))
    return 0 if result["success"] else 2


if __name__ == "__main__":
    raise SystemExit(main())

