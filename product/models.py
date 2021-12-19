from os import name
from django.db import models

class details(models.Model):
    name=models.CharField(max_length=100)
    weight = models.FloatField()
    price =models.FloatField()
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()