from django.contrib import admin

from ..models.categoria import Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = [
        "nome",
        "supermercados",
    ]

    search_fields = [
        "nome",
    ]

    list_filter = ["nome"]
