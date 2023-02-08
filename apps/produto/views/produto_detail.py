from django.shortcuts import render
from django.views.generic import DetailView
from produto.models.produto import Produto
from utils.decorators import LoginRequiredMixin
from rolepermissions.mixins import HasRoleMixin
class ProdutoDetailView(HasRoleMixin, LoginRequiredMixin, DetailView):
    model = Produto
    allowed_roles = ["usuario_comum", "administrador"]
    template_name = "produto/produto_detail.html"

    def supermercado_detail_view(request, id):
        produto = Produto.objects.get(id=id)
        # url = reverse("supermercado_detail", args=(id,))
        context = {"produto": produto}
        return render(request, context)
