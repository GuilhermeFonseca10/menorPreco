from django.shortcuts import render
from django.views.generic import DetailView
from promocao.models.promocao import Promocao


class PromocaoDetailView(DetailView):
    model = Promocao
    template_name = "promocao/promocao_detail.html"

    def promocao_detail_view(request, id):
        promocao = Promocao.objects.get(id=id)
        # url = reverse("supermercado_detail", args=(id,))
        context = {"promocao": promocao}
        return render(request, context)
