from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Student, Teacher, Tutor, User


@receiver(post_save, sender=User)
def create_related_profile(sender, instance: User, created: bool, *args, **kwargs):
    if instance and created:
        if instance.is_student:
            instance.student = Student.objects.get_or_create(id=instance)
        if instance.is_tutor:
            instance.tutor = Tutor.objects.get_or_create(id=instance)
        if instance.is_teacher:
            instance.teacher = Teacher.objects.get_or_create(id=instance)
        instance.save()
