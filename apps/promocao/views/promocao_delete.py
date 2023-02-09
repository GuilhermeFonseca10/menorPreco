from django.views.generic import DeleteView
from promocao.models.promocao import Promocao
from rolepermissions.mixins import HasRoleMixin

from utils.decorators import LoginRequiredMixin


class PromocaoDeleteView(HasRoleMixin, LoginRequiredMixin, DeleteView):
    model = Promocao
    allowed_roles = "administrador"
    template_name = "promocao/promocao_confirm_delete.html"
    success_url = "/dashboard"
