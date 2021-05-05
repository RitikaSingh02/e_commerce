from django.db import models


class UserEmail(models.Model):
    email = models.CharField(max_length=100, default="NULL", unique=True)
    status = models.CharField(max_length=10, default="rendered")

# Create your models here.
