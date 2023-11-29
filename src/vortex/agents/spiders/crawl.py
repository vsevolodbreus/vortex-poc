"""
Rule-based Crawl Spider Agent

Uses `Rule` class to define crawling logic.
"""

from vortex.agents.spiders import SpiderAgent
from vortex.request import Request


class CrawlSpiderAgent(SpiderAgent):

    def __init__(self):
        super().__init__()

        if not hasattr(self, 'rules'):
            self.rules = ()

    async def _initiate_process(self):
        # Enqueue seed urls
        await self.new_requests_appeared.emit(
            [Request(url) for url in self.seed_urls])

    async def initiate_process(self):
        await self._initiate_process()