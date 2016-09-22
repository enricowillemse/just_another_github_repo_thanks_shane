from django.contrib.auth.models import User
from django.db import models


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    active = models.IntegerField()
    stock = models.IntegerField()
    cost_price = models.DecimalField(decimal_places=2, max_digits=10)
    images = models.TextField()
    barcode = models.CharField(max_length=255)


class UserProducts(models.Model):
    id = models.AutoField(primary_key=True)
    user_email = models.ForeignKey(User)
    product = models.ForeignKey(Products)


class UserOrders(models.Model):
    id = models.AutoField(primary_key=True)
    user_email = models.ForeignKey(User)
    order_status = models.CharField(max_length=255)
    customer_products = models.TextField()
    customer_address = models.TextField()
    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=255)
    customer_email = models.CharField(max_length=255)
