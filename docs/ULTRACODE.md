# Fable and native Dynamic Workflows

Fable 5.2 is the preferred **manager-only** main model for this policy when available and chosen for the session. It defines acceptance criteria, assigns bounded work, resolves conflicts, checks material evidence, and delivers the result. It may write the orchestration plan or a native workflow definition. Routine application edits, long searches, and ordinary test runs belong to an appropriate worker. This is a policy preference, not a runtime enforcement mechanism.

Select Fable with `/model fable` in a supported Claude Code session or start with `claude --model claude-fable-5-2`. Check `/model` for the actual model. Fable 5.2 requires Claude Code **v2.1.321 or later**. Gateway and organization restrictions can change availability. A Skill cannot switch the parent model. If Fable is unavailable or requires credits you do not want to use, select Opus explicitly with `/model opus` and check the resolved version. Do not enable credits or substitute models silently.

## Two execution modes

| Mode | Task owner | Worker selection |
| --- | --- | --- |
| Ordinary | Main coordinator assigns one bounded custom agent as needed | `.claude/agents/aao-*.md` selects Haiku, Sonnet, or exceptional Opus review |
| Dynamic Workflow | Main coordinator sets policy and verifies the final outcome; Claude Code's workflow runtime owns stage execution | Name stage models explicitly where supported; check actual agents in `/tasks` or `/workflows` |

Use ordinary mode for small or serial work. Request one workflow for a task with worthwhile staged coordination. Do not start a separate custom-agent fleet during an active workflow. Give stages exclusive files and distinct evidence requirements. Avoid recursive delegation and repeated research. `workflowSizeGuideline=small` aims for fewer than five agents; it is **advice, not a limit**. The policy's smaller desired cap also depends on model compliance. Inspect a proposed plan before running it when the host presents one.

For one interactive task, include `ultracode` in the prompt or explicitly ask Claude Code to create a workflow. For automatic workflow planning throughout the session, use `/effort ultracode`; `/effort ultracode off` turns it off. Automatic mode can create multiple workflows for a single request and can use substantially more tokens. The keyword trigger does not apply to `claude -p` prompts. Dynamic Workflows must be enabled in the running Claude Code host and permitted by its configuration. On Pro, enable them in `/config` if needed. Workflow launch and stage tools follow the host's approval and permission mode.

## Model routing and verification

Claude Code resolves a workflow stage model as the subagent invocation model, ahead of custom-agent frontmatter, `CLAUDE_CODE_SUBAGENT_MODEL`, and the parent model. `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` can override stage and frontmatter selection. Organization restrictions can substitute a model. A global `CLAUDE_CODE_EFFORT_LEVEL` can override an agent's `effort` setting. Check `/tasks` and `/workflows` for observed models and usage. Mark a model `NOT OBSERVABLE` if those views do not show it. Never assume every stage inherited Fable or used the requested worker.

This repository has static validation only. The runtime matrix in [OPERATIONS.md](OPERATIONS.md#runtime-regression-scenarios) describes small live tests. Until tests A–E run in an authenticated Claude Code installation, manager-only behavior, agent discovery, actual worker routing, and workflow coexistence are **UNVERIFIED**. A denied permission, missing model, missing workflow support, or exhausted usage is a `BLOCKED` test outcome. No live integration success is claimed from static files.

Official references: [Fable model selection](https://code.claude.com/docs/en/model-config), [Dynamic Workflows](https://code.claude.com/docs/en/workflows), and [custom subagents](https://code.claude.com/docs/en/sub-agents).
