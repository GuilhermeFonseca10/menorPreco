from crum import get_current_user
from django import forms
from promocao.models.promocao import Promocao
from supermercado.models.supermercado import Supermercado


class PromocaoForm(forms.ModelForm):
    class Meta:
        model = Promocao

        fields = [
            "nome",
            "produtos",
            "supermercados",
        ]

    def __init__(self, *args, **kwargs):
        super(PromocaoForm, self).__init__(*args, **kwargs)
        user = get_current_user()
        self.initial["usuario"] = user.id
        supermercado = Supermercado.objects.filter(usuario=user)
        self.fields["supermercados"].queryset = supermercado
