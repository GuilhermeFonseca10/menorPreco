from django.urls import reverse_lazy
from django.views.generic import UpdateView
from produto.models.produto import Produto
from rolepermissions.mixins import HasRoleMixin

from utils.decorators import LoginRequiredMixin


class ProdutoUpdateView(HasRoleMixin, LoginRequiredMixin, UpdateView):
    model = Produto
    allowed_roles = "administrador"
    fields = [
        "nome",
        "imagem",
        "valor",
        "estoque",
        "descricao",
        "categorias",
        "supermercados",
    ]
    success_url = reverse_lazy("supermercado_detail")

    def get_success_url(self):
        return reverse_lazy("supermercado_detail", args=(self.object.pk,))
