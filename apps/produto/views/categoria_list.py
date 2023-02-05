from django.views.generic import ListView
from produto.models.categoria import Categoria


class CategoriaListView(ListView):
    model = Categoria
    template_name = "categoria/categoria_list.html"

    def supermercado(self):

        categoria = Categoria.objects.all()

        return categoria
