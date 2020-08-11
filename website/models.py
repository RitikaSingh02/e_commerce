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

class payment(models.Model):
    user=models.ForeignKey(users,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(products,null=True,on_delete=models.SET_NULL)
    date_of_purchase=models.DateField(auto_now_add=True,auto_now=False)

class otp_table(models.Model):
    
    otp=models.CharField(max_length=10,default="NULL")
    phone=models.CharField(max_length=10,default="NULL",unique=True)
    status=models.CharField(max_length=10,default="active")

# Create your models here.
