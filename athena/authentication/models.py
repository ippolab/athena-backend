from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from athena.core.models import UUIDModel
from athena.edu.models import StudentGroup, Subject


class Role(UUIDModel):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """
        Create and save a user with the given username, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser):
    """
    Default user for authorization and statistics collection.

    Username and password are required. Other fields are optional.
    """
    id = models.UUIDField(primary_key=True, default=uuid4)
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    second_name = models.CharField(_('second name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    roles = models.ManyToManyField(Role, related_name="user")
    objects = UserManager()

    USERNAME_FIELD = 'username'

    class Meta(AbstractUser.Meta):
        verbose_name = _('user')
        verbose_name_plural = _('users')


class Student(UUIDModel):
    cipher = models.CharField(max_length=15, unique=True)
    user = models.OneToOneField(User, related_name="student", on_delete=models.CASCADE)
    student_group = models.ForeignKey(
        StudentGroup, related_name="student", null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return "{} {} {}".format(self.user.second_name, self.user.first_name, self.user.last_name)


class Tutor(UUIDModel):
    user = models.OneToOneField(User, related_name="tutor", on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {}".format(self.user.second_name, self.user.first_name, self.user.last_name)


class Teacher(UUIDModel):
    user = models.OneToOneField(User, related_name="teacher", on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, related_name="teacher")

    def __str__(self):
        return "{} {} {}".format(self.user.second_name, self.user.first_name, self.user.last_name)
