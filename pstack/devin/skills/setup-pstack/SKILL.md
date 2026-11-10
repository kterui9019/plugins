---
name: setup-pstack
description: Configure which models pstack uses per role and at what reasoning budget. Detects your available models and writes an always-applied rule that overrides the skill defaults. Use for /setup-pstack, "configure pstack models", "pstack budget", or changing pstack's model choices.
triggers: [user]
---

Before following this workflow, read [the Devin adapter](../../ADAPTER.md). Apply its tool, model, path, permission and service mappings throughout this task. Skip Cursor-only operations even when an upstream example calls them mandatory.

# Setup pstack in Devin

Inspect the available worker profiles and the active session model. When using the CLI, use `devin models` if available to list choices for the signed-in account. Explain which kinds of work can be delegated in this session.

For a request to change the primary model, show the user's chosen available value with Devin's /model command. For repeated runs with a fixed worker model, a local custom agent profile may specify its own model. Only write a project-specific profile if requested, and keep the original plugin profiles available. A role-by-role Cursor budget has no direct equivalent. Record any preference that cannot be applied. Finish with a small investigation prompt and its expected evidence.
