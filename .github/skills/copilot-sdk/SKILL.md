---
name: copilot-sdk
description: Use when building Python automations or tools that interact with GitHub Copilot SDK sessions, events, and tool-calling workflows. Includes setup, lifecycle, and reliability guidance for async usage.
license: Complete terms in LICENSE.txt
---

# Copilot SDK Skill

## When to Use

- Creating Python utilities on top of GitHub Copilot SDK
- Building event-driven prompt/session workflows
- Adding custom tool handlers for Copilot sessions

## Prerequisites

- Python 3.9+
- `github-copilot-sdk` installed

## Workflow

1. Install dependency with `uv`.
2. Create client/session via async context managers.
3. Subscribe to events and wait for `session.idle`.
4. Add strongly typed tools and schemas.
5. Handle timeout/error paths and cleanup.

## References

- See `../../instructions/copilot-sdk-python.instructions.md`
