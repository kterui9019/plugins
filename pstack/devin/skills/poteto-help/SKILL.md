---
name: poteto-help
description: Guides users through pstack setup, /poteto-mode, and picking the skill, playbook, or principle for a task. Type /poteto-help with a question.
triggers: [user]
---

Before following this workflow, read [the Devin adapter](../../ADAPTER.md). Apply its tool, model, path, permission and service mappings throughout this task. Skip Cursor-only operations even when an upstream example calls them mandatory.

# Help with pstack in Devin

For setup and installation, read the [Devin README](../../README.md). For model choices, service limits, and worker behavior, read the [Devin bindings](../../ADAPTER.md).

For a user goal, read the [playbook index](../poteto-mode/SKILL.md) and the matching playbook or sibling skill. Explain when to choose it, what inputs it needs, what it produces, and give a concrete prompt using the installed namespace. Use the [guide](../../docs/guide/README.md) for the engineering techniques. Apply the Devin adapter when a guide example uses a different host.

Common starting points include `/pstack-devin:how` for an explanation of a subsystem, `/pstack-devin:architect` for design alternatives, `/pstack-devin:statechart` for a state-machine model, and `/pstack-devin:create-verification-skill` for a repeatable real-surface check. For a help question, give the instructions and wait for an actual request to run the workflow.
