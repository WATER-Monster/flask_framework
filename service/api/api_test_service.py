import redis_lock
from db_driver.redis_driver import Redis_driver


def api_test_service(data):
    redis = Redis_driver()

    lock = redis_lock.Lock(redis.conn, "test-lock")
    # # 悲观锁
    # if lock.acquire(blocking=True,timeout=30):
    #     val = redis.get("test")
    #     if val is None:
    #         val = 0
    #     val = int(val)
    #     if val >= 10:
    #         lock.release()
    #         return True, "sold out"
    #     redis.set("test", value=str(val+1), expire=120)
    #     lock.release()
    #
    #     return True, "ok"
    # else:
    #     return False, "time out"

    # 乐观锁 在并发抢购的模式中，乐观锁确实优秀些
    val = redis.get("test")
    if val is None:
        val = 0
    val = int(val)
    if val >= 10:
        return True, "sold out case 1"
    if lock.acquire(blocking=True, timeout=30):
        val = redis.get("test")
        if val is None:
            val = 0
        val = int(val)
        if val < 10:
            redis.set("test", value=str(val+1), expire=120)
        else:
            lock.release()
            return True, "sold out case 2"
        lock.release()

    return True, "ok"