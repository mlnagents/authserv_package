import requests
import json
from django.conf import settings


class AuthServ:
    api_path = "api/v1"
    headers = {"X-Token": settings.AUTHSERV_TOKEN, "Content-Type": "application/json"}

    def auth(self, username, password, user_agent=None, ip=None):
        resp = requests.post(
            url=f"{settings.AUTHSERV_HOST}/{self.api_path}/auth", data=json.dumps({
                "username": username,
                "password": password,
                "user_agent": user_agent,
                "ip": ip
            }), headers=self.headers
        )
        return {"status": resp.status_code, "body": resp.json()}

    def auth_session(self, token):
        resp = requests.get(
            url=f"{settings.AUTHSERV_HOST}/{self.api_path}/session?token={token}&service={settings.AUTHSERV_SERVICE_NAME}", headers=self.headers
        )
        return {"status": resp.status_code, "body": resp.json()}