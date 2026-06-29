# Implementation Plan Template

Use this base template for all plans. Keep only sections that matter for the risk.

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
- [ ] Run `[focused command]`

## Verification
- [ ] `[full command]`

## Out of Scope
- [Excluded work]
```

## Migration Add-Ons

For schema, data, public API, or rollout work, add:

- Compatibility contract.
- Rollback path.
- Data validation before and after.
- Rollout order.
- Negative tests for auth/security changes.
