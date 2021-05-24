from django.apps import AppConfig


class ResponseConfig(AppConfig):
    name = 'apps.response'

    def ready(self):
        import apps.response.signals  # noqa