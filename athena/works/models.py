import os

from django.core.validators import FileExtensionValidator
from django.db import models

from athena.authentication.models import Student, Tutor, Teacher
from athena.core.models import UUIDModel
from athena.core.storage import OverwriteStorage
from athena.edu.models import StudentGroup, Subject, Speciality


def report_upload_to(instance: "Report", file_name: str):
    # Год/Направление/Предмет/Группа/Студент/
    return os.path.join(
        "reports",
        str(instance.task.create_datetime.year),
        str(instance.student.student_group.speciality),
        str(instance.task.subject),
        str(instance.student.student_group),
        str(instance.student),
        str(instance.task),
        file_name
    )


def task_upload_to(instance: "Task", file_name: str):
    return os.path.join(
        "tasks",
        str(instance.create_datetime.year),
        str(instance.student_group.speciality),
        str(instance.subject),
        str(instance),
        file_name
    )


class Task(UUIDModel):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256, blank=True)
    file = models.FileField(
        upload_to=report_upload_to,
        storage=OverwriteStorage(),
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])],
        null=True,
    )
    attachment = models.FileField(
        upload_to=task_upload_to,
        storage=OverwriteStorage(),
        validators=[FileExtensionValidator(allowed_extensions=["zip"])],
        null=True,
    )
    deadline = models.DateTimeField(null=True)
    create_datetime = models.DateTimeField(auto_now_add=True)
    edit_datetime = models.DateTimeField(auto_now=True)
    subject = models.ForeignKey(Subject, related_name="tasks", on_delete=models.CASCADE)
    student_group = models.ForeignKey(StudentGroup, related_name="tasks", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("name", "subject", "student_group",)

    def __str__(self):
        return self.name


class Report(UUIDModel):
    STATUSES = (("A", "Accepted"), ("F", "To fix"), ("N", "Not done"))

    name = models.CharField(max_length=254)
    file = models.FileField(
        upload_to=report_upload_to,
        storage=OverwriteStorage(),
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])],
        null=True,
    )
    attachment = models.FileField(
        upload_to=report_upload_to,
        storage=OverwriteStorage(),
        validators=[FileExtensionValidator(allowed_extensions=["zip"])],
        null=True,
    )
    status = models.CharField(max_length=1, choices=STATUSES, default="N")
    create_datetime = models.DateTimeField(auto_now_add=True)
    edit_datetime = models.DateTimeField(null=True)
    check_datetime = models.DateTimeField(null=True)
    comment = models.CharField(max_length=256, blank=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="reports")
    student = models.ForeignKey(Student, related_name="reports", on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, related_name="reports", null=True, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, related_name="reports", null=True, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("task", "student")

    def __str__(self):
        return self.name
