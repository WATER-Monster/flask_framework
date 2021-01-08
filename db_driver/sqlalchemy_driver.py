from flask_sqlalchemy import SQLAlchemy
from application import app


class SqlAlchemy_Driver:
    """
    原生的pymysql需要考虑sql注入等问题，也无法做model映射数据库，需要做一些简单有效的查询时，可以使用SqlAlchemy_Driver
    """
    def __init__(self):
        db = SQLAlchemy()
        db.init_app(app)
