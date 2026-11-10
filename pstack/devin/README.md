# pstack for Devin

This skills-only port packages two user-invoked commands. Use `/pstack-devin:poteto-mode` with a task and Devin selects the bug fix, feature, investigation, or verification workflow. Use `/pstack-devin:tdd` for a focused failing-before, passing-after regression check. For example:

```text
/pstack-devin:poteto-mode Investigate where duplicate requests are filtered. Cite the call sites.
/pstack-devin:tdd Fix the duplicate request in the retry path and show the test before and after.
```

## Try the MVP branch locally

Check out `feature/devin-adapter-mvp` in the fork. From the repository root, run:

```sh
devin auth login
devin plugins install --local ./pstack/devin
devin plugins info pstack-devin
```

Open a new session in the project you want to work on and enter one of the commands above. Local installation links the checkout on this machine. Keep the checkout available. If using the standalone archive, extract it and pass the extracted directory containing `.devin-plugin` to the same install command.

After the adapter reaches the fork's default branch, use `devin plugins install 'OWNER/plugins#pstack/devin'` (replace OWNER with the fork owner) for a personal installation. For Cloud, add the fork and the same subdirectory through **Customize → Plugins → Add plugin → From repository**, subject to organization policy.

## Porting choices

The [Cursor workflow](../skills/poteto-mode/SKILL.md) orchestrates other pstack skills. The [Claude Code adapter](../docs/harness/claude-code.md) translates tool names, paths and model arguments at runtime. This MVP packages the four routes inline so a Devin session can follow them from the installed plugin alone.

| Upstream dependency | Devin behavior |
| --- | --- |
| Cursor tools and configuration paths | Use the current project's files and session tools. The manifest and skills live under the Devin plugin root. |
| Model rules, effort and worker selection | Inherit the session configuration. When available, use the built-in explore profile for research and general for scoped implementation. The lead handles the work when delegation is unavailable. |
| Bugbot, Automations, cloud-agent launches, other pstack skills | Skip unavailable steps, report the reason, and identify any evidence that could not be collected. |
| Custom agent profiles | Optional in Devin CLI and Desktop. Cloud does not load plugin custom subagents. This adapter ships none. |

## Validation

From the repository root, run:

```sh
python3 pstack/devin/tests/test_package.py
node scripts/check-pstack-docs.mjs
node scripts/generate-pstack-harness-trees.mjs --check
```

All three commands passed on the MVP branch. On macOS with Devin CLI 3000.12.43, copying both skill directories into a scratch project's `.devin/skills/` made `devin skills list` display both as user-triggered. `devin skills show` loaded each body. This exercised Devin's skill parser. Plugin installation stopped at the CLI sign-in requirement, before namespaced command discovery.

To finish runtime verification, install the plugin while signed in, confirm both namespaced commands appear, then run the investigation and regression examples against a known fixture. Check the cited source and the actual failing and passing outputs. Repeat with delegation unavailable and in Cloud. Plugin installation, task execution, delegated model selection, and Cloud behavior remain unverified.

Official references: [Plugins](https://docs.devin.ai/cli/extensibility/plugins/overview), [Creating skills](https://docs.devin.ai/cli/extensibility/skills/creating-skills), [Subagents](https://docs.devin.ai/cli/subagents).

Adapted from pstack by Lauren Tan and contributors under the [MIT license](LICENSE).
