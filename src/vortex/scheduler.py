"""
Vortex Scheduler Component
"""
import asyncio
from asyncio import Queue
from contextlib import suppress

from vortex.request import Request
from vortex.utils.signals import Signal


class Scheduler:

    def __init__(self, agent, settings):
        self.request_queue = Queue()

        self._is_started = False  # TODO: Task.isRunning???

        # Signals
        self.request_enqueued = Signal()
        self.request_dequeued = Signal()

        # Start
        self._start()

    async def enqueue_requests(self, requests: [Request]):
        for request in requests:
            self.request_queue.put_nowait(request)  # TODO: put_nowait()

    async def dequeue_request(self):
        if self.request_queue.qsize() > 0:
            await self.request_dequeued.emit(self.request_queue.get_nowait())  # TODO: get_nowait()

    def _start(self):
        if not self._is_started:
            self._is_started = True
            self._task = asyncio.create_task(self._loop())

    async def _stop(self):
        if self._is_started:
            self._is_started = False
            self._task.cancel()
            with suppress(asyncio.CancelledError):  # TODO: suppress???
                await self._task

    async def _loop(self):
        while True:
            await self.dequeue_request()
            await asyncio.sleep(1)  # TODO: '1' from settings
