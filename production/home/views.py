from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import Profile, Stat, Special
from . forms import CustomUserCreationForm, ProfileForm, StatForm, SpecialForm

def profiles(request):
    profiles = Profile.objects.all()

    context = {'profiles': profiles}
    return render(request, 'home/profiles.html', context)

#User CRUD Forms:
@login_required(login_url='login')
def registerUser(request):
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

    context = {'page': page, 'form': form}
    return render(request, 'home/register.html', context)

@login_required(login_url='login')
def updateProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profiles')

    context = {'form': form}
    return render(request, 'home/profile_form.html', context)

@login_required(login_url='login')
def deleteProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    
    if request.method == 'POST':
        profile.delete()
        return redirect('profiles')
 
    context = {'object': profile}
    return render(request, 'delete_form.html', context)

# Stat & Special CRUD forms:
def displays(request):
    stats = Stat.objects.all() 
    specials = Special.objects.all() 

    context = {'stats': stats, 'specials': specials}
    return render(request, 'home/displays.html', context)

@login_required(login_url='login')
def createStat(request): 
    stats = Stat.objects.all() 
    form = StatForm()

    if request.user.is_superuser:
        if request.method == 'POST':
            form = StatForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.owner = stats
                post.save()
            return redirect('displays')

    context = {'form': form, 'stats': stats}
    return render(request, 'home/profile_form.html', context)

@login_required(login_url='login')
def updateStat(request, pk):
    stat = Stat.objects.get(id=pk)
    form = StatForm(instance=stat)
    
    if request.method == 'POST':

        form = StatForm(request.POST, request.FILES, instance=stat)
        if form.is_valid():
            stat = form.save()

        return redirect('displays')
 
    context = {'form': form, 'stat': stat}
    return render(request, 'home/profile_form.html', context)

@login_required(login_url='login')
def deleteStat(request, pk):
    stat = Stat.objects.get(id=pk)
    
    if request.method == 'POST':
        stat.delete()
        return redirect('displays')
 
    context = {'object': stat}
    return render(request, 'delete_form.html', context)

@login_required(login_url='login')
def createSpecial(request): 
    specials = Special.objects.all() 
    form = SpecialForm()

    if request.user.is_superuser:
        if request.method == 'POST':
            form = SpecialForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.owner = specials
                post.save()
            return redirect('displays')

    context = {'form': form, 'specials': specials}
    return render(request, 'home/profile_form.html', context)

@login_required(login_url='login')
def updateSpecial(request, pk):
    special = Special.objects.get(id=pk)
    form = SpecialForm(instance=special)
    
    if request.method == 'POST':

        form = SpecialForm(request.POST, request.FILES, instance=special)
        if form.is_valid():
            special = form.save()

        return redirect('displays')
 
    context = {'form': form, 'special': special}
    return render(request, 'home/profile_form.html', context)

@login_required(login_url='login')
def deleteSpecial(request, pk):
    special = Special.objects.get(id=pk)
    
    if request.method == 'POST':
        special.delete()
        return redirect('displays')
 
    context = {'object': special}
    return render(request, 'delete_form.html', context)