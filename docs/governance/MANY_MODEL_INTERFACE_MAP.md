# Many-Model Interface and Distribution Truth Map

Status: Authoritative baseline interface and distribution map for Many-Model Thinking extension.  
Task: T02  
Verification: `Mitchell Hashimoto` (Primary), `Boris Cherny` (Verifier)  

---

## 1. CLI Entrypoint and Command Tree

* **CLI entry configuration:** [`pyproject.toml:13`](../../pyproject.toml#L13) maps `capital = "capital_decision_lab.plugin.commands:main"`.
* **CLI Implementation:** [`plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py)
* **Parser definition:** `setup_cli(parser)` at [`commands.py:72-158`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L72-L158)
* **Dispatcher implementation:** `_dispatch(args, *, local_root)` at [`commands.py:177-504`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L177-L504)
* **Programmatic entry:** `run_cli(argv, *, local_root)` at [`commands.py:506-510`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L506-L510)
* **Main entry:** `main(argv)` at [`commands.py:520-525`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L520-L525)

### Documented Subcommands and Dispatch Map

| Command String | Parser Line | Dispatch Line | Handler / Implementation Symbol |
|---|---|---|---|
| `capital doctor` | [`commands.py:75`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L75) | [`commands.py:179-180`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L179-L180) | `doctor()` at [`commands.py:47-69`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L47-L69) |
| `capital validate --synthetic` | [`commands.py:76-77`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L76-L77) | [`commands.py:448-466`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L448-L466) | `validate_contract` over [`fixtures/valid/contracts/`](../../fixtures/valid/contracts) |
| `capital analyze --case <path> [--assumption-update <path>]` | [`commands.py:78-80`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L78-L80) | [`commands.py:467-492`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L467-L492) | `analyze_case` at [`orchestration/analyze.py:10`](../../plugins/capital-decision-lab/capital_decision_lab/orchestration/analyze.py#L10) |
| `capital compare --case <path>` | [`commands.py:81-82`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L81-L82) | [`commands.py:467-492`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L467-L492) | `compare_case` at [`orchestration/compare.py:11`](../../plugins/capital-decision-lab/capital_decision_lab/orchestration/compare.py#L11) |
| `capital record --analysis <path> --authorization <path>` | [`commands.py:83-85`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L83-L85) | [`commands.py:493-503`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L493-L503) | `record_from_files` at [`orchestration/record.py:9`](../../plugins/capital-decision-lab/capital_decision_lab/orchestration/record.py#L9) |
| `capital evidence validate --file <path>` | [`commands.py:88-89`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L88-L89) | [`commands.py:389-412`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L389-L412) | `validate_local_evidence` at [`evidence/validation.py:27`](../../plugins/capital-decision-lab/capital_decision_lab/evidence/validation.py#L27) |
| `capital evidence analyze-event-market --snapshot <path>` | [`commands.py:90-92`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L90-L92) | [`commands.py:389-412`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L389-L412) | `analyze_event_market` at [`evidence/event_market.py:13`](../../plugins/capital-decision-lab/capital_decision_lab/evidence/event_market.py#L13) |
| `capital evidence analyze-polymarket --snapshot <path>` | [`commands.py:90-92`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L90-L92) | [`commands.py:389-412`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L389-L412) | `analyze_event_market` at [`evidence/event_market.py:13`](../../plugins/capital-decision-lab/capital_decision_lab/evidence/event_market.py#L13) |
| `capital evidence analyze-social --batch <path>` | [`commands.py:93-94`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L93-L94) | [`commands.py:389-412`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L389-L412) | `analyze_social` at [`evidence/social.py:10`](../../plugins/capital-decision-lab/capital_decision_lab/evidence/social.py#L10) |
| `capital evidence synthesize --inputs <path>` | [`commands.py:95-96`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L95-L96) | [`commands.py:389-412`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L389-L412) | `synthesize_evidence` at [`evidence/synthesis.py:9`](../../plugins/capital-decision-lab/capital_decision_lab/evidence/synthesis.py#L9) |
| `capital evidence gather --case <path> --source <src> --query <q>` | [`commands.py:97-100`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L97-L100) | [`commands.py:354-372`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L354-L372) | `ConnectorRegistry.gather` at [`connectors/registry.py:30`](../../plugins/capital-decision-lab/capital_decision_lab/connectors/registry.py#L30) |
| `capital evidence inbox --case <path> --folder <fld>` | [`commands.py:101-103`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L101-L103) | [`commands.py:379-388`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L379-L388) | Reads json files in folder |
| `capital evidence verify --item <path>` | [`commands.py:104-105`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L104-L105) | [`commands.py:373-378`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L373-L378) | Sets `verification_status = "user_verified"` |
| `capital belief update --case <path> (--synthesis\|--evidence) <path> --sensitivity <path>` | [`commands.py:106-113`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L106-L113) | [`commands.py:413-438`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L413-L438) | `build_belief_update` at [`evidence/bayesian.py:11`](../../plugins/capital-decision-lab/capital_decision_lab/evidence/bayesian.py#L11) |
| `capital assumption propose --belief-update <path>` | [`commands.py:114-117`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L114-L117) | [`commands.py:439-447`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L439-L447) | `create_assumption_proposal` at [`evidence/proposals.py:10`](../../plugins/capital-decision-lab/capital_decision_lab/evidence/proposals.py#L10) |
| `capital portfolio import --file <path>` | [`commands.py:118-122`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L118-L122) | [`commands.py:280-287`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L280-L287) | `import_portfolio_file` at [`research/portfolio.py:9`](../../plugins/capital-decision-lab/capital_decision_lab/research/portfolio.py#L9) |
| `capital portfolio validate --file <path>` | [`commands.py:118-122`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L118-L122) | [`commands.py:288-290`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L288-L290) | `validate_portfolio_snapshot` at [`research/portfolio.py:47`](../../plugins/capital-decision-lab/capital_decision_lab/research/portfolio.py#L47) |
| `capital thesis start --portfolio <path>` | [`commands.py:123-125`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L123-L125) | [`commands.py:291-297`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L291-L297) | `evaluate_research_readiness` at [`research/loop.py:10`](../../plugins/capital-decision-lab/capital_decision_lab/research/loop.py#L10) |
| `capital thesis refine --case <path>` | [`commands.py:123-126`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L123-L126) | [`commands.py:291-297`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L291-L297) | `evaluate_research_readiness` at [`research/loop.py:10`](../../plugins/capital-decision-lab/capital_decision_lab/research/loop.py#L10) |
| `capital research loop --case <path>` | [`commands.py:127-129`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L127-L129) | [`commands.py:298-323`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L298-L323) | `evaluate_research_readiness` at [`research/loop.py:10`](../../plugins/capital-decision-lab/capital_decision_lab/research/loop.py#L10) |
| `capital research run --case <path> --host-inputs <path>` | [`commands.py:127-130`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L127-L130) | [`commands.py:302-323`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L302-L323) | `run_analyze_position` at [`orchestration/research_run.py:34`](../../plugins/capital-decision-lab/capital_decision_lab/orchestration/research_run.py#L34) |
| `capital analyze-position --case <path> --host-inputs <path> [--method <m>]` | [`commands.py:131-134`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L131-L134) | [`commands.py:231-249`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L231-L249) | `run_analyze_position` + `run_method_pack` |
| `capital method list` | [`commands.py:135-137`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L135-L137) | [`commands.py:184-185`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L184-L185) | `available_method_packs` at [`methods/runner.py:12`](../../plugins/capital-decision-lab/capital_decision_lab/methods/runner.py#L12) |
| `capital method run --pack <pack> --case <path>` | [`commands.py:135-138`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L135-L138) | [`commands.py:190-192`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L190-L192) | `run_method_pack` at [`methods/runner.py:21`](../../plugins/capital-decision-lab/capital_decision_lab/methods/runner.py#L21) |
| `capital method committee --packs <p...> --case <path>` | [`commands.py:135-139`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L135-L139) | [`commands.py:193-195`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L193-L195) | `run_committee` at [`methods/runner.py:90`](../../plugins/capital-decision-lab/capital_decision_lab/methods/runner.py#L90) |
| `capital confirmation queue --case <path> --host-inputs <path>` | [`commands.py:140-142`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L140-L142) | [`commands.py:200-210`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L200-L210) | `build_confirmation_queue` at [`host/confirmation_queue.py:11`](../../plugins/capital-decision-lab/capital_decision_lab/host/confirmation_queue.py#L11) |
| `capital confirmation apply --queue <path> --responses <path>` | [`commands.py:140-143`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L140-L143) | [`commands.py:211-220`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L211-L220) | `pair_confirmation_responses` at [`host/confirmation_queue.py:24`](../../plugins/capital-decision-lab/capital_decision_lab/host/confirmation_queue.py#L24) |
| `capital confirmation status --case <path>` | [`commands.py:140-144`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L140-L144) | [`commands.py:221-230`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L221-L230) | Checks `pending_count` |
| `capital model-health check --case <path> --evidence <path>` | [`commands.py:145-147`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L145-L147) | [`commands.py:324-334`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L324-L334) | `evaluate_model_health` at [`recommendation/health.py:11`](../../plugins/capital-decision-lab/capital_decision_lab/recommendation/health.py#L11) |
| `capital recommend --case <path>` | [`commands.py:148`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L148) | [`commands.py:335-343`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L335-L343) | `build_recommendation` at [`recommendation/engine.py:13`](../../plugins/capital-decision-lab/capital_decision_lab/recommendation/engine.py#L13) |
| `capital decision record --recommendation <path> --authorization <path>` | [`commands.py:149-151`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L149-L151) | [`commands.py:344-351`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L344-L351) | `record_recommendation` at [`recommendation/records.py:12`](../../plugins/capital-decision-lab/capital_decision_lab/recommendation/records.py#L12) |
| `capital host capabilities` | [`commands.py:152-154`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L152-L154) | [`commands.py:251-252`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L251-L252) | Returns `CAPABILITIES` from [`host/bridge.py:19`](../../plugins/capital-decision-lab/capital_decision_lab/host/bridge.py#L19) |
| `capital host ingest --capability-response <path>` | [`commands.py:152-155`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L152-L155) | [`commands.py:253-261`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L253-L261) | `ingest_capability_response` at [`host/bridge.py:34`](../../plugins/capital-decision-lab/capital_decision_lab/host/bridge.py#L34) |
| `capital host extract --source <src> --input <path>` | [`commands.py:152-156`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L152-L156) | [`commands.py:262-268`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L262-L268) | `extract_source` at [`host/bridge.py:46`](../../plugins/capital-decision-lab/capital_decision_lab/host/bridge.py#L46) |
| `capital host confirm --extraction <path> --confirmation <path>` | [`commands.py:152-157`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L152-L157) | [`commands.py:269-278`](../../plugins/capital-decision-lab/capital_decision_lab/plugin/commands.py#L269-L278) | `apply_confirmation` at [`host/confirmation.py:10`](../../plugins/capital-decision-lab/capital_decision_lab/host/confirmation.py#L10) |

---

## 2. Method Packs vs DLC Investor Personas

### Executable Method Pack Registry
* **Source of truth:** `PACKS` dict defined in [`plugins/capital-decision-lab/capital_decision_lab/methods/packs.py:6-46`](../../plugins/capital-decision-lab/capital_decision_lab/methods/packs.py#L6-L46)
* **Registered executable packs:**
  1. `"core"`: Fast default decision workflow ([`packs.py:7-14`](../../plugins/capital-decision-lab/capital_decision_lab/methods/packs.py#L7-L14))
  2. `"thorp"`: Sizing, survival, and edge-compression process ([`packs.py:15-22`](../../plugins/capital-decision-lab/capital_decision_lab/methods/packs.py#L15-L22))
  3. `"mauboussin"`: Outside-view and expectations process ([`packs.py:23-30`](../../plugins/capital-decision-lab/capital_decision_lab/methods/packs.py#L23-L30))
  4. `"contrarian_filings"`: Primary-source balance-sheet and cash-flow process ([`packs.py:31-38`](../../plugins/capital-decision-lab/capital_decision_lab/methods/packs.py#L31-L38))
  5. `"committee"`: Multi-pack comparison and synthesis router ([`packs.py:39-45`](../../plugins/capital-decision-lab/capital_decision_lab/methods/packs.py#L39-L45))
* **Listing function:** `available_method_packs()` returns `['committee', 'contrarian_filings', 'core', 'mauboussin', 'thorp']` ([`runner.py:12-13`](../../plugins/capital-decision-lab/capital_decision_lab/methods/runner.py#L12-L13))
* **Execution interface:** `run_method_pack(pack_id, case_bundle, *, base_result=None)` ([`runner.py:21-87`](../../plugins/capital-decision-lab/capital_decision_lab/methods/runner.py#L21-L87)) produces `nhi.method_pack_result.v1`.
* **Committee execution:** `run_committee(pack_ids, case_bundle)` ([`runner.py:90-111`](../../plugins/capital-decision-lab/capital_decision_lab/methods/runner.py#L90-L111)) produces `nhi.committee_result.v1`.

### Distinction from Root `dlc-*` Personas
* **Root simulated voices:** Root files `dlc`, `dlc-Galloway`, `dlc-Gerstner`, `dlc-camillo`, `dlc-laffont`, `dlc-mauboussin`, `dlc-munger-buffett`, `dlc-shkreli`, `dlc-thorp`.
* **Nature:** Plain-text markdown prompt templates for Hermes conversation and analytical personas.
* **Non-executable:** Root `dlc-*` files are **not** executable Python packages or CLI targets. They cannot compute formulas or produce deterministic receipts.
* **Planned `dlc-page`:** Follows the same distinction: an executable pack registered under `PACKS["page"]` in `packs.py`/`runner.py` for calculation, and a non-executable persona prompt `dlc-page` for Hermes chat explanation.

---

## 3. Schema Validation Registry and Contracts

* **Implementation:** [`plugins/capital-decision-lab/capital_decision_lab/contracts/validation.py`](../../plugins/capital-decision-lab/capital_decision_lab/contracts/validation.py)
* **Schema directory:** [`schemas/`](../../schemas) resolved dynamically via `SCHEMA_ROOT` ([`validation.py:12`](../../plugins/capital-decision-lab/capital_decision_lab/contracts/validation.py#L12))
* **Schema registry map (`_SCHEMA_FILES`):** [`validation.py:22-53`](../../plugins/capital-decision-lab/capital_decision_lab/contracts/validation.py#L22-L53) maps 30 contract version strings to JSON files in `schemas/`:
  - `nhi.assumption_register.v1` -> `assumption-register.v1.schema.json`
  - `nhi.assumption_update_proposal.v1` -> `assumption-update-proposal.v1.schema.json`
  - `nhi.bayesian_update.v1` -> `bayesian-update.v1.schema.json`
  - `nhi.belief_state.v1` -> `belief-state.v1.schema.json`
  - `nhi.decision_analysis.v1` -> `decision-analysis.v1.schema.json`
  - `nhi.decision_authorization.v1` -> `decision-authorization.v1.schema.json`
  - `nhi.decision_case.v1` -> `decision-case.v1.schema.json`
  - `nhi.decision_comparison.v1` -> `decision-comparison.v1.schema.json`
  - `nhi.decision_ledger.v1` -> `decision-ledger.v1.schema.json`
  - `nhi.decision_proposal.v1` -> `decision-proposal.v1.schema.json`
  - `nhi.event_market_signal.v1` -> `event-market-signal.v1.schema.json`
  - `nhi.event_market_snapshot.v1` -> `event-market-snapshot.v1.schema.json`
  - `nhi.evidence_batch.v1` -> `evidence-batch.v1.schema.json`
  - `nhi.evidence_item.v1` -> `evidence-item.v1.schema.json`
  - `nhi.evidence_source.v1` -> `evidence-source.v1.schema.json`
  - `nhi.host_capability_request.v1` -> `host-capability-request.v1.schema.json`
  - `nhi.host_capability_response.v1` -> `host-capability-response.v1.schema.json`
  - `nhi.host_extraction_result.v1` -> `host-extraction-result.v1.schema.json`
  - `nhi.host_source_artifact.v1` -> `host-source-artifact.v1.schema.json`
  - `nhi.host_user_confirmation.v1` -> `host-user-confirmation.v1.schema.json`
  - `nhi.kill_condition.v1` -> `kill-condition.v1.schema.json`
  - `nhi.portfolio_intent.v1` -> `portfolio-intent.v1.schema.json`
  - `nhi.portfolio_position.v1` -> `portfolio-position.v1.schema.json`
  - `nhi.portfolio_snapshot.v1` -> `portfolio-snapshot.v1.schema.json`
  - `nhi.recommendation.v1` -> `recommendation.v1.schema.json`
  - `nhi.recommendation_authorization.v1` -> `recommendation-authorization.v1.schema.json`
  - `nhi.scenario_assumption.v1` -> `scenario-assumption.v1.schema.json`
  - `nhi.social_evidence_signal.v1` -> `social-evidence-signal.v1.schema.json`
  - `nhi.stock_thesis.v1` -> `stock-thesis.v1.schema.json`
  - `nhi.thesis_sensitivity_map.v1` -> `thesis-sensitivity-map.v1.schema.json`
* **Evidence Atom Contract:**
  - `PROVENANCE_CLASSES` ([`validation.py:13-21`](../../plugins/capital-decision-lab/capital_decision_lab/contracts/validation.py#L13-L21)): `("measured", "assumed", "calculated", "modeled", "forecast", "decided", "unavailable")`
  - `_ATOM_PROPERTIES` ([`validation.py:54-62`](../../plugins/capital-decision-lab/capital_decision_lab/contracts/validation.py#L54-L62)): `{"value", "provenance_class", "unit", "input_refs", "formula_ref", "limitations", "reason"}`
  - `validate_evidence_atom` ([`validation.py:118-150`](../../plugins/capital-decision-lab/capital_decision_lab/contracts/validation.py#L118-L150))
  - `unavailable_result` helper ([`validation.py:94-116`](../../plugins/capital-decision-lab/capital_decision_lab/contracts/validation.py#L94-L116))
* **Validator function:** `validate_contract(document, *, schema_root=None)` ([`validation.py:278-315`](../../plugins/capital-decision-lab/capital_decision_lab/contracts/validation.py#L278-L315)) enforces recursive JSON Schema keywords (`type`, `const`, `enum`, `required`, `properties`, `additionalProperties`, `items`, `minItems`, `minLength`, `pattern`, `allOf`, `if/then/else`, local `$ref`) and validates embedded evidence atoms.

---

## 4. Deterministic Canonicalization and Hashing

* **Implementation:** [`plugins/capital-decision-lab/capital_decision_lab/contracts/canonical.py`](../../plugins/capital-decision-lab/capital_decision_lab/contracts/canonical.py)
* **Canonical JSON:** `canonical_json(value)` ([`canonical.py:11-19`](../../plugins/capital-decision-lab/capital_decision_lab/contracts/canonical.py#L11-L19)):
  - `sort_keys=True`
  - `separators=(",", ":")`
  - `ensure_ascii=False` (UTF-8 encoding)
  - `allow_nan=False`
* **Canonical SHA-256:** `canonical_sha256(value)` ([`canonical.py:22-24`](../../plugins/capital-decision-lab/capital_decision_lab/contracts/canonical.py#L22-L24)): `hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()`
* **Contract Payload Hash:** `contract_payload_hash(document)` ([`canonical.py:27-34`](../../plugins/capital-decision-lab/capital_decision_lab/contracts/canonical.py#L27-L34)): Deep-copies document, strips top-level `"canonical_hash"`, and hashes the remaining structure.

---

## 5. Distribution and Private-Data Staging Architecture

* **Distribution Spec:** [`distribution.yaml`](../../distribution.yaml)
  - `distribution_owned` entries ([`distribution.yaml:6-13`](../../distribution.yaml#L6-L13)):
    - `SOUL.md`
    - `config.yaml`
    - `.env.EXAMPLE`
    - `skills`
    - `schemas`
    - `fixtures/valid`
    - `plugins/capital-decision-lab`
* **Profile Staging Script:** [`scripts/build_profile_staging.py`](../../scripts/build_profile_staging.py)
  - `_ALLOWED_FILES`: `distribution.yaml`, `SOUL.md`, `config.yaml`, `.env.EXAMPLE` ([`build_profile_staging.py:22-25`](../../scripts/build_profile_staging.py#L22-L25))
  - `_ALLOWED_DIRS`: `skills`, `schemas`, `fixtures/valid`, `plugins/capital-decision-lab` ([`build_profile_staging.py:26-29`](../../scripts/build_profile_staging.py#L26-L29))
  - `_FORBIDDEN_TOP_LEVEL`: `{".git", ".venv", "docs", "local", "logs", "outputs", "tests", "tmp"}` ([`build_profile_staging.py:30-32`](../../scripts/build_profile_staging.py#L30-L32))
  - Preflight / Postflight scanners: `scan_repository(..., policy="domain")` and `scan_repository(..., policy="advice")` ([`build_profile_staging.py:90, 107`](../../scripts/build_profile_staging.py#L90))
* **Private-Data Staging Scanner:** [`scripts/check_staged_private_data.py`](../../scripts/check_staged_private_data.py)
  - Enforces rejection of any path containing `local` or file containing the literal string `"private_sentinel"` ([`check_staged_private_data.py:10-22`](../../scripts/check_staged_private_data.py#L10-L22)).
