from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Users(models.Model):
	name = models.CharField(max_length=264,unique=True)
	
class Restaurants(models.Model):
	restaurants = models.TextField()

class Billing(models.Model):
	billingdetails = models.CharField(max_length=200)

class Promo(models.Model):
	Promocodes = models.CharField(max_length=200)

class Orderdetails(models.Model):
	totalorders = models.TextField()

class Deliveryboydetails(models.Model):
	name = models.CharField(max_length=200,unique=True)




