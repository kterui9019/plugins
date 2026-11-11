---
name: principle-encode-lessons-in-structure
description: "Apply when you catch yourself writing the same instruction a second time, or notice a recurring correction. Encode the rule as a lint, metadata flag, runtime check, or script instead of more text."
triggers: [user]
---

Before following this workflow, read [the Devin adapter](../../ADAPTER.md). Apply its tool, model, path, permission and service mappings throughout this task. Skip Cursor-only operations even when an upstream example calls them mandatory.

# Encode Lessons in Structure

If the lesson needs judgment and cannot be encoded, make the instruction more prominent and add an example of the failure mode.

**Corollary:** If the fix is structural, only use the structural fix. The instruction is the symptom.
