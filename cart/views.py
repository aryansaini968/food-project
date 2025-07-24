from django.shortcuts import render, redirect, get_object_or_404
from menu.models import Fooditem
from .models import CartItem
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, fooditem_id):
    fooditem = get_object_or_404(Fooditem, id=fooditem_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        fooditem=fooditem
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')


@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.get_total_price() for item in cart_items)
    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'total': total
    })

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)

    if request.method == 'POST':
        cart_item.delete()
        return redirect('cart')

    return render(request, 'cart/remove_from_cart.html', {'cart_item': cart_item})


@login_required
def update_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    
    if request.method == 'POST':
        new_quantity = int(request.POST.get('quantity', 1))
        if new_quantity < 1:
            new_quantity = 1
        cart_item.quantity = new_quantity
        cart_item.save()
        return redirect('cart')

    return render(request, 'cart/update_quantity.html', {'cart_item': cart_item})

