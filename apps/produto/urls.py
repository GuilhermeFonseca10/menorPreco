from django.urls import path
from produto.views.produto_create_ import ProdutoCreateView

urlpatterns = [
    path("cad", ProdutoCreateView.as_view(), name="produto_create"),
]
