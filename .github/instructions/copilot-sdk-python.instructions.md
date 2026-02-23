---
applyTo: '**.py, pyproject.toml, setup.py'
description: 'Guidance for building Python applications using GitHub Copilot SDK'
name: 'GitHub Copilot SDK Python Instructions'
---

# Copilot SDK Python Notes

- Requires Python 3.9+.
- Use async/await patterns.
- Prefer `async with` for client/session lifecycle safety.
- Use event-driven handling with `session.idle` and `session.error`.
- Prefer explicit typing for configs and tool args.

## Install

- `uv add github-copilot-sdk`

## Session Practices

- Use streaming only when needed for UX.
- Keep tool schemas explicit and validated.
- Use append-mode system messages to preserve safeguards.

## Reliability

- Always unsubscribe handlers when done.
- Handle retries and timeout paths.
- Clean up sessions in `finally` blocks when not using context managers.
