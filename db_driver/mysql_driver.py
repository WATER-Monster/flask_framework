import pymysql
from dbutils.pooled_db import PooledDB
from config.constans import *
from exception.BaseExpection import Base_Exception


class Mysql_Driver:
    def __init__(self):
        self.POOL = PooledDB(
            creator=pymysql,  # 使用链接数据库的模块
            maxconnections=MAXCONNECTIONS,
            mincached=MINCACHED,
            maxcached=MAXCACHED,
            maxshared=MAXSHARED,
            blocking=BLOCKING,
            maxusage=MAXUSAGE,
            setsession=SETSESSION,
            ping=PING,
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE,
            charset=MYSQL_CHARSET
        )
    def __new__(cls, *args, **kw):
        """
        启用单例模式
        """
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    def _connect(self):
        conn = self.POOL.connection()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        return conn, cursor

    @staticmethod
    def connect_close(conn, cursor):
        cursor.close()
        conn.close()

    def fetchone(self, sql, *param):
        """
        所有execute执行的时候都必须把参数挂在execute函数的第二个参数里，而不是自己拼接字符串
        为的是防止sql注入
        :param sql:
        :return:
        """
        conn, cursor = self._connect()
        cursor.execute(sql, param)
        result = cursor.fetchone()
        self.connect_close(conn, cursor)
        return result

    def fetchall(self, sql, *param):
        conn, cursor = self._connect()
        cursor.execute(sql, param)
        result = cursor.fetchall()
        self.connect_close(conn, cursor)
        return result

    def execute_one(self, sql, *param):
        conn, cursor = self._connect()
        try:
            cursor.execute(sql, param)
            conn.commit()
        except Base_Exception:
            conn.rollback()
            self.connect_close(conn, cursor)
            return False
        self.connect_close(conn, cursor)
        return True

    def execute_without_commit(self, sql, *param):
        conn, cursor = self._connect()
        cursor.execute(sql, param)

    class Transaction:
        """
        事务开关，使用方式 with Transaction() as t:
        """
        def __enter__(self):
            db_instance = Mysql_Driver()
            self.conn, self.cursor = db_instance._connect()
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            try:
                if exc_type:
                    raise exc_type
                self.conn.commit()
            except Exception:
                self.conn.rollback()
            finally:
                Mysql_Driver.connect_close(self.conn, self.cursor)

        def t_execute(self, sql, *param):
            self.cursor.execute(sql, param)

db = Mysql_Driver()