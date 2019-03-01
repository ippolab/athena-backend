from django.apps import AppConfig


class WorksConfig(AppConfig):
    name = "athena.works"
    label = "works"
    verbose_name = "Students Works"


default_app_config = "athena.works.WorksConfig"
