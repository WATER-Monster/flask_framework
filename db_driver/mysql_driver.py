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

    def fetchone(self, sql):
        conn, cursor = self._connect()
        cursor.execute(sql)
        result = cursor.fetchone()
        self.connect_close(conn, cursor)
        return result

    def fetchall(self, sql):
        conn, cursor = self._connect()
        cursor.execute(sql)
        result = cursor.fetchall()
        self.connect_close(conn, cursor)
        return result

    def execute_one(self, sql):
        conn, cursor = self._connect()
        try:
            cursor.execute_one(sql)
            conn.commit()
        except Base_Exception:
            conn.rollback()
            self.connect_close(conn, cursor)
            return False
        self.connect_close(conn, cursor)
        return True

    def begin(self):
        """
        事务开始
        实际上pymysql一直都是autocommit(0)，所以写个begin在代码层面上没有意义
        但在结构层面可以标志这是一个事务，便于代码理解
        :return: conn, cursor 使用begin开始的事务，使用cursor.execute()执行sql
        """
        conn, cursor = self._connect()
        return conn, cursor

    def end(self, conn, cursor):
        """
        事务结束
        :return:
        """
        try:
            conn.commit()
        except Exception:
            conn.rollback()
            self.connect_close(conn, cursor)

db = Mysql_Driver()