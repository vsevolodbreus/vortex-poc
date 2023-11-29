"""
Signals for communication between components
"""
import asyncio
from typing import Any, Callable

import aiojobs


class Signal:

    def __init__(self):
        self._receivers = set()
        asyncio.create_task(self._create())

    async def _create(self):
        self._jobs = await aiojobs.create_scheduler()

    def bind(self, receiver: Callable):
        self._receivers.add(receiver)

    def unbind(self, receiver: Callable):
        self._receivers.remove(receiver)

    async def emit(self, data: Any):
        for receiver in self._receivers:
            await self._jobs.spawn(receiver(data))
