from django.views.generic import ListView
from promocao.models.promocao import Promocao
from utils.decorators import LoginRequiredMixin
from rolepermissions.mixins import HasRoleMixin

class PromocaoListView(HasRoleMixin, LoginRequiredMixin, ListView):
    model = Promocao
    allowed_roles = ["usuario_comum", "administrador"]
    template_name = "promocao/promocao_list.html"

    def promocao(self):

        promocao = Promocao.objects.all()

        return promocao
