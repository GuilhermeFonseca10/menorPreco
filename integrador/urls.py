from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("usuario/", include("usuario.urls")),
    path("", include("django.contrib.auth.urls")),
]
