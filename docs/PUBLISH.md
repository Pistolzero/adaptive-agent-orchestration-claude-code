# Publish as a separate GitHub repository

Create an empty public repository named `adaptive-agent-orchestration-claude-code`. Use Git to commit and push the source, including the hidden `.claude/` tree. Keep the Codex edition in its own repository.

Before pushing, inspect `git ls-files -- .claude` and run the package suite from a fresh export of the exact commit being published. For example, from a Git shell:

```sh
export_dir=$(mktemp -d)
git archive --format=tar HEAD > "$export_dir/source.tar"
tar -xf "$export_dir/source.tar" -C "$export_dir"
(cd "$export_dir" && python3 -m unittest discover -s tests -v)
```

After pushing, check that GitHub shows the expected commit and that its tree includes the Skill, its six reference files, and all seven agent presets. Use the matching changelog version if creating a GitHub release.
