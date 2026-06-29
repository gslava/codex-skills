# Change Categorization

Prefer PR/MR titles over raw commit subjects when available.

## Keep a Changelog Categories

- `Added`: new features.
- `Changed`: changes to existing functionality.
- `Deprecated`: soon-to-be removed features.
- `Removed`: removed features.
- `Fixed`: bug fixes.
- `Security`: vulnerabilities.

## Conventional Commit Mapping

- `feat` -> `Added`.
- `fix` -> `Fixed`.
- `perf`, `refactor` -> `Changed`.
- `security` or subjects mentioning CVE/security -> `Security`.
- `deprecate` -> `Deprecated`.
- `remove` -> `Removed`.
- `docs` -> documentation notes, usually omit from customer release notes unless user-facing.
- `test`, `ci`, `build`, `chore` -> usually omit unless they affect users or release reliability.
- `!` or `BREAKING CHANGE` -> Breaking changes; drives major release consideration.

## Noise Filters

Filter by default:

- Merge commits with no useful PR title.
- Version bump commits.
- Lockfile-only changes unless dependency updates are part of the release.
- Formatting-only commits.
- Version bump or release housekeeping commits.

Do not filter:

- Security fixes.
- Dependency updates that fix vulnerabilities.
- Migration or compatibility changes.

## Tag Selection

- Prefer the latest stable SemVer tag for customer-facing release notes.
- Use prerelease tags only when the user asks for prerelease-to-prerelease changes or the project releases only prereleases.
