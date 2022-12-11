from django.shortcuts import render
from . models import Amenity

# Create your views here.
def amenity(request):
    amenity = Amenity.objects.all()

    context = {'amenity': amenity}
    return render(request, 'amenity/amenity.html', context)