"""Hermes plugin registration for Capital Decision Lab."""

from .capital_decision_lab.plugin import commands


def register(ctx) -> None:
    """Register the supported ``hermes capital`` command tree."""
    ctx.register_cli_command(
        name="capital",
        help="Run guided capital research and recommendation workflows",
        description="Portfolio, evidence, sizing, model-health, recommendation, and record commands",
        setup_fn=commands.setup_cli,
        handler_fn=commands.handle_cli,
    )
