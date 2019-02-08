import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, **kwargs):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


# todo refactor upload
def upload_task(instance, file_name):
    file_path = os.path.join(
        'tasks_files',
        # str(instance.group),
        # str(instance.subject),
        # str(instance.subject_type),
        # str(instance.title)
    )

    return file_path


# todo
def upload_work(instance, file_name):
    file_path = os.path.join(
        'students_files',
        # str(instance.student.group),
        # str(instance.student),
        # str(instance.task.subject),
        # str(instance.task.subject_type),
        # str(instance.task.title),
        file_name
    )

    return file_path
