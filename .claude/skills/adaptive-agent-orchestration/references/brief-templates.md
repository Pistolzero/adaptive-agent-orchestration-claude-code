# Required delegation briefs

A delegate starts without the entire parent conversation. Do not send it a bare request such as "figure it out". Fill the following with exact known facts and paths.

## Mandatory universal brief

```text
TASK_ID:
ROLE_INSTANCE / intended model & effort:
WHY_DELEGATE:
OBJECTIVE (one artifact or answer):
KNOWN_FACTS + evidence:
INPUTS (exact paths, URLs, ranges, timestamps):
EXCLUDED_SCOPE / forbidden modifications:
PERMITTED_TOOLS / read-write boundaries:
ORDERED_STEPS:
ACCEPTANCE_CRITERIA:
FAILURE_AND_EDGE_CASE_BEHAVIOR:
OUTPUT_PATH / format / length cap:
DEPENDENCIES / when to stop or escalate:
FINAL_REPORT: Use failure-and-evidence-report.md; all fields required.
```

## Mechanical Haiku worker

Give the schema, allowed transforms, ordering, tie breaks, malformed examples, exact output columns, expected counts where known and a source spot-check. Do not permit free-form inference from ambiguous records. Process bounded batches and report read/accepted/rejected/ambiguous counts.

**Example**: Read `records/a.csv` only. Normalize unambiguous ISO timestamps, leave unknown dates flagged, output a source-preserving comparison, and report all rejected lines; do not write to input files.

## Sonnet research worker

Set narrow factual question, required version/date, source priority (official docs, source code, specifications first), expected citations, and handling when primary sources disagree. No blind installation or mutation. Limit initial browsing to the few highest-value queries; reassess before broadening.

**Example**: Determine whether product version X supports feature Y. Return exact linked evidence, supported/unsupported/unknown classification and caveats. No device modifications.

## Builder worker

Provide exact file ownership, behavior spec, existing failing signal, minimal fix approach, relevant tests, rollback and what not to refactor. Require before/after diff summary and actual test command/output. If blocked by a design/permission decision, pause that branch and report it rather than guessing.

**Example**: Only edit `src/parser.py` and `tests/test_parser.py`. Reproduce the reported bug, make a minimal patch, add malformed-input case, run focused tests. No dependency install.

## Independent reviewer

Provide original requirement, changed-file paths or diff, relevant tests and risk criteria. Require direct inspection, severity-ranked defects with file/line locations, missing tests and acceptance decision. Reviewer should not edit the same files by default.

## Before dispatch

- Could the delegate judge completion without inventing context?
- Are source paths, allowed writes and disallowed steps concrete?
- Are test and evidence criteria explicit?
- Is selected model adequate for the task's ambiguity and consequence?
- Is the expected short return useful for independent verification?

If any answer is no, refine the brief before spending usage.
