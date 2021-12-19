from django.db import models
from django.contrib.auth.models import User

class post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.CharField(max_length=400)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()


