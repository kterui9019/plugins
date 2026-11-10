---
name: make-bot-ui
description: >-
  Use when building a custom UI (page, dashboard, buttons) that should wake a
  Grok Bot over a webhook, when the user must provide a webhook sender key, or
  when exposing that UI on Tailscale.
triggers: [user]
---

Before following this workflow, read [the Devin adapter](../../ADAPTER.md). Apply its tool, model, path, permission and service mappings throughout this task. Skip Cursor-only operations even when an upstream example calls them mandatory.

# Build a UI for an existing webhook

Devin cannot provision the upstream Grok Bot routine. First establish whether the user has already configured a compatible, authorized webhook and provided its documented payload and authentication scheme. If any prerequisite is missing, report it and stop before creating a live integration.

With an existing endpoint, implement the requested controls using the project's server and UI conventions. Validate submitted actions server-side against an explicit allowlist. Read the server credential from the project's secret store and keep it out of browser responses and logs. Send a test request to a local stub and verify the payload, failure response, and duplicate-submit handling. Contact the real endpoint or expose the UI externally only when authorized. Report exactly which endpoint behavior was exercised.
