import json
import threading
import requests
from gevent.threadpool import ThreadPoolExecutor

# pool = ThreadPoolExecutor(max_workers=10)


def api_hbc_service(data):
    url = data.get("url")
    param = data.get("param")
    method = data.get("method").lower()
    content_type = data.get("Content-Type")

    req = getattr(requests, method, None)
    if req is None:
        return "method not allowed"

    if content_type == "application/json":
        param = json.dumps(param)

    # requests模块会把dict类型的参数自动转换为get或post类型的参数
    t = threading.Thread(target=req)
    t.start()
    # future_res = pool.submit(req, (url, param))
    # future_res.add_done_callback(lambda future:print(future.result()))

    return True, "ok", None
