from django.shortcuts import render
from django.views.generic import DetailView
from supermercado.models.supermercado import Supermercado
from rolepermissions.mixins import HasRoleMixin
from utils.decorators import LoginRequiredMixin


class SupermercadoPromocaoView(HasRoleMixin, LoginRequiredMixin, DetailView):
    model = Supermercado
    allowed_roles = "administrador"
    template_name = "supermercado/supermercado_detail_promocao.html"

    def supermercado_detail_view(request, id):
        supermercado = Supermercado.objects.get(id=id)
        # url = reverse("supermercado_detail", args=(id,))
        context = {"supermercado": supermercado}
        return render(request, context)
