from django.apps import AppConfig


class ContactConfig(AppConfig):
    name = 'contact'
    verbose_name = 'Contact'

    def ready(self):
        import contact.signals
