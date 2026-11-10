# Benny in a Devin session

Benny takes a Slack report through triage and, when a trusted verdict exists, reproduction and a possible draft fix. This port supports an operator-invoked run for one thread. It supplies no listener, scheduler, Slack identity, tracker connection or secret.

Start poteto mode and ask for Benny triage or Benny reproduction on a specific Slack permalink. Supply the authorized repository and configuration path, the permitted actions and scope, and a safe control environment for reproduction. Obtain the channel and root timestamp through the connected Slack reader and check them against configuration. Read the [Devin bindings](../ADAPTER.md) and the matching procedure in this folder. Treat trigger fields as verified thread metadata and automation output as the current session report.

- For triage, follow [triage-issue-reports](skills/triage-issue-reports/SKILL.md), including the deduplication and compensation checks before tracker writes.
- For reproduction, follow [reproduce-and-fix-issues](skills/reproduce-and-fix-issues/SKILL.md). Check the marker author and thread again. Use the configured application driver and collect real before/after evidence.
- The [configuration example](configuration.example.yaml) is a checklist. Replace example values in a project-owned config. Never put credentials in it. Use only configured actions actually provided by Devin. Keep expected posting identity, thread-only posting, and worker isolation intact. If authentication, permission or required compensation is missing, report the blocked phase before taking external action.
