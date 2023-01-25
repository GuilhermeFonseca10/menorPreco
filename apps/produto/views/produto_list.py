from django.views.generic import ListView
from produto.models.produto import Produto


class ProdutoListView(ListView):
    model = Produto

    def supermercado(self):

        produto = Produto.objects.all()

        return produto
