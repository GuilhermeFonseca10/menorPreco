from django import views
from django.urls import path

from usuario.views.login_view import LoginView
from usuario.views.register_view import RegisterView

app_name = "usuario"

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
]
