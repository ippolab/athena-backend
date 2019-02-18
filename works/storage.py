import os
import pathlib

from django.conf import settings
from django.core.files.storage import FileSystemStorage


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, **kwargs):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


def compare_dirs(path: str, filename: str) -> bool:
    try:
        abspath = pathlib.Path(settings.MEDIA_ROOT)
        abspath /= filename
        return os.path.samefile(abspath, path)
    except FileNotFoundError:
        return False


# todo refactor upload
def upload_task(instance, file_name: str):
    file_path = os.path.join("templates", str(instance), file_name)
    return file_path


# todo refactor upload
def upload_report(instance, file_name: str):
    file_path = os.path.join(
        "reports",
        str(instance.student.student_group),
        str(instance.student),
        str(instance),
        str(file_name),
    )

    return file_path
