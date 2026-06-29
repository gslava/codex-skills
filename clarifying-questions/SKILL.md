---
name: clarifying-questions
description: "Check whether a request is clear enough before planning, editing, executing, publishing, or giving a final recommendation. Use when missing details could change scope, target behavior, permissions, acceptance criteria, or other decision-critical outcomes."
---

# Clarifying Questions

Resolve decision-critical ambiguity before continuing.

## Clarifying Questions

- Use this protocol before continuing when the request is not yet clear enough.
- Keep asking until the next action can be completed without decision-critical assumptions.

## Rules

- Before planning, editing, executing, publishing, or giving a final recommendation, first check whether any decision-critical detail is missing, contradictory, or unclear.
- Do not assume missing user intent. Use local evidence when it can resolve the ambiguity safely; otherwise ask.
- Do not ask about details that can be verified quickly from code, docs, tests, config, or recent changes.
- In non-critical situations, still avoid invented assumptions: either cite local evidence or ask the user.

## Trigger When

- The request could reasonably mean more than one thing.
- Scope, target behavior, permissions, constraints, or acceptance criteria are unclear.
- A wrong assumption could change code, data, release behavior, or user-facing output.
- The user asked for clarification-first behavior.

## Do Not Trigger

- The task is already clear enough to complete safely.
- The answer is recoverable from local evidence without meaningful risk.
- The missing detail would not change the decision or result.

## Question Protocol

- Ask only decision-critical questions.
- Ask numbered questions with lettered options; option A must be the recommended choice.
- Keep each batch short, usually 1-3 questions.
- Continue until the next action can be completed without decision-critical assumptions.
- Include a custom-answer option when useful.

## Handoff

- Once the request is clear, continue with the relevant domain skill or normal workflow.
- If another skill already has a `Clarifying Questions` section, treat it as domain-specific fallback, not a replacement for this protocol.

## Output

```markdown
1. [Question]
A. [Recommended]
B. [Alternative]
C. [Alternative]
D. [Alternative]
E. [Alternative]
F. [Alternative]
```
