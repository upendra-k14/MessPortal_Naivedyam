# encoding: utf-8
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Meal(models.Model):
	name = models.CharField(max_length=30)
	starttime = models.TimeField()
	endtime = models.TimeField()
	rate = models.FloatField()

class Mess(models.Model):
	name = models.CharField(max_length=100)
	venue = models.CharField(max_length=100)
	capacity = models.IntegerField()
	vendor = models.CharField(max_length=100)

class Student(models.Model):
	account_balance = models.FloatField()
	rollno = models.CharField(max_length=20)
	default_mess = models.CharField(max_length=100)

class Non_Student(models.Model):
	account_balance = models.FloatField()
	default_mess = models.CharField(max_length=100)

class Vendor(models.Model):
	account_balance = models.FloatField()

class Account(models.Model):
	balance = models.CharField()
	regdate = models.DateTimeField()
	expdate = models.DateTimeField()

class Booking(models.Model):
	book_date = models.DateTimeField()
	
class Unregister(models.Model):
	unreg_date = models.DateTimeField()

class Menu(models.Model):
	mealitems = models.
	

