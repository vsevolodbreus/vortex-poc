"""
Base Spider Agent Class
"""
from vortex.agents import Agent
from vortex.utils.signals import Signal


class SpiderAgent(Agent):

    def __init__(self):
        super().__init__()

        # Seed Urls
        if not hasattr(self, 'seed_urls'):
            self.seed_urls = []

        # Signals
        self.new_requests_appeared = Signal()  # TODO: rename signal

    async def initiate_process(self):
        raise NotImplementedError()

    async def run(self):
        await self.initiate_process()
