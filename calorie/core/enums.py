from django.db import models


class UserRole(models.IntegerChoices):
    SIMPLE = 1
    ADMIN = 2
