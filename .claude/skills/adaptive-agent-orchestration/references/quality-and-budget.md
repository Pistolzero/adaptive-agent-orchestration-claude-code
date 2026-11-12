# Quality, completion and cost ledger

Optimize for **verified user value per total work**, not number of agents or the illusion of autonomy.

## Minimal ledger when observable

- Budget profile, timestamp and source, model/window applicability, or `UNKNOWN`.
- Main model/effort selected by user; delegate actual models/efforts if reported by runtime.
- Task IDs and file ownership, active and total agents, retry count, output artifacts.
- Observed elapsed time, token use, cost or quota status **only where genuinely surfaced**.
- Verification evidence: tests, diffs, raw results, sources and failed/unrun checks.
- Approval boundaries and scope of incomplete work.

## Effective execution

- Read existing decision summaries instead of repeatedly loading the entire repository.
- Give small models enough concrete examples to avoid speculative retries.
- Keep any big tool output in a delegate's context; return concise checkable excerpts.
- Do not start two agents on the same mutable files.
- Verify key claims, but avoid redundant rechecks when the evidence is already fresh and direct.
- Stop a futile access loop; record the actual blocker and pursue independent safe work.
- Do not claim persistent background activity when the session cannot do it.
- In workflow mode, check actual stage count and usage in `/workflows`; policy instructions and size guidelines do not enforce a hard spending cap.

## Measuring improvement

A claim such as "40% less token use" requires a controlled baseline: same inputs, acceptance requirements, actual measured total tokens/cost, comparable conditions and validation standards. If a measurement is absent, say `NOT OBSERVABLE` and make no savings claim.

## Final verification checklist

1. Does the deliverable satisfy the request?
2. Did mandatory tests pass, fail or remain unrun—with reasons?
3. Were sources and modifications independently checked?
4. Are errors, retries, risk and missing evidence disclosed?
5. Were permissions respected and secrets protected?
6. Is the budget summary grounded in actual, applicable observations?
