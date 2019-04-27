from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

from athena.authentication.models import Role, RolesEnum, User


def create_roles(_sender, **_kwargs):
    """Create default roles in database when server start"""

    for role in RolesEnum:
        Role.objects.get_or_create(name=role.value[0])


@receiver(m2m_changed, sender=User.roles.through)
@receiver(post_save, sender=User)
def create_related_profile(_sender, instance: User, *_args, **_kwargs):
    """Use user roles to create profiles"""

    profiles = {role.value[0]: role.value[1] for role in RolesEnum}
    if instance:
        for role in instance.roles.all():
            profiles[str(role)].objects.get_or_create(id=instance)
