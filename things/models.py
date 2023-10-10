from django.db import models
from django.contrib.auth.models import Model

# Create your models here.

class Thing(Model):
    name = models.CharField()
    description = models.CharField()
    quantity = models.IntegerField()
    