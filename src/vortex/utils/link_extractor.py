"""
Link Extractor
"""
import re
from typing import Tuple, List, Optional
from typing import re as re_type

from lxml import html as html_parser
from vortex.response import Response

IGNORED_EXTENSIONS = [
    # archives
    '7z', '7zip', 'bz2', 'rar', 'tar', 'tar.gz', 'xz', 'zip',

    # images
    'mng', 'pct', 'bmp', 'gif', 'jpg', 'jpeg', 'png', 'pst', 'psp', 'tif',
    'tiff', 'ai', 'drw', 'dxf', 'eps', 'ps', 'svg', 'cdr', 'ico',

    # audio
    'mp3', 'wma', 'ogg', 'wav', 'ra', 'aac', 'mid', 'au', 'aiff',

    # video
    '3gp', 'asf', 'asx', 'avi', 'mov', 'mp4', 'mpg', 'qt', 'rm', 'swf', 'wmv',
    'm4a', 'm4v', 'flv', 'webm',

    # office suites
    'xls', 'xlsx', 'ppt', 'pptx', 'pps', 'doc', 'docx', 'odt', 'ods', 'odg',
    'odp',

    # other
    'css', 'pdf', 'exe', 'bin', 'rss', 'dmg', 'iso', 'apk'
]

# Type Aliases
Regex = re_type.Pattern

# TODO: consider redoing types to accept list & str (like scrapy)
class LinkExtractor:

    def __init__(
            self,
            allow: Tuple[Regex, ...]=(),
            deny: Tuple[Regex, ...]=(),
            # allow_domains: Tuple[Regex, ...]=(),
            # deny_domains: Tuple[Regex, ...]=(),
            # restrict_xpath: Tuple[str, ...]=(),
            # restrict_css: Tuple[str, ...]=(),
            # restrict_regex: Optional[Union[Regex, List[Regex]]]=None,
            deny_extensions: Optional[List]=None,
            # tags: Tuple[str, ...]=('a', 'area'), # Tuple?
            # attrs: Tuple[str, ...]=('href',), # Tuple?
            # canonicalize: bool=False,
            # unique: bool=True,
            # process_value: Optional[Callable]=None,
            # strip: bool=True
    ) -> None:
        """

        :param allow:
        :param deny:
        :param allow_domains:
        :param deny_domains:
        :param deny_extensions:
        :param restrict_xpath:
        :param restrict_css:
        :param restrict_regex:
        :param tags:
        :param attrs:
        :param canonicalize:
        :param unique:
        :param process_value:
        :param strip:
        """
        self.allow_regexes = [
            regex if isinstance(regex, Regex) else re.compile(regex)
            for regex in allow
        ]

        self.deny_regexes = [
            regex if isinstance(regex, Regex) else re.compile(regex)
            for regex in deny
        ]

        # TODO: instead of replacing, append?
        if deny_extensions is None:
            deny_extensions = IGNORED_EXTENSIONS
        self.deny_extensions = {f'.{ext}' for ext in deny_extensions}

    def _extract_links(self):
        pass

    # TODO: change type to Link?
    # TODO: implement url filtering, using allow & deny
    def extract_links(self, response: Response) -> List[str]:
        print(f'length: {len(response.body)}')
        tree = html_parser.fromstring(response.body)
        urls = tree.xpath("//a[contains(@href, 'http')]/@href")
        return urls
