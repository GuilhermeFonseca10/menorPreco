from django.urls import reverse_lazy
from django.views.generic import DeleteView
from produto.models.produto import Produto

from utils.decorators import LoginRequiredMixin


class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    model = Produto

    success_url = "/dashboard"
