
from django.contrib.auth.backends import ModelBackend, RemoteUserBackend
from django.contrib.auth.models import User
from authserv.clients.auth import AuthServ

class AuthservUserBackend(RemoteUserBackend):
    def configure_user(self, request, user):
        """
        Configure a user after creation and return the updated user.

        By default, return the user unmodified.
        """
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user
    
    def user_can_authenticate(self, user):
        return True


class AuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        auth_result = AuthServ().auth(username, password)
        if auth_result is None:
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User(username=username)
            user.is_staff = True
            user.save()
        return user