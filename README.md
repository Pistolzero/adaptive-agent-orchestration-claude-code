# Adaptive Agent Orchestration — Claude Code Edition

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**A general-purpose, budget-aware delegation policy for Claude Code.** Choose the smallest useful team, route bounded tasks to appropriate Claude models, require candid failure reports, and verify delegated work before claiming success.

> Version **1.0.1** · Instruction-based Skill and optional native Claude Code subagents · **English-only documentation** · No extra dependencies or background processes required. This is an independent community project, **not affiliated with or endorsed by Anthropic**.
>
> Adapted from the original [Adaptive Agent Orchestration for Codex](https://github.com/Pistolzero/adaptive-agent-orchestration) project. The original Codex repository remains unchanged.

## Features

- **Adaptive team size:** 0, 1, or 2 delegates for typical work; up to 3 when independent tasks and confirmed budget justify it. No automatic fleet for trivial tasks.
- **Claude-native subagents:** optional `.claude/agents/*.md` presets with **Haiku**, **Sonnet**, and a conditional **Opus** reviewer. Each preset pins its own supported `model` and `effort` where available.
- **Manager-led operation:** the user's main-session model remains their choice; it plans, routes, adjudicates important contradictions, and verifies outcomes. Bounded execution can be delegated rather than duplicating long research in the main context.
- **Budget awareness:** `QUALITY`, `BALANCED`, `CONSERVE`, `CRITICAL`, and `UNKNOWN` modes. Never guesses subscription quotas or token savings.
- **Mandatory transparency:** every delegate reports attempted work, failed attempts (including recovered errors), omitted checks, changes, evidence, and open risks.
- **Safe autonomy:** independent read-only analysis may proceed without repeated questions. System, account, network, purchase, production, and destructive actions still require the approvals and permissions that apply to the environment.
- **No dependency on external orchestration frameworks:** no installed plugin, API key, paid service, shell hook, or undocumented quota API is required by the Skill.

## Quick start — Claude Code on Windows

1. Download and extract the repository.
2. Follow the [Windows PowerShell installation steps](docs/INSTALL.md#windows-powershell--safe-copy-for-all-projects) or use a project-only installation.
3. Start Claude Code in the target project. Use `/adaptive-agent-orchestration` and include the task you want completed.
4. Use `/agents` to confirm discovery. For one delegated read-only task, see the [installation check](docs/INSTALL.md#verify-without-wasting-many-model-requests).

### Project-only installation

Copy the repo's `.claude/skills/adaptive-agent-orchestration/` and any desired `.claude/agents/aao-*.md` files into **your target project's** `.claude/` directory. This is normally safer than a global install. Do not copy this project's `.claude` into an unrelated existing repository without reviewing its policies.

For safe Windows copying with an existing agent directory, see [Installation guide](docs/INSTALL.md).

## Default routing

| Work | Delegate | Model | Effort |
| --- | --- | --- | --- |
| Tiny/serial task or critical final decision | Main session | User-selected | User-selected |
| Deterministic extraction / classification | `aao-bulk-analyst` | `haiku` | `low` |
| Scoped documentation or technical research | `aao-researcher` | `sonnet` | `medium` |
| Complex research and edge cases | `aao-researcher-deep` | `sonnet` | `high` |
| Scoped implementation and targeted tests | `aao-builder` | `sonnet` | `medium` |
| Hard bounded implementation | `aao-builder-deep` | `sonnet` | `high` |
| Independent code/claim verification | `aao-reviewer` | `sonnet` | `high` |
| High-stakes second opinion when justified | `aao-critical-reviewer` | `opus` | `high` |

Model aliases resolve to versions supported by the provider and may change. Unsupported or restricted combinations can fall back. **Do not assert the actual model until observed.** The Opus reviewer is optional and expensive; it is *not* automatically required. These are presets, not a required team.

## Budget modes

| Mode | Reliable remaining capacity, if user supplies it | Suggested active delegates |
| --- | --- | --- |
| QUALITY | 60% or more | 0–3 |
| BALANCED | 30–59% | 0–2 |
| CONSERVE | 10–29% | 0–1 |
| CRITICAL | Less than 10%, near/exhausted | 0 new |
| UNKNOWN | No fresh reliable figure | 0–1 |

CONSERVE and UNKNOWN default to at most one new delegate over the whole user task, including sequential replacements.

These bands are **custom heuristics**, not official Claude usage thresholds. `/usage` and related interfaces may report only particular models, products, or reset windows. An agent must not scrape private account files or pretend to monitor live limits. A cheaper agent can waste *more* tokens if retried repeatedly.

## How it works

1. The main agent states the user deliverable, acceptance criteria, permissible actions, evidence gaps, and available budget.
2. It uses [routing rules](.claude/skills/adaptive-agent-orchestration/references/routing-matrix.md) and [team sizing](.claude/skills/adaptive-agent-orchestration/references/dynamic-team-sizing.md) to decide **whether** to delegate.
3. It gives each delegate an explicit [brief](.claude/skills/adaptive-agent-orchestration/references/brief-templates.md), including file ownership and a mandatory [failure report](.claude/skills/adaptive-agent-orchestration/references/failure-and-evidence-report.md).
4. The delegate returns a concise result and evidence. The coordinator independently checks consequential claims against actual files, test output, primary sources, or other records.
5. The coordinator delivers the user's actual result—not an ever-expanding series of status documents. It may continue with independent low-risk tasks, but pauses at genuine approval or access boundaries.

## Important limitations

- A Skill is a **policy**, not an agent launcher, sandbox, quota monitor, billing controller, or independent background service. Native Claude Code features must exist and be enabled for delegation to occur.
- Subagents consume usage from the same account as the parent session. More simultaneous agents may increase total tokens. This project offers **no guaranteed savings**.
- Claude Code's `maxTurns` and `effort` settings are version/model dependent. Use `/agents`, `/tasks`, and `/usage` to verify actual behavior where supported.
- Prompt instructions never override real permissions or approvals. An allowed tool such as `Bash`/`PowerShell` can still perform material changes; permissions must be set outside this Skill.
- The included Skill and agents **have not been executed on the user's Windows Claude Code installation**. Static package validation does not establish live runtime compatibility.

## Documentation

- [Install and verify](docs/INSTALL.md)
- [Architecture and conflict prevention](docs/DESIGN.md)
- [Budget and operations](docs/OPERATIONS.md)
- [Security and trust](docs/SECURITY.md)
- [Publishing a separate GitHub repository](docs/PUBLISH.md)
- [Usage examples](examples/USAGE.md)

## License

Original and adapted material is available under the [MIT License](LICENSE). Please verify third-party licenses before incorporating third-party Skills or code. This project does not redistribute the contents of third-party orchestration Skills.
