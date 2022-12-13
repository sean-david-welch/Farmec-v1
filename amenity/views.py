from django.shortcuts import render
from . models import Amenity
from suppliers.models import Supplier
from amenity.models import Amenity


# Create your views here.
def amenitys(request):
    amenitys = Amenity.objects.all()
    suppliers = Supplier.objects.all()


    context = {'amenitys': amenitys, 'suppliers': suppliers}
    return render(request, 'amenity/amenitys.html', context)

def amenity(request, pk):
    amenity = Amenity.objects.get(id=pk)
    suppliers = Supplier.objects.all()
    amenitys = Amenity.objects.all()


    context = {'amenity': amenity, 'suppliers': suppliers, 'amenitys': amenitys}
    return render(request, 'amenity/amenity.html', context)