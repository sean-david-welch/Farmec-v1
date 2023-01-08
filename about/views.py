from django.shortcuts import render
from . models import Employee, Timeline
from suppliers.models import Supplier

# Create your views here.
def about(request):
    employee = Employee.objects.all()
    suppliers = Supplier.objects.all()


    context = {'employee': employee, 'suppliers': suppliers}
    return render(request, 'about/about.html', context)

def timeline(request):
    timeline = Timeline.objects.all()
    suppliers = Supplier.objects.all()


    context = {'timeline': timeline, 'suppliers': suppliers}
    return render(request, 'about/timeline.html', context)