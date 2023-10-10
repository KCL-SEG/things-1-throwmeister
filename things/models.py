from typing import Any
from django.contrib.auth import models
from django.db import models

class BaseModel(models.Model):
    class Meta:
        abstract=True

class Thing(BaseModel):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
