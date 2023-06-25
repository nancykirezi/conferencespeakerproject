from django.db import models
from django.urls import path

class Conference(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    date = models.DateField()
    venue = models.CharField(max_length=100)
    theme = models.CharField(max_length=100)

    def __str__(self):
        return self.name

   