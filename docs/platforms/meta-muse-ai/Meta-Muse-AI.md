# Meta-Muse-AI: capability-gated onboarding

**Status:** proposed host adaptation, not a verified repository integration. Reviewed 2026-10-09 against repository commit `5bfe72972ee9b3ade55923e5419ca7ede1ac70ba`. “Meta-Muse-AI” is this guide's label; it does not identify a particular installed Meta application, executor, or subscription.

Start with the [shared onboarding contract](../common.md). Its investor introduction, evidence gates, beginner-friendly explanations, privacy rules, and approval requirements apply unchanged here. This document adds deployment checks rather than promising that a model endpoint supplies an operating system.

## 1. Identify the actual stack

Record these separately before asking for portfolio data:

1. **Model/provider:** exact configured model identifier, provider route, and whether it is a direct Meta API or an intermediary. Read non-secret configuration; do not expose keys.
2. **Host:** actual application/harness name and version, e.g. an explicitly configured Hermes installation. A consumer chat, API endpoint, and a shell-enabled agent are different surfaces.
3. **Executor:** machine/container where repository Python would run, allowed directories, and available tools.
4. **Storage and scheduling:** durable private artifact location and the actual process that would wake the agent.

Meta's official announcement documents Muse Spark 1.1 and the Meta Model API preview. It does not establish this user's filesystem, scheduler, brokerage access, or a tested Capital Decision Lab adapter. The repository references `muse-spark-1.2-contributor` in operational skills; that is a repository configuration example, not verification that the exact identifier exists on the selected account today. Resolve it from the configured provider's current catalog before a separately approved model call. Do not substitute a model silently. [Official Meta announcement](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/).

## 2. Deployment matrix

These are requirements for choosing a deployment, not tested installation claims.

| Deployment | Executor and private storage required | Scheduling requirement | Important boundary |
|---|---|---|---|
| VPS | A named host runs the harness and Python; a private durable directory holds evidence and outputs | An actual configured service, such as the host's scheduler or a verified Hermes gateway | A remote API model is not the VPS. Server administrators, logs, backups, and outbound model requests affect privacy |
| Managed cloud | Confirm the specific product exposes a repository-capable executor and an approved private durable store | Verify a supported scheduled-job mechanism and job receipt | Consumer chat or model API access alone does not prove any of these capabilities; temporary workspaces are insufficient for recurring portfolio state |
| Local computer | An authorized harness reads the clone and approved portfolio folder; engine runs locally | Installed scheduler plus machine availability; otherwise on demand only | Local Python does not mean local inference. Data included in API prompts leaves the machine |
| Local VM | Guest contains the clone and runtime; intentionally mount only approved inputs and persistent output storage | Guest scheduler, VM uptime, and host uptime all matter | NAT/bridged networking, shared folders, clipboard, and provider egress must be assessed; “VM” does not mean network-isolated |

If the host is Hermes, also use the [Hermes guide](../hermes-thrice-great/Hermes-Thrice-Great.md). Changing the model does not remove Hermes's host-version or storage constraints.

## 3. Read-only readiness audit

Ask the assistant:

> Audit readiness without installing software, modifying configuration, creating schedules, running repository code, making paid model calls, reading secret values, or uploading private data. Identify the configured model/provider and actual executor. Inspect only approved files and non-secret metadata. Return the following capability matrix with evidence, blockers, and the smallest next step.

| Capability | Evidence required to mark verified | Otherwise |
|---|---|---|
| Repository read | Selected revision plus successful read of `pyproject.toml`, `SOUL.md`, and workflow files | Ask for an approved clone or file selection |
| Python/dependencies | Runtime inventory showing Python `>=3.11,<3.14`; dependency declarations inspected | Report engine execution unavailable; do not install or import code during this audit |
| Deterministic executor | Named shell/runner tool, working directory, and permission scope | Research-only mode; no calculated engine output claimed |
| Browser/search | Actual available tool and source-access permission | Accept user-provided sources; label absent retrieval unavailable |
| Images/OCR | Available host tool or approved model capability, source path, and transmission destination | Use CSV or ask for transcription; do not infer measured numbers |
| Private state | Approved location, access metadata, persistence documentation, and retention owner | No durable workflow promised; a write/readback test requires a later authorized step |
| Scheduler | Existing scheduler identity, timezone, job listing, run history, delivery destination | On demand only; an API completion is not a scheduled run |
| API/BYOK | Credential-presence status only, correct provider route, and user-approved budget | Ask the user to configure credentials securely; never ask for a key in chat |

The engine has no required third-party runtime dependencies in this revision. Dev/test dependencies are separate. Do not install a provider SDK merely to read these guides. Exact prices, context limits, cache discounts, and tool support must be checked for the selected model; historical examples in skills are not current billing guarantees.

## 4. First useful session

1. Introduce the assistant as a research partner and explain that Python owns the calculations. Ask what decision the user wants help thinking through, how familiar they are with investing, and their preferred explanation depth.
2. Present the eight [shared investor cards](../common.md): Thorp, Mauboussin, Munger/Buffett, Laffont, Galloway, **Brad Gerstner**, Shkreli, and Chris Camillo. Offer Scott Page separately as an optional many-model lens. Ask for a primary analysis lens and a separate risk discipline. The host model is not an investor persona.
3. Start with synthetic data, or an explicitly selected private CSV/screenshot after agreeing where it may be processed. Confirm extracted holdings, currency, snapshot date, and ambiguous values.
4. Explain one thesis, one disconfirming observation, and one limitation. If execution is unavailable, produce a research outline and explicit missing-input list instead of guessed Kelly or margin results.
5. When execution is separately authorized, use the actual repository engine and preserve its receipt. Review evidence and assumptions before any belief update; request explicit authorization before a decision record is saved.

## 5. Required output and stopping rules

- Present the four customer-facing evidence labels **Measured**, **Calculated**, **Modeled**, and **Forecasted**. Map source-engine `measured`, `calculated`, `modeled`, and `forecast` to those labels without changing their meaning. Retain **Narrative** and **Unknown** as distinct additional categories; neither is measured evidence. Keep source URL/file reference, retrieval or snapshot time, input hash, user-verification state, engine revision, and command/result provenance. A confident model answer is not a calculation receipt.
- Source extraction and human verification gates still apply when the model can see images or browse. Browser text alone is not a belief update.
- Report missing tools, missing data, failed execution, stale inputs, and invalid domains explicitly. Stop the affected step; continue only independent research.
- BYOK belongs in the host's secret facility or private environment, never tracked files, reports, fixtures, prompts, or public logs. A private folder and `.gitignore` do not prevent API transmission.
- No brokerage login, account connection, trade execution, or movement of money. Persona selection cannot relax survivability checks or approval gates.

## Sources and support boundary

- [Shared onboarding contract](../common.md)
- [Repository architecture](../../architecture/system-boundary.md), [host bridge](../../host/hermes-host-bridge.md), [capability contract](../../host/capability-injection.md), [source extraction](../../host/source-extraction-adapters.md)
- [Runtime declaration](../../../pyproject.toml), [operational model references](../../../skills/decision-prediction/SKILL.md)
- [Official Meta announcement](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/) accessed 2026-10-09. The specific developer model page was unavailable to this documentation review; exact current model IDs, access entitlements, cache behavior, and “Meta-Muse-AI” host semantics remain unverified.

**Acceptance is not deployment:** this guide passes only when the onboarding matrix is filled with host-specific evidence, a user has selected preferences, and the assistant can describe blockers honestly. No live Meta calls or end-to-end integration tests were performed for this document.
