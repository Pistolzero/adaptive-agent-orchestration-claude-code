# Dynamic team sizing and independence

The valid answer to "How many delegates?" is often **zero**.

1. List only independent, ready units with explicit evidence inputs, deliverables, acceptance checks, and write ownership.
2. Apply [budget-policy.md](budget-policy.md) and the user's concurrency cap. Never exceed 3 concurrent delegates under this Skill without an explicit user override, even if Claude Code permits more.
3. Under UNKNOWN/CONSERVE, start at most one new delegate per user task by default. Under BALANCED, use 0–2. Under QUALITY, start <= 2 and reserve the third for truly independent work.
4. Estimate setup cost, repeated context, integration cost and validation cost. If a subtask is tiny or serial, the main should do it.
5. Multiple instances of the same role can process **non-overlapping** partitions. Assign unique task IDs. Writers get non-overlapping files. Do not let the same files be edited concurrently.
6. Resolve prerequisites first. Use one targeted second opinion only when a substantive unresolved claim could affect the outcome.
7. If a required approval is blocked, proceed on safe independent work, but never treat the approval as granted.
8. Do not spawn chains of subagents recursively to evade fan-out caps. Nested or agent-team features, if used at all, count toward the user-defined total-policy intention.
9. Track actually launched agents, not planned prompts or static files.

## Typical choices

| Scenario | Plan |
|---|---|
| Simple bug and clear fix | Main alone, or one builder if manager-only requested |
| Two truly independent documents | Two separate read-only workers only if budget permits |
| Large dataset with uniform rules | 1 Haiku worker; consider 2 disjoint partitions under QUALITY |
| Security-sensitive production action | Main approval gate; delegates gather evidence only |
| Near quota limit | No new delegates; preserve state and report honestly |

Claude Code may have a higher runtime concurrency limit. This Skill's smaller default cap is a **cost policy**, not a claim about the runtime limit. Parallel speedups may cost more tokens overall.
