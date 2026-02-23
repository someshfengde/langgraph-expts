---
description: 'Guidelines for creating high-quality Agent Skills for GitHub Copilot'
applyTo: '**/.github/skills/**/SKILL.md, **/.claude/skills/**/SKILL.md'
---

# Agent Skills File Guidelines

## Purpose

Use this file to keep all local skills in this repository portable, discoverable,
and easy to evolve.

## Required Frontmatter for `SKILL.md`

Every skill must include:

- `name` (lowercase, hyphen-separated, <= 64 chars)
- `description` (what it does + when to use it; <= 1024 chars)

Optional:

- `license`

## Skill Folder Structure

Recommended:

- `SKILL.md` (required)
- `LICENSE.txt` (recommended)
- `scripts/` (optional automation)
- `references/` (optional docs)
- `assets/` (optional static files used as-is)
- `templates/` (optional starter files the agent modifies)

## Description Writing Rules

Your description should include:

1. What the skill does
2. When to use it (triggers)
3. Keywords a user might type

## Authoring Best Practices

- Keep instructions action-oriented.
- Use clear steps for repeatable workflows.
- Use relative links for bundled files.
- Avoid secrets in skill files.
- Keep `SKILL.md` concise; move long docs to `references/`.

## Validation Checklist

- Frontmatter present and valid
- Name follows `lowercase-with-hyphens`
- Description is specific and trigger-friendly
- No hardcoded credentials
- Resource links resolve
