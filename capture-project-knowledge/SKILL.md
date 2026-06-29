---
name: capture-project-knowledge
description: "Capture reusable project instructions discovered during a session, such as architecture, conventions, testing patterns, build commands, operational notes, gotchas, and integration details. Use when the user asks to save durable project knowledge, update AGENTS.md, update project instructions, or preserve lessons that should affect future Codex sessions."
---

# Capture Project Knowledge

Save only knowledge that will help future Codex sessions work better in this project.

## Rules

- Capture only durable, reusable project facts backed by code, docs, commands, or observed project behavior.
- Do not save session-specific trivia, one-off implementation choices, temporary workarounds, TODOs, secrets, credentials, tokens, personal data, or private customer data.
- Check existing AGENTS.md, CODEX.md, README, or project instruction files before proposing new entries.
- Prefer project-local instructions, then existing docs. Use memory only if a memory tool exists and the user explicitly confirms it.
- Ask for confirmation before writing persistent instructions.
- If no durable knowledge was found, say so and do not propose a write.

## Clarifying Questions

- Ask before proposing or writing if the target location, durability, privacy impact, or user intent is unclear.
- Do not proceed on assumptions that affect whether knowledge belongs in AGENTS.md, docs, memory, or nowhere.
- Ask numbered questions with lettered options; option A must be recommended. Continue until the write target and content are clear.

## Do Not Trigger

- General note-taking that will not affect future Codex work.
- Documentation of today's implementation unless it reveals reusable project convention.
- Any memory or project-instruction write without explicit confirmation.

## Workflow

1. Review the session for durable facts: architecture, conventions, test/build commands, configuration gotchas, integrations, debugging procedures, or non-obvious constraints.
2. Check existing project knowledge for duplicates.
3. Propose concise entries grouped by topic and target location.
4. Show exact text or patch before writing.
5. Write only after explicit confirmation.

## Output

```markdown
**Proposed Knowledge**
1. [Topic]: [imperative entry]. Evidence: `path/file` or `[command]`.

**Recommended Location**
[AGENTS.md / docs / memory / none]

**Why**
[Why future sessions need this.]
```
