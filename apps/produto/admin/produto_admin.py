from django.contrib import admin

from ..models.produto import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = [
        "nome",
        "valor",
        "estoque",
        "criado",
        "modificado",
    ]

    search_fields = [
        "nome",
    ]

    list_filter = [
        "criado",
        "modificado",
    ]
