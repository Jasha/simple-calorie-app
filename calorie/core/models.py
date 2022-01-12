from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from calorie.core.managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    is_superuser = models.BooleanField(default=False)
    calories_threshold = models.IntegerField(default=2100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()
