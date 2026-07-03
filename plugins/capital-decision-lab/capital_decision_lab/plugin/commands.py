"""Capital Decision Lab CLI boundary."""

from __future__ import annotations

import argparse
import importlib.metadata
import json
from collections.abc import Callable


EXPECTED_HERMES_VERSION = "0.16.0"


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


def _dispatch(args: argparse.Namespace) -> tuple[int, dict]:
    action = args.capital_action
    if action == "doctor":
        return doctor()
    return 2, {
        "command": f"capital {action}",
        "status": "failed",
        "issues": [{"code": "CLI_FEATURE_DEFERRED"}],
        "network_attempts": 0,
        "model_calls": 0,
    }


def run_cli(argv: list[str]) -> tuple[int, dict]:
    parser = argparse.ArgumentParser(prog="capital")
    setup_cli(parser)
    args = parser.parse_args(argv)
    return _dispatch(args)


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
