from django.urls import path
from produto import viewsets
from produto.views.categoria_create import CategoriaCreateView
from produto.views.categoria_delete import CategoriaDeleteView
from produto.views.categoria_detail import CategoriaDetailView
from produto.views.categoria_detail_admin import CategoriaAdminDetailView
from produto.views.categoria_list import CategoriaListView
from produto.views.categoria_update import CategoriaUpdateView
from produto.views.produto_create_ import ProdutoCreateView
from produto.views.produto_delete import ProdutoDeleteView
from produto.views.produto_detail import ProdutoDetailView
from produto.views.produto_update import ProdutoUpdateView
from rest_framework import routers

produto_router = routers.DefaultRouter()
produto_router.register(
    "api_produtos",
    viewsets.ProdutoViewSet,
    basename="produtos_api",
)

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
        "delete/<int:pk>/",
        ProdutoDeleteView.as_view(),
        name="produto_delete",
    ),
    # categoria
    path(
        "categoria_cad",
        CategoriaCreateView.as_view(),
        name="categoria_create",
    ),
    path(
        "categoria_list",
        CategoriaListView.as_view(),
        name="categoria_list",
    ),
    path(
        "categoria_detail/<int:pk>/",
        CategoriaDetailView.as_view(),
        name="categoria_detail",
    ),
    path(
        "categoria_detail_admin/<int:pk>/",
        CategoriaAdminDetailView.as_view(),
        name="categoria_detail_admin",
    ),
    path(
        "categoria_update/<int:pk>/",
        CategoriaUpdateView.as_view(),
        name="categoria_update",
    ),
    path(
        "categoria_delete/<int:pk>/",
        CategoriaDeleteView.as_view(),
        name="categoria_delete",
    ),
] + produto_router.urls
