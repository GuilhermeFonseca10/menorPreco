from django.apps import AppConfig


class SupermercadoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "supermercado"

    def ready(self):
        import supermercado.signals
