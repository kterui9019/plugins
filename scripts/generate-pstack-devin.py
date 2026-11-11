"""Render the independent Devin package from tracked upstream sources."""
import argparse
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "pstack"
OUT = SOURCE / "devin"
NATIVE = ROOT / "scripts/pstack-devin"
TREES = ("skills", "agents", "docs/guide")
# Grok Bot routine creation is intrinsic to this workflow.
EXCLUDED_SKILLS = {"make-bot-ui"}
OMITTED_GUIDE_SECTIONS = {
    "docs/guide/07-overnight.md": "## Let loops start themselves",
    "docs/guide/09-make-it-yours.md": "## Build a bot UI with `/make-bot-ui`",
}
BODY_OVERRIDES = {
    "skills/poteto-help/SKILL.md": "poteto-help.md",
    "skills/setup-pstack/SKILL.md": "setup-pstack.md",
    "agents/poteto-agent.md": "poteto-agent.md",
}
ADAPTER = (
    "Before following this workflow, read [the Devin adapter]({path}). "
    "Apply its tool, model, path, permission and service mappings throughout this task. "
    "Skip Cursor-only operations even when an upstream example calls them mandatory."
)


def entrypoint(path, content):
    _, header, body = content.split("---\n", 2)
    # Preserve YAML block scalars in upstream descriptions.
    header = re.sub(r"^(?:icon|color|paths|disable-model-invocation|is_background):.*\n",
                    "", header, flags=re.MULTILINE)
    skill = path.startswith("skills/")
    if skill:
        header += "triggers: [user]\n"
    if path in BODY_OVERRIDES:
        body = (NATIVE / BODY_OVERRIDES[path]).read_text()
    if path == "skills/poteto-mode/SKILL.md":
        start, end = body.index("## Subagents"), body.index("## Writing the reply")
        body = body[:start] + "## Subagents\n\nUse the worker profiles and model selection in the Devin adapter. Give each delegate its scope and review the returned evidence.\n\n" + body[end:]
        body += "\nFor a verification-only request, identify the exact revision and behavior, run the closest real-surface check and report observed outcomes and unavailable checks. Keep the investigation read-only.\n"
    adapter = "../../ADAPTER.md" if skill else "../ADAPTER.md"
    return "---\n" + header + "---\n\n" + ADAPTER.format(path=adapter) + "\n\n" + body.strip() + "\n"


def render(path, raw):
    if not path.endswith(".md"):
        return raw
    content = raw.decode()
    if path in OMITTED_GUIDE_SECTIONS:
        before, section = content.split(OMITTED_GUIDE_SECTIONS[path], 1)
        _, after = section.split("**Pitfall:**", 1)
        content = before + "**Pitfall:**" + after
    if path.endswith("/SKILL.md") or path.startswith("agents/"):
        content = entrypoint(path, content)
    elif path.endswith("/playbooks/worktree-cleanup.md"):
        content = (NATIVE / "worktree-cleanup.md").read_text()
    if path.startswith("docs/guide/"):
        content = content.replace("../harness/claude-code.md",
                                  "https://github.com/cursor/plugins/blob/main/pstack/docs/harness/claude-code.md")
    content = content.replace("~/.cursor/skills/", "~/.config/devin/skills/")
    content = content.replace(".cursor/skills/", ".devin/skills/")
    return content.encode()


def inputs():
    paths = subprocess.check_output(
        ["git", "ls-files", "-z", "--", *TREES], cwd=SOURCE
    ).decode().split("\0")
    for path in filter(None, paths):
        if any(path.startswith(f"skills/{name}/") for name in EXCLUDED_SKILLS):
            continue
        # The Devin cleanup playbook uses git directly and cannot infer activity
        # from the upstream shell helper's Cursor transcript scan.
        if path != "skills/poteto-mode/scripts/worktree-audit.sh":
            yield path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    check = parser.parse_args().check
    expected = set(inputs())
    errors = []
    for path in sorted(expected):
        src, dest = SOURCE / path, OUT / path
        data = render(path, src.read_bytes())
        mode = 0o755 if src.stat().st_mode & 0o111 else 0o644
        if check:
            if (not dest.is_file() or dest.read_bytes() != data
                    or bool(dest.stat().st_mode & 0o111) != (mode == 0o755)):
                errors.append(f"out of date: {path}")
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
            dest.chmod(mode)

    # Detect leftover files from the earlier Benny package too.
    for tree in (*TREES, "benny"):
        for file in (OUT / tree).rglob("*"):
            if file.is_file() and file.relative_to(OUT).as_posix() not in expected:
                errors.append(f"unexpected package file: {file.relative_to(OUT)}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"{len(expected)} package files {'verified' if check else 'rendered'}")


if __name__ == "__main__":
    main()
