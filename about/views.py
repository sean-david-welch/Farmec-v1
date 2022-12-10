from django.shortcuts import render
from . models import Employee, Timeline

# Create your views here.
def about(request):
    employee = Employee.objects.all()

    context = {'employee': employee}
    return render(request, 'about/about.html', context)

def timeline(request):
    timeline = Timeline.objects.all()

    context = {'timeline': timeline}
    return render(request, 'about/timeline.html', context)