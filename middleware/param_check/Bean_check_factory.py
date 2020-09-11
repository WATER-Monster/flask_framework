import json
import functools
from flask import request, g
from controller.param_check_beans import beans
from utils.response_generator import ResponseGenerator


def check_params(bean):

    if request.method == "GET":
        req = request.values
        msg = bean_param_check(req, bean)
        return msg

    elif request.method == "POST" and request.headers.get("Content-Type") == "application/json":
        req = request.get_data()
        req = json.loads(req)
        msg = bean_param_check(req, bean)
        return msg

    elif request.method == "POST" and request.headers.get("Content-Type") == "application/x-www-form-urlencoded":
        req = request.values
        msg = bean_param_check(req, bean)
        return msg

    else:
        return "content-type illegal"


def bean_param_check(req, bean):
    g.data = dict()
    for param in bean:
        if isinstance(req.get(param), bean.get(param)):
            g.data[param] = req.get(param)
        else:
            return f"{param}'s type should be {bean.get(param)}, not {type(req.get(param))}"

    return 1

#  带参装饰器
def bean_check_wrapper(bean_name):
    def middle(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            bean = getattr(beans, bean_name)
            pc = check_params(bean)
            if pc != 1:
                response = ResponseGenerator.resp_fail(pc)
                return response
            res = func(*args, **kwargs)
            return res

        return wrapper
    return middle
