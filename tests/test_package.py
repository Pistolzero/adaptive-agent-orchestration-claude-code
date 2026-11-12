"""Static checks only; never starts Claude Code or executes role instructions."""
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILL = ROOT / '.claude' / 'skills' / 'adaptive-agent-orchestration'
AGENTS = ROOT / '.claude' / 'agents'
EXPECTED_ROLES = {
    'aao-bulk-analyst', 'aao-researcher', 'aao-researcher-deep',
    'aao-builder', 'aao-builder-deep', 'aao-reviewer',
    'aao-critical-reviewer',
}
EXPECTED_REFS = {
    'brief-templates.md', 'budget-policy.md', 'dynamic-team-sizing.md',
    'failure-and-evidence-report.md', 'quality-and-budget.md',
    'routing-matrix.md',
}


def frontmatter(text):
    match = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
    if not match:
        return None
    pairs = {}
    for line in match.group(1).splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            pairs[k.strip()] = v.strip()
    return pairs


class TestPackage(unittest.TestCase):
    def test_skill_and_references(self):
        self.assertTrue((SKILL / 'SKILL.md').is_file())
        body = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
        fields = frontmatter(body)
        self.assertEqual(fields.get('name'), 'adaptive-agent-orchestration')
        self.assertTrue(fields.get('description'))
        self.assertEqual({p.name for p in (SKILL / 'references').glob('*.md')}, EXPECTED_REFS)
        for link in re.findall(r'\]\((references/[^)]+\.md)\)', body):
            self.assertTrue((SKILL / link).is_file(), link)

    def test_agents(self):
        found = {p.stem for p in AGENTS.glob('aao-*.md')}
        self.assertEqual(found, EXPECTED_ROLES)
        for p in AGENTS.glob('aao-*.md'):
            body = p.read_text(encoding='utf-8')
            fm = frontmatter(body)
            self.assertIsNotNone(fm, p.name)
            self.assertEqual(fm.get('name'), p.stem)
            self.assertIn(fm.get('model'), {'haiku', 'sonnet', 'opus'})
            self.assertIn(fm.get('effort'), {'low', 'medium', 'high'})
            self.assertTrue(fm.get('tools'))
            for field in ('ATTEMPTS_AND_ERRORS:', 'UNRUN_OR_FAILED_CHECKS:',
                          'ACCEPTANCE_CHECKLIST:', 'NEEDS_MAIN_AGENT_DECISION:'):
                self.assertIn(field, body, (p, field))

    def test_main_docs(self):
        for p in ('README.md', 'LICENSE', 'CHANGELOG.md',
                  'CONTRIBUTING.md', 'SECURITY.md',
                  'docs/INSTALL.md', 'docs/DESIGN.md',
                  'docs/OPERATIONS.md', 'docs/SECURITY.md',
                  'docs/PUBLISH.md', 'examples/USAGE.md'):
            self.assertTrue((ROOT / p).is_file(), p)
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        for target in re.findall(r'\]\((docs/[^)]+\.md|examples/[^)]+\.md|LICENSE)\)', readme):
            self.assertTrue((ROOT / target).is_file(), target)

    def test_no_codex_role_configs(self):
        self.assertFalse(list(ROOT.rglob('*.toml')))
        self.assertFalse((ROOT / '.agents').exists())
        for p in ROOT.rglob('*.md'):
            text = p.read_text(encoding='utf-8')
            self.assertNotIn('model_reasoning_effort =', text)


if __name__ == '__main__':
    unittest.main()
