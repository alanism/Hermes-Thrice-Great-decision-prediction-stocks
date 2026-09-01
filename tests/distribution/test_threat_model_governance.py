"""Verification test for threat model governance requirements in Task T04."""

from pathlib import Path


def test_threat_model_and_clearance_matrix():
    threat_path = Path(__file__).resolve().parents[2] / "docs" / "safety-boundaries" / "many-model-threat-model.md"
    assert threat_path.is_file(), f"Threat model missing at {threat_path}"
    content = threat_path.read_text(encoding="utf-8").lower()

    # Verify trust classes
    for trust_class in ["synthetic_test", "user_verified", "verified_local", "untrusted_external"]:
        assert trust_class in content, f"Missing trust class {trust_class}"

    # Verify threat vectors
    vectors = [
        "prompt injection",
        "path escape",
        "hostile numeric types",
        "nonfinite values",
        "oversized input",
        "free-text smuggling",
        "calculation egress",
        "private data leakage",
    ]
    for vector in vectors:
        assert vector in content, f"Missing threat vector {vector}"

    # Verify model clearance tiers
    for model_tier in ["sol", "deepseek", "gemini", "pure deterministic"]:
        assert model_tier in content, f"Missing model tier {model_tier}"
