from django.db import models
from datetime import datetime, date
from customer.models import CustomUser


class products(models.Model):
    product_name = models.CharField(max_length=200, default="NULL")
    description = models.CharField(max_length=200, default="NULL")
    price = models.CharField(max_length=200, default="NULL")
    product_img = models.CharField(max_length=200, default="NULL")
    status = models.CharField(max_length=200, default="available")


class orders(models.Model):
    cust = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)
    order_id = models.CharField(max_length=200, default="NULL")
    cust_mail = models.CharField(max_length=200, default="NULL")
    checksum = models.CharField(max_length=250, default="NULL")
    trans_id = models.CharField(max_length=250, default="NULL")
    product_id = models.CharField(max_length=250, default="NULL")
    status = models.CharField(max_length=250, default="pending")
