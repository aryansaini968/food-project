from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage


# Create your views here.
# @login_required(login_url='login')  
def home(request):
    # if not request.user.is_authenticated:
    #     return redirect(reverse('login'))
    print(f"Inside the home function")
    return render(request, "home.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            messages.success(request, " You are Logout in succesfully.")
            return render(request, "home.html")
        else:
            messages.error(request, "Your Password and username doesnot match .")
            print("Password and username doesnot match")
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')


        if not username or not password:
            print("sodioafisjfa")
            return render(request, 'register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please try some different usrname.")
            return render(request, 'register.html', {'error': 'Username already exists.'})
        if not all([username,email,password,confirm_password]):
            messages.error(request, "All fields are required.")
            return redirect('register')

        if len(username) < 3:
            messages.error(request, "Please enter a valid username.")
            return redirect('register')
        
        if not first_name.isalpha():
            messages.error(request, 'First name must contain only letters.')
            return redirect('register')
        
        if not last_name.isalpha():
            messages.error(request, 'Last name must contain only letters.')
            return redirect('register')

        if '@' not in email:
            messages.error(request, "Please enter a valid email.")
            return redirect('register')

        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            return redirect('register')

        if password != confirm_password:
             messages.error(request,"Passwords do not match.")
             return redirect('register')

        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
        user.save()
        
        # redirect to list page
        return redirect('login')
    return render(request,'register.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def orders(request):
    return render(request, 'orders.html')


@login_required(login_url='login')  
def profile(request):
    return render(request, 'profile.html')


def edit_profile(request, pk):
    if request.method == "GET":
         obj = User.objects.get(pk=pk)
         return render(request, "edit_profile.html", {'obj':obj})
    else:
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]

        if User.objects.filter(username=username).exists():
           messages.error(request, "Username already exists. Please try some different usrname.")
           return render(request, 'profile.html', {'error': 'Username already exists.'})

        if len(username) < 3:
           messages.error(request, "Please enter a valid username.")
           return redirect('profile.html')
         
        if not first_name.isalpha():
           messages.error(request, 'First name must contain only letters.')
           return redirect('profile.html')
         
        if not last_name.isalpha():
           messages.error(request, 'Last name must contain only letters.')
           return redirect('profile.html')



        obj = User.objects.get(pk=pk)
        obj.username = username
        obj.first_name = first_name
        obj.last_name = last_name
        obj.save()


    return redirect('profile.html')


def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        try:
            ContactMessage.objects.create(name=name, email=email, message=message)
        except Exception as e:
            print("Error saving message:", e)


        send_mail(
            subject=f"Message from {name}",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_EMAIL],
        )

        return render(request, 'contact_us.html', {'success': True})
    return render(request, 'contact_us.html')