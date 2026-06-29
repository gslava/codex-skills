---
name: make-implementation-plan
description: "Create rigorous implementation plans for feature work, bug fixes, refactors, migrations, test work, and multi-step code changes. Use when the user asks for a plan, roadmap, implementation plan, task breakdown, or when a change is large enough that coding immediately would hide risk."
---

# Make Implementation Plan

Create plans specific enough to execute without rediscovering context.

Use [references/plan-templates.md](references/plan-templates.md) for the base plan shape.

## Core Rules

- Do a focused codebase scan before planning. Do not produce generic plans.
- Ask before writing the plan when any decision-critical detail remains unknown after discovery.
- Do not edit implementation files while creating a plan unless the user explicitly asks to plan and implement in the same turn.
- Keep plans executable: exact files, task boundaries, tests, commands, acceptance criteria, and out-of-scope items.
- Every code-changing task must include tests or an explicit reason tests are not applicable.
- Avoid speculative architecture, future features, broad cleanup, and phase plans that hide implementation detail.

## Clarifying Questions

- Ask if target behavior, acceptance criteria, constraints, plan location, tests, rollout, compatibility, migration safety, or scope is unclear.
- Do not write a final plan with unresolved decision-critical assumptions. If the user forbids questions, mark the plan as draft/blocked.
- Ask numbered questions with lettered options; option A must be recommended. Continue once the plan can be written without decision-critical assumptions.

## Do Not Trigger

- Small, clear implementation requests where the user explicitly wants code now.
- Review of an existing plan.
- Debugging when the cause is unknown.

## Discovery

1. Identify task type: feature, bug fix, refactor, migration, tests, release, or investigation.
2. Inspect relevant files, existing patterns, project instructions, test setup, and recent status when useful.
3. Summarize known facts, resolved decisions, and blocking questions.

## Plan Rules

- Use the smallest plan that fits the risk.
- Low risk: one file family, no persistence/auth/API/release impact, obvious rollback.
- Medium risk: cross-layer changes, new config/dependency, public behavior change, integration tests/manual verification.
- High risk: auth, secrets, payments, data integrity, migrations, public API, release, concurrency, retries, idempotency.
- High-risk tasks need mitigation and rollback/compatibility notes.
- If no plan-file convention exists and the user did not specify a path, ask before writing.

## Output

```markdown
# [Plan Title]

## Goal
[Outcome and reason.]

## Evidence
- [Files/patterns/tests read.]

## Resolved Decisions
- [Decision and source.]

## Open Questions
- [Only if draft/blocked.]

## Acceptance Criteria
- [ ] [Outcome]

## Tasks
### Task 1: [Outcome]
Risk: [low/medium/high]
Files: `path/file`, `path/test`
- [ ] [Specific implementation step]
- [ ] [Test]
- [ ] Run `[command]`

## Verification
- [ ] `[full command]`

## Out of Scope
- [Excluded work]
```
