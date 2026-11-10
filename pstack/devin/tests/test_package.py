import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PackageTest(unittest.TestCase):
    def test_manifest_and_catalog(self):
        manifest = json.loads((ROOT / ".devin-plugin/plugin.json").read_text())
        self.assertEqual(manifest["name"], "pstack-devin")
        skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
        self.assertEqual(len(skills), 58)
        for skill in skills:
            with self.subTest(skill=skill.parent.name):
                _, header, body = skill.read_text().split("---\n", 2)
                self.assertIn(f"name: {skill.parent.name}\n", header)
                self.assertIn("triggers: [user]\n", header)
                self.assertEqual(set(re.findall(r"^([\w-]+):", header, re.M)),
                                 {"name", "description", "triggers"})
                self.assertTrue(body.lstrip().startswith("Before following this workflow"))
                self.assertTrue((skill.parent / "../../ADAPTER.md").is_file())

    def test_workers_and_playbooks(self):
        profiles = sorted((ROOT / "agents").glob("*.md"))
        self.assertEqual([p.stem for p in profiles], ["comment-sicko", "poteto-agent"])
        for profile in profiles:
            self.assertIn("../ADAPTER.md", profile.read_text())
            self.assertNotIn("is_background:", profile.read_text())
        playbooks = ROOT / "skills/poteto-mode/playbooks"
        self.assertEqual(len(list(playbooks.glob("*.md"))), 23)
        self.assertNotIn("worktree-audit.sh", (playbooks / "worktree-cleanup.md").read_text())
        self.assertFalse((ROOT / "skills/poteto-mode/scripts/worktree-audit.sh").exists())

    def test_native_commands(self):
        for name, forbidden in [("setup-pstack", ".mdc"), ("make-bot-ui", "update_state"),
                                ("poteto-help", "/add-plugin")]:
            self.assertNotIn(forbidden, (ROOT / f"skills/{name}/SKILL.md").read_text())


if __name__ == "__main__":
    unittest.main()
