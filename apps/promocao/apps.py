from django.apps import AppConfig


class PromocaoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "promocao"

    def ready(self):
        import promocao.signals
