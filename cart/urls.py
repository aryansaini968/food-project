from django.urls import path
from .views import add_to_cart, cart, remove_from_cart, update_quantity
urlpatterns = [
    path('add_to_cart/<int:fooditem_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    # Optional for quantity update
    path('update/<int:item_id>/', update_quantity, name='update_quantity'),
]
