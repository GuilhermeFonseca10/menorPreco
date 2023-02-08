from django.views.generic import ListView
from rolepermissions.mixins import HasRoleMixin
from supermercado.models.supermercado import Supermercado

from utils.decorators import LoginRequiredMixin


class DashboardView(HasRoleMixin, LoginRequiredMixin, ListView):
    model = Supermercado
    allowed_roles = "administrador"

    def get_queryset(self):
        usuario = self.request.user

        return Supermercado.objects.filter(usuario=usuario)

    template_name = "core/dashboard.html"
