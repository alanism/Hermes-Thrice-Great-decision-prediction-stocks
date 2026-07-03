"""Capital Decision Lab CLI boundary."""

from __future__ import annotations

import argparse
import importlib.metadata
import json
from collections.abc import Callable
from pathlib import Path

from capital_decision_lab.contracts.validation import validate_contract
from capital_decision_lab.orchestration.analyze import analyze_case
from capital_decision_lab.orchestration.compare import compare_case
from capital_decision_lab.orchestration.record import record_from_files
from capital_decision_lab.privacy.containment import validate_contained_path


EXPECTED_HERMES_VERSION = "0.16.0"
PROFILE_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_LOCAL_ROOT = PROFILE_ROOT / "local"
SYNTHETIC_CONTRACT_ROOT = PROFILE_ROOT / "fixtures" / "valid" / "contracts"


def doctor(
    version_getter: Callable[[str], str] = importlib.metadata.version,
) -> tuple[int, dict]:
    try:
        installed = version_getter("hermes-agent")
    except importlib.metadata.PackageNotFoundError:
        installed = None
    compatible = installed == EXPECTED_HERMES_VERSION
    issues = [] if compatible else [{"code": "HERMES_VERSION_MISMATCH"}]
    return (
        0 if compatible else 2,
        {
            "command": "capital doctor",
            "status": "ok" if compatible else "failed",
            "distribution_id": "hermes-thrice-great-nhi",
            "profile": "nhi",
            "expected_hermes_version": EXPECTED_HERMES_VERSION,
            "installed_hermes_version": installed,
            "issues": issues,
            "network_attempts": 0,
            "model_calls": 0,
        },
    )


def setup_cli(parser: argparse.ArgumentParser) -> None:
    """Build the command tree for standalone and Hermes registration."""
    subcommands = parser.add_subparsers(dest="capital_action", required=True)
    subcommands.add_parser("doctor")
    validate = subcommands.add_parser("validate")
    validate.add_argument("--synthetic", action="store_true", required=True)
    analyze = subcommands.add_parser("analyze")
    analyze.add_argument("--case", required=True)
    compare = subcommands.add_parser("compare")
    compare.add_argument("--case", required=True)
    record = subcommands.add_parser("record")
    record.add_argument("--analysis", required=True)
    record.add_argument("--authorization", required=True)


def _base(command: str) -> dict:
    return {"command": command, "network_attempts": 0, "model_calls": 0}


def _load_local_json(path: str, local_root: Path) -> tuple[dict | None, str | None]:
    check = validate_contained_path(local_root, Path(path))
    if not check["allowed"]:
        return None, check["issues"][0]["code"]
    try:
        value = json.loads(Path(check["resolved_path"]).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None, "LOCAL_DOCUMENT_INVALID"
    if not isinstance(value, dict):
        return None, "LOCAL_DOCUMENT_INVALID"
    return value, None


def _dispatch(args: argparse.Namespace, *, local_root: Path | None = None) -> tuple[int, dict]:
    action = args.capital_action
    if action == "doctor":
        return doctor()
    root = Path(local_root or DEFAULT_LOCAL_ROOT)
    if action == "validate":
        failures: dict[str, list] = {}
        fixtures = sorted(SYNTHETIC_CONTRACT_ROOT.glob("*.json"))
        for path in fixtures:
            try:
                document = json.loads(path.read_text(encoding="utf-8"))
                issues = validate_contract(document)
            except (OSError, json.JSONDecodeError):
                issues = [{"code": "SYNTHETIC_FIXTURE_INVALID", "path": "$"}]
            if issues:
                failures[path.name] = issues
        payload = {
            **_base("capital validate"),
            "status": "ok" if not failures and fixtures else "failed",
            "validated_contracts": len(fixtures) - len(failures),
            "failures": failures,
            "issues": [] if not failures and fixtures else [{"code": "SYNTHETIC_VALIDATION_FAILED"}],
        }
        return (0 if payload["status"] == "ok" else 2), payload
    if action in {"analyze", "compare"}:
        case, error = _load_local_json(args.case, root)
        if error:
            return 2, {**_base(f"capital {action}"), "status": "failed", "issues": [{"code": error}]}
        contract_issues = validate_contract(case)
        if contract_issues:
            return 2, {**_base(f"capital {action}"), "status": "failed", "issues": contract_issues}
        try:
            result = analyze_case(case) if action == "analyze" else compare_case(case)
        except (TypeError, ValueError, OverflowError):
            return 2, {**_base(f"capital {action}"), "status": "failed", "issues": [{"code": "ORCHESTRATION_INPUT_INVALID"}]}
        key = "analysis" if action == "analyze" else "comparison"
        payload = {**_base(f"capital {action}"), "status": "ok", "issues": []}
        if action == "analyze":
            payload[key] = result
        else:
            payload.update(result)
        return 0, payload
    result = record_from_files(
        Path(args.analysis), Path(args.authorization), local_root=root
    )
    return (
        0 if result["success"] else 2,
        {
            **_base("capital record"),
            "status": "ok" if result["success"] else "failed",
            **result,
        },
    )


def run_cli(argv: list[str], *, local_root: Path | None = None) -> tuple[int, dict]:
    parser = argparse.ArgumentParser(prog="capital")
    setup_cli(parser)
    args = parser.parse_args(argv)
    return _dispatch(args, local_root=local_root)


def handle_cli(args: argparse.Namespace) -> int:
    """Handle an invocation dispatched by Hermes."""
    exit_code, result = _dispatch(args)
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return exit_code


def main(argv: list[str] | None = None) -> int:
    import sys

    exit_code, result = run_cli(list(sys.argv[1:] if argv is None else argv))
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
