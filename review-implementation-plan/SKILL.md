---
name: review-implementation-plan
description: "Review implementation plans before coding. Use when the user asks to review, validate, sanity-check, de-risk, simplify, or find gaps in a plan, especially docs/plans files, task checklists, migrations, refactors, and multi-step feature plans."
---

# Review Implementation Plan

Perform a read-only review of a plan before implementation.

## Rules

- Do not edit files while reviewing.
- Read the plan and enough project context to validate it.
- Findings come first, ordered by severity.
- Report only issues that affect correctness, maintainability, scope, safety, or testability.
- Do not nitpick wording unless it creates implementation ambiguity.
- If the user asks to revise the plan, report findings first, then edit only after explicit instruction.

## Clarifying Questions

- Ask before reviewing if the plan target, relevant context, base branch, review depth, or permission to read project files is unclear.
- Do not proceed on assumptions that affect whether the plan is correct, safe, or executable.
- Ask numbered questions with lettered options; option A must be recommended. Continue once the review target and context are clear.

## Do Not Trigger

- Code diff or PR review.
- Creating a new plan.
- Executing a plan.

## Checklist

Check correctness, scope control, concrete task files, tests, verification commands, compatibility/migration safety, operational risk, and project fit. Cite line numbers when available; otherwise cite section or task names.

## Output

```markdown
**Findings**
1. [critical/major/minor] [section/task] [issue]
   Impact: [why it matters]
   Fix: [specific plan change]

**Open Questions**
1. [Only if blocking]

**Verdict**
[APPROVE / APPROVE WITH RESIDUAL RISK / NEEDS REVISION]

**Suggested Next Step**
[Revise plan / implement / investigate]
```

Use `APPROVE` only when the plan is clear, concrete, testable, scoped, and safe. Use `APPROVE WITH RESIDUAL RISK` for non-blocking context or verification gaps. Use `NEEDS REVISION` when findings should be fixed before implementation.

If there are no findings, say `No blocking findings` and list residual risks or `None identified`.
