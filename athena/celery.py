import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "athena.settings")

app = Celery("athena")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
