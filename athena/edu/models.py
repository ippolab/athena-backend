from django.db import models
from athena.core.models import UUIDModel


class Subject(UUIDModel):
    name = models.CharField(max_length=50)
    semester = models.PositiveSmallIntegerField(default=1)

    class Meta:
        unique_together = ("name", "semester")

    def __str__(self):
        return "{} [{}]".format(self.name, self.semester)


class StudentGroup(UUIDModel):
    name = models.CharField(max_length=30, unique=True)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
