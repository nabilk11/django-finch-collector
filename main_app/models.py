from django.contrib.auth.models import User
from django.db import models

# Create your models here.

POSITION_CHOICES = (
    ("F", "Forward"),
    ("G", "Guard"),
    ("C", "Center"),
)

# Accessories Model - in future use singular for proper naming convention ie. Accessory
class Accessories(models.Model):
    name = models.CharField(max_length=55)
    color = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=50)
    team = models.CharField(max_length=20)
    img = models.CharField(max_length=500)
    height = models.IntegerField()
    position = models.CharField(max_length=10, choices = POSITION_CHOICES)
    created_at = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']