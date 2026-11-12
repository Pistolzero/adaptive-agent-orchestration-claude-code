# Usage examples

These prompts are examples, not commands that automatically grant permissions.

## Balanced coding task

```text
Use /adaptive-agent-orchestration on the existing repository.
My budget profile is BALANCED. Keep the main model I selected.
Choose zero or one delegate unless a second independent task would be clearly valuable.
Fix the parser bug in src/parser.ts without changing unrelated files.
Require evidence of the failing case, a targeted test, the diff, and a complete failure log.
Do not install packages or deploy without asking.
```

## Manager-led research

```text
Use adaptive-agent-orchestration. The main model is manager-only: it should route
bounded work to an appropriate Sonnet subagent and only perform critical review.
Investigate whether version X of framework Y supports feature Z.
Prefer primary sources; separate facts from unsupported claims.
Do not spawn a second delegate unless the first evidence conflicts materially.
Report missing or inaccessible documentation rather than inventing a result.
```

## Mechanical data extraction

```text
Use the aao-bulk-analyst role for this narrow read-only task.
From files/records.csv, classify each row using the exact supplied rubric.
Preserve source values, flag ambiguous cases, and report read/accepted/rejected counts.
Show five sampled source comparisons. No file modification.
```

## Low remaining usage

```text
Use adaptive-agent-orchestration in CONSERVE mode. Do not create parallel agents.
Finish the highest-value verified portion of the existing work.
Stop new delegation if the usage status becomes critical.
Show incomplete checks, evidence and the smallest next action.
```

## Required conclusion example

```text
Coordinator: selected model [user choice]; one aao-researcher used (actual model if observable).
Result: supported claim with source lines / URL.
Not done: vendor build-specific confirmation.
Failures: first documentation URL unavailable, alternative primary source checked.
No files changed. Budget: UNKNOWN/CONSERVE; actual token usage NOT OBSERVABLE.
```
