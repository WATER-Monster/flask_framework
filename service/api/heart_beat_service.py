import json
import threading
import requests
from gevent.threadpool import ThreadPoolExecutor
from db_driver.mysql_driver import db


def api_hbc_service(data):
    if data.get("user_name") == "admin" and data.get("pwd") == 123:
        return True, "ok", {"u_code":100, "token":123}
    return False, "user_name or pwd wrong", None


def api_login_get(data):

    with db.Transaction() as t:
        t.t_execute("insert into test(name,pwd) values (%s,%s)", 333, 444)
        t.t_execute("update test set name=888 where name=%s", 333)

    return True, "ok", None