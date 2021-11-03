import requests
import json
from django.conf import settings


class AuthServ:
    api_path = "api/v1"
    headers = {"X-Token": settings.AUTHSERV_TOKEN, "Content-Type": "application/json"}

    def auth(self, username, password):
        resp = requests.post(
            url=f"{settings.AUTHSERV_HOST}/{self.api_path}/auth", data=json.dumps({
                "phone": username,
                "password": password,
                "service": "policiesserv"
            }), headers=self.headers
        )
        print(resp.text)
        if resp.status_code != 200:
            return None
        else:
            return resp.json()

    def session(self, token):
        resp = requests.get(
            url=f"{settings.AUTHSERV_HOST}/{self.api_path}/session?token={token}", headers=self.headers
        )
        print(resp.text)
        if resp.status_code != 200:
            return None
        else:
            return resp.json()