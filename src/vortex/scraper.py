"""
Vortex Scraper Component

# TODO: use https://github.com/rushter/selectolax , instead of LXML
"""
from typing import Optional, Callable

from vortex.request import Request
from vortex.response import Response
from vortex.utils.link_extractor import LinkExtractor
from vortex.utils.signals import Signal


class Rule:

    def __init__(
            self,
            link_extractor: LinkExtractor = None,
            callback=None,
            follow=None
    ):
        """

        :param link_extractor:
        :param callback:
        :param follow:
        """
        self.link_extractor = link_extractor
        self.callback = callback
        self.follow = follow

    def process_links(self, links):
        return links


class Scraper:

    def __init__(self, agent, settings):
        self.rules = agent.rules
        self.settings = settings

        # Signals
        self.links_collected = Signal()

    async def _process_response(
            self,
            response: Response,
            callback: Optional[Callable],
            follow: bool = True
    ) -> str:
        """

        :param response:
        :param callback:
        :param follow:
        :return:
        """
        seen = set()

        if callback:
            callback_result = callback(response) or ()
            for request_or_item in callback_result:
                yield request_or_item

        if follow:
            for rule_index, rule in enumerate(self.rules):

                # Get all links
                links = [
                    link for link in
                    rule.link_extractor.extract_links(response)
                ]

                # Yield requests from links
                for link in rule.process_links(links):
                    seen.add(link)
                    # yield Request(
                    #     url=link,
                    # )
                    yield link

    async def process_response(self, response):
        urls = [
            r async for r in
            self._process_response(response, callback=None, follow=True)
        ]

        # TODO: How to filter items vs requests
        await self.links_collected.emit(
            [Request(url) for url in urls if len(urls) > 0])
