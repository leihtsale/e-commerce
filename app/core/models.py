from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models


class UserManager(BaseUserManager):
    """
    User Manager
    """
    def create_user(self, email, password, **kwargs):

        if not email:
            raise ValueError(_('Email is required.'))

        if not kwargs.get('username'):
            raise ValueError(_('Username is required.'))

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):

        admin = self.create_user(email, password, **kwargs)
        admin.is_staff = True
        admin.is_superuser = True
        admin.save()

        return admin


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model where email is the primary identifier
    """
    alphanumeric = RegexValidator(
        r'^[0-9a-zA-Z]*$',
        _('Only alphanumeric characters are allowed.')
    )
    letters_only = RegexValidator(
        r'^[a-zA-Z ]*$',
        _('Only letters are allowed.'))

    first_name = models.CharField(
        max_length=128,
        validators=[letters_only]
    )
    last_name = models.CharField(
        max_length=128,
        validators=[letters_only]
    )
    username = models.CharField(
        max_length=100,
        unique=True,
        validators=[alphanumeric]
    )
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
