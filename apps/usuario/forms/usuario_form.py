from django.contrib.auth.forms import UserCreationForm

from ..models.usuario import Usuario


class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ["username", "email"]

