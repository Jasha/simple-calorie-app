from django.db import models

from calorie.core.models import User


class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="food")
    name = models.CharField(max_length=255)
    calorie = models.IntegerField()
    date = models.DateTimeField()
