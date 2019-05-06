import os

from django.core.validators import FileExtensionValidator
from django.db import models

from athena.authentication.models import Student, Teacher, Tutor, User
from athena.core.models import UUIDModel
from athena.core.storage import OverwriteStorage
from athena.edu.models import Speciality, StudentGroup, Subject


def report_upload_to(instance: "Report", file_name: str):
    return os.path.join(
        "reports",
        str(instance.task.created_at.year),
        str(instance.student.student_group.speciality),
        str(instance.task.subject),
        str(instance.student.student_group),
        str(instance.student),
        str(instance.task),
    )


def task_upload_to(instance: "Task", file_name: str):
    return os.path.join(
        "tasks",
        str(instance.created_at.year),
        str(instance.student_group.speciality),
        str(instance.subject),
        str(instance.student_group),
        str(instance),
    )


class Task(UUIDModel):
    name = models.CharField(max_length=127)
    description = models.CharField(max_length=255, null=True)
    file = models.FileField(
        max_length=255,
        upload_to=task_upload_to,
        storage=OverwriteStorage(),
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])],
        null=True,
    )
    attachment = models.FileField(
        max_length=255,
        upload_to=task_upload_to,
        storage=OverwriteStorage(),
        validators=[FileExtensionValidator(allowed_extensions=["zip"])],
        null=True,
    )
    deadline = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subject = models.ForeignKey(Subject, related_name="tasks", on_delete=models.PROTECT)
    student_group = models.ForeignKey(
        StudentGroup, related_name="tasks", on_delete=models.PROTECT
    )

    class Meta:
        unique_together = ("name", "subject", "student_group")

    def __str__(self):
        return self.name


class Report(UUIDModel):
    name = models.CharField(max_length=255)
    file = models.FileField(
        max_length=255,
        upload_to=report_upload_to,
        storage=OverwriteStorage(),
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])],
        null=True,
    )
    attachment = models.FileField(
        max_length=255,
        upload_to=report_upload_to,
        storage=OverwriteStorage(),
        validators=[FileExtensionValidator(allowed_extensions=["zip"])],
        null=True,
    )
    status = models.CharField(
        max_length=1,
        choices=(("A", "Accepted"), ("D", "Done"), ("F", "To fix"), ("N", "Not done")),
        default="N",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    checked_at = models.DateTimeField(null=True)
    comment = models.CharField(max_length=255, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="reports")
    student = models.ForeignKey(
        Student, related_name="reports", on_delete=models.PROTECT
    )
    verified_by = models.ForeignKey(
        User, related_name="reports", null=True, on_delete=models.PROTECT
    )

    class Meta:
        unique_together = ("task", "student")

    def __str__(self):
        return self.name
