---
name: investigate-root-cause
description: "Systematic debugging and root cause analysis for concrete failures: errors, failing tests, build failures, logs, stack traces, flaky behavior, performance regressions, integration failures, and reproducible wrong behavior. Use before applying fixes when the cause is uncertain; use clarify-confusion for expectation mismatches without failure evidence."
---

# Investigate Root Cause

Find the cause before changing code.

## Rules

- Do not start with a fix.
- Reproduce or verify the symptom when practical.
- Separate observation, inference, and hypothesis.
- Prefer commands and code references over guesses.
- Stop and ask before using production systems, secrets, destructive commands, or external services.

## Clarifying Questions

- Ask before investigation if the failing command, expected behavior, environment, reproduction steps, affected version, or recent change is missing and cannot be discovered locally.
- Do not proceed on assumptions that affect the symptom, cause, safety, data, environment, or verification.
- Ask numbered questions with lettered options; option A must be recommended. Continue once the failure can be investigated without decision-critical assumptions.

## Do Not Trigger

- Root cause is already proven and the user asks for a small direct fix.
- Design tradeoffs.
- Expectation mismatch without failure evidence.

## Workflow

1. Define the symptom: what failed, what was expected, what changed, what environment is involved.
2. Gather evidence: run the failing command when practical, read logs/stack traces, search error text and related code/config.
3. Build a cause chain: immediate failure, local code/config/input cause, missing guardrail, recurrence-prevention change.
4. Validate hypotheses with the smallest command or inspection that can disprove them.
5. If not reproduced, report commands tried, observed result, missing evidence, and safest next step.
6. Recommend or implement the smallest safe fix only after the cause is validated.

## Output

```markdown
**Symptom**
[Observed failure.]

**Evidence**
- [Command/log/code reference.]

**Root Cause**
[Validated cause, or "not reproduced".]

**Fix**
[Smallest safe change or next diagnostic step.]

**Verification**
[Command/result.]
```

For incident/postmortem-lite output, include impact, timeline, detection, resolution, root/contributing causes, and follow-up actions.

## Anti-Patterns

- Do not patch error handling without understanding why the error occurred.
- Do not assume flaky behavior is infrastructure until local causes are checked.
- Do not broaden scope into refactoring unless required for the fix.
