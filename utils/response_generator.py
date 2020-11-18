from flask import jsonify


class ResponseGenerator:
    @staticmethod
    def make_response(status, msg, data):
        if status:
            return ResponseGenerator._resp_ok(msg, [data])
        else:
            return ResponseGenerator._resp_fail(msg, [data])

    @staticmethod
    def _resp_ok(msg="ok", data=None):
        response = dict()
        response["code"] = 200
        response["msg"] = msg
        if data is not None:
            response["data"] = data
        return jsonify(response)

    @staticmethod
    def _resp_fail(msg="fail", data=None):
        response = dict()
        response["code"] = 400
        response["msg"] = msg
        if data is not None:
            response["data"] = data
        return jsonify(response), 400

