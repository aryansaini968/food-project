from django.urls import path
from .views import home, login_view, register, logout_view, orders, contact_us, profile, edit_profile


urlpatterns = [
    path('home/', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout-view/', logout_view, name='logout_view.html'),
    path('orders/', orders, name='orders.html'),
    path('contact_us/', contact_us, name='contact_us.html'),
    path('profile/', profile, name='profile.html'),
    path('edit_profile/<int:pk>', edit_profile, name='edit_profile'),
]
