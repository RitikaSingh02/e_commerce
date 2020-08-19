from django.db import models
from datetime import datetime,date

class users(models.Model):
    user_name=models.CharField(max_length=200,default="NULL")
    password=models.CharField(max_length=50,default="NULL")
    email=models.EmailField(max_length=200,default="NULL",unique=True)
    phone=models.CharField(max_length=10,default="NULL",unique=True)
    
class products(models.Model):
    product_name=models.CharField(max_length=200,default="NULL")
    description=models.CharField(max_length=200,default="NULL")
    price=models.CharField(max_length=200,default="NULL")
    product_img=models.CharField(max_length=200,default="NULL")
    status=models.CharField(max_length=200,default="available")

class orders(models.Model):
    cust=models.ForeignKey(users,null=True,on_delete=models.SET_NULL)
    order_id=models.CharField(max_length=200,default="NULL")
    cust_mail=models.CharField(max_length=200,default="NULL")
    checksum=models.CharField(max_length=250,default="NULL")
    trans_id=models.CharField(max_length=250,default="NULL")
    product_id=models.CharField(max_length=250,default="NULL")
    status=models.CharField(max_length=250,default="pending")
    
class otp_table(models.Model):
    
    otp=models.CharField(max_length=10,default="NULL")
    phone=models.CharField(max_length=10,default="NULL",unique=True)
    status=models.CharField(max_length=10,default="active")

class verified_emails(models.Model):
    email=models.CharField(max_length=100,default="NULL",unique=True)
    status=models.CharField(max_length=10,default="rendered")
