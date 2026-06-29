---
name: dialectic-analysis
description: "Stress-test claims, architecture decisions, refactors, performance assumptions, safety claims, and proposed solutions by arguing both for and against them. Use when the user asks to prove/disprove, challenge, sanity-check, stress test, argue both sides, or decide whether a claim is really true."
---

# Dialectic Analysis

Use opposing analysis to reduce confirmation bias.

## Rules

- State the claim precisely and make it testable.
- Analyze the strongest case for and against the claim.
- Ground both sides in code, docs, commands, or explicit evidence.
- Verify cited evidence before the final verdict.

## Clarifying Questions

- Ask before analysis if the claim, decision criteria, scope, or required evidence is unclear.
- Do not proceed on assumptions that could change approve/reject/revise.
- Ask numbered questions with lettered options; option A must be recommended. Continue until the claim can be judged or explicitly marked under-evidenced.

## Do Not Trigger

- Ordinary brainstorming.
- Root-cause debugging unless the user asks to challenge a specific hypothesis.
- Direct implementation with clear requirements.

## Workflow

1. State the claim and decision being made.
2. Make the strongest positive case.
3. Make the strongest negative case.
4. Verify the most important evidence and label weak points as likely, speculative, or unknown.
5. Synthesize: `approve`, `revise`, `reject`, or `investigate`.

## Output

```markdown
**Claim**
[Precise statement.]

**For**
- [Evidence]

**Against**
- [Evidence]

**Unknowns**
- [Only decision-relevant gaps.]

**Verdict**
[approve / revise / reject / investigate, with confidence.]

**Recommendation**
[Concrete next step.]
```

## Quality Bar

- Prefer one decisive contradiction over a long list of weak concerns.
- Do not balance evidence artificially. If one side is much stronger, say so.
- If confidence is low, state what evidence would change the verdict.
