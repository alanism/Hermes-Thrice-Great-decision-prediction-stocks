# Hermes-Thrice-Great: inspect the profile before onboarding

**Status:** documentation for the repository's intended Hermes host, with current upstream guidance distinguished from repository and installation evidence. Reviewed 2026-10-09 against repository commit `5bfe72972ee9b3ade55923e5419ca7ede1ac70ba`. No user's installed Hermes profile was inspected or changed for this document.

Start with the [shared onboarding contract](../common.md). The objective is a helpful research conversation with verified boundaries, not simply loading a large persona prompt.

## 1. Three versions and three locations

Record separately:

- **Repository:** checkout revision and engine distribution version. This revision declares distribution `0.2.0` and `hermes_requires: "==0.16.0"` in [distribution.yaml](../../../distribution.yaml).
- **Installed host:** actual Hermes version, active profile name/path, model/provider, and selected terminal backend. Current online documentation may describe features unavailable in the pinned version.
- **Installed profile:** manifest/revision and actual files present. A checked-out repository is not proof that its contents were installed into the active profile.

Also distinguish profile state, terminal working directory, and private research storage. Upstream docs state that profiles organize state through `HERMES_HOME`; profiles do not sandbox filesystem access. Default host subprocesses can use ordinary user-level CLI configuration. A profile name is therefore not a security boundary. [Official profiles documentation](https://hermes-agent.nousresearch.com/docs/user-guide/profiles/).

The repository contains `thorpe` paths and `muse-spark-1.2-contributor` references in operational skills. Treat them as installation-specific examples, not facts about a fresh user's machine. Do not assume token-meter scripts, sanitized example reports, portfolio folders, models, or cron jobs exist.

## 2. Deployment matrix

Upstream configuration documents local, Docker, SSH, and several managed/container terminal backends. Backend selection determines where shell commands execute; the installed version must be checked before using a documented option. [Official configuration documentation](https://hermes-agent.nousresearch.com/docs/user-guide/configuration/).

| Deployment | Verify execution and storage | Verify scheduling | Main gotcha |
|---|---|---|---|
| VPS | Exact server/account, terminal backend, project directory, private data directory, and persistent disk | Gateway/service status, correct profile, timezone, job identity, and run history | A desktop profile does not prove the VPS has the same files, dependencies, model route, or approved credentials |
| Managed cloud/container | Actual supported backend in installed Hermes; clone/mount available inside it; explicit durable volume | Identify where the gateway lives and whether it can wake the selected executor | Temporary sandboxes and durable profile state are separate; files visible on the gateway host may not be visible inside the terminal backend |
| Local computer | Authorized workspace and private inputs; Python runtime; account permissions | Gateway runs on an available machine; inspect actual job and receipts | Local backend can access the user account's filesystem; profile separation is not filesystem isolation |
| Local VM | Guest installation/runtime and narrowly scoped mounts; persistent guest storage | Guest gateway plus VM and host uptime | VM networking, shared folders, clipboard, and model/API egress need independent review |

Model provider choice is independent of this table. Hermes can be the host while a separately configured provider supplies inference; do not describe API data as remaining local just because Python runs locally.

## 3. What a profile installation actually includes

The [staging builder](../../../scripts/build_profile_staging.py) uses a deny-by-default allowlist. At this revision it includes distribution/configuration/SOUL files, `.env.EXAMPLE`, `dlc-page.md`, skills, schemas, valid synthetic fixtures, and the engine. It excludes `docs/`, `local/`, tests, logs, outputs, and other forbidden roots. The eight root hero playbooks are not in its file allowlist.

Consequences:

1. These onboarding guides are source-repository documentation. They are **not automatically included in an installed profile**.
2. Do not promise that root hero files or linked documentation can be read from a staged profile. Inspect the manifest and actual paths; use a separately authorized source checkout or a future reviewed distribution change if needed.
3. Read-only onboarding should not call the staging builder: it writes a new tree. Installation, profile switching, dependency installation, and staging are separate authorized steps.
4. Never point a profile installer at a source tree merely to bypass staging exclusions. Preserve the private-data checks and install-source validation.

Historical verification receipts in `docs/governance/` document their specific candidates and environments. They do not certify a new installation or prove current upstream compatibility. Version mismatch is a blocker to report, not permission to upgrade the user silently.

## 4. Non-mutating first-session audit

Ask Hermes:

> Read the shared onboarding contract. Inspect my selected profile and approved project metadata without changing files, switching profiles, installing packages, reading secret values, running repository code, making paid calls, or creating schedules. Report verified capabilities and blockers. Do not assume that any installation-specific path from a skill exists.

| Audit item | Required evidence | When missing |
|---|---|---|
| Host/profile identity | Host version; active profile name and resolved state directory; non-secret model/provider metadata | Ask the user to select the intended existing profile |
| Workspace/executor | Tool inventory, terminal backend, actual working directory, readable clone or staged manifest | Research-only mode until an approved executor is available |
| Runtime/dependencies | Python inventory compared with `>=3.11,<3.14`; `pyproject.toml` read; required runtime dependencies are empty | Report exact runtime gap; do not install |
| Source capabilities | Available browser, fetch, file-picker, OCR, clipboard and confirmation tools; permission scope | Return actionable blocked states rather than claiming the host bridge provides tools automatically |
| Storage/containment | Approved private root, access/ownership metadata, retention and persistence evidence | Do not save real inputs or claim durability; later write/readback verification needs authorization |
| Credentials | Presence/status only in the intended profile; no credential contents | Have the user configure secrets through the appropriate secure flow |
| Cron | Existing scheduler/gateway status, selected profile's jobs, timezone, destination, last-run outcome | On demand only; document schedule as requested or proposed, never active |
| Pack availability | Actual files/skills and supported method-pack inventory, compared with the source checkout | Keep conversational hero lenses distinct from executable CLI packs |

Inspecting declarations does not execute the engine. A later authorized synthetic run must retain the exact command, input hashes, repository revision, exit/result, and output path before labeling the integration tested.

## 5. Introduce the eight investor lenses accurately

Use the complete [shared investor cards](../common.md), including purpose, fit, blind spot, and example question. The source files are:

| Card | Source file | Core use |
|---|---|---|
| Edward Thorp | `dlc-thorp` | Quantified edge, fractional Kelly, hedging, and survival |
| Michael Mauboussin | `dlc-mauboussin` | Base rates, expectations embedded in price, calibration |
| Munger & Buffett | `dlc-munger-buffett` | Business quality, moat, competence, long-horizon value |
| Thomas and Philippe Laffont | `dlc-laffont` | Technology and secular growth theses |
| Scott Galloway | `dlc-Galloway` | Brand, platform economics, and market structure |
| **Brad Gerstner / Altimeter** | `dlc-Gerstner` | Crossover investing and technology supercycles |
| Martin Shkreli | `dlc-shkreli` | Filings-first company analysis, catalysts, and event risk, including biotech/pharma |
| Chris Camillo | `dlc-camillo` | Consumer/cultural observations and social-arbitrage hypotheses |

The root README's “corporate turnaround” description for Gerstner conflicts with the actual playbook's Brad Gerstner/Altimeter identity. Use the playbook identity for onboarding; do not silently recast him as Lou Gerstner.

Scott Page's [many-model lens](../../../dlc-page.md) is optional and separate from these eight cards. A card is a simulated research framework, not the real investor's opinion, affiliation, or endorsement. Nor does a card imply a corresponding `capital method` CLI identifier exists.

Ask: “Which lens should lead the research, and which should challenge the risk?” Preserve the two choices separately. Explain terms at the user's preferred level, begin with a synthetic example, and give the user a chance to revise the choices after seeing one comparison.

## 6. Research flow and safe failure behavior

1. Agree on one question, explanation depth, approved input files, private output location, and any provider transmission. No brokerage credentials or account linking.
2. Capture file/source reference, timestamp, acquisition method, raw hash, and limitations. Confirm screenshot-derived values and dates before treating them as measured.
3. Use the [host bridge](../../host/hermes-host-bridge.md) and [source-specific extraction](../../host/source-extraction-adapters.md) contracts. A generic capability response is not yet eligible for a belief update.
4. Present the four customer-facing evidence labels **Measured**, **Calculated**, **Modeled**, and **Forecasted**, mapping source-engine `measured`, `calculated`, `modeled`, and `forecast` respectively. Retain **Narrative** and **Unknown** as distinct additional categories, never measured evidence. Only eligible user-verified evidence updates beliefs. Run deterministic math in the verified executor, never replace unavailable engine results with language-model arithmetic.
5. Show disagreement between lenses, scenario assumptions, stale inputs, and survivability constraints. Margin danger can override Kelly.
6. Request explicit authorization before a decision record is saved. No automatic trades, order placement, brokerage connection, or money movement under any persona or schedule.

BYOK values stay in private host secret storage/environment, never in Git, reports, fixtures, prompts, or diagnostic output. `local/` is ignored except its README, but `.gitignore` is not a network privacy control. Cloud backups, provider prompts, screenshots, and browser uploads each need their own data boundary.

## 7. Cron is a deployment fact, not a documentation promise

Upstream Hermes documents gateway-based cron, with jobs and run state tied to the selected profile. It also documents setting the job working directory explicitly rather than assuming repository context. Check the installed version's supported interface before relying on current examples. [Official cron documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron/).

`START_HERE.md` describes a live macro scan and a planned artifact-refresh schedule for the originating setup. A new clone installs neither. Inspect the actual jobs before creating or duplicating any. Do not copy a timezone, “every other Saturday” assumption, recency guard, delivery target, or installed `xurl` claim without verifying it.

Before an authorized schedule, record its purpose, exact cadence/timezone, model budget, allowed sources, approved output/delivery, persistence, failure reporting, and cancellation method. Unattended runs must stop at new human confirmation gates. Missing gateway, paused VM, absent credentials, or missing files means blocked, not completed.

## Sources and support status

- [Shared contract](../common.md), [distribution](../../../distribution.yaml), [staging builder](../../../scripts/build_profile_staging.py), [runtime manifest](../../../pyproject.toml)
- [Host capabilities](../../host/capability-injection.md), [system boundary](../../architecture/system-boundary.md), [private-data policy](../../safety-boundaries/private-data-policy.md), [START_HERE](../../../START_HERE.md)
- [Hermes profiles](https://hermes-agent.nousresearch.com/docs/user-guide/profiles/), [configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration/), [cron](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron/), accessed 2026-10-09

This guide establishes a readiness checklist and known source-level constraints. It does not certify an installed profile, host version upgrade, new deployment backend, provider model, scheduled job, or live end-to-end research run.
