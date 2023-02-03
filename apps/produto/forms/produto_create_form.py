from crum import get_current_user
from django import forms
from produto.models.produto import Produto
from supermercado.models.supermercado import Supermercado


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto

        fields = [
            "nome",
            "valor",
            "estoque",
            "imagem",
            "descricao",
            "categorias",
            "supermercados",
        ]

    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        user = get_current_user()
        self.initial["usuario"] = user.id
        supermercado = Supermercado.objects.filter(usuario=user)
        self.fields["supermercados"].queryset = supermercado
