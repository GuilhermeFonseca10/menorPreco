from django.shortcuts import render
from django.views.generic import DetailView
from supermercado.models.supermercado import Supermercado


class SupermercadoDetailView(DetailView):
    model = Supermercado
    template_name = "supermercado/supermercado_detail.html"

    def supermercado_detail_view(request, id):
        supermercado = Supermercado.objects.get(id=id)
        # url = reverse("supermercado_detail", args=(id,))
        context = {"supermercado": supermercado}
        return render(request, context)