import os

from django.core.validators import FileExtensionValidator
from django.db import models

from athena.authentication.models import Student
from athena.core.models import UUIDModel
from athena.core.storage import OverwriteStorage
from athena.edu.models import StudentGroup, Subject


def report_upload(instance, file_name):
    return os.path.join(
        "reports",
        str(instance.created_datetime.year),
        str(instance.task.subject.semester),
        str(instance.task.subject.name),
        str(instance.student.student_group),
        str(instance.student),
        str(instance.task.theme),
        str(file_name),
    )


def task_upload(instance, file_name):
    return os.path.join(
        "templates",
        str(instance.created_datetime.year),
        str(instance.subject.semester),
        str(instance.subject.name),
        str(instance.theme),
        str(file_name),
    )


class Task(UUIDModel):
    theme = models.CharField(max_length=63)
    description = models.CharField(max_length=254)
    created_datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    templates = models.FileField(
        upload_to=task_upload,
        storage=OverwriteStorage(),
        validators=[FileExtensionValidator(allowed_extensions=["zip"])],
        null=True,
    )
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="tasks")
    groups = models.ManyToManyField(StudentGroup, related_name="task")

    class Meta:
        unique_together = ("subject", "theme")

    def __str__(self):
        return self.theme


class Report(UUIDModel):
    STATUSES = (("A", "Accepted"), ("F", "To fix"), ("N", "Not done"))

    title = models.CharField(max_length=254, blank=False)
    document = models.FileField(
        upload_to=report_upload,
        storage=OverwriteStorage(),
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])],
        null=True,
    )
    attachment = models.FileField(
        upload_to=report_upload,
        storage=OverwriteStorage(),
        validators=[FileExtensionValidator(allowed_extensions=["zip"])],
        null=True,
    )
    status = models.CharField(max_length=1, choices=STATUSES, default="N", blank=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    checked = models.DateTimeField(null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="reports"
    )

    class Meta:
        unique_together = ("task", "student")

    def __str__(self):
        return self.title
