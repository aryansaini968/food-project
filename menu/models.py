from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
        name = models.CharField(max_length=256)
        image = models.ImageField(upload_to='category_images/') 
        

        def __str__(self):
                return self.name
        
class Fooditem(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='Fooditem/') 
    is_vegetarian = models.BooleanField(default=True)
    description = models.TextField()
    prize = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

