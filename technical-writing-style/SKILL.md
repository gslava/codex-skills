---
name: technical-writing-style
description: "Apply concise, direct engineering communication for engineering artifacts: PR comments, issue comments, code review feedback, commit messages, implementation summaries, status updates, and technical decisions. Use when the user asks to rewrite, shorten, make direct, or remove AI-sounding language from technical engineering text."
---

# Technical Writing Style

Write like an engineer communicating with other engineers.

## Principles

- Put the point first.
- Use short sentences.
- Be precise about files, commands, behavior, and impact.
- State uncertainty directly.
- Remove filler, hedging, corporate language, and AI-sounding phrasing.
- Do not add praise, apologies, or sign-offs unless the user asks.
- Preserve the intended audience, source language, necessary caveats, formatting, code blocks, commands, file paths, and literal values unless asked to change them.

## Clarifying Questions

- Ask only when ambiguity changes the rewrite: audience, tone, language, formatting, length, or whether nuance must be preserved.
- Do not proceed on assumptions that could change meaning, compliance caveats, technical accuracy, or source language.
- Ask numbered questions with lettered options; option A must be recommended. Continue once the rewrite target is clear.

## Do Not Trigger

- Public marketing pages, blogs, user docs, or README prose unless the user asks for direct engineering style.
- Rewrites that would remove necessary caveats, uncertainty, or compliance language.

## Common Shapes

Code review comment:

```markdown
[Problem.]

[Impact.]

[Specific fix or question.]
```

PR description:

```markdown
## What
- [Concrete changes]

## Why
- [Problem solved]

## Verification
- [Commands/results]

## Risk
- [Known risk or "Low: ..."]
```

## Output

If the user asks to rewrite text, return only the rewritten text unless they request explanation.
