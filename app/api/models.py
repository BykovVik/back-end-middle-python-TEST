from django.db import models

class User(models.Model):
    name = models.CharField(max_length=16)
    age = models.CharField(max_length=3)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)