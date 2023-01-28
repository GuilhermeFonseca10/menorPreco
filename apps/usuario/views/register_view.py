from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView
from usuario.forms.usuario_form import UsuarioCreationForm

User = get_user_model()


class RegisterView(CreateView):
    model = User

    form_class = UsuarioCreationForm
    template_name = "usuario/register.html"
    success_url = reverse_lazy("dashboard")
