
from django.conf import settings
from django.contrib.auth.middleware import RemoteUserMiddleware
from django.http import HttpResponseRedirect
from authserv.clients.auth import AuthServ

class AuthservMiddleware(RemoteUserMiddleware):
    header = "AUTHSERV_USER"

    response_redirect_class = HttpResponseRedirect

    def process_request(self, request):
        if request.path.startswith(settings.STATIC_URL):
            return super().process_request(request)

        authserv_token = request.COOKIES.get("authserv_token")
        auth_result = AuthServ().auth_session(authserv_token)

        print(auth_result)
        if auth_result["status"] is not 200:
            if auth_result["status"] == 401:
                self._remove_invalid_user(request)
                return self.response_redirect_class(f"{auth_result['body']['redirect_url']}?redirect_url={request.build_absolute_uri()}")
            if auth_result["status"] == 403:
                self._remove_invalid_user(request)
                return self.response_redirect_class(f"{auth_result['body']['redirect_url']}")
            

        request.META[self.header] = auth_result["body"]['username']
        super().process_request(request)
