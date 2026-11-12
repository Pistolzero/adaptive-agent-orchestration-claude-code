# Mandatory failure and evidence disclosure

Every delegated task must return **every field** below. A recovered error is still an error and stays in the report. Never include secrets or unnecessarily reveal user-specific or third-party private data.

```text
TASK_ID:
ROLE_INSTANCE:
MODEL_EFFORT: <observed actual, or NOT OBSERVABLE>
STATUS: COMPLETE | PARTIAL | BLOCKED | FAILED
SCOPE:
COMPLETED:
NOT_DONE: <all omitted/incomplete items or none>
ATTEMPTS_AND_ERRORS: <attempt -> observed failure -> recovery -> outcome; or none>
UNRUN_OR_FAILED_CHECKS: <test/check -> reason or none>
EVIDENCE: <source files/lines, direct links, exact checks and observed results>
MODIFICATIONS: <created/changed/deleted files or none>
ASSUMPTIONS_AND_UNCERTAINTIES:
RISKS_OR_SIDE_EFFECTS:
ACCEPTANCE_CHECKLIST: <criterion -> PASS/FAIL/NOT_TESTED + evidence>
NEEDS_MAIN_AGENT_DECISION:
SUGGESTED_NEXT_ACTION:
```

## Status rules

- **COMPLETE**: every mandatory acceptance criterion passed and has evidence.
- **PARTIAL**: useful output exists but some required check is missing or a step incomplete.
- **BLOCKED**: progress depends on permission, access, external data or user action.
- **FAILED**: task's required outcome was not achieved.

Passing after retry does not erase earlier failures. Do not call a check passed if only a command was prepared or its output was inferred. Never represent an agent as having run when only its definition or task prompt exists.

## Main-agent audit

1. Reconcile report against the original brief and every acceptance criterion.
2. Open the actual output/diff/source sample where possible. Check high-impact claims against original evidence.
3. Compare `COMPLETED` with `NOT_DONE`, errors, unrun checks, modifications and risks. A missing field triggers a targeted follow-up, not automatic acceptance.
4. Re-run a focused deterministic test or request an independent reviewer only when the risk justifies the extra usage.
5. Retry a recoverable failure once at most after addressing its cause, within the delegation cap. Summarize any unresolved check in the final user-facing answer.
