# pstack for Devin

This package exposes all 58 skills in the upstream pstack snapshot, including the 24 engineering principles. Poteto mode includes all 23 playbooks. The package also contains the two local agent profiles, reference material, command-line helpers and fixtures. Some workflows depend on host services. Their coverage is listed below.

## Install from this branch

```sh
git clone --branch feature/devin-full-catalog --single-branch https://github.com/kterui9019/plugins.git
cd plugins
devin auth login
devin plugins install --local ./pstack/devin
devin plugins info pstack-devin
```

Keep the checkout available and start a new session in your target project. For the standalone ZIP, extract it and give the directory containing `.devin-plugin` to the same install command. Once this branch reaches the fork's default branch, the personal install command is `devin plugins install 'kterui9019/plugins#pstack/devin'`. The web app accepts the same repository and subdirectory.

```text
/pstack-devin:poteto-help How can I verify a retry bug on the real surface?
/pstack-devin:poteto-mode Fix the retry bug and show the reproduction before and after.
/pstack-devin:architect Compare two designs for idempotent retries.
/pstack-devin:statechart Model the allowed transitions of the retry queue.
```

## What runs where

| Upstream feature | Devin implementation | Boundary |
| --- | --- | --- |
| 34 workflow skills and 24 principles | User-invoked slash commands, cross-skill reads and bundled references | All 58 are explicit entry points. Cursor path-based activation is omitted. |
| 23 playbooks | The poteto-mode router loads the playbook file relative to its skill | Review, test, forge, simulator and recording steps depend on tools and permissions in the session. |
| poteto-agent and comment-sicko | Both local plugin profiles include the [Devin bindings](ADAPTER.md) | In Cloud, pass the task and profile instructions to a built-in worker if available. Report missing independent verification if working alone. |
| Parallel design and review | Split by scope, run available profiles and aggregate evidence | Per-call Cursor model IDs, effort selection and guaranteed multi-model voting are unavailable. |
| Verification, statechart, PR polling | Bundled scripts and fixtures. Worktree cleanup uses a Devin-specific inventory procedure. | Some helpers need Bun, Node, Java/TLC, app control or forge credentials. Cursor chat activity cannot establish safe deletion. |
| Session pickup, recall, reflect | Current conversation, authorized exports and repository state | No automatic access to historical Cursor chats or persistent Custom Mode. |
| Benny triage and reproduction | [Manual, one-thread procedures](benny/README.md) | Requires configured Slack, tracker and app control. Event triggers and background automation installation are external. |
| Bot UI, Bugbot and autonomous loops | An existing compatible webhook, ordinary forge review threads, and bounded foreground checks | The plugin cannot provision a Cursor routine, start Bugbot or schedule a persistent wake. |

The generator keeps upstream workflow prose and examples. Each skill and agent loads the Devin bindings before interpreting them. Native replacements cover setup, help, the webhook entry point, the poteto delegate and destructive cleanup. Use the examples above for Devin invocation.

## Validation and updates

From the repository root:

```sh
python3 scripts/generate-pstack-devin.py
python3 scripts/generate-pstack-devin.py --check
python3 pstack/devin/tests/test_package.py
node scripts/check-pstack-docs.mjs
node scripts/generate-pstack-harness-trees.mjs --check
```

Make workflow changes in the upstream sources or in the generator's native overrides under `scripts/pstack-devin/` and regenerate. The check compares generated contents and executable bits with upstream. Update the coverage assertions when upstream adds or removes a workflow.

Verified on macOS with Devin CLI 3000.12.43. In a scratch project, the CLI listed all 58 project skills as user-triggered and showed their bodies. The package tests, generator checks, upstream documentation checks and all seven plan-checker tests passed. Of 75 statechart rendering and TLC-output tests, 74 passed. The live TLC re-run was skipped because its JAR was unavailable.

The CLI requires sign-in for plugin installation. Namespaced discovery after installation, local profile dispatch, model behavior, real task execution, Cloud, and external services still need authenticated testing. To smoke-test, verify the plugin info, run poteto-help, run a TDD task with a known failing reproducer and capture its two results. In CLI/Desktop, request a scoped comment review and check which profile was used. Repeat in Cloud and record the fallback.

[Devin plugins](https://docs.devin.ai/cli/extensibility/plugins/overview) · [Skills](https://docs.devin.ai/cli/extensibility/skills/creating-skills) · [Subagents](https://docs.devin.ai/cli/subagents) · [MIT license](LICENSE)
