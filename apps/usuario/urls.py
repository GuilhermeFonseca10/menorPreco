from django.urls import path
from usuario.views.register_view import RegisterView
from usuario.views.usuario_list import UsuarioListView

app_name = "usuario"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("list/", UsuarioListView.as_view(), name="usuario_list"),
]
