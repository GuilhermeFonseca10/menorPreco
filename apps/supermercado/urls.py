from django.urls import path

from .views.supermercado_create import SupermercadoCreateView
from .views.supermercado_dashboard import DashboardSupermercadoView
from .views.supermercado_list import SupermercadoListView

urlpatterns = [
    path("list", SupermercadoListView.as_view(), name="supermercado_list"),
    path("cad", SupermercadoCreateView.as_view(), name="supermercado_create"),
    path("dashboard", DashboardSupermercadoView.as_view(), name="dashboard"),
]
