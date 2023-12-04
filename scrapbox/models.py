from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    profile_pic=models.ImageField(upload_to="profilepics",null=True,blank=True)

    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    name=models.CharField(max_length=200)

class Scraps(models.Model):
    name=models.CharField(max_length=200)
    condition=models.CharField(max_length=200)
    price=models.IntegerField()
    picture=models.ImageField(upload_to="products")
    user=models.ForeignKey(User,related_name="seller")
    place=models.CharField(max_length=200)
    category=models.ForeignKey(Category)
    created_date=models.DateField()
    status=models.BooleanField()



class Bids(models.Model):
    user=models.ForeignKey(User,related_name="buyer")
    scrap=models.ForeignKey(Scraps)
    amount=models.PositiveIntegerField()
    status=models.BooleanField()
