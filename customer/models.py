from django.db import models


class CustomUser(models.Model):
    user_name = models.CharField(max_length=200, default="NULL")
    password = models.CharField(max_length=50, default="NULL")
    email = models.EmailField(max_length=200, default="NULL", unique=True)
    phone = models.CharField(max_length=10, default="NULL", unique=True)

# Create your models here.
