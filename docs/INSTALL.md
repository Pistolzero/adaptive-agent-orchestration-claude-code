# Install and verify (Claude Code)

This repository contains **text-only** configuration: one Skill and optional Claude Code subagent definitions. There is no installer, hook, or dependency. You do not need to install the original Codex edition.

## Recommended: project scope

Copy these directories into your **actual target project**, preserving their nesting:

```text
YOUR-PROJECT/
  .claude/
    skills/
      adaptive-agent-orchestration/
        SKILL.md
        references/*.md
    agents/
      aao-*.md                  # optional role presets
```

Start a new Claude Code session in that project. Invoke `/adaptive-agent-orchestration` or request it by name. `/agents` should show the installed agent names. A displayed agent is *configured*, not proof that its model executed.

## Windows PowerShell — safe copy for all projects

From a **PowerShell opened in the extracted repository root**, inspect the files first. The following copies only `.md` files; it does not touch `settings.json` or change Windows execution policy.

```powershell
$src = (Get-Location).Path
$skillSource = Join-Path $src '.claude\skills\adaptive-agent-orchestration'
$skillRoot = Join-Path $HOME '.claude\skills'
$agentRoot = Join-Path $HOME '.claude\agents'

if (-not (Test-Path (Join-Path $skillSource 'SKILL.md'))) {
    throw 'Open PowerShell in the extracted repository root first.'
}
$agents = @(Get-ChildItem -LiteralPath (Join-Path $src '.claude\agents') -Filter 'aao-*.md' -File -ErrorAction Stop)
$skillDest = Join-Path $skillRoot 'adaptive-agent-orchestration'
$destinations = @($skillDest) + @($agents | ForEach-Object { Join-Path $agentRoot $_.Name })
$conflicts = @($destinations | Where-Object { Test-Path -LiteralPath $_ })
if ($conflicts.Count) {
    throw "Already installed. Compare and back up these paths before updating: $($conflicts -join ', ')"
}
New-Item -ItemType Directory -Force $skillRoot, $agentRoot -ErrorAction Stop | Out-Null
Copy-Item -LiteralPath $skillSource -Destination $skillRoot -Recurse -ErrorAction Stop
foreach ($agent in $agents) {
    Copy-Item -LiteralPath $agent.FullName -Destination $agentRoot -ErrorAction Stop
}
Test-Path (Join-Path $skillDest 'SKILL.md')
Get-ChildItem $agentRoot -Filter 'aao-*.md' | Select-Object -ExpandProperty Name
```

If you want only a limited set of roles, copy those `.md` files individually instead of using the loop. If updating, back up and compare installed text files before replacing them.

## Verify without wasting many model requests

1. Open a fresh **Claude Code** session in the target project.
2. Run `/agents` and confirm only the role names you copied. The built-in agents may also appear.
3. Invoke `/adaptive-agent-orchestration` with a small read-only task and a maximum of one delegate; such as asking `aao-reviewer` to read the first heading of `README.md` and return its source line.
4. If your session displays `/tasks`, inspect the model reported for a live delegate. The YAML `model` field by itself is not execution telemetry.
5. If `/usage` is offered for your account, it may provide an official but scoped usage view. The Skill does not fetch hidden quotas.
6. For local static checks, use `py -3 -m unittest discover -s tests -v` from the extracted repo root (Python 3 is optional, needed only for package validation).

## Compatibility and caveats

- Claude Code uses **`.claude/agents/*.md` with YAML frontmatter**, not Codex's `.toml` role presets. Skills belong in `.claude/skills/` (or `~/.claude/skills/`).
- These agent presets use `model: haiku|sonnet|opus` aliases and `effort: low|medium|high`. A particular version/account/provider may restrict those combinations; verify in the actual host. Environment-wide model/effort overrides may supersede role frontmatter.
- A Skill is not a mandatory always-on coordinator. If Superpowers or another workflow plugin is installed, designate **one** source of task-allocation policy to avoid duplicated agent waves.
- Parent permissions, approval gates and tool restrictions apply. Never widen them solely to satisfy a Skill.
- Claude Code cloud/remote contexts may not see files installed on your local Windows machine.

Official upstream references: [Claude Code Skills](https://code.claude.com/docs/en/skills) and [Custom subagents](https://code.claude.com/docs/en/sub-agents).
