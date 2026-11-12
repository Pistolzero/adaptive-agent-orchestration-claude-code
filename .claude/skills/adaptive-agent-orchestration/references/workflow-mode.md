# Native workflow execution

Choose one owner for each delegated task. The coordinator defines the outcome, scope, budget, ownership, and acceptance evidence. In ordinary mode it uses a Claude Code custom subagent. In workflow mode the native Dynamic Workflow owns its stages, retries, and result integration. Do not spawn ordinary agents to repeat a stage while that workflow is active. A stage must not recursively delegate its assigned work.

Use a workflow only when several bounded stages have a meaningful dependency or independent verification that justifies the extra usage. Normally choose one worker. Ask for at most two worker stages in a small smoke test. A prompt cap and `workflowSizeGuideline=small` are instructions and guidance, not hard limits. Inspect the proposed plan and `/workflows` during execution. If the runtime chooses a larger plan than the task warrants, stop or revise it using the normal interface.

Specify a worker model for each stage where supported. For an agent spawned by a workflow, stage model is the per-invocation model. The usual precedence is invocation, custom-agent frontmatter, `CLAUDE_CODE_SUBAGENT_MODEL`, then parent model. `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` changes that behavior. Organization model rules may substitute a model. `CLAUDE_CODE_EFFORT_LEVEL` can override agent effort. Inspect `/tasks` and `/workflows` for actual models and effort, and record substitutions or `NOT OBSERVABLE`.

Do not equate a skill instruction with a runtime permission or spending cap. Follow the host's workflow approval and per-tool permissions. If the workflow is unavailable or denied, finish safe independent work through the ordinary route when authorized. Keep skipped stages, failures, and unresolved checks in the final report.

See [Claude Code workflows](https://code.claude.com/docs/en/workflows), [custom subagents](https://code.claude.com/docs/en/sub-agents), and [model configuration](https://code.claude.com/docs/en/model-config).
