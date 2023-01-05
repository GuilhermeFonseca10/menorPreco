from django import forms

from ..models.usuario import Usuario


class UsuarioAdminForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["username", "email", "nome", "is_active", "is_staff"]
