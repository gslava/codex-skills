---
name: clarify-confusion
description: "Resolve user confusion, expectation mismatches, contradictory assumptions, and surprising behavior questions before deciding whether to explain, document, configure, fix, or plan. Use investigate-root-cause instead for failing commands, logs, stack traces, or concrete failures."
---

# Clarify Confusion

Explain the gap between what the user expected and what the system actually does.

## Rules

- Investigate before explaining.
- Do not assume the user is mistaken or the code is broken.
- Use concrete evidence: files, config, docs, commands, or behavior.
- If it is a real issue, explain the evidence first, then recommend the smallest next step.

## Clarifying Questions

- Ask before explaining if the expected behavior, actual behavior, source of expectation, or target system is unclear.
- Do not proceed on assumptions that affect whether this is expected behavior, a docs gap, a config issue, or a bug.
- Ask numbered questions with lettered options; option A must be recommended. Continue until the mismatch is clear.

## Do Not Trigger

- Normal "explain this code" requests without expectation mismatch.
- Failing commands, logs, stack traces, or reproducible concrete failures.
- Rejected implementation direction.

## Workflow

1. Extract the mismatch: expected behavior, actual behavior, source of expectation.
2. Gather evidence from relevant code, configuration, docs, tests, or command output.
3. Classify the case:
   - Explain: behavior is intentional, documented, or test-backed.
   - Document: behavior is correct but docs/comments/instructions mislead or omit details.
   - Configure: desired behavior exists behind config, flags, environment, or setup.
   - Fix: implementation contradicts docs, tests, product behavior, or clear intent and the fix is small.
   - Plan: issue affects multiple components, APIs, data, auth, migration, or release behavior.
4. Explain directly or recommend the smallest correction.

## Output

```markdown
**Expectation**
[What the user expected.]

**Actual**
[What the system does.]

**Evidence**
- [File/line, config, docs, command, or behavior.]

**Assessment**
[Explain / Document / Configure / Fix / Plan]

**Next Step**
[Concrete action.]
```

## Tone

- Be direct and factual.
- Avoid "you are wrong" framing.
- If the behavior is surprising, say why it is surprising.
