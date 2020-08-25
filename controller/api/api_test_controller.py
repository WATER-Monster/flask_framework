from application import app
from middleware.josnWebToken.josn_web_token import jwt_wrapper
from service.api.api_test_service import *
from utils.Bean_check_factory import bean_check_wrapper


@app.route('/test')
@bean_check_wrapper("API_TEST_BEAN")
@jwt_wrapper
def api_test():
    return
