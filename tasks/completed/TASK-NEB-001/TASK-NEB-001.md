---
id: TASK-NEB-001
title: Copy Claude Desktop exemplar files into this repo
status: completed
created: 2026-04-03T19:00:00Z
updated: 2026-04-03T19:15:00Z
completed: 2026-04-03T19:20:00Z
completed_location: tasks/completed/TASK-NEB-001/
priority: high
complexity: 3
parent_review: TASK-R7B3
feature_id: FEAT-NEB
wave: 1
implementation_mode: task-work
tags: [copy, setup]
previous_state: in_review
organized_files:
  - TASK-NEB-001.md
---

# Copy Claude Desktop Exemplar Files

## Description

Copy all source files from `nats-asyncio-service-exemplar-claude-desktop` into this repo, preserving the directory structure.

## Source

`/Users/richardwoollcott/Projects/appmilla_github/nats-asyncio-service-exemplar-claude-desktop/`

## Files to Copy

```
AGENTS.md
Dockerfile
docker-compose.yml
pyproject.toml
README.md
src/example_service/__init__.py
src/example_service/__main__.py
src/example_service/app.py
src/example_service/config.py
src/example_service/handlers/__init__.py
src/example_service/handlers/domain.py
src/example_service/schemas/__init__.py
src/example_service/services/__init__.py
src/example_service/services/domain.py
tests/conftest.py
tests/test_handler.py
tests/test_service.py
tests/test_integration.py
```

## Acceptance Criteria

- [x] All files copied with correct directory structure
- [x] No modifications yet (fixes come in TASK-NEB-002)
