from django.core import validators
from django.db import models

from athena.core.models import UUIDModel


class Subject(UUIDModel):
    name = models.CharField(max_length=64)
    semester = models.PositiveSmallIntegerField(
        default=1, validators=[validators.RegexValidator(r"[1-8]{1}")]
    )

    class Meta:
        unique_together = ("name", "semester")

    def __str__(self):
        return "{} [{}]".format(self.name, self.semester)


class Speciality(UUIDModel):
    cipher = models.CharField(
        max_length=8,
        unique=True,
        validators=[validators.RegexValidator(r"[\d{2}.\d{2}}.\d{2}")],
    )
    name = models.CharField(max_length=64, unique=True)
    speciality = models.ManyToManyField(Subject, related_name="specialities")

    def __str__(self):
        return "{}. {}".format(self.cipher, self.name)


class StudentGroup(UUIDModel):
    name = models.CharField(
        max_length=32,
        unique=True,
        validators=[validators.RegexValidator(r"[А-Яа-я]{4,6}-\d{2}-\d{2}")],
    )

    speciality = models.ForeignKey(
        Speciality, related_name="groups", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
