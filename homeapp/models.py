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

    def __str__(self):
        return self.customer.username


class CategoryModel(models.Model):
    category_name=models.CharField(max_length=100,unique=True)
       

    def __str__(self):
        return self.category_name 


class ProductModel(models.Model):
    pname=models.CharField(max_length=100)
    pdes=models.CharField(max_length=250)
    pimg=models.ImageField(upload_to='images/',null=True,blank=True)
    pprice=models.IntegerField()
    pqty=models.IntegerField()
    pcat=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.pname
    

class CartModel(models.Model):
    user=models.ForeignKey(CustomerModel,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(default=1)  


class Eventpack(models.Model):
    name=models.CharField(max_length=200)
    des=models.CharField(max_length=300)
    price=models.IntegerField()  

    def __str__(self):
        return self.name 

class Menupack(models.Model):
    name=models.CharField(max_length=200)
    des=models.CharField(max_length=300)
    price=models.IntegerField()  

    def __str__(self):
        return self.name  





