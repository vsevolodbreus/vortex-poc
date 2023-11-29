"""
Crawler Example

Website: http://guiamexico.com.mx/

Schema:
- name
- website
- address
- telephone
- description

"""
from vortex.agents.spiders.crawl import CrawlSpiderAgent
from vortex.runner import Runner
from vortex.settings import Settings
from vortex.scraper import Rule
from vortex.utils.link_extractor import LinkExtractor


class GuiaMexicoSpiderAgent(CrawlSpiderAgent):
    # Agent name
    name = "guia_mexico"

    # Custom settings
    custom_settings = {'property': 1}

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

    #
    def parse_item(self, response):
        pass


# TODO: convert to command line interface: vortex run <mod_name> --params
if __name__ == '__main__':
    settings = Settings.from_toml("settings.toml")
    Runner.run(GuiaMexicoSpiderAgent, settings)
