from django.db import models

class register_tb(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    user=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class cart_tb(models.Model):
    name=models.CharField(max_length=20)
    shippingaddress=models.CharField(max_length=20)
    phonenumber= models.IntegerField()
    quantity=models.IntegerField()
    totalprice=models.IntegerField()
    productid=models.ForeignKey('seller.product_tb', on_delete=models.CASCADE)
    buyerid=models.ForeignKey(register_tb, on_delete=models.CASCADE)
class order_tb(models.Model):
    shippingaddress=models.CharField(max_length=20)
    quantity=models.IntegerField()
    phone=models.IntegerField()
    totalprice=models.IntegerField()
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    buyerid=models.ForeignKey(register_tb, on_delete=models.CASCADE)
    productid=models.ForeignKey('seller.product_tb', on_delete=models.CASCADE)
    sellerid=models.ForeignKey('seller.seller_register_tb', on_delete=models.CASCADE)
    status=models.CharField(max_length=20, default='pending')
    

# Create your models here.
