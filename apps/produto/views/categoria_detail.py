from django.shortcuts import render
from django.views.generic import DetailView
from produto.models.categoria import Categoria
from rolepermissions.mixins import HasRoleMixin

from utils.decorators import LoginRequiredMixin


class CategoriaDetailView(HasRoleMixin, LoginRequiredMixin, DetailView):
    model = Categoria
    allowed_roles = ["usuario_comum", "administrador"]
    template_name = "categoria/categoria_detail.html"

    def categoria_detail_view(request, id):
        categoria = Categoria.objects.get(id=id)
        # url = reverse("supermercado_detail", args=(id,))
        context = {"categoria": categoria}
        return render(request, context)
