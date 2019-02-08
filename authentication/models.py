from django.contrib.auth.models import AbstractUser


# todo create profiles

# todo : subject_id = ManyToManyField(Subject, related_name='student_group')

class User(AbstractUser):
    """Dummy user class"""
    pass
