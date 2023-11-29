from aiohttp import ClientSession

from vortex.request import Request
from vortex.response import Response
from vortex.utils.signals import Signal


class Downloader:

    def __init__(self, agent, settings):
        self.agent = agent
        self.settings = settings

        # Signals
        self.response_received = Signal()

    async def fetch(self, request: Request):
        client_session = ClientSession()
        resp = await client_session.get(request.url)

        # Construct Response from aiohttp.Response
        response = Response(
            url=resp.url,
            headers=resp.headers,
            body=await resp.text(),
            request=request
        )

        # Emit signal & send data
        await self.response_received.emit(response)

        await client_session.close()
