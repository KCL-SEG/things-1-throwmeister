from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class Thing(AbstractBaseUser):
    name = models.CharField()
    description = models.CharField()
    quantity = models.IntegerField()
    