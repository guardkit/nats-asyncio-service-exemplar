"""Entry point for running the service: python -m example_service."""

from __future__ import annotations

import asyncio

from example_service.app import app


def main() -> None:
    """Run the FastStream application."""
    asyncio.run(app.run())


if __name__ == "__main__":
    main()
