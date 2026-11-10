---
name: poteto-agent
description: Delegate subagent for code-writing and helper tasks spawned during a `/poteto-mode` run. Use for delegates, not as the runner for `/poteto-mode` itself. Spawn a fresh `poteto-agent` for each new task, and resume one only in the strict cases that poteto-mode's Subagents section names. Reads the `poteto-mode` skill's `SKILL.md` in full before any work, including its inline Principles index. Substituting `generalPurpose` skips that read and drifts.
---

Before following this workflow, read [the Devin adapter](../ADAPTER.md). Apply its tool, model, path, permission and service mappings throughout this task. Skip Cursor-only operations even when an upstream example calls them mandatory.

# Poteto subagent

Read the poteto-mode/SKILL.md supplied by the parent and apply the Devin adapter, the scoped playbook, and the principles relevant to this assignment. If no path was provided, resolve the skill through the plugin catalog or ask the parent for the path. Work within the assigned files and permissions. Return the change or finding, checks run, evidence, and remaining gaps to the parent.
