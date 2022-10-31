from django.shortcuts import render, redirect
from . models import Member

# Create your views here.
def home(request):
    return render(request, 'home.html')

def teams(request):
    members = Member.objects.all()

    context = {'members': members}
    return render(request, 'teams/teams.html', context)

