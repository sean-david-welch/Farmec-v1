from django.shortcuts import render
from . models import Employee, Timeline
from suppliers.models import Supplier

# Create your views here.
def about(request):
    employee = Employee.objects.all()
    timeline = Timeline.objects.all()
    suppliers = Supplier.objects.all()

    context = {'employee': employee, 'suppliers': suppliers, 'timeline': timeline,}
    return render(request, 'about/about.html', context)