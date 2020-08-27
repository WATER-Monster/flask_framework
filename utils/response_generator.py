from flask import jsonify


class ResponseGenerator:

    @staticmethod
    def resp_ok(msg="ok", data=None):
        response = dict()
        response["code"] = 200
        response["msg"] = msg
        if data is not None:
            response["data"] = data
        return jsonify(response)

    @staticmethod
    def resp_fail(msg="fail", data=None):
        response = dict()
        response["code"] = 400
        response["msg"] = msg
        if data is not None:
            response["data"] = data
        return jsonify(response)

