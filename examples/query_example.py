"""
Query Example

Website: http://guiamexico.com.mx/

Schema:
- name
- website
- address
- telephone
- description

"""
from vortex.agents.spiders.query import QuerySpiderAgent
from vortex.request import Request
from vortex.runner import Runner
from vortex.scraper import Rule
from vortex.settings import Settings
from vortex.utils.link_extractor import LinkExtractor


class QueryExample(QuerySpiderAgent):
    # Agent name
    name = "query_example"

    # Custom settings
    custom_settings = {
        'plugins': {'redis': {'address': 'localhost', 'channel': 'ch1', 'signals': ['message_dequeued']}}}

    # Seed urls
    seed_urls = ['https://guiamexico.com.mx/']

    # Crawl rules
    rules = (
        Rule(
            LinkExtractor(allow=(r'[0-9]+\/category',))
        ),
        Rule(
            LinkExtractor(allow=(r'detail\/[0-9]+',)),
            follow=True,
            callback='parse_item'
        ),
    )

    async def initiate_process(self):
        pass

    async def handle_message_dequeued(self, data):
        print(data)
        await self.new_requests_appeared.emit(
            [Request(url) for url in self.seed_urls])

    #
    def parse_item(self, response):
        pass


# TODO: convert to command line interface: vortex run <mod_name> --params
if __name__ == '__main__':
    settings = Settings.from_toml("settings.toml")
    Runner.run(QueryExample, settings=settings)
