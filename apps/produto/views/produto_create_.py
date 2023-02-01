from django.views.generic import CreateView
from produto.forms.produto_create_form import ProdutoForm

from utils.decorators import LoginRequiredMixin

from ..models.produto import Produto


class ProdutoCreateView(LoginRequiredMixin, CreateView):
    model = Produto

    form_class = ProdutoForm

    success_url = "/"
