from crum import get_current_user
from django import forms
from produto.models.categoria import Categoria
from supermercado.models.supermercado import Supermercado


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria

        fields = [
            "nome",
            "supermercados",
        ]

    def __init__(self, *args, **kwargs):
        super(CategoriaForm, self).__init__(*args, **kwargs)
        user = get_current_user()
        self.initial["usuario"] = user.id
        supermercado = Supermercado.objects.filter(usuario=user)
        self.fields["supermercados"].queryset = supermercado
