from django.views.generic import ListView
from produto.models.categoria import Categoria

from utils.decorators import LoginRequiredMixin


class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria

    template_name = "categoria/categoria_list.html"

    def categoria(self):

        categoria = Categoria.objects.all()

        return categoria
