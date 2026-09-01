"""Verification test for PRD governance requirements in Task T03."""

from pathlib import Path


def test_many_model_thinking_prd_fields():
    prd_path = Path(__file__).resolve().parents[2] / "docs" / "product" / "many-model-thinking.md"
    assert prd_path.is_file(), f"PRD missing at {prd_path}"
    content = prd_path.read_text(encoding="utf-8").lower()

    required_fields = [
        "user",
        "job",
        "current failure",
        "baseline metric",
        "target",
        "non-goals",
        "six-string recommendation delta",
        "binding-permission delta",
        "zero-delta branch",
        "input owner and location",
    ]

    missing = [field for field in required_fields if field not in content]
    assert not missing, f"PRD missing required fields: {missing}"

    # Verify both thesis runs are documented
    assert "thesis run 1" in content
    assert "thesis run 2" in content
    assert "local/" in content
