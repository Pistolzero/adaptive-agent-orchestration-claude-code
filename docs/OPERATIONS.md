# Operating the orchestration Skill

## Budget profiles

`QUALITY`, `BALANCED`, `CONSERVE`, `CRITICAL` and `UNKNOWN` are custom policy modes, not Anthropic plan tiers. Apply `UNKNOWN/CONSERVE` when remaining usage is not clearly reported for the relevant model and window. Relevant percentage bands in the Skill are only configurable heuristics.

- **QUALITY:** 0–3 concurrent delegates if each has independent valuable work; start with 1–2.
- **BALANCED:** 0–2; reduce duplicated context and keep verification budget.
- **CONSERVE / UNKNOWN:** At most one new delegate per user task by default, including any sequential attempts. Resume it if possible and useful.
- **CRITICAL:** 0 new; checkpoint and disclose unfinished work. No automatic future continuation promise.

Subagents draw on the same account usage as the main Claude Code session. A smaller model is often cheaper per request but extra retries, context-loading and parallelism can make a supposedly economical run expensive.

## Manager-led mode

Use when the user requests the main model to plan and adjudicate rather than execute the bulk of analysis. The main model still reads enough evidence to judge completion. Give the worker exact sources, exit conditions and expected artifacts; avoid sending the full codebase or conversation repeatedly.

## Bounded autonomy

Continue authorized work using prior verified results. Preserve original errors and report remaining blockers together. An unchanged permission denial or rate limit should end retries for that operation. If several independent safe checks remain, continue and report together. Stop the affected branch at a real permission, credential, hardware or authorization boundary; continue independent safe work when practical. For impactful changes, batch a narrow, reversible approval request, but never interpret a generalized statement as bypassing real permissions.

## Escalation

Escalate only when an unresolved contradiction materially changes the outcome, a required test cannot run, a stronger model is necessary, or an approval is truly required. One independent second opinion can be useful, but repeated debate with no new evidence is not.

## Runtime regression scenarios

Use a scratch project and an authenticated Claude Code session. Run only the scenarios relevant to your setup. Inspect actual tool calls and outcomes before marking any scenario passed.

| Scenario | Setup | Expected evidence |
| --- | --- | --- |
| Missing or stale quota | Ask for a small task with two independent parts in UNKNOWN mode | No more than one new delegate across the full task, with the chosen main model preserved |
| Blocked access | Ask for two harmless reads, one denied by an existing permission rule and one allowed | One denial, no repeat under the same conditions, the allowed result delivered, and the denial recorded |
| Prior work and changed scope | Supply a completed check with its output and request a different read-only result | The completed check is reused where relevant and the requested result is delivered in the same session |
| Native discovery and routing | Follow the [installation check](INSTALL.md#verify-without-wasting-many-model-requests) | Skill and roles are discoverable. A single requested delegate returns its evidence, and observed model identity is recorded if available |

## Audit questions

- Did the worker actually run on the intended model, or is the model `NOT OBSERVABLE`?
- Are all acceptance criteria tied to evidence?
- Are failed attempts, skipped checks and temporary work visible?
- Were unauthorized files changed, tools installed, or commands executed?
- Are total usage savings measured, or merely presumed?
- Does the final answer contain the requested deliverable rather than just a set of internal process reports?
