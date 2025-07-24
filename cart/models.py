from django.db import models
from django.conf import settings # To access the User model
from django.contrib.auth.models import User
from menu.models import Fooditem # Assuming you have a Product model

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fooditem = models.ForeignKey('menu.Fooditem', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.fooditem.name}"


    def get_total_price(self):
        return self.quantity * self.fooditem.prize