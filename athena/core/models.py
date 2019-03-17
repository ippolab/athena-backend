from django.db import models

import uuid
import os


class UUIDModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid5(uuid.NAMESPACE_DNS, os.getenv("DJANGO_UUID5_VALUE", "athena")),
    )

    class Meta:
        abstract = True
