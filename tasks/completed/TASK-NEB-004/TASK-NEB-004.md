---
id: TASK-NEB-004
title: Verify all quality gates pass
status: completed
completed: 2026-04-03T20:45:00Z
completed_location: tasks/completed/TASK-NEB-004/
created: 2026-04-03T19:00:00Z
priority: high
complexity: 3
parent_review: TASK-R7B3
feature_id: FEAT-NEB
wave: 2
implementation_mode: direct
dependencies: [TASK-NEB-002]
tags: [verify, quality]
---

# Verify All Quality Gates

## Description

Run all verification checks from Phase 4 of the task spec to confirm the exemplar is ready for `/template-create`.

## Checks

- [x] `pip install -e ".[dev]"` succeeds
- [x] `pytest` passes (unit tests only, no NATS server) — 5 passed, 1 deselected (integration)
- [x] `ruff check src/ tests/` passes
- [x] `mypy src/` passes — 9 source files checked
- [x] `python -m example_service` starts (and connects or fails gracefully without NATS)
- [x] All spec success criteria from template-spec met

## Acceptance Criteria

- [x] All checks pass
- [x] Any issues found are documented and fixed
- [x] Exemplar ready for `/template-create --name nats-asyncio-service --path .`

## Issues Found and Fixed

1. **`ruff` UP035**: `from typing import AsyncIterator` → `from collections.abc import AsyncIterator` in `app.py`
2. **`ruff` I001**: Import sort order fixed in `app.py`
3. **`ruff` config deprecation**: Moved `select` from `[tool.ruff]` to `[tool.ruff.lint]` in `pyproject.toml`
4. **`mypy` arg-type**: `NatsBroker` expects `int` for `connect_timeout` and `reconnect_time_wait` — changed from `float` to `int` in `config.py`
5. **Runtime crash**: `lifespan(app: FastStream)` signature incompatible with FastStream's DI — removed the `app` parameter per FastStream docs
