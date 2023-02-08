from django.views.generic import DeleteView
from rolepermissions.mixins import HasRoleMixin
from supermercado.models.supermercado import Supermercado

from utils.decorators import LoginRequiredMixin


class SupermercadoDeleteView(HasRoleMixin, LoginRequiredMixin, DeleteView):
    model = Supermercado
    allowed_roles = "administrador"
    success_url = "/dashboard"
