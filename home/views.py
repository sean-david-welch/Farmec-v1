from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from . models import Profile, Stat, Special
from suppliers.models import Supplier
from spareparts.models import SupplierPage
from . forms import CustomUserCreationForm, ProfileForm, StatForm, SpecialForm

def profiles(request):
    profiles = Profile.objects.all()
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 

    context = {'profiles': profiles, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'home/profiles.html', context)

#User CRUD Forms:
@login_required(login_url='login')
def registerUser(request):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            return redirect('home')
        else:
            messages.error(request, 'User Format is invalid')

    context = {'page': page, 'form': form, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'home/register.html', context)

@login_required(login_url='login')
def updateProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profiles')

    context = {'form': form, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'home/profile_form.html', context)

@login_required(login_url='login')
def deleteProfile(request, pk):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 
    profile = Profile.objects.get(id=pk)
    
    if request.method == 'POST':
        profile.delete()
        return redirect('profiles')
 
    context = {'object': profile, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'delete_form.html', context)

# Stat & Special CRUD forms:
def displays(request):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 
    stats = Stat.objects.all() 
    specials = Special.objects.all() 

    context = {'suppliers': suppliers, 'spareparts': spareparts, 'stats': stats, 'specials': specials}
    return render(request, 'home/displays.html', context)

@login_required(login_url='login')
def createStat(request): 
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()
    stats = Stat.objects.all() 
    form = StatForm()

    if request.user.is_superuser:
        if request.method == 'POST':
            form = StatForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.owner = suppliers
                post.save()
            return redirect('displays')

    context = {'form': form, 'suppliers': suppliers, 'spareparts': spareparts, 'stats': stats}
    return render(request, 'home/profile_form.html', context)

@login_required(login_url='login')
def updateStat(request, pk):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 
    stat = Stat.objects.get(id=pk)
    form = StatForm(instance=stat)
    
    if request.method == 'POST':

        form = StatForm(request.POST, request.FILES, instance=stat)
        if form.is_valid():
            suppliers = form.save()

        return redirect('displays')
 
    context = {'form': form, 'suppliers': suppliers, 'spareparts': spareparts, 'stat': stat}
    return render(request, 'home/profile_form.html', context)

@login_required(login_url='login')
def deleteStat(request, pk):
    stat = Stat.objects.get(id=pk)
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 
    
    if request.method == 'POST':
        suppliers.delete()
        return redirect('displays')
 
    context = {'object': stat, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'delete_form.html', context)

@login_required(login_url='login')
def createSpecial(request): 
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()
    specials = Special.objects.all() 
    form = SpecialForm()

    if request.user.is_superuser:
        if request.method == 'POST':
            form = SpecialForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.owner = suppliers
                post.save()
            return redirect('displays')

    context = {'form': form, 'suppliers': suppliers, 'spareparts': spareparts, 'specials': specials}
    return render(request, 'home/profile_form.html', context)

@login_required(login_url='login')
def updateSpecial(request, pk):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 
    special = Special.objects.get(id=pk)
    form = SpecialForm(instance=special)
    
    if request.method == 'POST':

        form = SpecialForm(request.POST, request.FILES, instance=special)
        if form.is_valid():
            suppliers = form.save()

        return redirect('displays')
 
    context = {'form': form, 'suppliers': suppliers, 'spareparts': spareparts, 'special': special}
    return render(request, 'home/profile_form.html', context)

@login_required(login_url='login')
def deleteSpecial(request, pk):
    special = Special.objects.get(id=pk)
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 
    
    if request.method == 'POST':
        suppliers.delete()
        return redirect('displays')
 
    context = {'object': special, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'delete_form.html', context)