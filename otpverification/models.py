from django.db import models

# Create your models here.


class OtpRender(models.Model):

    otp = models.CharField(max_length=10, default="NULL")
    phone = models.CharField(max_length=10, default="NULL", unique=True)
    status = models.CharField(max_length=10, default="active")
