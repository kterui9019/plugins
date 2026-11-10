import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PackageTest(unittest.TestCase):
    def test_manifest_and_discoverable_skills(self):
        manifest = json.loads((ROOT / '.devin-plugin/plugin.json').read_text())
        self.assertEqual(manifest['name'], 'pstack-devin')
        self.assertRegex(manifest['name'], r'^[a-z0-9]+(?:[-.][a-z0-9]+)*$')
        for name in ('poteto-mode', 'tdd'):
            content = (ROOT / 'skills' / name / 'SKILL.md').read_text()
            self.assertRegex(content, rf'(?m)^name: {re.escape(name)}$')
            self.assertRegex(content, r'(?m)^description: .+')
            self.assertTrue(content.startswith('---\n'))

    def test_explicit_invocation_and_inherited_permissions(self):
        for path in (ROOT / 'skills').glob('*/SKILL.md'):
            with self.subTest(skill=path.parent.name):
                _, header, body = path.read_text().split('---\n', 2)
                fields = dict(line.split(': ', 1) for line in header.splitlines())
                self.assertEqual(set(fields), {'name', 'description', 'triggers'})
                self.assertEqual(fields['triggers'], '[user]')
                self.assertTrue(body.strip())

    def test_workflows_and_safe_fallbacks_are_packaged(self):
        content = (ROOT / 'skills/poteto-mode/SKILL.md').read_text()
        for heading in ('Bug fix', 'Feature', 'Investigation', 'Verification', 'TDD', 'Devin compatibility'):
            self.assertIn(f'## {heading}', content)
        for phrase in ('subagent_explore', 'subagent_general', 'do the work directly', 'not a model', 'Skip unsupported steps'):
            self.assertIn(phrase, content)


if __name__ == '__main__':
    unittest.main()
