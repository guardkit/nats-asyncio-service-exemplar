---
id: TASK-NEB-003
title: Implement integration test stub
status: completed
completed: 2026-04-03T20:45:00Z
created: 2026-04-03T19:00:00Z
priority: medium
complexity: 4
parent_review: TASK-R7B3
feature_id: FEAT-NEB
wave: 2
implementation_mode: task-work
dependencies: [TASK-NEB-002]
tags: [test, integration]
---

# Implement Integration Test

## Description

Replace the `pytest.skip()` stub in `test_integration.py` with a working integration test that verifies the full publish → handler → service → publish roundtrip using a real NATS server.

## Expected Implementation

```python
@pytest.mark.integration
@pytest.mark.asyncio
async def test_full_roundtrip_with_real_nats():
    # 1. Connect to real NATS at localhost:4222
    # 2. Subscribe to domain.action.result
    # 3. Publish InboundMessage to domain.action.request
    # 4. Assert OutboundMessage received on domain.action.result
    # 5. Verify correlation_id links request to response
```

## Prerequisites

- Requires `docker compose up -d nats` running
- Test gated behind `@pytest.mark.integration`

## Acceptance Criteria

- [x] Integration test runs successfully with real NATS
- [x] Verifies full message roundtrip
- [x] Verifies correlation_id linking
- [x] Still skipped in default `pytest` run
