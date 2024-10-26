from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Business(models.Model):
    LOW = "$"
    MID_LOW = "$$"
    MID = "$$$"
    MID_HIGH ="$$$$"
    HIGH = "$$$$$"
    
    PRICES_CHOICES = [
        (LOW, "Very Cheap"),
        (MID_LOW, "Cheap"),
        (MID_HIGH, "Moderate"),
        (HIGH, "Expennsive")
    ]
    
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=100,unique=True,blank=True,null=True)
    description = models.TextField()
    price_range = models.CharField(max_length=10, choices=PRICES_CHOICES)
    street_adress = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    website = models.URLField(max_length=255)
    url = models.URLField(max_length=255)
    phone = models.CharField(max_length=255)
    hour = models.CharField(max_length=255)


class Review(models.Model):
    title= models.CharField(max_length=255)
    content = models.TextField()
    stars = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    business = models.ForeignKey(Business,on_delete=models.CASCADE)
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=100,unique=True,blank=True,null=True)
    ordinal = models.IntegerField()
    business = models.ManyToManyField('Business')
    
