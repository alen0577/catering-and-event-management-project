from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomerModel(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=200)
    mobile=models.CharField(max_length=20)
    age=models.IntegerField()
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    pincode=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    photo=models.ImageField(null=True,blank=True,upload_to='images/')
