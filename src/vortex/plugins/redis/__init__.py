from vortex.plugins.redis.main import RedisPlugin
from vortex.settings import Settings


def create(settings: Settings):
    return RedisPlugin(settings)
