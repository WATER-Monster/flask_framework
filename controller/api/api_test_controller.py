from flask import g
from controller.api import api
from middleware.josnWebToken.josn_web_token import jwt_wrapper
from middleware.param_check.Bean_check_factory import bean_check_wrapper
from service.api.api_test_service import api_test_service
from utils.response_generator import ResponseGenerator


@api.route('/test', methods=["GET"])
@bean_check_wrapper("API_TEST_BEAN")
# @jwt_wrapper
def api_test():
    status, msg = api_test_service(g.data)
    if status is True:
        return ResponseGenerator.resp_ok(msg)
    else:
        return ResponseGenerator.resp_fail(msg)
