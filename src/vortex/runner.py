"""

"""
import asyncio

from vortex.engine import Engine
from vortex.settings import Settings


class Runner:

    def __init__(self):
        pass

    @staticmethod
    async def _launch_engine(agent_cls, settings):
        agent = agent_cls()
        engine = Engine(agent, settings)
        await engine.run()

    @staticmethod
    def run(agent_cls, settings: Settings = None):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(Runner._launch_engine(agent_cls, settings))

        # TODO: fix this...
        # Let's also finish all running tasks:
        pending = asyncio.Task.all_tasks()
        loop.run_until_complete(asyncio.gather(*pending))
