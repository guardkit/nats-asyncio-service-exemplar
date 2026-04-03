# Implementation Guide: Build NATS Asyncio Service Exemplar

## Overview

Build the definitive NATS asyncio service exemplar by copying the reviewed Claude Desktop exemplar and applying minor fixes.

## Wave 1: Copy and Fix (Sequential)

### TASK-NEB-001: Copy Exemplar Files
**Method**: task-work

Copy all files from `/Users/richardwoollcott/Projects/appmilla_github/nats-asyncio-service-exemplar-claude-desktop/` preserving directory structure. The existing `migrations/` directory in this repo can be removed (not part of the spec).

### TASK-NEB-002: Apply Minor Fixes
**Method**: task-work
**Depends on**: TASK-NEB-001

Four fixes:
1. Remove `version: '3.8'` from docker-compose.yml
2. Add `env_file=".env"` to Settings config
3. Create `.env.example` with all SERVICE_ vars documented
4. Fix explicit conftest imports in test files

## Wave 2: Verify (Parallel)

### TASK-NEB-003: Implement Integration Test
**Method**: task-work

Replace pytest.skip stub with working roundtrip test using nats-py direct connection.

### TASK-NEB-004: Verify Quality Gates
**Method**: direct

Run: pip install, pytest, ruff, mypy, python -m example_service.

## Key Reference Files

- **Template spec**: `/Users/richardwoollcott/Projects/appmilla_github/guardkit/docs/research/dark_factory/template-spec-nats-asyncio-service.md`
- **Review report**: `.claude/reviews/TASK-R7B3-review-report.md`
- **Source exemplar**: `/Users/richardwoollcott/Projects/appmilla_github/nats-asyncio-service-exemplar-claude-desktop/`
