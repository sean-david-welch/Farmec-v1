from multiprocessing import context
from django.shortcuts import render, redirect
from . models import Member

# Create your views here.
def teams(request):
    members = Member.objects.all()

    context = {'members': members}
    return render(request, 'teams/teams.html', context)

def home(request):
    return render(request, 'teams/home.html')