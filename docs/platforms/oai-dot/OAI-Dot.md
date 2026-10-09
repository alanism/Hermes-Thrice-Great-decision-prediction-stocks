# Decision Prediction with dot

Version 0.1 · Reviewed 2026-10-09 · Source-repository guide

Use this guide with the [shared onboarding requirements](../common.md) and [setup manual](../../Decision-Prediction-onboard-setup.md). It describes a proposed first-use experience for dot and the capability checks required to provide it truthfully. It does not install a native dot plugin or make the repository automatically discoverable.

## First use

When the repository or this guide is supplied in a task, inspect the full [Decision Prediction skill](../../../skills/decision-prediction/SKILL.md), [report anatomy](../../../skills/decision-prediction/references/monocle-report-anatomy.md) and actual cards. Confirm what can run in the selected environment. A filename is not an activation mechanism.

Then proactively introduce the eight original research perspectives and Scott Page’s additional lens. Ask which should lead the analysis and, separately, what risk/sizing discipline and constraints apply. Offer a balanced overview when the user has no preference. Gerstner/Laffont analysis with Thorp-inspired survival checks and Buffett/Munger business-quality analysis are examples, not assumed user profiles.

Describe only verified availability. A suitable introduction after verifying the files is:

> I can use this repository’s investor-inspired playbooks to structure your research. For a requested report, I’ll label evidence, keep the calculations separate from commentary and show where the perspectives disagree. Which lenses should lead the analysis, and what risk constraints should I use? We can start with a balanced overview. I’ll check the Python runtime before promising calculated results; recurring reviews are optional.

If the reviewed adapter is also available and passes checks, say that supplied-case Python calculations can run. If it is absent, explain that commentary is available but engine outputs are not. Do not silently substitute model-generated arithmetic.

## Runtime choices

The assistant’s chat surface and the environment executing the research are separate. Choose a suitable authorized environment and test it; do not infer shell access, file persistence or connectivity from the fact that the user is chatting with dot.

| Environment | Required checks | Boundary |
| --- | --- | --- |
| Managed cloud workspace | Available Python, reviewed bundle, contained inputs, persistence/retention and permitted source access | A working supervised cloud evaluation is not a native plugin or portable installer |
| User’s local machine | Actual connected execution environment, selected repository, runtime and narrowly authorized files | Do not assume the assistant can see arbitrary local files or broker apps |
| Local VM | Guest OS/runtime, mount boundaries, shared folders, private-data retention and VM availability | A VM does not automatically establish a safe boundary or host scheduling |
| VPS or remote server | Authorized remote environment, OS/Python, deployment identity, persistent storage and source access | Remote deployment, unattended scheduling and secrets handling need explicit setup and validation |

The recorded adapter evidence covers Linux x86_64 and Python 3.12.14. It does not validate every managed cloud, local machine, VM or VPS. macOS, native Windows and relocation remain untested in that evidence. The existing adapter’s fixed source path and POSIX timeout require attention before portability claims.

Use secure account setup when needed. Never place passwords, API keys or brokerage credentials in prompts, source files or reports. Confirm the data destination before introducing private financial information, including when moving from a local machine to cloud execution.

## What dot should do within a requested report

- Follow the entire skill and [completeness gate](../../Decision-Prediction-onboard-setup.md#full-report-completeness-gate).
- Use verified Python for available deterministic calculations; retain raw engine outputs, identities, units and limits.
- Label Measured, Calculated, Modeled and Forecasted figures; keep screenshot transcriptions unconfirmed until exact values are genuinely confirmed.
- Present all eight original perspectives in a full report, plus Page separately, with simulated-perspective disclaimers, disagreement and adverse facts.
- Keep preferred analysis lenses separate from risk constraints and from executable pack selection.
- Answer an explicit single-lens request as a labeled focused view without pretending it is a full committee report.
- Explain unavailable sources, unmet formal Bayesian gates and sections not run. Do not claim full application when only the numerical subset ran.
- Preserve source/capture/as-of/retrieval times and dated report changes in the authorized destination.

These are documented host expectations. This file alone does not implement them or prove every requirement was satisfied in earlier reports.

## Optional recurring work

After an on-demand example, ask whether the user wants an optional five-stock daily rotation, weekly chosen-ticker refresh such as META, or separate macro review. Agree the schedule, time zone, inputs, rotation, destination and retention. Use an actually available scheduling facility and verify setup before claiming it is enabled. A successful scheduled run must be verified separately.

Neither the adapter nor this guide installs native cron, creates a daemon, enables account access or places trades. Research permission is not trading permission. Preserve one report identity with dated versions where supported; report persistence or source failures honestly.

## Release acceptance

Before advertising automatic first-use onboarding in dot, test a new user from guide discovery through preference selection, synthetic calculation and a visibly scoped report. Verify both a successful path and unavailable-runtime/source/confirmation paths. A future native integration needs implementation and acceptance tests; this documentation is not such an integration.

The Hermes staging configuration currently excludes these `docs` guides and the eight original root cards. A source checkout can expose them, but staged-profile discovery needs separate distribution work. Do not change the runtime allowlist merely to make this guide appear installed.
