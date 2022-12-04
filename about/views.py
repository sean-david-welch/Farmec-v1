from django.shortcuts import render
from . models import Employee

# Create your views here.
def about(request):
    employee = Employee.objects.all()

    context = {'employee': employee}
    return render(request, 'about/about.html', context)

# def timeline(request):
#     timelines = Timeline.objects.all()

#     context = {'timelines': timelines}
#     return render(request, 'teams/teams.html', context)