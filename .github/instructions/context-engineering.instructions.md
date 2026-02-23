---
description: 'Guidelines for structuring code and projects to maximize GitHub Copilot effectiveness through better context management'
applyTo: '**'
---

# Context Engineering

## Project Structure

- Use descriptive file paths.
- Colocate related code, tests, and docs.
- Export stable public APIs from clear module boundaries.

## Code Style for Better AI Context

- Prefer explicit type hints in Python.
- Use semantic names over short ambiguous names.
- Replace magic numbers with named constants.

## Copilot Workflow

- Keep relevant files open when working on a task.
- Position cursor where context matters.
- Use chat for cross-file changes and planning.

## Context Hints

- Keep architecture notes in `.github/copilot-instructions.md` and `AGENTS.md`.
- Add brief top-level comments for complex modules.
- Reference concrete in-repo patterns when requesting code changes.

## Multi-File Change Pattern

- State impacted files up front.
- Make incremental updates.
- Re-validate after each logical step.
