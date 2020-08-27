import pymysql
from DBUtils.PooledDB import PooledDB
from config.constans import MAXCONNECTIONS, MINCACHED, MAXCACHED, MAXSHARED, BLOCKING, MAXUSAGE, SETSESSION, PING, \
    MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE, MYSQL_CHARSET
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
        :param args:
        :param kw:
        :return: cls._instance
        """
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    def connect(self):
        """
        启动连接
        :return:conn, cursor
        """
        conn = self.POOL.connection()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        return conn, cursor

    def connect_close(self,conn, cursor):
        """
        关闭连接
        :param conn:
        :param cursor:
        :return: None
        """
        cursor.close()
        conn.close()

    def fetchone(self, sql):
        conn, cursor = self.connect()
        cursor.execute(sql)
        result = cursor.fetchone()
        self.connect_close(conn, cursor)
        return result

    def fetchall(self, sql):
        conn, cursor = self.connect()
        cursor.execute(sql)
        result = cursor.fetchall()
        self.connect_close(conn, cursor)
        return result

    def execute(self, sql):
        conn, cursor = self.connect()
        cursor.execute(sql)
        try:
            cursor.commit()
        except Base_Exception:
            conn.rollback()
            return False
        self.connect_close(conn, cursor)
        return True
