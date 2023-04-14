from django.db import models

# Create your models here.
class Notification(models.Model):
    notificationtext=models.CharField(max_length=1000)
    notificationdate=models.CharField(max_length=20)

class Product(models.Model):
    productid=models.CharField(max_length=10,primary_key=True)
    productname=models.CharField(max_length=50)
    unitprice=models.IntegerField()
    mfgdate=models.CharField(max_length=20)
    expdate=models.CharField(max_length=20)