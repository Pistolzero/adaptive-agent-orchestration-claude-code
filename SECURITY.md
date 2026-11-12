# Security policy

This project consists of Skill instructions, Markdown agent definitions, and optional static tests. It requests no API key, password, or expanded permission. It cannot implement isolation or modify Claude Code's actual authorization system.

**Report vulnerabilities with redacted reproduction steps.** Prefer private vulnerability reporting if enabled. Do not publish raw user logs, real credentials or private account/organization information.

Main threat areas: prompt injection through retrieved content, overbroad tool permissions, unreviewed shell commands, accidental exposure of secrets, unsupported assumptions about live quotas, and false positive success claims. The policies mitigate these risks but do not guarantee protection.
