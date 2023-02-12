from django import forms
from django_filters import CharFilter, FilterSet
from produto.models.produto import Produto


class FilterBook(FilterSet):
    nome = CharFilter(
        lookup_expr="icontains",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Produto
        fields = ["nome"]
