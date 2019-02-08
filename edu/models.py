from django.db import models
from django.db.models import Model, CharField, ForeignKey, CASCADE

from authentication.models import User


class Subject(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ManyToManyField(User, related_name='subject')


class StudentGroup(Model):
    name = CharField(max_length=30)
    student = ForeignKey(User, on_delete=CASCADE, related_name='student_group')
