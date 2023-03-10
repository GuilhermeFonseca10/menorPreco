from django.contrib import admin

from ..models.produto import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
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

    filter_horizontal = [
        "categorias",
    ]
