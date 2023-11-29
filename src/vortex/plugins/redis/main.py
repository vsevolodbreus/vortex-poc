import asyncio
import os

import aioredis

from vortex.request import Request
from vortex.settings import Settings
from vortex.utils.signals import Signal

config_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "config.toml")


class RedisPlugin:

    def __init__(self, settings: Settings):
        self._settings = settings

        # Config
        self.config = Settings.from_toml(config_path)

        # Signals
        self.message_dequeued = Signal()

        # Async create
        asyncio.create_task(self._create())

    async def _create(self):
        self._redis = await aioredis.create_redis('redis://' + self._settings.get('address'))
        channel = await self._redis.subscribe(self._settings.get('channel'))
        self._task = asyncio.create_task(self._loop(channel[0]))

    # TODO: for test
    async def handle_request_dequeued(self, request: Request):
        print(request.url)

    async def _loop(self, channel):
        while await channel.wait_message():
            message = await channel.get()
            await self.message_dequeued.emit(message)

# await sub.unsubscribe('chan:1')
# await tsk
# sub.close()
# pub.close()
# self._redis.close()
# await self._redis.wait_closed()
