from django.urls import path
from produto.views.produto_list import ProdutoListView

urlpatterns = [
    path("list", ProdutoListView.as_view(), name="produto_list"),
]
