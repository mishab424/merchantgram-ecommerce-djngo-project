from django.db import models
from django.utils import timezone

class Merchants(models.Model):
    name=models.CharField(max_length=50)
    merchantid=models.AutoField(primary_key=True)
    adress=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Product(models.Model):
    product_name=models.CharField(max_length=50)
    image=models.ImageField(null=True)
    description=models.TextField(blank=True,null=True)
    Delivery_place=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    merchant_username= models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.product_name



class Costomer(models.Model):
    name = models.CharField(max_length=50)
    user_id = models.AutoField(primary_key=True)
    adress = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    costomer_username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.costomer_username

class Status(models.Model):
    status=models.CharField(max_length=15)

    def __str__(self):
        return self.status


class Order(models.Model):
    product_name=models.CharField(max_length=50,blank=True,null=True)
    merchant_username=models.CharField(max_length=50,blank=True,null=True)
    costomer_name=models.CharField(max_length=50)
    adress = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    pincode=models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    qty=models.IntegerField()
    costomer_username=models.CharField(max_length=50,blank=True,null=True)
    price=models.CharField(max_length=50,blank=True,null=True)
    status=models.BooleanField(default=False,null=True)
    d_status=models.CharField(max_length=30,default='order_placed',blank=True,null=True)
    d_status_time = models.DateTimeField(default=timezone.now, blank=True, null=True)
    total_amount=models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.costomer_name

class Help(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    qry=models.TextField()

    def __str__(self):
        return self.name

class Admin(models.Model):
    admn=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=25)

    def __str__(self):
        return self.admn

class Delivery_status(models.Model):
    order_id=models.CharField(max_length=30,blank=True,null=True)
    delivery_date=models.DateTimeField(default=timezone.now,blank=True,null=True)
    delivery_status=models.CharField(max_length=30,default='order placed',blank=True,null=True)

    def __str__(self):
        return self.delivery_status
