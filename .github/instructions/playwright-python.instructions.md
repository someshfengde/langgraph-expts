---
description: 'Playwright Python AI test generation instructions based on official documentation.'
applyTo: '**'
---

# Playwright Python Test Guidance

- Prefer user-facing locators (`get_by_role`, `get_by_label`, `get_by_text`).
- Prefer web-first assertions with `expect(...)`.
- Avoid hard waits and unnecessary timeout inflation.
- Keep test names descriptive and behavior-focused.

## Baseline Pattern

- Import: `from playwright.sync_api import Page, expect`
- Use `page: Page` fixture
- Navigate early in each test (`page.goto(...)`)
- Keep test files under `tests/` with `test_*.py`
