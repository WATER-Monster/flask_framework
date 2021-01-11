class Mysql_lock:
    """
    在redis-lock无法使用时使用此锁。
    更新: 要做MySQL锁自己去写 for update ，自己优化
    """
    def __init__(self, db_conn, lock_name):
        self._db_conn = db_conn
        self._lock_name = lock_name

    def acquire(self, blocking=True, timeout=None):
        pass

    def release(self):
        pass
