# nats-asyncio-service-exemplar

Source exemplar for the `nats-asyncio-service` GuardKit template. This project
encodes the key patterns that `/template-create` will extract into a reusable template.

**This is NOT a production service.** It exists solely as the source for template extraction.

## Key Patterns Encoded

| Pattern | Location | Why It Matters |
|---------|----------|---------------|
| Handler/Service separation | `handlers/domain.py` → `services/domain.py` | Handlers are thin dispatchers; business logic is independently testable |
| TestNatsBroker for unit tests | `tests/test_handler.py` | Zero-infrastructure unit tests — no real NATS needed |
| Factory function test data | `tests/conftest.py` | `make_inbound_message()` — readable, self-contained test setup |
| pydantic-settings config | `config.py` | Environment variable configuration with typed defaults |
| Lifespan context manager | `app.py` | Startup/shutdown lifecycle for shared resources |
| Pydantic message schemas | `schemas/__init__.py` | Typed wire format with `extra="ignore"` for forward compat |
| Docker Compose with JetStream | `docker-compose.yml` | NATS with `-js` flag + service container |
| AGENTS.md boundaries | `AGENTS.md` | ALWAYS/NEVER/ASK for agent guidance |
| stderr-only logging | `app.py` | No stdout pollution |
| `__main__.py` entry point | `__main__.py` | `python -m example_service` |

## Template Extraction

```bash
cd ~/Projects/appmilla_github/guardkit
/template-create --name nats-asyncio-service --path ~/Projects/appmilla_github/nats-asyncio-service-exemplar
```

## Post-Extraction

Run `/agent-enhance` on generated specialist agents, especially:
- `nats-service-specialist` — subject hierarchy, TestNatsBroker, handler/service split
- `nats-testing-specialist` — TestNatsBroker in-memory vs integration test discipline
- `nats-schema-specialist` — Pydantic message design, subject-to-schema mapping
