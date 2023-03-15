from django.db import models

class user_tb(models.Model):
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)

class category_tb(models.Model):
    category=models.CharField(max_length=20)

# Create your models here.
