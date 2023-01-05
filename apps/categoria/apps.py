from django.apps import AppConfig


class CategoriaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "categoria"

    def ready(self):
        import categoria.signals
