---
name: execute-implementation-plan
description: "Safely execute an existing implementation plan task by task. Use when the user asks to implement, execute, run, continue, or finish a plan file or checklist, especially plans under docs/plans or Codex-created implementation plans."
---

# Execute Implementation Plan

Implement plan tasks sequentially while keeping the plan, code, and verification results aligned.

## Safety Rules

- Read the plan and project instructions before editing.
- Ask before editing when task order, target files, acceptance criteria, verification, or scope is unclear.
- Do not use destructive git commands unless explicitly requested and approved.
- Do not auto-rebase, squash, push, publish, or create releases.
- Respect existing uncommitted changes. Never revert user changes without explicit instruction.
- Execute only the requested scope.

## Clarifying Questions

- Ask before implementation if the selected task, plan order, scope, required files, or acceptance criteria are missing, contradictory, or unclear.
- Do not proceed on assumptions that affect behavior, tests, data, APIs, release actions, or user changes.
- Ask numbered questions with lettered options; option A must be recommended. Continue only when the next task can be completed without decision-critical assumptions.

## Do Not Trigger

- No existing plan or checklist.
- Exploratory design or tradeoff analysis.
- Publishing releases, pushing branches, or rewriting history.

## Execution Loop

1. Establish baseline: read the plan, check git status, identify the next incomplete task.
2. Implement one coherent task: read relevant files, make the smallest scoped change, add/update tests.
3. Verify immediately with focused commands. Fix failures before moving on.
4. Update plan state only after work is done; record blockers and newly required work without silently changing scope.
5. Stop when the next task needs user input, credentials, external systems, or a scope change.
6. Run broader verification listed in the plan when selected scope is complete.

## Commit Policy

- Do not commit unless the user explicitly asks.
- If commits are requested, commit only completed logical units with passing verification.
- Never amend, rebase, squash, or push unless explicitly requested.

## Output

```markdown
**Implemented**
- [Changed behavior.]

**Files**
- [Touched files.]

**Verification**
- `[command]`: [passed/failed/not run + reason]

**Remaining**
- [Blockers, skipped checks, or risks.]
```

## Done Criteria

- Selected plan scope is complete or explicitly blocked.
- Verification was run when available.
- Skipped verification and remaining risks are reported.
