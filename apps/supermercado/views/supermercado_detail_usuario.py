from django.shortcuts import render
from django.views.generic import DetailView
from supermercado.models.supermercado import Supermercado

from utils.decorators import LoginRequiredMixin


class SupermercadoUsuarioDetailView(LoginRequiredMixin, DetailView):
    model = Supermercado

    template_name = "supermercado/supermercado_detail_usuario.html"

    def supermercado_detail_usuario_view(request, id):
        supermercados = Supermercado.objects.get(id=id)
        # url = reverse("supermercado_detail", args=(id,))
        context = {"supermercados": supermercados}
        return render(request, context)
