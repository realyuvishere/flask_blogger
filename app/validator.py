from werkzeug.exceptions import HTTPException
from flask import make_response
import json

class ValidationError(HTTPException):
    def __init__(self, status_code=400, error_message=''):
        data = { "code" : status_code, "message": error_message }
        self.response = make_response(json.dumps(data), status_code)

class NotFoundError(HTTPException):
    def __init__(self, status_code=404, error_message=''):
        data = {'code': status_code, 'message': error_message}
        self.response = make_response(json.dumps(data), status_code)