#!/usr/bin/env python3
"""Validate local Codex skill folders without external dependencies."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


RESOURCE_RE = re.compile(r"\((?P<path>(references|scripts)/[^)]+)\)|`(?P<tick>(references|scripts)/[^`]+)`")
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
TARGET_SKILL_LINES = 90
WARN_SKILL_LINES = 110
FAIL_SKILL_LINES = 150
MAX_DESCRIPTION_WORDS = 50
REQUIRED_SECTION_TITLES = {"## Clarifying Questions"}


def fail(errors: list[str], path: Path, message: str) -> None:
    errors.append(f"{path}: {message}")


def warn(warnings: list[str], path: Path, message: str) -> None:
    warnings.append(f"{path}: {message}")


def iter_files(root: Path, pattern: str) -> list[Path]:
    matches: list[Path] = []
    for path in root.rglob(pattern):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        matches.append(path)
    return matches


def frontmatter(skill_md: Path, errors: list[str]) -> dict[str, str]:
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(errors, skill_md, "missing YAML frontmatter")
        return {}
    try:
        raw = text.split("---", 2)[1]
    except IndexError:
        fail(errors, skill_md, "unterminated YAML frontmatter")
        return {}

    data: dict[str, str] = {}
    for line in raw.strip().splitlines():
        if ":" not in line:
            fail(errors, skill_md, f"invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    if set(data) != {"name", "description"}:
        fail(errors, skill_md, f"frontmatter keys must be name and description only, got {sorted(data)}")
    return data


def mentioned_resources(text: str) -> set[str]:
    resources: set[str] = set()
    for match in RESOURCE_RE.finditer(text):
        resource = match.group("path") or match.group("tick")
        if resource:
            resources.add(resource)
    return resources


def has_agent_field(agent_text: str, field: str) -> bool:
    interface = False
    for line in agent_text.splitlines():
        if line.strip() == "interface:":
            interface = True
            continue
        if interface and re.match(rf"^\s{{2}}{re.escape(field)}\s*:", line):
            return True
    return False


def validate_skill(skill_dir: Path, errors: list[str], warnings: list[str]) -> None:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        fail(errors, skill_dir, "missing SKILL.md")
        return

    data = frontmatter(skill_md, errors)
    if data.get("name") != skill_dir.name:
        fail(errors, skill_md, f"name {data.get('name')!r} does not match folder {skill_dir.name!r}")
    if not data.get("description"):
        fail(errors, skill_md, "description is empty")
    elif len(data["description"].split()) > MAX_DESCRIPTION_WORDS:
        warn(warnings, skill_md, f"description is long ({len(data['description'].split())} words)")

    agent_yaml = skill_dir / "agents" / "openai.yaml"
    if not agent_yaml.exists():
        fail(errors, skill_dir, "missing agents/openai.yaml")
    else:
        agent_text = agent_yaml.read_text(encoding="utf-8")
        for field in ["display_name", "short_description", "default_prompt"]:
            if not has_agent_field(agent_text, field):
                fail(errors, agent_yaml, f"missing interface.{field}")

    text = skill_md.read_text(encoding="utf-8")
    line_count = len(text.splitlines())
    for title in REQUIRED_SECTION_TITLES:
        if title not in text:
            fail(errors, skill_md, f"missing required section {title!r}")
    if line_count > FAIL_SKILL_LINES:
        fail(errors, skill_md, f"SKILL.md is too long ({line_count} lines; target {TARGET_SKILL_LINES}, max {FAIL_SKILL_LINES})")
    elif line_count > WARN_SKILL_LINES:
        warn(warnings, skill_md, f"SKILL.md is long ({line_count} lines; target {TARGET_SKILL_LINES})")

    resources = mentioned_resources(text)
    for resource in resources:
        if not (skill_dir / resource).exists():
            fail(errors, skill_md, f"missing referenced file {resource}")

    for folder_name in ["references", "scripts"]:
        folder = skill_dir / folder_name
        if not folder.exists():
            continue
        for resource_file in folder.rglob("*"):
            if resource_file.is_dir():
                continue
            if any(part in SKIP_DIRS for part in resource_file.parts):
                continue
            rel = resource_file.relative_to(skill_dir).as_posix()
            if rel not in resources:
                warn(warnings, resource_file, "resource is not mentioned in SKILL.md")

    for script in (skill_dir / "scripts").glob("*.py") if (skill_dir / "scripts").exists() else []:
        try:
            compile(script.read_text(encoding="utf-8"), str(script), "exec")
        except SyntaxError as exc:
            fail(errors, script, f"syntax error: {exc}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path("."), help="Directory containing skill folders")
    args = parser.parse_args()

    root = args.root.resolve()
    errors: list[str] = []
    warnings: list[str] = []
    for junk in iter_files(root, ".DS_Store"):
        fail(errors, junk, "remove local macOS metadata file")
    for skill_dir in sorted(path.parent for path in root.glob("*/SKILL.md")):
        validate_skill(skill_dir, errors, warnings)

    for warning in warnings:
        print(f"warning: {warning}", file=sys.stderr)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("Skill validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
