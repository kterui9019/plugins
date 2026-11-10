---
name: poteto-mode
description: Use when explicitly asked for poteto mode or a pstack workflow for a bug fix, feature, investigation, or verification.
---

# Poteto mode for Devin

State the goal and expected smallest useful change. Work autonomously within the user's instructions and existing permissions. Ask before consequential irreversible operations when authorization is missing. Keep replies concise and evidence-based; distinguish observed results, inference, and unverified claims.

Choose the workflow below matching the request. If the request combines workflows, use each relevant section. Maintain a short task list for multi-step work. The lead owns decisions, checks delegated work, and reports the actual evidence and remaining gaps.

## Bug fix

1. Reproduce on the affected surface when accessible. Record the trigger and observed failure. If reproduction is blocked, explain the limitation; do not claim a pass.
2. Investigate competing causes and establish the mechanism with evidence. Select the smallest fix justified by the evidence.
3. For a cheap, meaningful regression test, follow the TDD workflow below: run it before and after the fix. If impractical, explain why and use the closest useful check.
4. Verify the original reproduction on the affected surface and run relevant checks. Report the cause, change, evidence, and limitations.

## Feature

1. Inspect existing behavior, requirements, and constraints. Identify the data shape and smallest design that fits the codebase.
2. Identify blocking steps, independent work, and shared files. Delegate only if permitted and useful; avoid concurrent writes to the same files.
3. Implement in verifiable increments and review the resulting diff.
4. Verify the requested behavior on the relevant surface. Report the design choice, evidence, and any gaps.

## Investigation

Keep the work read-only unless the user authorizes changes. Inspect relevant sources, distinguish evidence from inference, and cite the locations that support the answer. For a decision, compare material tradeoffs and give a reasoned recommendation. Say what remains unknown.

## Verification

Identify the requested behavior and the actual artifact or revision to check. Run the narrowest relevant checks, including the real surface when feasible. Report commands or reproduction steps and outcomes; distinguish a failure, a skipped check, and an unavailable check from a pass. Do not change code unless authorized.

## TDD

For an explicitly requested TDD cycle or a cheap meaningful regression test, write a focused test of observable behavior, run it and confirm it fails for the intended reason, make the smallest fix, and rerun it. If the test already passes or fails for an unrelated reason, correct the reproduction first. When a failing test is impractical, explain why and use the closest useful verification. Do not weaken a test to hide a defect.

## Devin compatibility

Use only tools and arguments actually exposed in this session. When subagents are available and delegation is allowed, use `subagent_explore` for read-only research and `subagent_general` for implementation; provide the goal, relevant paths, scope, and expected evidence. The lead reviews all results. If subagents are disabled or unavailable, do the work directly. Do not assume plugin custom subagents exist in Cloud sessions. Avoid parallel edits to shared files.

Do not pass Cursor `Task` fields, model slugs, effort levels, or Cursor configuration paths to Devin. `run_subagent` selects a profile, not a model. The general profile uses the parent model; explore uses the configured or routed subagent model. Do not promise a particular model or automatically change the user's settings.

Do not invoke Cursor Automations, Bugbot, Cursor cloud agents, `/loop`, or unrelated pstack skills as if they were available. Skip unsupported steps and say what was skipped. Use a working forge tool only when available and authorized; do not claim a PR was created without confirming it. Do not fetch plugin instructions from an arbitrary remote copy. Follow the active session's permissions and higher-priority instructions.
