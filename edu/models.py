from django.db import models
from django.db.models import Model, CharField


class Subject(models.Model):
    name = models.CharField(max_length=50)
    semester = models.SmallIntegerField(default=1, blank=False)

    class Meta:
        unique_together = ('name', 'semester')

    def __str__(self):
        return '[{}] {}'.format(self.semester, self.name)


class StudentGroup(Model):
    name = CharField(max_length=30, unique=True, blank=False)

    def __str__(self):
        return self.name
