"""

"""
from typing import AnyStr

from aiohttp import ClientSession


class Request:

    def __init__(
            self,
            url: str,
            method: AnyStr = 'GET',
            client_session: ClientSession = None
    ):
        """
        Request Initialization Parameters

        :param url:
        :param method:
        :param client_session:
        """
        self.url = url
        self.method = method
        self.client_session = client_session
