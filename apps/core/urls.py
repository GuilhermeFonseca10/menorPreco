from django.urls import path
from core.views.home_view import HomeView
from core.views.dashboard_view import DashboardView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("dashboard", DashboardView.as_view(), name="dashboard")
]
