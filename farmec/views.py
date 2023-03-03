from django.shortcuts import render 

def home(request):

    context = {}
    return render(request, 'home.html', context)

def loginPage(request):
    context = {}
    return render(request, 'login.html', context)

def logoutPage(request):
    context = {}
    return render(request, 'logout.html', context)