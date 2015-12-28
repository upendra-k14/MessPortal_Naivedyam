# encoding: utf-8
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Meal(models.Model):
	name = models.CharField(max_length=30)
	booktime = models.DurationField(default=timedelta())
	canceltime = models.DurationField(default=timedelta())
	rate = models.FloatField()

	def __str__(self):
		return self.name

class Account(models.Model):
        balance = models.FloatField()
        regdate = models.DateTimeField()
        expdate = models.DateTimeField()

        def __str__(self):
                return str(self.balance)

class Vendor(models.Model):
        id = models.OneToOneField(User, primary_key=True)
        account_balance = models.OneToOneField(Account)

        #def __str__(self):
        #        return self.id.first_name+" "+self.id.last_name


class Mess(models.Model):
	name = models.CharField(max_length=100)
	venue = models.CharField(max_length=100)
	capacity = models.IntegerField()
	vendor = models.OneToOneField(Vendor)

	def __str__(self):
		return self.name

class Student(models.Model):
	id = models.OneToOneField(User, primary_key=True)
	account_balance = models.OneToOneField(Account)
	rollno = models.CharField(max_length=20)
	default_mess = models.CharField(max_length=100)

	#def __str__(self):
	#	return self.id.first_name+" "+self.id.last_name

class Non_Student(models.Model):
	id = models.OneToOneField(User, primary_key=True)
	account_balance = models.OneToOneField(Account)
	default_mess = models.CharField(max_length=100)
	
	#def __str__(self):
        #        return self.id.first_name+" "+self.id.last_name

class Unregister(models.Model):
	sid = models.ForeignKey(User)
	unreg_date = models.DateField()
	mealid = models.ForeignKey(Meal)

class Booking(models.Model):
	sid = models.ForeignKey(User)
	mealid = models.ForeignKey(Meal)
	book_date = models.DateField()
	mess = models.ForeignKey(Mess)

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
	mealid = models.ForeignKey(Meal)
	mealitems = ArrayField(models.CharField(max_length=50))
	weekday = models.CharField(max_length=20,choices=WEEK_DAYS)

class Suggestion(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=150)
	iffile = models.BooleanField(default=False)
	sgg_content = models.CharField(max_length=1000)
	sgg_file = models.FileField(null=True, blank=True, upload_to='')

