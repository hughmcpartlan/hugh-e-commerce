from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone
from django.db import models

# Create your models here.
class AccountUserManager(UserManager):
    def create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):

        now = timezone.now()
        if not email:
            raise ValueError('the given username must be set')

        email = self.normalize_email(email)
        user = self.model(username=email, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

class User(AbstractUser):

    objects = AccountUserManager()