from django.shortcuts import render
from . models import Amenity

# Create your views here.
def amenitys(request):
    amenitys = Amenity.objects.all()

    context = {'amenitys': amenitys}
    return render(request, 'amenity/amenitys.html', context)

def amenity(request, pk):
    amenity = Amenity.objects.get(id=pk)

    context = {'amenity': amenity}
    return render(request, 'amenity/amenity.html', context)