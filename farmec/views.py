from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from suppliers.models import Supplier
from blog.models import Blog
from home.models import Profile, Special, Stat
from home.forms import CustomUserCreationForm
from spareparts.models import SupplierPage

def home(request):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()
    special = Special.objects.all()
    stat = Stat.objects.all()
    blogs = Blog.objects.order_by('-created')[:2]

    context = {'suppliers': suppliers, 'blogs': blogs, 'specials': special, 'stats': stat, 'spareparts': spareparts}
    return render(request, 'home.html', context)


def contactPage(request):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()

    context = {'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'contact_page.html', context)

def loginPage(request):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR Password is incorrect')

    context = {'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('home')




