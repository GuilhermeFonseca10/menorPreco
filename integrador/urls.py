from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

handler403 = "core.views.handler403.handler403"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("usuario/", include("usuario.urls")),
    path("supermercado/", include("supermercado.urls")),
    path("produto/", include("produto.urls")),
    path("promocao/", include("promocao.urls")),
    path("", include("django.contrib.auth.urls")),
    path("accounts/", include("allauth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
