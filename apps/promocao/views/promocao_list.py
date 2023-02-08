from django.views.generic import ListView
from promocao.models.promocao import Promocao
from rolepermissions.mixins import HasRoleMixin

from utils.decorators import LoginRequiredMixin


class PromocaoListView(HasRoleMixin, LoginRequiredMixin, ListView):
    model = Promocao
    allowed_roles = ["usuario_comum", "administrador"]
    template_name = "promocao/promocao_list.html"

    def promocao(self):

        promocao = Promocao.objects.all()

        return promocao
