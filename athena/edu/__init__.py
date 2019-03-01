from django.apps import AppConfig


class EduConfig(AppConfig):
    name = "athena.edu"
    label = "edu"
    verbose_name = "Education"


default_app_config = "athena.edu.EduConfig"
