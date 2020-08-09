from django.db import models

class users(models.Model):
    user_name=models.CharField(max_length=200,default="NULL")
    password=models.CharField(max_length=50,default="NULL")
    email=models.EmailField(max_length=200,default="NULL")
    phone=models.CharField(max_length=10,default="NULL")


# Create your models here.
