
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth.models import User
from policiesserv.services.auth import AuthServ

# class SessionMiddleware(SessionMiddleware):
#     def process_request(self, request):
#         session_key = request.COOKIES.get("sessionid")
#         if session_key:
#             request.session = self.SessionStore(session_key)
#         else:
#             pass