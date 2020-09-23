import redis_lock
from db_driver.redis_driver import Redis_driver


def api_test_service(data):
    redis = Redis_driver()

    lock = redis_lock.Lock(redis.conn, "test-lock")
    if lock.acquire(blocking=True,timeout=30):
        val = redis.get("test")
        if val is None:
            val = 0
        val = int(val)
        if val >= 10:
            lock.release()
            return True, "sold out"
        redis.set("test", value=str(val+1), expire=120)
        lock.release()

        return True, "ok"
    else:
        return False, "time out"