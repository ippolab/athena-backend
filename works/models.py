from django.core.validators import FileExtensionValidator
from django.db import models

from authentication.models import Student
from edu.models import StudentGroup, Subject
from works.storage import OverwriteStorage, upload_report, upload_task


class Task(models.Model):
    theme = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=254, blank=False)
    templates = models.FileField(
        upload_to=upload_task,
        storage=OverwriteStorage(),
        validators=[FileExtensionValidator(allowed_extensions=["zip"])],
        null=True,
    )
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    groups = models.ManyToManyField(StudentGroup, related_name="task")
    deadline = models.DateTimeField()

    class Meta:
        unique_together = ("subject", "theme")

    def __str__(self):
        return "{}. {}".format(self.subject, self.theme)


class Report(models.Model):
    title = models.CharField(max_length=254, blank=False)
    document = models.FileField(
        upload_to=upload_report,
        storage=OverwriteStorage(),
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])],
        null=True,
    )
    attachment = models.FileField(
        upload_to=upload_report,
        storage=OverwriteStorage(),
        validators=[FileExtensionValidator(allowed_extensions=["zip"])],
        null=True,
    )
    STATUSES = (("A", "Accepted"), ("F", "To fix"), ("N", "Not done"))
    status = models.CharField(max_length=1, choices=STATUSES, default="N", blank=False)
    checked = models.DateTimeField(null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="reports"
    )

    class Meta:
        unique_together = ("task", "student")

    def __str__(self):
        return "{}. {}".format(self.task, self.title)
