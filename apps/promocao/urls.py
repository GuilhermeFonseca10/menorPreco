from django.urls import path
from promocao.views.promocao_create import PromocaoCreateView
from promocao.views.promocao_delete import PromocaoDeleteView
from promocao.views.promocao_detail import PromocaoDetailView
from promocao.views.promocao_detail_admin import PromocaoAdminDetailView
from promocao.views.promocao_list import PromocaoListView
from promocao.views.promocao_update import PromocaoUpdateView

urlpatterns = [
    path("cad", PromocaoCreateView.as_view(), name="promocao_create"),
    path("list", PromocaoListView.as_view(), name="promocao_list"),
    path(
        "detail/<int:pk>/",
        PromocaoDetailView.as_view(),
        name="promocao_detail",
    ),
    path(
        "promocao_detail_admin/<int:pk>/",
        PromocaoAdminDetailView.as_view(),
        name="promocao_detail_admin",
    ),
    path(
        "promocao_update/<int:pk>/",
        PromocaoUpdateView.as_view(),
        name="promocao_update",
    ),
    path(
        "promocao_delete/<int:pk>/",
        PromocaoDeleteView.as_view(),
        name="promocao_delete",
    ),
]
