from django.views.generic import UpdateView
from supermercado.models.supermercado import Supermercado

from utils.decorators import LoginRequiredMixin


class SupermercadoUpdateView(LoginRequiredMixin, UpdateView):
    model = Supermercado
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
