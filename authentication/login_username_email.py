from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


class LoginUsernameEmail(ModelBackend):
    def authenticate(self, request, **kwargs):
        try:
            user = get_user_model().objects.get(
                Q(username=kwargs["username"]) | Q(email=kwargs["username"])
            )
            return user if user.check_password(kwargs["password"]) else None
        except:
            return None
