from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
from supermercado.models.supermercado import Supermercado


class SupermercadoDetailView(DetailView):
    model = Supermercado

    def supermercado_detail_view(request, id):
        supermercado = get_object_or_404(Supermercado, supermercado=id)
        return render(
            request,
            "supermercado/supermercado_detail.html",
            context={"supermercado": supermercado},
        )
