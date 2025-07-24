from django.urls import path
from .views import menu, fooditems_by_category, category_form, fooditem_form, category_detail, category_delete, categories_update
from .views import categories_list, search_view, fooditem_detail


urlpatterns = [
    path('', menu, name='menu_list'),
    path('category/<int:category_id>', fooditems_by_category, name='fooditems_by_category'),
    path('category_form/', category_form, name='category_form'),
    path('fooditem_form/', fooditem_form, name='fooditem_form'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),

    #admin urls
    path('category_delete/<int:pk>', category_delete, name='category_delete'),
    path('categories_update/<int:pk>', categories_update, name='categories_update'),
    path('categories_list/', categories_list, name='categories_list'),
    path('search_results/', search_view, name='search_results'),
    path('fooditem_detail/<int:item_id>', fooditem_detail, name='fooditem_detail'),
    
    
]
