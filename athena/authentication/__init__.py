from django.apps import AppConfig
from django.db.models.signals import post_migrate


class AuthConfig(AppConfig):
    name = "athena.authentication"
    label = "authentication"
    verbose_name = "Authentication"

    def ready(self):
        import athena.authentication.signals
        post_migrate.connect(athena.authentication.signals.create_roles, sender=self)


default_app_config = "athena.authentication.AuthConfig"
