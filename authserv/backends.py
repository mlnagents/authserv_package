
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from authserv.clients.auth import AuthServ

# class AuthenticationBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, token=None, **kwargs):
#         print(request.COOKIES)
#         auth_result = AuthServ().auth(username, password)

#         if auth_result is None:
#             return None

#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             user = User(username=username)
#             user.is_staff = True
#             user.save()
#         return user

class ValidateTokenBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, token=None, **kwargs):
        print(request.COOKIES)
        authserv_token = request.COOKIES.get("authserv_token")
        if authserv_token is None:
            return None

        auth_result = AuthServ().session(authserv_token)
        if auth_result is None:
            return None

        try:
            user = User.objects.get(username=auth_result['phone'])
        except User.DoesNotExist:
            user = User(username=auth_result['phone'])
            user.is_staff = True
            user.is_superuser = True

            user.save()
        return user