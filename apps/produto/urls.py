from django.urls import path
from produto.views.produto_create_ import ProdutoCreateView
from produto.views.produto_detail import ProdutoDetailView
from produto.views.produto_list_admin import ProdutoListAdminView
from produto.views.produto_update import ProdutoUpdateView

urlpatterns = [
    path("cad", ProdutoCreateView.as_view(), name="produto_create"),
    path(
        "detail/<int:pk>/",
        ProdutoDetailView.as_view(),
        name="produto_detail",
    ),
    path(
        "update/<int:pk>/",
        ProdutoUpdateView.as_view(),
        name="produto_update",
    ),
    path(
        "listadmin",
        ProdutoListAdminView.as_view(),
        name="produto_list_admin",
    ),
]
