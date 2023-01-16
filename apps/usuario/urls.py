from django.urls import path
from usuario.views.register_view import RegisterView

app_name = "usuario"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
]
