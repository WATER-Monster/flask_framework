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
    def __init__(self, param):
        self.param = param

    def create_token(self):
        exp = int(time.time() + TOKEN_EXPIRE_TIME)
        payload = {
            PAYLOAD_PARAM: self.param,
            "exp": exp
        }

        token = jwt.encode(payload=payload, key=SECRET_KEY, algorithm=TOKEN_ALGORITHM, headers=TOKEN_HEADERS).decode(TOKEN_ENCODE_TYPE)
        return token

    def check_token(self, token):
        try:
            info = jwt.decode(token, SECRET_KEY, True, algorithm=TOKEN_ALGORITHM)
        except ExpiredSignatureError: #  token 过期
            return 0
        if info.get(PAYLOAD_PARAM) == self.param: #  验证通过
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

        payload_param = g.get(PAYLOAD_PARAM)

        jwt = JWT(payload_param)
        result = jwt.check_token(token)

        if result == -1:
            return jsonify({'code': 400, 'msg': 'token验证未通过'})
        elif result == 0:
            return jsonify({'code': 400, 'msg': 'token过期，请重新登陆'})
        else:
            res = func(*args,**kwargs)

        return res
    return wrapper