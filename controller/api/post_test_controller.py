from flask import g
from controller.api import api
from middleware.josnWebToken.josn_web_token import jwt_wrapper
from middleware.param_check.Bean_check_factory import bean_check_wrapper
from service.api.api_post_service import api_post_service
from utils.response_generator import ResponseGenerator


@api.route('/post', methods=["POST"])
@bean_check_wrapper("API_POST_BEAN")
# @jwt_wrapper
def api_post():
    status, msg, data = api_post_service(g.data)
    return ResponseGenerator.make_response(status, msg, data)