from django.db import models

class seller_register_tb(models.Model):
    na=models.CharField(max_length=20)
    ad=models.CharField(max_length=20)
    ge=models.CharField(max_length=20)
    ph=models.CharField(max_length=20)
    do=models.CharField(max_length=20)
    co=models.CharField(max_length=20)
    im=models.FileField()
    us=models.CharField(max_length=20)
    pa=models.CharField(max_length=20)
    status=models.CharField(max_length=20, default='pending')

class product_tb(models.Model):
    productname=models.CharField(max_length=20)
    price=models.IntegerField()
    image=models.FileField()
    stock=models.CharField(max_length=20)
    details=models.CharField(max_length=20)
    category=models.ForeignKey('site_admin.category_tb', on_delete=models.CASCADE)
    sellerid=models.ForeignKey(seller_register_tb, on_delete=models.CASCADE)
class tracking_tb(models.Model):
    orderid=models.ForeignKey('buyer.order_tb', on_delete=models.CASCADE)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    details=models.CharField(max_length=20)
# Create your models here.
