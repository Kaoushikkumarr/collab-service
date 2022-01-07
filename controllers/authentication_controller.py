import json


class AuthenticationController:

    def __init__(self):
        from app import app
        self.requests = app.config['REQUESTS'].req
        self.platform_url = app.config['PLATFORM_AUTH_URL']
        self.headers = app.config['JSON_REQUEST_HEADERS']

    def authenticate(self, payload):
        results = self.requests.post(str(self.platform_url), data=json.dumps(payload), headers=self.headers)
        return results.json()
