from django.views.generic import ListView
from supermercado.models.supermercado import Supermercado

from utils.decorators import LoginRequiredMixin


class SupermercadoListView(LoginRequiredMixin, ListView):
    model = Supermercado

    def get_queryset(self):

        super = Supermercado.objects.all()

        return super
