from django import forms
from supermercado.models.supermercado import Supermercado


class SupermercadoForm(forms.ModelForm):
    class Meta:
        model = Supermercado

        fields = [
            "nome",
            "imagem",
            "cpf",
            "cnpj",
            "cep",
            "cidade",
            "bairro",
            "rua",
            "numero",
            "usuario",
        ]