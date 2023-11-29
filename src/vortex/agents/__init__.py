"""
Base Agent Class
"""


class Agent:
    # Agent name
    name = None

    # Custom settings
    custom_settings = {}

    def __init__(self):
        pass

    async def run(self):
        raise NotImplementedError
