"""Example NATS asyncio service — exemplar for nats-asyncio-service template."""

from __future__ import annotations

from example_service.app import app, broker
from example_service.config import Settings

__all__ = ["app", "broker", "Settings"]
