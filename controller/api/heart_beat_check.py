from flask import g
from controller.api import api
from middleware.param_check.Bean_check_factory import bean_check_wrapper
from service.api.heart_beat_service import api_hbc_service
from utils.response_generator import ResponseGenerator


@api.route('/heartBeatCheck', methods=["POST"])
@bean_check_wrapper("API_HBC_BEAN")
def heart_beat_check():
    status, msg, data = api_hbc_service(g.data)
    return ResponseGenerator.make_response(status, msg, data)