# pstack for Devin (MVP)

This is a separate, skills-only Devin adapter inspired by pstack. It preserves the original pstack plugin and Claude Code adapter. It provides `/pstack-devin:poteto-mode` and `/pstack-devin:tdd`. Poteto mode includes bug fix, feature, investigation, verification, and TDD workflows. It does not implement all original pstack principles, playbooks, model routing, automations, or cross-skill orchestration.

## Install

After this branch is pushed to your fork, install the `pstack/devin` subdirectory from that fork. Replace `OWNER` with the actual fork owner; the remote install normally tracks its default branch, so merge the branch first or use a supported ref-pinned source.

```sh
devin auth login
devin plugins install 'OWNER/plugins#pstack/devin'
devin plugins info pstack-devin
```

For local development, from the repository root:

```sh
devin auth login
devin plugins install --local ./pstack/devin
```

Start a new session and invoke `/pstack-devin:poteto-mode` with a task, or `/pstack-devin:tdd` for the standalone regression workflow. In the web app, use Customize → Plugins → Add plugin → From repository with your fork and subdirectory `pstack/devin`. Installation and use are subject to organization policy.

The instructions choose the available Devin tools at runtime and avoid Cursor-only fields. Built-in subagents are optional; if unavailable, the lead executes directly. The general profile uses the parent model and explore uses Devin's subagent router or configured model. Plugin custom subagents are not available in Cloud, so this MVP does not require them. Cursor Automations, Bugbot initiation, Cursor cloud agents, and other pstack skills are skipped rather than simulated.

## Validation and limitations

Run `python3 pstack/devin/tests/test_package.py` from the repository root. These static checks verify packaging and the presence of workflow and fallback instructions; they do not prove that an agent follows them. A real Devin installation, slash-command discovery, Local and Cloud execution, model routing, and actual delegated tasks still require manual end-to-end testing. Skills are instructions, not hard enforcement or a substitute for permissions.

Suggested smoke test: install the plugin, start a new session, confirm both commands appear, and run an investigation and a small bug fix with a failing-then-passing test. Repeat with subagents disabled, then in a Cloud session. Record the client version, prompt, observed tool calls, result, and any skipped checks. Do not interpret static validation as a completed smoke test.

## Sources

- [Devin plugins](https://docs.devin.ai/cli/extensibility/plugins/overview)
- [Devin subagents](https://docs.devin.ai/cli/subagents)
- [Devin skills](https://docs.devin.ai/product-guides/skills)
- [Original pstack](../README.md) and [Claude Code adapter](../docs/harness/claude-code.md)

Adapted from pstack by Lauren Tan and contributors, distributed under the [MIT license](LICENSE).
