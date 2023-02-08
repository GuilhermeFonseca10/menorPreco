from django.views.generic import CreateView
from produto.forms.produto_create_form import ProdutoForm
from rolepermissions.mixins import HasRoleMixin
from utils.decorators import LoginRequiredMixin

from ..models.produto import Produto


class ProdutoCreateView(HasRoleMixin, LoginRequiredMixin, CreateView):
    model = Produto
    allowed_roles = "administrador"
    form_class = ProdutoForm

    success_url = "/"
