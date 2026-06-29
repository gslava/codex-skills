# Codex Skills

Small standalone skills for Codex.

## Structure

Each skill lives in its own folder and includes:

- `SKILL.md`
- `agents/openai.yaml`
- optional `references/`
- optional `scripts/`

## Skills

- `brainstorm-design` - design tradeoffs before implementation
- `capture-project-knowledge` - save durable project conventions
- `clarifying-questions` - resolve decision-critical ambiguity before acting
- `clarify-confusion` - explain expectation mismatches
- `cut-release` - prepare and publish releases
- `dialectic-analysis` - argue both sides of a claim or decision
- `execute-implementation-plan` - implement an approved plan
- `inspect-unreleased-changes` - summarize changes since a tag or base ref
- `investigate-root-cause` - debug concrete failures before fixing them
- `make-implementation-plan` - write task-by-task implementation plans
- `reset-approach` - recover from a bad implementation direction
- `review-implementation-plan` - review a plan before coding
- `review-pull-request` - review a PR, branch diff, or local changes
- `technical-writing-style` - rewrite engineering text in a direct style

## Validate

```bash
python3 scripts/validate_skills.py .
```

The validator checks:

- frontmatter
- `agents/openai.yaml`
- referenced local resources
- Python script syntax
- required `## Clarifying Questions` sections
- stray `.DS_Store` files

## Install

Copy one skill folder or the whole repo into your Codex skills directory.

## License

This repository is licensed under `CC BY 4.0`. See [LICENSE](LICENSE).
