from django.apps import AppConfig


class OpeningConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'opening'

    def ready(self):
        import opening.signals
