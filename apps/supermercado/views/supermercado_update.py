from django.views.generic import UpdateView
from rolepermissions.mixins import HasRoleMixin
from supermercado.models.supermercado import Supermercado

from utils.decorators import LoginRequiredMixin


class SupermercadoUpdateView(HasRoleMixin, LoginRequiredMixin, UpdateView):
    model = Supermercado
    allowed_roles = "administrador"
    fields = [
        "nome",
        "imagem",
        "cpf",
        "cnpj",
        "cep",
        "cidade",
        "bairro",
        "rua",
        "numero",
        "usuario",
    ]
    success_url = "/dashboard"
