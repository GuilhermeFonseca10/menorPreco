from django.urls import path

from .views.supermercado_create import SupermercadoCreateView
from .views.supermercado_delete import SupermercadoDeleteView
from .views.supermercado_detail import SupermercadoDetailView
from .views.supermercado_detail_categoria import SupermercadoCategoriaView
from .views.supermercado_detail_promocao import SupermercadoPromocaoView
from .views.supermercado_detail_usuario import SupermercadoUsuarioDetailView
from .views.supermercado_list import SupermercadoListView
from .views.supermercado_update import SupermercadoUpdateView

urlpatterns = [
    path("list", SupermercadoListView.as_view(), name="supermercado_list"),
    path("cad", SupermercadoCreateView.as_view(), name="supermercado_create"),
    path(
        "update/<int:pk>/",
        SupermercadoUpdateView.as_view(),
        name="supermercado_update",
    ),
    path(
        "detail/<int:pk>/",
        SupermercadoDetailView.as_view(),
        name="supermercado_detail",
    ),
    path(
        "delete/<int:pk>/",
        SupermercadoDeleteView.as_view(),
        name="supermercado_delete",
    ),
    path(
        "detailusuario/<int:pk>/",
        SupermercadoUsuarioDetailView.as_view(),
        name="supermercado_detail_usuario",
    ),
    path(
        "supermercado_categoria/<int:pk>/",
        SupermercadoCategoriaView.as_view(),
        name="supermercado_categoria",
    ),
    path(
        "supermercado_promocao/<int:pk>/",
        SupermercadoPromocaoView.as_view(),
        name="supermercado_promocao",
    ),
]
