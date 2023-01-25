# from crum import get_current_user
from django import forms
from supermercado.models.supermercado import Supermercado


class SupermercadoForm(forms.ModelForm):
    class Meta:
        model = Supermercado

        fields = [
            "nome",
            "cnpj",
            "cpf",
            "cep",
            "cidade",
            "bairro",
            "rua",
            "numero",
            "imagem",
            "usuario",
        ]

    def __init__(self, *args, **kwargs):
        super(SupermercadoForm, self).__init__(*args, **kwargs)
        self.initial["usuario"] = get_current_user().id
        # self.fields["usuario"].widget.attrs["disabled"] = True
