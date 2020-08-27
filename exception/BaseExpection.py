from flask import jsonify
from fralog.FraLog import LogModule
from utils.response_generator import ResponseGenerator

log = LogModule()


class Base_Exception(Exception):
    def __init__(self, message=None):
        self.message = message
        super(Base_Exception, self).__init__(message)
        self._log_exception()

    def _log_exception(self):
        log.error(self.message)

    # def response_error(self):
    #     response = ResponseGenerator.resp_fail(self.message)
    #     return response