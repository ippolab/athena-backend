from django.core.validators import FileExtensionValidator
from django.db import models

from authentication.models import User
from edu.models import Subject, StudentGroup
from works.storage import OverwriteStorage, upload_task, upload_work


class Task(models.Model):
    theme = models.CharField(max_length=50)
    description = models.CharField(max_length=254)
    templates = models.FileField(
        upload_to=upload_task,
        storage=OverwriteStorage(),
        validators=[FileExtensionValidator(allowed_extensions=['zip'])],
        null=True
    )
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE)
    group_id = models.ManyToManyField(StudentGroup, related_name='task')
    deadline = models.DateTimeField(name='deadline')


class Report(models.Model):
    title = models.CharField(max_length=254)
    document = models.FileField(
        upload_to=upload_work,
        storage=OverwriteStorage(),
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        null=True
    )
    attachment = models.FileField(
        upload_to=upload_work,
        storage=OverwriteStorage(),
        validators=[FileExtensionValidator(allowed_extensions=['zip'])],
        null=True
    )
    STATUSES = (
        ('A', 'Accepted'),
        ('F', 'To fix'),
        ('N', 'Not done'),
    )
    status = models.CharField(max_length=1, choices=STATUSES, default='N', blank=False)
    checked = models.DateTimeField(null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
