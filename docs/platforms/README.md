# Platform onboarding guides

Start here to use Decision > Prediction through an assistant. Every platform follows the [shared requirements](common.md): discover the actual lenses, ask for analysis and risk preferences separately, preserve evidence and dissent, run only available calculations, and disclose missing work.

## Choose your host

- [dot](oai-dot/OAI-Dot.md)
- [Meta Muse AI](meta-muse-ai/Meta-Muse-AI.md)
- [Grok Bot](grok-bot/Grok-Bot.md)
- [Claude Cloud](claude-cloud/Claude-Cloud.md)
- [Hermes Thrice Great](hermes-thrice-great/Hermes-Thrice-Great.md)

These are guide names, not claims that a product, native connector or installer with each name exists. A model provider, assistant host and execution environment are different components. Read the individual guide’s verified-versus-conditional support statement.

The [setup manual](../Decision-Prediction-onboard-setup.md) records the tested adapter boundary, evidence labels and [full-report completeness gate](../Decision-Prediction-onboard-setup.md#full-report-completeness-gate). The [customer lessons](../dot-onboarding-lessons.md) explain why successful arithmetic alone is insufficient.

## Source documentation versus installation

These files make onboarding discoverable in the source repository when linked or supplied to an assistant. They do not automatically activate a host workflow. The reviewed Hermes staging allowlist excludes `docs` and the eight original root investor cards, while including `dlc-page.md`. Native discovery, packaging or installer integration requires a separate reviewed change and tests; this documentation release does not modify that allowlist.

The guides describe cloud workspaces, VPS deployments, local machines and local VMs without assuming every host supports every environment. Verify the selected runtime and data boundary before running code. Start with a synthetic on-demand example. Recurring reviews are opt-in and trade execution is outside this onboarding.

Reviewed against source `5bfe72972ee9b3ade55923e5419ca7ede1ac70ba` on 2026-10-09. Platform availability and APIs can change; consult current official documentation before setup.
