from django.contrib import admin
from turtle import home

from home.models import *

# Register your models here.

admin.site.register(Driver)
#admin.site.register(Passager)
admin.site.register(City)
admin.site.register(District)
admin.site.register(Car_category)
#admin.site.register(Location)
#admin.site.register(Speed)
#admin.site.register(Order)
admin.site.register(Car_type)
