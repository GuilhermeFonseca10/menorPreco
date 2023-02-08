from django.shortcuts import render
from django.views.generic import DetailView
from promocao.models.promocao import Promocao
from rolepermissions.mixins import HasRoleMixin

from utils.decorators import LoginRequiredMixin


class PromocaoAdminDetailView(HasRoleMixin, LoginRequiredMixin, DetailView):
    model = Promocao
    allowed_roles = "administrador"
    template_name = "promocao/promocao_detail_admin.html"

    def promocao_detail_view(request, id):
        promocao = Promocao.objects.get(id=id)
        # url = reverse("supermercado_detail", args=(id,))
        context = {"promocao": promocao}
        return render(request, context)
