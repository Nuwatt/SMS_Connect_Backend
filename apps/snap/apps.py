from django.apps import AppConfig


class SnapConfig(AppConfig):
    name = 'apps.snap'

    def ready(self):
        import apps.snap.signals  # noqa
