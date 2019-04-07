from athena.core.models import UUIDModel
from django.db import models


class Speciality(UUIDModel):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Subject(UUIDModel):
    name = models.CharField(max_length=64)
    semester = models.PositiveSmallIntegerField(default=1)

    class Meta:
        unique_together = ("name", "semester")

    def __str__(self):
        return "{} [{}]".format(self.name, self.semester)


class StudentGroup(UUIDModel):
    name = models.CharField(max_length=32, unique=True)
    quantity = models.PositiveSmallIntegerField(default=0)
    speciality = models.ForeignKey(
        Speciality, related_name="groups", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
