from flask import request
from flask_restful import Resource
from controllers.authentication_controller import AuthenticationController


class Authentication(Resource):

    def post(self):
        auth = AuthenticationController()
        payload = request.get_json()
        result = auth.authenticate(payload)
        if result['response'] is False:
            return result, 401
        return result, 200