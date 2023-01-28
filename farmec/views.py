from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from suppliers.models import Supplier
from blog.models import Blog
from home.models import Profile, Special, Stat
from home.forms import CustomUserCreationForm
from spareparts.models import SupplierPage
from . forms import ContactForm

def home(request):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()
    special = Special.objects.all()
    stat = Stat.objects.all()
    blogs = Blog.objects.order_by('-created')[:2]
    form = ContactForm

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid:
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            body = form.cleaned_data['name']
            send_mail(
                'Contact for sent by: ' + name,
                body,
                email,
                ['jennie@farmec.ie']
            )
            messages.success('Form was sent!')
            return redirect('contact')
        else:
            messages.error(request, 'Form is not valid!')


    context = {'suppliers': suppliers, 'blogs': blogs, 'specials': special, 'stats': stat, 'spareparts': spareparts, 'form': form}
    return render(request, 'home.html', context)


def contactPage(request):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()
    form = ContactForm

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid:
            name = form['name']
            email = form['email']
            body = form['name']
            send_mail(
                f'Contact Form sent by: {name}',
                body,
                email,
                ['jennie@farmec.ie']
            )
            messages.success('Form was sent!')
            return redirect('contact')
        else:
            messages.error(request, 'Form is not valid!')

    context = {'suppliers': suppliers, 'spareparts': spareparts, 'form': form}
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
