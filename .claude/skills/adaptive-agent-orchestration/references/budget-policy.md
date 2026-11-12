# Budget-aware delegation and usage boundaries

## Reliable inputs

1. Fresh official usage information legitimately visible in this Claude Code session, when it clearly identifies the applicable quota/window/model. The terminal `/usage` command may show usage for accounts and plans where available.
2. A recent user-supplied official status, including timestamp and the relevant plan or model window.
3. Explicit user budget preference and agent cap.
4. Otherwise **UNKNOWN/CONSERVE**.

Never access credentials, hidden authentication files or undocumented quota endpoints. Do not infer remaining usage from subscription name, screenshots without scope, or messages sent. Do not assume an official usage UI means a stable programmatic quota API is available.

## Optional heuristic tiers — NOT official Anthropic thresholds

| Profile | Relevant remaining allowance, if reliably supplied | Active delegates | Policy |
|---|---|---:|---|
| QUALITY | >= 60% | 0–3 | Begin with 1–2 independent tasks; third only if justified |
| BALANCED | 30–59% | 0–2 | Focused work; conditional review |
| CONSERVE | 10–29% | 0–1 | One bounded worker or main alone |
| CRITICAL | < 10%, exhausted, or explicit near-limit warning | 0 new | Checkpoint; minimize new work |
| UNKNOWN | No fresh reliable input | 0–1 | Conservative default, no speculative branches |

In CONSERVE and UNKNOWN, the default also limits **total new delegates per user task** to one. Finishing or failing a delegate does not free that allowance. Resume the same delegate if supported and useful. A fresh budget signal can move the task to another profile, and an explicit user override can raise the cap. CRITICAL starts no new delegates.

These bands are policy suggestions only. They do not map to token counts. Provider limits can differ by model, subscription or time window. User-specified stricter caps take precedence. A user can deliberately request higher quality if supported by their account and approval context.

## Routing with a budget

- Main agent: prefer Fable 5.2 when selected and available, or an explicitly selected Opus fallback; delegate expensive bounded work rather than transferring final responsibility. The Skill cannot set the session model.
- `aao-bulk-analyst`: Haiku low; precise, repeatable extraction. Bad input or ambiguous rules require escalation.
- `aao-researcher` / `aao-builder`: Sonnet medium by default. Reusing one good worker is often cheaper than serially spawning many.
- `aao-researcher-deep` / `aao-reviewer`: Sonnet high for difficult analysis or material verification.
- `aao-critical-reviewer`: Opus high only for consequential independent review with a credible expected benefit.

A role's configured model/effort is not guaranteed to run unchanged: per-invocation options, environment settings, account restrictions, provider routing and version-specific fallback may intervene. Report actual resolution only when observable. Check `/tasks` if supported.

For a native workflow, count stage agents toward the planned staffing budget, specify smaller models explicitly, and inspect `/workflows` for actual usage. `workflowSizeGuideline=small` is advisory; ultracode can plan more than one workflow per request and can consume much more usage. Do not turn on paid Fable credits or start a large workflow merely to satisfy this policy.

## Keep consumption bounded

- Delegation overhead is real: include concise context, not entire chat transcripts or every log.
- A cheap model retried three times may cost more than one successful Sonnet attempt. Allow at most **one targeted retry** after addressing a recoverable cause, within the task’s delegation cap. An unchanged denial or rate limit calls for a permitted alternative or a checkpoint.
- `maxTurns` controls a single subagent's agentic-turn limit; it does not establish a token budget or a whole-session limit.
- Parent may still consume substantial tokens coordinating and verifying. "Manager-only" is a workflow preference, not a zero-cost mode.
- Keep separate budget snapshots for distinct models/windows; a rate-limit or remaining-percent indicator is not a token meter.
- Never turn on paid credits, change plans or bypass account limits without specific authorization.

## Ledger

Profile + evidence source/time/window; planned/actual agents; task partitions; actual model/effort if visible; retries/errors; artifacts; verified checks; measured usage when observable; unknowns. Never claim savings without a comparable, measured baseline.
