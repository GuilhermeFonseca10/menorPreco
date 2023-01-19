from django.contrib import admin

from ..models.supermercado import Supermercado


@admin.register(Supermercado)
class SupermercadoAdmin(admin.ModelAdmin):
    list_display = [
        "nome",
        "cidade",
    ]

    search_fields = [
        "nome",
    ]

    list_filter = [
        "nome",
        "cidade",
    ]
