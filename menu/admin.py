from django.contrib import admin

# Register your models here.
from .models import Category, Fooditem

admin.site.register(Category) 
admin.site.register(Fooditem) 