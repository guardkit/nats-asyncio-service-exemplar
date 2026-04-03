---
id: TASK-R7B3
title: Review and build best NATS asyncio service exemplar
status: review_complete
created: 2026-04-03T18:30:00Z
updated: 2026-04-03T18:30:00Z
priority: high
tags: [nats, faststream, template, exemplar, review]
complexity: 7
task_type: review
test_results:
  status: pending
  coverage: null
  last_run: null
---

# Task: Review and Build Best NATS Asyncio Service Exemplar

## Description

Review the Claude Desktop exemplar (`nats-asyncio-service-exemplar-claude-desktop`) against the template spec, then build the definitive exemplar in this repo by combining the best of both approaches (Claude Desktop output + Claude Code cookiecutter-based approach). The goal is to produce a source repo ready for `/template-create --name nats-asyncio-service`.

## Context

### Spec Reference
- **Template spec**: `/Users/richardwoollcott/Projects/appmilla_github/guardkit/docs/research/dark_factory/template-spec-nats-asyncio-service.md`
- **Session guide**: `/Users/richardwoollcott/Projects/appmilla_github/guardkit/docs/research/dark_factory/template-creation-session.md`
- **Claude Desktop exemplar**: `/Users/richardwoollcott/Projects/appmilla_github/nats-asyncio-service-exemplar-claude-desktop/`

### Two Approaches to Compare
1. **Claude Desktop** — manually crafted exemplar (already exists in `nats-asyncio-service-exemplar-claude-desktop/`)
2. **Claude Code + cookiecutter** — bootstrap from `cookiecutter-faststream` template then enhance (cookiecutter already installed)

## Phase 1: Review Claude Desktop Exemplar

Evaluate the Claude Desktop exemplar against the template spec checklist:

- [ ] FastStream NatsBroker with JetStream (not raw nats-py)
- [ ] Handler/Service separation (thin handlers, logic in services/)
- [ ] TestNatsBroker for infrastructure-free unit tests
- [ ] pydantic-settings configuration (Settings class with env_file)
- [ ] Lifespan context manager for startup/shutdown
- [ ] Pydantic message schemas with `extra="ignore"`
- [ ] docker-compose.yml with NATS `-js` flag
- [ ] AGENTS.md with ALWAYS/NEVER/ASK boundaries
- [ ] Subject hierarchy convention: `domain.action.qualifier.{id}`
- [ ] Factory function test data pattern (conftest.py)
- [ ] stderr-only logging
- [ ] pytest with asyncio_mode="auto" and `-m "not integration"` default gate
- [ ] `__main__.py` for `python -m` execution
- [ ] Dockerfile
- [ ] pyproject.toml with correct dependencies and markers
- [ ] correlation_id in response messages

### Review Findings
Document: What's done well, what's missing, what deviates from spec.

## Phase 2: Generate Cookiecutter FastStream Project

```bash
cookiecutter https://github.com/airtai/cookiecutter-faststream.git
# Select: NATS broker
# Name: nats-asyncio-service-exemplar
```

Review what the cookiecutter generates vs what the spec requires. Document gaps.

## Phase 3: Build the Best Exemplar

Combine the best of both approaches into THIS repo (`nats-asyncio-service-exemplar`):

### Required Structure
```
src/example_service/
  __init__.py
  __main__.py
  app.py              # FastStream app + broker + lifespan
  config.py            # pydantic-settings Settings
  handlers/
    __init__.py
    domain.py          # @broker.subscriber — thin
  services/
    __init__.py
    domain.py          # Business logic — testable without NATS
  schemas/
    __init__.py        # Pydantic message models
tests/
  conftest.py          # Factory functions for test data
  test_handler.py      # TestNatsBroker tests
  test_service.py      # Pure unit tests for service logic
  test_integration.py  # Marked @pytest.mark.integration
pyproject.toml
docker-compose.yml
Dockerfile
AGENTS.md
README.md
```

### Key Decisions to Make
- Which patterns from each approach to keep
- Whether cookiecutter scaffolding adds value or just noise
- Handler naming and subject conventions

## Phase 4: Verify Exemplar

- [ ] `pip install -e ".[dev]"` succeeds
- [ ] `pytest` passes (unit tests only, no NATS server)
- [ ] `pytest -m integration` passes with `docker compose up -d nats`
- [ ] `python -m example_service` starts and connects to NATS
- [ ] `ruff check src/ tests/` passes
- [ ] `mypy src/` passes
- [ ] All spec success criteria from template-spec met

## Acceptance Criteria

- [ ] Claude Desktop exemplar reviewed with documented findings
- [ ] Cookiecutter approach evaluated
- [ ] Best exemplar built in this repo combining both approaches
- [ ] All tests pass (unit without NATS, integration with NATS)
- [ ] AGENTS.md present with ALWAYS/NEVER/ASK
- [ ] Ready for `/template-create --name nats-asyncio-service --path .`

## Implementation Notes

The cookiecutter is already installed (`python3 -m pip install cookiecutter`).

The Claude Desktop exemplar already covers most spec requirements well:
- Good handler/service separation
- Correct pyproject.toml with markers
- Proper AGENTS.md
- docker-compose with JetStream
- TestNatsBroker pattern

Areas to verify more closely:
- Lifespan context manager implementation
- Schema `extra="ignore"` on all models
- correlation_id pattern
- Factory functions in conftest.py

## Test Execution Log
[Automatically populated by /task-work]
