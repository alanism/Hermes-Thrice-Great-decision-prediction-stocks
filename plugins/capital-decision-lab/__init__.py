"""Hermes plugin registration for Capital Decision Lab."""

from .capital_decision_lab.plugin import commands


def register(ctx) -> None:
    """Register the supported ``hermes capital`` command tree."""
    ctx.register_cli_command(
        name="capital",
        help="Run local capital comparison checks",
        description="Deterministic offline capital comparison commands",
        setup_fn=commands.setup_cli,
        handler_fn=commands.handle_cli,
    )
