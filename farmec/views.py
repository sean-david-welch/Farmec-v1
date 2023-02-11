from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from django.core.mail import send_mail

from suppliers.models import Supplier
from blog.models import Blog
from home.models import Special, Stat
from spareparts.models import SupplierPage
from stripepayments.models import PaymentProduct
from . forms import ContactForm, LoginPageForm

def home(request):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()
    specials = Special.objects.all()
    stat = Stat.objects.all()
    blogs = Blog.objects.order_by('-created')[:2]
    form = ContactForm

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            body = form.cleaned_data['body']
            send_mail(
                f'Contact Form sent by: {name}',
                body + ',' + '\n' + 'email sent by: ' + email,
                'jennie@farmec.ie',
                ['jennie@farmec.ie']
            )
            messages.success(request, 'Form was sent!')
            return redirect('home')
        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0]  == 'This field is required.':
                    messages.error(request, 'Please complete the form validation')
                    home_url = reverse('home')
                    return redirect(home_url + "#contact-form")
                messages.error(request, error)


    context = {'suppliers': suppliers, 'blogs': blogs, 'specials': specials, 'stats': stat, 'spareparts': spareparts, 'form': form}
    return render(request, 'home.html', context)

def loginPage(request):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()
    form = LoginPageForm

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        form = LoginPageForm(request.POST)

        if form.is_valid():
            try:
                User.objects.get(username=username)
            except:
                messages.error(request, 'Username does not exist')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                for key, error in list(form.errors.items()):
                    if key == 'captcha' and error[0]  == 'This field is required.':
                        messages.error(request, 'Please complete the form validation')
                messages.error(request, 'Username OR Password is incorrect')

    context = {'suppliers': suppliers, 'spareparts': spareparts, 'form': form}
    return render(request, 'login.html', context)

def logoutPage(request):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()

    if request.method == 'POST':   
        logout(request)
        return redirect('home')

    context = {'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'logout.html', context)

