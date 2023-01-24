from django.views.generic import ListView
from supermercado.models.supermercado import Supermercado


class SupermercadoListView(ListView):
    model = Supermercado

    def supermercado(self):

        super = Supermercado.objects.all()

        return super
