from django.shortcuts import render
from . models import Employee, Timeline
from suppliers.models import Supplier
from amenity.models import Amenity



# Create your views here.
def about(request):
    employee = Employee.objects.all()
    suppliers = Supplier.objects.all()
    amenitys = Amenity.objects.all()


    context = {'employee': employee, 'suppliers': suppliers, 'amenitys': amenitys}
    return render(request, 'about/about.html', context)

def timeline(request):
    timeline = Timeline.objects.all()
    suppliers = Supplier.objects.all()
    amenitys = Amenity.objects.all()


    context = {'timeline': timeline, 'suppliers': suppliers, 'amenitys': amenitys}
    return render(request, 'about/timeline.html', context)