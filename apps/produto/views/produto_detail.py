from django.shortcuts import render
from django.views.generic import DetailView
from produto.models.produto import Produto

from utils.decorators import LoginRequiredMixin


class ProdutoDetailView(LoginRequiredMixin, DetailView):
    model = Produto

    template_name = "produto/produto_detail.html"

    def supermercado_detail_view(request, id):
        produto = Produto.objects.get(id=id)
        # url = reverse("supermercado_detail", args=(id,))
        context = {"produto": produto}
        return render(request, context)
