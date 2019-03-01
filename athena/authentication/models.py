from django.contrib.auth.models import AbstractUser
from django.db import models

from athena.edu.models import StudentGroup, Subject


class User(AbstractUser):
    """Dummy (~proxy) user class"""

    pass


class Student(models.Model):
    user = models.OneToOneField(User, related_name="student", on_delete=models.CASCADE)
    student_group = models.ForeignKey(
        StudentGroup, related_name="student", null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return "{} {}".format(self.user.last_name, self.user.first_name)


class Tutor(models.Model):
    user = models.OneToOneField(User, related_name="tutor", on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.user.last_name, self.user.first_name)


class Teacher(models.Model):
    user = models.OneToOneField(User, related_name="teacher", on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, related_name="teacher")

    def __str__(self):
        return "{} {}".format(self.user.last_name, self.user.first_name)
