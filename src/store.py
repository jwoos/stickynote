import redis

from src.conf import REDIS
from src.utils import hash


redis_client = redis.StrictRedis(**REDIS)
