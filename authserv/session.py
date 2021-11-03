
from django.contrib.sessions.middleware import SessionMiddleware as DjangoSessionMiddleweare
from django.contrib.auth.models import User
from authserv.clients.auth import AuthServ

class SessionMiddleware(DjangoSessionMiddleweare):
    def process_request(self, request):
        pass