# Running pstack workflows in Devin

Use these bindings throughout a run, including nested skills, playbooks, examples, docs and delegated briefs. They take precedence over platform-specific instructions in upstream prose. The user's scope and session permissions apply throughout.

## Locate the implementation

Resolve relative files from the loaded SKILL.md. Its directory contains the skill's references and scripts, and its parent contains sibling skills. Read a named workflow from that sibling's SKILL.md, even if it is user-triggered. Show a human the slash command `/pstack-devin:<name>`. For a missing project-specific skill, check the active project's skill catalog. Never search Cursor caches, fetch a replacement skill from the internet, or run an installer from upstream examples.

Use the project's own verification harness. Generate new verification or formal verification skills under `.devin/skills/<name>/`. Use flat skill directories and Devin frontmatter. Resolve personal skill locations with `devin skills paths` when available. Adapt references to create-skill by writing and validating the SKILL.md with `devin skills show <name>`. Edits to an installed skill belong in its source checkout.

## Tools and workers

Use available read, glob, grep, edit and exec tools. Present a question in chat when its answer is required. Keep a short checklist when the client has no task list. Follow the user's authorization for spawning workers, persistent operations, publishing, and destructive actions.

A Cursor Task describes a worker brief. In Devin use the available subagent tool with a profile, goal, scope, acceptance check, and any necessary paths. For discovery use subagent_explore. For implementation use subagent_general. Local sessions can use pstack-devin:poteto-agent or pstack-devin:comment-sicko when offered. Pass the full path to poteto-mode/SKILL.md in the former case. If the custom profile is missing, give a permitted built-in worker the profile's local instructions. If workers are unavailable, perform independent scopes sequentially and disclose the loss of independent review. Never report a quorum, multi-model consensus or independent verdict when those checks did not take place. A shipping gate that requires independent verification stays pending.

Omit Cursor model IDs, speed, effort, environment, resume IDs and file attachment fields. General workers inherit the parent model. Explore and unpinned custom profiles use the Devin subagent default. Background work may have fewer permitted tools. Only use background execution or an isolated checkout when the client actually provides it. Do not trigger a cloud handoff as a substitute for a local worker.

## Session history and external services

Use the visible conversation, an explicitly supplied Devin session export, and repository evidence for recall, reflect and session-pickup. Skip transcript globbing and Cursor JSONL parsing, including shell snippets. Report the time range actually covered. For generated artifacts, return the real path or an attachment supported by the active client.

Use git and an authenticated forge client for authorized PR and review actions. Existing Bugbot comments are review input. Starting Bugbot, Cursor Automations (including Benny), Grok Bot webhooks, Origin-only services and Cursor Custom Modes need their respective platforms. Skip their provisioning and dependent actions. Never run Cursor setup commands or request secrets for these steps. Use bounded foreground checks in place of /loop or routine wakes. Report remaining checks when the session ends. Only describe a schedule or notification as active after an authorized integration confirms it.

Use locally installed dependencies for the bundled helpers. Inspect the helper requirements first. Model checking may require a runtime and TLC. A missing dependency, expired credential, unavailable fixture or skipped surface is a verification gap. A destructive cleanup needs explicit approval for the actual targets. Missing session history is never evidence of an unused worktree.
