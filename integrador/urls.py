from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework import routers

main_router = routers.DefaultRouter()

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
    # api
    # YOUR PATTERNS
    path("api/", include(main_router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
