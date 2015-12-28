from django.contrib import admin

from .models import Meal, Mess, Student, Non_Student, Vendor, Account, Booking, Unregister, Menu, Suggestion
# Register your models here.

admin.site.register(Meal)
admin.site.register(Mess)
admin.site.register(Student)
admin.site.register(Non_Student)
admin.site.register(Vendor)
admin.site.register(Booking)
admin.site.register(Unregister)
admin.site.register(Menu)
admin.site.register(Suggestion)

