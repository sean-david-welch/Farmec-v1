from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from suppliers.models import Supplier
from amenity.models import Amenity
from blog.models import Blog

def home(request):
    suppliers = Supplier.objects.all()
    amenitys = Amenity.objects.all()
    blogs = Blog.objects.order_by('created')[:3]

    context = {'suppliers': suppliers, 'amenitys': amenitys, 'blogs': blogs}
    return render(request, 'home.html', context)

def contact(request):
    suppliers = Supplier.objects.all()
    amenitys = Amenity.objects.all()

    context = {'suppliers': suppliers, 'amenitys': amenitys}
    return render(request, 'contact.html', context)

def navbar(request): 
    suppliers = Supplier.objects.all()
    amenitys = Amenity.objects.all()

    context = {'suppliers': suppliers, 'amenitys': amenitys}
    return render(request, 'navbar.hmtl', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            User.objects.get(username=username)
        except:
            print('Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print('Username OR Password is incorrect')

    context = {}
    return render(request, 'login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('home')






