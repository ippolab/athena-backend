from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = "athena.core"
    label = "core"
    verbose_name = "Core"


default_app_config = "athena.core.CoreConfig"
