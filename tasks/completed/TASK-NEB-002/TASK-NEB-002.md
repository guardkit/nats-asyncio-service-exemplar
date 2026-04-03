---
id: TASK-NEB-002
title: Apply minor fixes from review findings
status: completed
created: 2026-04-03T19:00:00Z
updated: 2026-04-03T19:30:00Z
completed: 2026-04-03T19:35:00Z
completed_location: tasks/completed/TASK-NEB-002/
priority: high
complexity: 2
parent_review: TASK-R7B3
feature_id: FEAT-NEB
wave: 1
implementation_mode: task-work
dependencies: [TASK-NEB-001]
tags: [fix, config]
previous_state: in_review
organized_files:
  - TASK-NEB-002.md
---

# Apply Minor Fixes from Review

## Description

Apply the 4 minor fixes identified in the TASK-R7B3 review.

## Fixes

### Fix 1: Remove deprecated `version` key from docker-compose.yml
Remove `version: '3.8'` line — modern Docker Compose doesn't need it.

### Fix 2: Add `env_file` support in config.py
```python
model_config = SettingsConfigDict(
    env_prefix="SERVICE_",
    env_file=".env",
    env_file_encoding="utf-8",
)
```

### Fix 3: Create `.env.example`
Document all SERVICE_ environment variables with defaults.

### Fix 4: Fix conftest imports in test files
Remove explicit `from conftest import make_inbound_message` — pytest auto-discovers conftest.py. Use direct function calls since conftest is automatically available.

## Acceptance Criteria

- [x] docker-compose.yml has no `version` key
- [x] config.py supports both env_file and env_prefix
- [x] .env.example exists with all documented vars
- [x] Tests don't use explicit conftest imports
