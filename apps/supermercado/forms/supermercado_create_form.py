from crum import get_current_user
from django import forms
from supermercado.models.supermercado import Supermercado


class SupermercadoForm(forms.ModelForm):
    class Meta:
        model = Supermercado

        fields = "__all__"
