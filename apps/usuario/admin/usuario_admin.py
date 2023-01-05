from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from ..forms.usuario_admin_form import UsuarioAdminForm
from ..forms.usuario_form import UserCreationForm
from ..models.usuario import Usuario


class UsuarioAdmin(BaseUserAdmin):
    add_form = UserCreationForm, UsuarioAdminForm
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                )
            },
        ),
    )
    fieldsets = (
        (None, {"fields": ("username", "email")}),
        (
            "Informações Básicas",
            {"fields": ("nome", "last_login")},
        ),
        (
            "Permissões",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    list_display = [
        "username",
        "nome",
        "email",
        "is_active",
        "is_staff",
        "date_joined",
    ]

    search_fields = ["username", "nome"]


admin.site.register(Usuario, UsuarioAdmin)
