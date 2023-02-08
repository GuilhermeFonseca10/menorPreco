from django.views.generic import DeleteView
from produto.models.produto import Produto
from rolepermissions.mixins import HasRoleMixin
from utils.decorators import LoginRequiredMixin


class ProdutoDeleteView(HasRoleMixin, LoginRequiredMixin, DeleteView):
    model = Produto
    allowed_roles = "administrador"


    success_url = "/dashboard"
