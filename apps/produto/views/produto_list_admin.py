from django.views.generic import ListView
from produto.models.produto import Produto


class ProdutoListAdminView(ListView):
    model = Produto
    template_name = "produto/produto_list_admin.html"
