# Grok-Bot: separate Grok from the execution host

**Status:** proposed host adaptation; no verified Grok-to-Capital-Decision-Lab integration. Reviewed 2026-10-09 against repository commit `5bfe72972ee9b3ade55923e5419ca7ede1ac70ba`. “Grok-Bot” is a requested guide label, not proof of a particular bot product, deployment, or permissions.

Use the [shared onboarding contract](../common.md) for the common conversation, investor cards, evidence standards, and approval gates. Establish whether the user means a consumer Grok surface, an xAI API client, or a separate agent harness using a Grok model.

## 1. Know what each layer does

The xAI API documents Python code execution. Its documented execution context is temporary, has limited filesystem access, and does not expose external networks or filesystems. This is not evidence that the user's repository is installed there. Reimplementing a formula in model-generated Python does not constitute execution of this repository's pinned engine. [Official code execution documentation](https://docs.x.ai/developers/tools/code-execution).

Remote MCP is a separately configured tool route. Its documentation currently says `require_approval` is unsupported in the OpenAI-compatible Responses API. Therefore a wrapper must not rely on that parameter as the repository's confirmation barrier. Expose only the tools actually intended and enforce approvals in the host/service before consequential actions. This document does not configure an MCP server or authorize data transmission to one. [Official remote MCP documentation](https://docs.x.ai/developers/tools/remote-mcp).

Record model identifier, API route, host/version, executor identity, storage, scheduler, and permitted source tools independently. The product name cannot answer these questions.

## 2. Deployment matrix

| Deployment | What must actually run | Durable storage and scheduling | Required check |
|---|---|---|---|
| VPS | A user-selected bot/harness and supported Python environment execute the pinned engine | Private server directory plus an installed scheduler/service | Verify service identity, repository path, timezone, budget, permissions, and logs; the xAI endpoint supplies no VPS by implication |
| Managed cloud | A named runner that can access approved code and inputs, or a separately approved bounded tool service | Explicit private durable store and actual scheduled-job facility | The API's temporary code execution context alone does not satisfy either persistence or recurring work |
| Local computer | Authorized local harness runs Python; Grok remains the configured inference provider | Local private files; scheduler needs host availability | Identify exactly which prompts/files leave the machine for inference or search |
| Local VM | Guest runtime executes pinned code and accesses only deliberate mounts | Persistent guest disk/output mount; scheduler needs VM and host up | Inspect egress, NAT/bridged networking, shared folders, and clipboard; VM use does not itself establish isolation |

A selected Hermes harness also needs the [Hermes guide](../hermes-thrice-great/Hermes-Thrice-Great.md). Do not treat an OpenAI-compatible API schema as an OpenAI host, installed plugin, filesystem mount, or scheduler.

## 3. Non-mutating capability probe

The initial audit reads approved code/configuration and tool metadata only. No installs, credentials, paid calls, repository execution, external uploads, test writes, or new schedules.

| Check | Pass evidence | Safe fallback |
|---|---|---|
| Host/model audit | Actual configured provider/model, host version, executor location; no secret values | Ask which application/runner the user intends |
| Repository/dependencies | Readable revision and `pyproject.toml`: Python `>=3.11,<3.14`, no mandatory external runtime dependencies | Describe missing runtime; do not install silently |
| Engine availability | Approved runner, known working directory, readable engine source, permitted invocation route | Research-only response; calculations marked unavailable |
| Browser/X/search | Available named tool and successful permitted public-source access, where allowed | Use supplied evidence with provenance; no claim of live X access merely because the model is Grok |
| OCR/local files | Explicitly authorized folder/file selection, OCR capability, transmission boundary | CSV or user transcription; ask for confirmation of ambiguous fields |
| Storage | Private destination, ownership/access metadata, retention and persistence documentation | Do not claim durable state from a response ID or conversation |
| Scheduler | Real scheduler identity and existing job/run metadata with timezone | On demand only |
| Secret/budget controls | Credential presence without value, tool exposure, budget cap, escalation behavior | Stop before any model or third-party tool call that would exceed approved scope |

Later, an authorized synthetic smoke run should capture the exact command, revision, input hashes, exit/result, output location, and limitations. Do not label the initial read-only probe an end-to-end execution test.

## 4. Onboard the investor, not just the API

Begin with a plain-language introduction: the assistant reads evidence, the deterministic engine calculates, and the user owns investment decisions. Ask the user's investing familiarity, goal, time horizon, explanation preference, and data-sharing comfort before collecting financial data.

Present all eight cards from [common.md](../common.md): Edward Thorp, Michael Mauboussin, Munger/Buffett, Thomas and Philippe Laffont, Scott Galloway, **Brad Gerstner/Altimeter**, Martin Shkreli, and Chris Camillo. Scott Page is an optional ninth many-model lens. Each is a simulated analytical framework, not the person's participation or endorsement. Ask separately for a primary research lens and a risk discipline; broad social-data access does not make Camillo the automatic default.

Use one synthetic thesis first. With approved real inputs, confirm shares, costs, currency, dates, margin assumptions, and source permissions. Treat X sentiment as evidence needing context and verification, never as a buy/sell trigger. A search hit is not a verified holding or probability.

## 5. Execution and report contract

1. Capture source URL/file, acquisition method, timestamp, raw-content hash, and limitations. Preserve source-specific extraction before analysis.
2. Present the four customer-facing evidence labels **Measured**, **Calculated**, **Modeled**, and **Forecasted**, mapping source-engine `measured`, `calculated`, `modeled`, and `forecast` respectively. Retain **Narrative** and **Unknown** as distinct additional categories, never measured evidence. Screenshot-derived values require human confirmation; only eligible user-verified evidence can affect beliefs.
3. Run repository math only through a verified executor after approval for that step. Preserve input references, seed when applicable, engine version, and output receipt. Do not replace failed engine output with generated arithmetic.
4. Show thesis, counterevidence, scenarios, risk constraints, and what would change the conclusion. Margin danger can override Kelly; an investor persona cannot waive that rule.
5. Request explicit authorization before saving a decision record. No brokerage connection, login, order placement, or money movement. Scheduled research is not recurring permission to trade or record decisions.

Store BYOK only in the chosen secret facility/private environment. Never include keys in MCP descriptions, reports, source files, committed fixtures, or model prompts. A remote MCP service introduces another data recipient: agree what it may receive before use. Keep raw portfolio data and generated private reports out of the public repository.

## Sources and unverified claims

- [Shared onboarding contract](../common.md), [system boundary](../../architecture/system-boundary.md), [capability injection](../../host/capability-injection.md), [source extraction](../../host/source-extraction-adapters.md)
- [Python/dependency declaration](../../../pyproject.toml), [evidence hierarchy](../../evidence/measured-calculated-modeled-forecast.md)
- [xAI code execution](https://docs.x.ai/developers/tools/code-execution), [remote MCP](https://docs.x.ai/developers/tools/remote-mcp), [tools overview](https://docs.x.ai/developers/tools/overview), accessed 2026-10-09

Consumer-product capabilities, current account entitlements, exact model selection, durable storage, scheduler support, and this repository's live compatibility are **unverified until the selected host passes the audit**. No xAI calls, account setup, paid tool use, or integration tests were performed for this guide.
