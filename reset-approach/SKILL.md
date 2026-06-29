---
name: reset-approach
description: "Recover after an attempted solution path has failed, become over-complicated, repeatedly failed verification, or the user rejects the current implementation direction. Use to pause, preserve useful work, reframe the problem, and choose a better path before more edits; not for ordinary git reset, undo, or revert requests."
---

# Reset Approach

Stop compounding a bad direction. Reframe the problem and choose a better path.

## Rules

- Pause implementation before making more edits.
- Do not defend the current approach.
- Identify what assumption failed.
- Preserve useful work only if it still fits the new direction.
- Ask before discarding, reverting, or rewriting substantial existing work.
- In a git repo, check `git status --short` before proposing cleanup; do not clean up automatically.

## Clarifying Questions

- Ask if the rejected direction, salvageable work, revert permission, minimal goal, or next constraint is unclear.
- Do not proceed on assumptions that affect what to keep, abandon, rewrite, or revert.
- Ask numbered questions with lettered options; option A must be recommended. Continue once the new direction and salvage policy are clear.

## Do Not Trigger

- No failed approach yet, unless the user explicitly says the direction is wrong.
- Initial design.
- Failing tests with unknown cause.
- Simple undo, revert, or git reset requests.

## Workflow

1. State what failed and the evidence.
2. Restate the smallest actual goal.
3. Identify what context is missing.
4. Recommend a smaller, clearer path.
5. Separate work to keep from work to abandon, and ask before destructive cleanup.

## Salvage Policy

- Keep reproduction steps, useful tests, and verified facts.
- Discard speculative abstractions and broad rewrites.
- Do not run git reset, checkout, or destructive cleanup without explicit approval.

## Output

```markdown
**Failed Assumption**
[What no longer holds.]

**Actual Goal**
[Minimal goal.]

**New Path**
[Recommended direction and why.]

**Keep**
[Facts/tests/changes worth preserving.]

**Stop**
[Work to abandon.]

**Needs Approval**
[Reverts or destructive cleanup, if any.]
```
