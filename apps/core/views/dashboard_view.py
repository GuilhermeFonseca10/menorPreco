from django.views.generic import ListView
from supermercado.models.supermercado import Supermercado

from utils.decorators import LoginRequiredMixin


class DashboardView(LoginRequiredMixin, ListView):
    model = Supermercado

    def get_queryset(self):
        usuario = self.request.user

        return Supermercado.objects.filter(usuario=usuario)

    template_name = "core/dashboard.html"
