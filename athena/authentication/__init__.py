from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = "athena.authentication"
    label = "authentication"
    verbose_name = "Authentication"

    def ready(self):
        import athena.authentication.signals


default_app_config = "athena.authentication.AuthConfig"
