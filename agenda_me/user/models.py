import uuid
from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from agenda_me.utils.empresas import EMPRESAS

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """Creates a new User, given a username and password."""
        user: User = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        """Creates a new User, with superuser status."""
        user: User = self.create_user(username=username, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user



class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=255, unique=True, null=False, blank=False)
    company = models.CharField(max_length=255, choices=EMPRESAS.CHOICES, default=EMPRESAS.GIMI)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    objects = UserManager()
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.full_name if (self.first_name) else self.username