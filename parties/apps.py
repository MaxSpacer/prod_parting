from django.apps import AppConfig


class PartiesConfig(AppConfig):
    name = 'parties'
    verbose_name = "Партии"
    def ready(self):
        import parties.signals  # noqa
