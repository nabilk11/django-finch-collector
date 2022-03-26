from turtle import position
from django.db import models

# Create your models here.

POSITION_CHOICES = (
    ("F", "Forward"),
    ("G", "Guard"),
    ("C", "Center"),
)

class Player(models.Model):
    name = models.CharField(max_length=50)
    team = models.CharField(max_length=20)
    img = models.CharField(max_length=500)
    height = models.IntegerField()
    position = models.CharField(max_length=10, choices = POSITION_CHOICES)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']