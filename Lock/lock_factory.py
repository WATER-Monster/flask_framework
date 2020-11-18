from Lock.mysql_lock.sql_lock import Mysql_lock
from db_driver.mysql_driver import Mysql_Driver
from db_driver.redis_driver import Redis_driver
from redis.exceptions import ConnectionError
import redis_lock


class Lock_Factory:
    def __init__(self, lock_name):
        try:
            #  TODO 证明redis service 不可用，才会降级使用sql-lock。但怎么证明不可用，一次访问失败就证明不可用吗？
            _redis = Redis_driver()
            self._lock = redis_lock.Lock(_redis.conn, lock_name)
        except ConnectionError:
            #  TODO mysql-lock 应在sql语句中使用 for update 控制加锁，难以抽象出来
            _mysql = Mysql_Driver()
            self._lock = Mysql_lock(_mysql, lock_name)

    def get_lock(self):
        return self._lock