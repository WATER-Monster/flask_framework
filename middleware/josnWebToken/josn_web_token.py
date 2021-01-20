import functools
import jwt
import time
from flask import request, jsonify, g
from jwt import ExpiredSignatureError
from config.constans import SECRET_KEY, TOKEN_EXPIRE_TIME, TOKEN_ALGORITHM, TOKEN_HEADERS, TOKEN_ENCODE_TYPE, \
    PAYLOAD_PARAM, TOKEN_NAME


class JWT:
    """
    JWT生成以及check
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    @staticmethod
    def create_token(param):
        exp = int(time.time() + TOKEN_EXPIRE_TIME)
        payload = {
            PAYLOAD_PARAM: param,
            "exp": exp
        }

        token = jwt.encode(payload=payload, key=SECRET_KEY, algorithm=TOKEN_ALGORITHM, headers=TOKEN_HEADERS).decode(TOKEN_ENCODE_TYPE)
        return token

    @staticmethod
    def check_token(token, param):
        try:
            info = jwt.decode(token, SECRET_KEY, True, algorithm=TOKEN_ALGORITHM)
        except ExpiredSignatureError: #  token 过期
            return 0
        if info.get(PAYLOAD_PARAM) == param: #  验证通过
            return 1
        else:
            return -1


def jwt_wrapper(func):
    """
    jwt 装饰器
    :return:
    """
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        token = request.headers.get(TOKEN_NAME)

        param_value = g.get(PAYLOAD_PARAM)

        jwt_instance = JWT()
        result = jwt_instance.check_token(token, param_value)

        if result == -1:
            return jsonify({'code': 400, 'msg': 'token验证未通过'})
        elif result == 0:
            return jsonify({'code': 400, 'msg': 'token过期，请重新登陆'})
        else:
            res = func(*args,**kwargs)

        return res
    return wrapper