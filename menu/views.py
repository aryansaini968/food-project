from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category,Fooditem
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.db.models import Q



def is_admin(request):
    return request.user.is_authenticated and request.user.is_admin



@login_required(login_url='login') 
def menu(request):
    categories = Category.objects.all()
    print(categories[0].name)
    return render(request, "menu.html", {"categories":categories})

def create_menu(request):
    if not is_admin(request.user):
        return HttpResponseForbidden("Access Denied.")
    
    
        



@login_required(login_url='login') 
def fooditems_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    food_items = Fooditem.objects.filter(category=category)
    return render(request, 'fooditem.html', {
        'category': category,
        'food_items': food_items
    })

def category_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')  

        if name and image:
            Category.objects.create(name=name, image=image)
            return redirect('category_form')  # your redirect url
        else:
            return render(request, 'category_form.html', {
                'error': 'Please provide both name and image.'
            })

    return render(request, 'category_form.html')


def fooditem_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        prize = request.POST.get('prize')
        category = request.POST.get('category')
        image = request.FILES.get('image')
        is_vegetarian = request.POST.get('is_vegetarian')
        # print(name)
        # print(description)
        # print(prize)
        # print(category)
        # print(image)
        # print(is_vegetarian)
        if name and image and prize and category:
            Fooditem.objects.create(
                name=name,
                description=description,
                prize=prize,
                category=category,
                image=image,
                is_vegetarian=is_vegetarian,
            )
            return redirect('fooditem_form')
        else:
            return render(request, 'fooditem_form.html', {
                'error': 'Please fill all fields and upload image.'
            })

    return render(request, 'fooditem_form.html')

    
def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'category_detail.html', {'category': category})


def category_delete(request, pk):
    obj = get_object_or_404(Category, pk=pk)
    print(obj)
    if request.method == 'POST':
        obj.delete()
        return redirect('success_url_name') # Replace with your success URL name
    return render(request, 'categories_delet.html', {'obj': obj})
    

def categories_update(request, pk):
    if request.method == "GET":
         obj = Category.objects.get(pk=pk)
         return render(request, "categories_update.html", {'obj':obj})
    else:
         name = request.POST["name"]
         image = request.FILES.get('image')
    

         obj = Category.objects.get(pk=pk)
         obj.name = name
         obj.image = image
         obj.save()

         return redirect('menu_list')
    

def categories_list(request):
    print("Inside the list function")
    category = Category.objects.all()
    print(category)
    print(category[0].name)
    fooditem = Fooditem.objects.all()
    print(fooditem)

    
    return render(request, "categories_list.html", {
        "categories" : category,
        "fooditem" : fooditem
    })
    

def search_view(request):
    query = request.GET.get('q')
    name = request.GET.get('name')
    is_vegetarian = request.GET.get('veg')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    category_id = request.GET.get('category')

    fooditems = Fooditem.objects.all()
    categories = Category.objects.all()

    if query:
        fooditems = fooditems.filter(Q(name__icontains=query))

    if is_vegetarian == 'on':
        fooditems = fooditems.filter(is_vegetarian=True)

    if min_price:
        fooditems = fooditems.filter(prize__gte=min_price)

    if max_price:
        fooditems = fooditems.filter(prize__lte=max_price)

    if category_id:
        fooditems = fooditems.filter(category__id=category_id)

    return render(request, 'search_results.html', {
        'query': query,
        'categories': categories,
        'fooditems': fooditems
    })

def fooditem_detail(request, item_id):
    food_item = get_object_or_404(Fooditem, id=item_id)
    return render(request, 'fooditem_detail.html', {'food_item': food_item})