import json
import threading
import requests
from gevent.threadpool import ThreadPoolExecutor

# pool = ThreadPoolExecutor(max_workers=10)


def api_hbc_service(data):
    if data.get("user_name") == "admin" and data.get("pwd") == 123:
        return True, "ok", {"code":100, "token":123}
    return False, "user_name or pwd wrong", None


def api_login_get(data):
    if data.get("user_name") == "admin" and data.get("pwd") == "123":
        return True, "ok", {"code":100, "token":123}
    return False, "user_name or pwd wrong", None