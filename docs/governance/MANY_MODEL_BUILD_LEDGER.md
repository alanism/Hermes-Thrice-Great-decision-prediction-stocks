# Many-Model Thinking — TDD Protocol and Build Ledger

Status: Authoritative TDD protocol and execution ledger specification.  
Task: T05  
Primary Hero: `Ryan Lopopolo`  
Verifier Hero: `Boris Cherny`  

---

## 1. Task-Claim & Lifecycle Protocol

Every task in [`docs/tasks_list.md`](../tasks_list.md) must advance strictly through the following state machine:

```text
PENDING ──> READY ──> IN_PROGRESS ──> RED_RECORDED ──> GREEN_VERIFIED ──> DONE
                                                                    └──> CUT (T12 zero-delta only)
```

### Invariant Rules
1. **Lowest-Numbered READY Task:** Always claim the lowest-numbered `READY` task whose dependencies are satisfied.
2. **Separation of Implementer and Verifier:** The primary implementation hero and the independent verifier hero must be distinct individuals.
3. **Immutability of Frozen Tests:** The verifier authors test cases and fixtures, records their SHA-256 hashes, and freezes them. The implementer edits production files only and cannot alter frozen test files to make tests pass.
4. **Assertion-Level RED:** A valid RED stage requires an assertion failure proving missing business logic or boundary enforcement—never an unhandled syntax error, import error, or dependency failure.
5. **No Regressions:** Full test suite count must be $\ge$ baseline test count (216 tests) with 0 failures at every GREEN gate.

---

## 2. Frozen-Test Hash Procedure

Before implementing any production code:
1. The verifier writes unit and rejection tests in `tests/` and synthetic fixtures in `fixtures/valid/contracts/`.
2. Compute SHA-256 hashes of all authored test files:
   ```bash
   Get-FileHash tests/contracts/test_*.py -Algorithm SHA256
   ```
3. Record the test paths and their exact SHA-256 hashes in the task receipt.
4. When validating GREEN status, verify that test hashes remain identical. Any change to a frozen test file invalidates the receipt and returns the task to `RED_RECORDED`.

---

## 3. Mutation Testing Policy

Each functional slice must kill at least one relevant injected mutant before advancing to `DONE`:
* **Threshold / Constant Mutants:** e.g., modifying $\alpha \le 2.0$ to $\alpha < 2.0$, or changing the two-thirds ensemble threshold $\lceil 2A / 3 \rceil$.
* **Boundary Condition Mutants:** e.g., allowing booleans as numbers, accepting $p + q > 1.0$ in Bass diffusion, or failing to check matrix row sums.
* **Safety Policy Mutants:** e.g., removing the `HEAVY_TAIL_UNDEFINED_MEAN` veto or falling back to `recommendations[0]` in Committee mode.

A mutant is successfully "killed" when the frozen test suite catches the injected fault and fails with a deterministic assertion error.

---

## 4. Build Ledger Task Receipt Schema & Template

Every completed task must record a receipt in `docs/tasks_list.md` adhering to this schema:

```markdown
### [Task ID] — [Task Title]

- **State:** DONE
- **Depends:** [Task IDs]
- **Intelligence/model:** [Tier / Model]
- **Primary hero:** [Hero Name]
- **Verifier hero:** [Hero Name]
- **Editable scope:** [Allowed paths]
- **Frozen Test Hashes:**
  - `[test_path_1]`: `[SHA256]`
  - `[test_path_2]`: `[SHA256]`
- **RED Evidence:**
  - Command: `[command]`
  - Exit Code: `[code != 0]`
  - Output: `[AssertionError snippet]`
- **GREEN Evidence:**
  - Command: `[command]`
  - Exit Code: `0`
  - Output: `[X passed, full suite passed (count >= baseline)]`
- **Mutant Killed:**
  - Mutation Description: `[Description of injected flaw]`
  - Test Failure: `[Assertion error caught by test]`
- **Risk IDs Retired:** `[MR-XX, ...]`
- **Gate:** [Specific criteria from plan]. Passed.
```
