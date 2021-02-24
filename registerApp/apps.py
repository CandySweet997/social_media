from django.apps import AppConfig


class RegisterappConfig(AppConfig):
    name = 'registerApp'

    def ready(self):
        from . import signals
