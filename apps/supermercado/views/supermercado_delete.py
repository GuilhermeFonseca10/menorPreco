from django.views.generic import DeleteView
from supermercado.models.supermercado import Supermercado

from utils.decorators import LoginRequiredMixin


class SupermercadoDeleteView(LoginRequiredMixin, DeleteView):
    model = Supermercado
    success_url = "/dashboard"
