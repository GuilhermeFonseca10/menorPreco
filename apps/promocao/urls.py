from django.urls import path
from promocao.views.promocao_create import PromocaoCreateView
from promocao.views.promocao_detail import PromocaoDetailView
from promocao.views.promocao_list import PromocaoListView

urlpatterns = [
    path("cad", PromocaoCreateView.as_view(), name="promocao_create"),
    path("list", PromocaoListView.as_view(), name="promocao_list"),
    path(
        "detail/<int:pk>/",
        PromocaoDetailView.as_view(),
        name="promocao_detail",
    ),
]
