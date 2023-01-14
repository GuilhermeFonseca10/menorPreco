from django.urls import path
from core.views.home_view import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home")
]
