import redis
from config.constans import REDIS_HOST, REDIS_PORT, REDIS_SET_EX


class Redis_driver:
    def __init__(self):
        pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
        self.conn = redis.StrictRedis(connection_pool=pool)

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    def set(self, key, value, expire=REDIS_SET_EX):
        self.conn.set(name=key, value=value, ex=expire)

    def set_nx(self, key, value, expire=REDIS_SET_EX):
        self.conn.set(name=key, value=value, ex=expire, nx=True)

    def get(self, key):
        return self.conn.get(name=key)

    def delete(self, key):
        self.conn.delete(key)

    def expire(self, key, expire=REDIS_SET_EX):
        self.conn.expire(name=key, time=expire)