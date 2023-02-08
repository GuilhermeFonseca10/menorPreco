from django.views.generic import ListView
from produto.models.categoria import Categoria
from rolepermissions.mixins import HasRoleMixin

from utils.decorators import LoginRequiredMixin


class CategoriaListView(HasRoleMixin, LoginRequiredMixin, ListView):
    model = Categoria
    allow_empty = ["usuario_comum", "administrador"]
    template_name = "categoria/categoria_list.html"

    def categoria(self):

        categoria = Categoria.objects.all()

        return categoria
