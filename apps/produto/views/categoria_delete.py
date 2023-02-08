from django.views.generic import DeleteView
from produto.models.categoria import Categoria

from utils.decorators import LoginRequiredMixin


class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = "categoria/categoria_confirm_delete.html"
    success_url = "/dashboard"
