# Claude-Cloud: verify the Claude surface first

**Status:** onboarding requirements and proposed adaptation, not a tested Claude deployment. Reviewed 2026-10-09 against repository commit `5bfe72972ee9b3ade55923e5419ca7ede1ac70ba`.

“Claude-Cloud” is this guide's label. Clarify whether it means Claude Code in the cloud, a Claude API client running on another host, Claude Code on a local computer, or a consumer Claude conversation. Those surfaces do not share identical tools, filesystem access, scheduling, or secrets.

Apply the [shared onboarding contract](../common.md) in full. This guide specifies how to preserve it across execution environments.

## 1. What official documentation establishes

Claude Code's cloud documentation describes Anthropic-managed isolated VM sessions and configurable network access. Self-hosted environments place isolation responsibility on the deployment operator. Disabling network access does not remove the model API communication path. Therefore “cloud sandbox” is not a promise that financial inputs never leave it. [Official cloud documentation](https://code.claude.com/docs/en/claude-code-on-the-web).

Scheduling is also surface-specific: cloud routines can run independently of the user's computer; Desktop schedules require that computer; `/loop` is session-scoped. Cloud scheduled work uses a fresh clone rather than the user's local files. Verify the current product's schedule, permissions, and availability before choosing one. [Official scheduling comparison](https://code.claude.com/docs/en/scheduled-tasks), [routines](https://code.claude.com/docs/en/routines).

These facts do not verify that Capital Decision Lab is installed or that a particular account can use these features. The Claude model API by itself is not a shell, a cloud workspace, or a recurring scheduler.

## 2. Choose a deployment deliberately

| Deployment | Execution and private data | Scheduling | Main gotcha |
|---|---|---|---|
| VPS | A named Claude-compatible host/runner executes the pinned engine under a dedicated approved account | A configured OS scheduler/service, or another verified scheduler | VPS disk, administrator access, backups, and inference egress need explicit data handling; API access alone supplies none of the host controls |
| Claude Code managed cloud | Confirm the selected session has the expected clone, Python, permissions, and approved private input route | A configured cloud routine, if available, with inspected task settings | Fresh clones do not include ignored `local/` data; do not commit portfolio files to make them appear in scheduled runs |
| Local computer | Local Claude Code or an explicitly chosen host runs the engine and reads only approved folders | Verified Desktop scheduling or host scheduler; `/loop` is for a running session | Local execution can still send content to the model provider; sleep/shutdown affects local schedules |
| Local VM | Install/use only a separately authorized guest host and Python runtime; restrict mounts | Guest scheduler plus VM and host availability | A guest does not automatically block internet, model API traffic, shared-folder access, or clipboard transfer |

For other managed cloud products, replace the Claude Code assumptions with that product's documented contract. For Hermes with a Claude provider, follow the [Hermes guide](../hermes-thrice-great/Hermes-Thrice-Great.md) rather than assuming Claude Code behavior.

## 3. Audit before setup or execution

Suggested first instruction:

> Read the shared onboarding contract and this guide. Identify my actual Claude product, configured provider/model, host version, executor, repository revision, persistence, and scheduler. Inspect only approved files and non-secret metadata. Do not install, create credentials, upload data, change permissions, create jobs, run repository code, or make paid API calls. Return verified, blocked, and unverified capabilities with evidence.

The report must include:

| Capability | Read-only evidence | Failure behavior |
|---|---|---|
| Repository/runtime | Selected checkout, readable workflow and engine files; Python inventory compared with `>=3.11,<3.14` in `pyproject.toml` | Stop calculations, state the required runtime |
| Dependencies | Manifest reviewed; engine runtime has no required external dependencies; development tests are separate | No implicit package install or dependency bootstrap |
| Tool permissions | Available shell/files/browser/OCR tools and allowed paths | Use research-only mode if engine or source tools are missing |
| Model route | Configured model/provider from non-secret metadata; plan/API route clearly distinguished | Do not assume a subscription is an API credential or select a paid fallback |
| Private storage | Actual private location, access scope, documented retention, and how a future session can retrieve it | No promise of persistent reports; later persistence tests require approval |
| Scheduling | Existing task identity, timezone, run history, machine dependency, and permitted delivery | Do not turn a chat promise or `/loop` into an indefinite scheduled service |
| Approval behavior | Whether the selected unattended job can ask the user; approved action allowlist | Restrict unattended scope to preapproved research/reporting and stop at evidence/decision gates |
| Browser/source access | Allowed domains and actual retrieval tool; source-specific limitations | Mark unavailable sources, never invent source content |

Do not enable a routine with broad autonomous write permissions merely because it is convenient. A scheduler that cannot obtain interactive confirmation cannot complete a step requiring new confirmation; prepare the review packet and wait.

## 4. Make the first conversation useful

1. Explain that the assistant organizes research and a fixed Python engine calculates. Ask familiarity, purpose, horizon, desired explanation depth, and privacy preferences.
2. Show all eight [investor cards](../common.md): Thorp, Mauboussin, Munger/Buffett, Laffont, Galloway, **Brad Gerstner**, Shkreli, and Camillo. Offer Scott Page as an optional many-model overlay. Ask for the primary analysis lens separately from risk discipline; do not default to the most aggressive persona.
3. Begin with a synthetic example. For real data, ask the user to choose the exact input file and permitted processing destination. Confirm snapshot date, currency, holdings, and extracted screenshot values.
4. Explain one piece of evidence, one competing interpretation, and the resulting question. Use plain language before introducing Kelly, convexity, or margin stress.
5. If a later synthetic execution is authorized, use pinned repository code and capture its receipt. Review real evidence before belief updates, and obtain explicit authorization before saving a decision record.

## 5. Preserve the repository's boundaries

- Model reasoning is not an execution receipt. An engine-backed result must identify revision, inputs/hashes, actual invocation, output, and seed where applicable. Missing execution means the calculated result is unavailable.
- Present the four customer-facing evidence labels **Measured**, **Calculated**, **Modeled**, and **Forecasted**, mapping source-engine `measured`, `calculated`, `modeled`, and `forecast` respectively. Retain **Narrative** and **Unknown** as distinct additional categories, never measured evidence. Every material number needs the appropriate label. Preserve source URLs/files, retrieval/snapshot dates, extraction method, limitations, and user-verification state.
- A source adapter must turn host content into an extraction result before it can support belief updates. Human confirmation gates still apply to OCR and screenshots.
- Store secrets only in the approved host secret mechanism/private environment. Never put BYOK values in `CLAUDE.md`, this guide, committed `.env` files, fixtures, reports, logs, or prompts. Do not copy the user's home-directory credentials into a VM as an onboarding shortcut.
- Keep private holdings, evidence, outputs, and authorized decision records outside committed content. Git-ignored files are not thereby protected from model transmission or cloud retention.
- No brokerage connection, trade execution, order placement, or money movement. Margin survivability can override a sizing model regardless of the selected hero.

## Sources and acceptance

- [Shared contract](../common.md), [system boundary](../../architecture/system-boundary.md), [host capability contract](../../host/capability-injection.md), [private-data policy](../../safety-boundaries/private-data-policy.md)
- [Runtime manifest](../../../pyproject.toml), [decision-record workflow](../../workflows/recommendation-records.md)
- [Claude Code cloud](https://code.claude.com/docs/en/claude-code-on-the-web), [scheduling comparison](https://code.claude.com/docs/en/scheduled-tasks), [routines](https://code.claude.com/docs/en/routines), accessed 2026-10-09

An acceptable onboarding result includes the completed host matrix, chosen investor preferences, consented data boundary, and explicit blockers. An execution-capable result additionally requires a later authorized synthetic engine receipt. No Claude account access, live model call, installation, scheduler setup, or integration test was performed to write this guide.
