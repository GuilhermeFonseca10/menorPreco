from django.views.generic import ListView
from rolepermissions.mixins import HasRoleMixin
from supermercado.models.supermercado import Supermercado

from utils.decorators import LoginRequiredMixin


class SupermercadoListView(HasRoleMixin, LoginRequiredMixin, ListView):
    model = Supermercado
    allowed_roles = ["usuario_comum", "administrador"]

    def supermercado(self):

        super = Supermercado.objects.all()

        return super
