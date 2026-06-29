---
name: brainstorm-design
description: "Collaborative design workflow for significant software changes: new features, architecture decisions, refactors, migrations, and ambiguous code implementation requests. Use before writing code when the right technical solution is unclear, risk is non-trivial, or multiple codebase-compatible approaches exist."
---

# Brainstorm Design

Turn an unclear idea into an implementation-ready direction before code changes begin.

## Core Rules

- Inspect local context before asking: relevant README, AGENTS.md, code, tests, and recent changes.
- Do not write code during brainstorming unless the user explicitly switches to implementation.
- Lead with a recommendation, not a neutral menu.
- Prefer "simple now, extensible later"; flag speculative abstractions.

## Clarifying Questions

- Ask before presenting options if decision-critical details are missing, contradictory, or unclear.
- Do not proceed on assumptions that affect scope, target behavior, safety, data, API, UX, or acceptance criteria.
- Ask numbered questions with lettered options; option A must be recommended. Continue until the design can be chosen without decision-critical assumptions.

## Do Not Trigger

- Direct low-risk edits with clear acceptance criteria.
- Ordinary code explanation without design alternatives.
- Concrete failures or stack traces.
- Already-approved plan execution.

## Workflow

1. Clarify the goal.
   - Restate the concrete outcome.
   - Identify success criteria, constraints, affected users, and failure modes.
   - Ask when missing context affects the recommendation.

2. Gather evidence.
   - Search for existing patterns before inventing new ones.
   - Read only the files needed to understand the area.
   - Note conventions, integration points, dependencies, and tests.

3. Compare options.
   - Present 2-3 materially different approaches only when tradeoffs matter.
   - Put the recommended approach first.
   - Include a smallest-useful option when scope looks inflated.
   - If evidence makes the direction obvious, do not invent alternatives.

4. Recommend the next action.
   - Plan substantial work.
   - Implement small clear work only after the direction is agreed or evidence fully resolves it.
   - Stress-test risky claims before committing to them.

## Output

Use the smallest output that preserves evidence, decision, and next action.

```markdown
**Context**
[Relevant code/docs evidence.]

**Options**
1. [Recommended]: [tradeoff]
2. [Alternative]: [tradeoff]
3. [Smallest useful version]: [tradeoff]

**Recommendation**
[Concrete direction and why.]

**Next Step**
[Ask, plan, implement, investigate, or stop.]
```

For non-trivial decisions, include the rejected alternatives, key risk, and validation required.

## Quality Bar

- Ground recommendations in codebase facts, not generic architecture advice.
- Separate hard requirements from preferences.
- Do not over-design for hypothetical future features.
