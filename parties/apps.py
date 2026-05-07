from django.apps import AppConfig


class PartiesConfig(AppConfig):
    name = 'parties'
    def ready(self):
        import parties.signals  # noqa
