from django.apps import AppConfig


class ProvecConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'provec'

    def ready(self):
        import provec.signals
