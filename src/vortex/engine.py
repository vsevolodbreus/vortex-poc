"""
Vortex engine.
"""
import asyncio

from vortex.agents.spiders import SpiderAgent
from vortex.downloader import Downloader
from vortex.pipeline import Pipeline
from vortex.plugins import setup_plugins
from vortex.scheduler import Scheduler
from vortex.scraper import Scraper
from vortex.settings import Settings

try:
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass


class Engine:

    def __init__(
            self,
            agent: SpiderAgent,
            settings: Settings
    ) -> None:
        """

        :param agent:
        :param settings:
        """
        self.agent = agent

        # TODO: Interesting construct, though there's probably a better way

        # Default settings
        self.settings = Settings.default()
        # Project settings
        if settings is not None:
            self.settings.override(settings)
        # Spider settings
        if isinstance(self.agent.custom_settings, dict):
            self.settings.override(self.agent.custom_settings)
        # CLI settings
        # TODO: if need

        # Async create
        self._create_task = asyncio.create_task(self._create())

    async def _create(self):
        # Initialize components
        self.scheduler = Scheduler(self.agent, self.settings)
        self.downloader = Downloader(self.agent, self.settings)
        self.scraper = Scraper(self.agent, self.settings)
        self.pipeline = Pipeline(self.agent, self.settings)

        # Interaction between components
        self.agent.new_requests_appeared.bind(self.scheduler.enqueue_requests)
        self.downloader.response_received.bind(self.scraper.process_response)
        self.scheduler.request_dequeued.bind(self.downloader.fetch)
        self.scraper.links_collected.bind(self.scheduler.enqueue_requests)

        # Plugins
        setup_plugins(self, self.settings)

    async def run(self):
        await self._create_task
        await self.agent.run()
