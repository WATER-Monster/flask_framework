"""
此处可替换为开源库 python-redis-lock
"""

import os
import threading
import time
from db_driver.redis_driver import Redis_driver


class Redission:
    def __init__(self):
        self.redis = Redis_driver()
        self.pid = os.getpid()

    def lock(self, key, value, expire=30):
        is_lock = self.redis.get(key)
        if is_lock:
            while True:
                pass
        v = {"pid": self.pid, "value": value}
        self.redis.set_nx(key, v, expire)
        return 1

    def release(self, key):
        value = self.redis.get(key)
        if value.get("pid") == self.pid:
            self.redis.delete(key)
            return 1
        else:
            return -1

    def extend_lock_time(self, key):
        t = threading.Thread(target=self.watch_dog, kwargs={"key":key})
        t.start()

    def watch_dog(self, key):
        while True:
            is_lock = self.redis.get(key)
            if is_lock:
                self.redis.expire(key, 10)
            else:
                break
            time.sleep(10)