from core.views.dashboard_view import DashboardView
from core.views.home_view import HomeView
from django.urls import path

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("dashboard", DashboardView.as_view(), name="dashboard"),
]
