from django.db import models
from django.contrib.auth.models import User
import datetime
import os

def getfilename(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)


class Category(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    images=models.ImageField(upload_to=getfilename,null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text='0-default,1-Hidden')
    createdate=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=150,null=False,blank=False)
    vendor=models.CharField(max_length=150,null=False,blank=False)
    productimages=models.ImageField(upload_to=getfilename,null=True,blank=True)
    originalprice=models.FloatField(null=False,blank=False)
    sellingprice=models.FloatField(null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text='0-default,1-Hidden')
    trending=models.BooleanField(default=False,help_text='0-default,1-Trending')
    createdate=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    productqty=models.IntegerField(null=False,blank=False)
    createdat=models.DateTimeField(auto_now_add=True)    
