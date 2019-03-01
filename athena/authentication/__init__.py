from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = "athena.authentication"
    label = "authentication"
    verbose_name = "Authorization"


default_app_config = "athena.authentication.AuthConfig"
