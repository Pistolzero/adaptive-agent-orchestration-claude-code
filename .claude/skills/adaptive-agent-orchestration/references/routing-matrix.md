# Claude Code routing matrix

This is a **decision aid**, not a mandatory team roster.

| Work class | Default owner | Optional subagent | Example preset | Caution |
|---|---|---|---|---|
| One-step or serial task | Main | None | — | Spawning adds overhead |
| Uniform extraction, fixed rubric, inventory | Mechanical | `aao-bulk-analyst` | Haiku low | Reject ambiguous records; report counts |
| Narrow code/document lookup, factual source verification | Research | `aao-researcher` | Sonnet medium | Prefer primary sources and version labels |
| Complex technical research/debug hypotheses | Research | `aao-researcher-deep` | Sonnet high | Distinguish conjecture from proof |
| Clear scoped change with tests | Builder | `aao-builder` | Sonnet medium | Exclusive file ownership and checkable tests |
| Consequential diff or test verification | Independent reviewer | `aao-reviewer` | Sonnet high | Do not trust builder summary blindly |
| High-stakes independent adjudication | Main + optional reviewer | `aao-critical-reviewer` | Opus high | Use sparingly; approval remains with main/user |
| Architecture, permissions, deployment, purchases | Main | Evidence-gathering delegates only | User-selected main model | Never transfer real authorizations |

## Algorithm

1. Classify complexity (routine/bounded/ambiguous), risk (low/medium/high), independent ready tasks and the quality bar.
2. Apply the budget profile **before each agent wave**. For UNKNOWN/CONSERVE, default to at most one new delegate for the entire user task.
3. Prefer the least expensive *adequate* model, not the least expensive absolute model. Use high tier only for consequential ambiguity.
4. Use project/user agent definitions in `.claude/agents/`, or the built-in agents when they better fit; check actual tool availability.
5. Give a full task brief, including owner and `NOT_DONE`/error disclosures.
6. Confirm actual model if possible (`/tasks`). If the runtime substitutes a model, evaluate whether it is adequate; do not invent model telemetry.
7. Main verifies actual outputs and integrates. No parallel writer collisions.

## Native Claude Code notes

- An agent definition uses **Markdown plus YAML frontmatter**, not Codex TOML.
- `model: haiku|sonnet|opus|inherit` and `effort: low|medium|high...` depend on model and client version. Do not hardcode future model version numbers without a reason.
- Project agents live at `.claude/agents/`; global agents at `~/.claude/agents/`. Skills live separately at `.claude/skills/` or `~/.claude/skills/`.
- The `Agent` tool and supported subagent features are provided by Claude Code; the Skill doesn't implement them.
- Third-party orchestration plugins (including Superpowers) may propose separate planning or delegation. Choose **one owner** for task allocation rather than duplicate planning and reviews.
