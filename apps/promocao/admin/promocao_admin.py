from django.contrib import admin

from ..models.promocao import Promocao


@admin.register(Promocao)
class PromocaoAdmin(admin.ModelAdmin):
    list_display = [
        "nome",
    ]

    search_fields = [
        "nome",
    ]

    list_filter = ["nome"]
