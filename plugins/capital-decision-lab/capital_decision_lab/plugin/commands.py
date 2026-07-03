"""Capital Decision Lab CLI boundary."""

from __future__ import annotations

import argparse
import importlib.metadata
import json
from collections.abc import Callable
from pathlib import Path

from capital_decision_lab.contracts.validation import validate_contract
from capital_decision_lab.contracts.canonical import contract_payload_hash
from capital_decision_lab.evidence.bayesian import build_belief_update
from capital_decision_lab.evidence.event_market import analyze_event_market
from capital_decision_lab.evidence.proposals import apply_approved_proposal, create_assumption_proposal
from capital_decision_lab.evidence.social import analyze_social
from capital_decision_lab.evidence.sensitivity import match_sensitivity
from capital_decision_lab.evidence.synthesis import synthesize_evidence
from capital_decision_lab.evidence.validation import validate_local_evidence
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
    analyze.add_argument("--assumption-update")
    compare = subcommands.add_parser("compare")
    compare.add_argument("--case", required=True)
    record = subcommands.add_parser("record")
    record.add_argument("--analysis", required=True)
    record.add_argument("--authorization", required=True)
    evidence = subcommands.add_parser("evidence")
    evidence_actions = evidence.add_subparsers(dest="evidence_action", required=True)
    evidence_validate = evidence_actions.add_parser("validate")
    evidence_validate.add_argument("--file", required=True)
    for name in ("analyze-event-market", "analyze-polymarket"):
        event = evidence_actions.add_parser(name)
        event.add_argument("--snapshot", required=True)
    social = evidence_actions.add_parser("analyze-social")
    social.add_argument("--batch", required=True)
    synthesize = evidence_actions.add_parser("synthesize")
    synthesize.add_argument("--inputs", required=True)
    belief = subcommands.add_parser("belief")
    belief_actions = belief.add_subparsers(dest="belief_action", required=True)
    update = belief_actions.add_parser("update")
    update.add_argument("--case", required=True)
    update.add_argument("--synthesis", required=True)
    update.add_argument("--sensitivity", required=True)
    assumption = subcommands.add_parser("assumption")
    assumption_actions = assumption.add_subparsers(dest="assumption_action", required=True)
    propose = assumption_actions.add_parser("propose")
    propose.add_argument("--belief-update", required=True)


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
    if action == "evidence":
        evidence_action = args.evidence_action
        option = "file" if evidence_action == "validate" else "snapshot" if evidence_action in {"analyze-event-market", "analyze-polymarket"} else "batch" if evidence_action == "analyze-social" else "inputs"
        document, error = _load_local_json(getattr(args, option), root)
        command = f"capital evidence {evidence_action}"
        if error:
            return 2, {**_base(command), "status": "failed", "issues": [{"code": error}]}
        try:
            if evidence_action == "validate":
                issues = validate_local_evidence(document, root)
                result = {"document_valid": not issues}
            elif evidence_action in {"analyze-event-market", "analyze-polymarket"}:
                issues = validate_local_evidence(document, root)
                result = {"signal": analyze_event_market(document)} if not issues else {}
            elif evidence_action == "analyze-social":
                issues = validate_local_evidence(document, root)
                result = {"signal": analyze_social(document)} if not issues else {}
            else:
                signals = document.get("signals")
                issues = [] if isinstance(signals, list) and signals else [{"code": "EVIDENCE_SIGNALS_REQUIRED", "path": "$.signals"}]
                result = {"synthesis": synthesize_evidence(signals)} if not issues else {}
        except (KeyError, TypeError, ValueError, OverflowError):
            issues = [{"code": "EVIDENCE_ANALYSIS_INPUT_INVALID", "path": "$"}]
            result = {}
        payload = {**_base(command), "status": "ok" if not issues else "failed", "issues": issues, **result}
        return (0 if not issues else 2), payload
    if action == "belief":
        belief, belief_error = _load_local_json(args.case, root)
        synthesis, synthesis_error = _load_local_json(args.synthesis, root)
        sensitivity, sensitivity_error = _load_local_json(args.sensitivity, root)
        error = belief_error or synthesis_error or sensitivity_error
        if error:
            return 2, {**_base("capital belief update"), "status": "failed", "issues": [{"code": error}]}
        try:
            if belief.get("contract_version") == "nhi.decision_case.v1":
                matched = match_sensitivity(synthesis, sensitivity)
                assumption_name = matched.get("affected_assumption")
                assumption_atom = belief.get("inputs", {}).get(assumption_name, {})
                prior = assumption_atom.get("value") if isinstance(assumption_atom, dict) else None
                if not isinstance(prior, (int, float)):
                    raise ValueError("BELIEF_PRIOR_UNAVAILABLE")
                case_hash = contract_payload_hash(belief)
                belief = {
                    "contract_version": "nhi.belief_state.v1",
                    "belief_id": f"belief_{belief['case_id']}_{assumption_name}",
                    "case_ref": belief["case_id"], "assumption": assumption_name,
                    "prior_probability": prior, "canonical_hash": case_hash,
                }
            update = build_belief_update(belief, synthesis, sensitivity)
        except (KeyError, TypeError, ValueError, OverflowError):
            return 2, {**_base("capital belief update"), "status": "failed", "issues": [{"code": "BELIEF_UPDATE_INPUT_INVALID"}]}
        return 0, {**_base("capital belief update"), "status": "ok", "issues": [], "belief_update": update}
    if action == "assumption":
        update, error = _load_local_json(args.belief_update, root)
        if error:
            return 2, {**_base("capital assumption propose"), "status": "failed", "issues": [{"code": error}]}
        try:
            proposal = create_assumption_proposal(update)
        except (KeyError, TypeError, ValueError):
            return 2, {**_base("capital assumption propose"), "status": "failed", "issues": [{"code": "ASSUMPTION_PROPOSAL_INPUT_INVALID"}]}
        return 0, {**_base("capital assumption propose"), "status": "ok", "issues": [], "proposal": proposal}
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
        if action == "analyze" and args.assumption_update:
            proposal, proposal_error = _load_local_json(args.assumption_update, root)
            if proposal_error:
                return 2, {**_base("capital analyze"), "status": "failed", "issues": [{"code": proposal_error}]}
            proposal_issues = validate_contract(proposal)
            if proposal_issues:
                return 2, {**_base("capital analyze"), "status": "failed", "issues": proposal_issues}
            case = apply_approved_proposal(case, proposal)
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
