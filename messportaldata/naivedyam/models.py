# encoding: utf-8
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
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
	user = models.OneToOneField(User)
	account_balance = models.OneToOneField(Account)
	rollno = models.CharField(max_length=20)
	default_mess = models.CharField(max_length=100)

class Non_Student(models.Model):
	user = models.OneToOneField(User)
	account_balance = models.OneToOneField(Account)
	default_mess = models.CharField(max_length=100)

class Vendor(models.Model):
	user = models.OneToOneField(User)
	account_balance = models.OneToOneField(Account)

class Account(models.Model):
	balance = models.FloatField()
	regdate = models.DateTimeField()
	expdate = models.DateTimeField()

class Unregister(models.Model):
	unreg_date = models.DateTimeField()

class Menu(models.Model):
	WEEK_DAYS=(
		('MO','Monday'),
		('TU','Tuesday'),
		('WE','Wednesday'),
		('TH','Thursday'),
		('FR','Friday'),
		('SA','Saturday'),
		('SU','Sunday'),
	)
	mealitems = ArrayField(models.CharField(max_length=50))
	weekday = models.CharField(max_length=20,choices=WEEK_DAYS)

class Suggestion(models.Model):
	title = models.CharField(max_length=150)
	iffile = models.BooleanField(default=False)
	sgg_content = models.CharField(max_length=1000)
	
	
	

