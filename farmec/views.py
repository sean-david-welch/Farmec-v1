from django.shortcuts import render
from suppliers.models import Supplier
from amenity.models import Amenity
from blog.models import Blog

def home(request):
    suppliers = Supplier.objects.all()
    amenitys = Amenity.objects.all()
    blogs = Blog.objects.order_by('created')[:3]

    context = {'suppliers': suppliers, 'amenitys': amenitys, 'blogs': blogs}
    return render(request, 'home.html', context)

def contact(request):
    suppliers = Supplier.objects.all()
    amenitys = Amenity.objects.all()

    context = {'suppliers': suppliers, 'amenitys': amenitys}
    return render(request, 'contact.html', context)

def navbar(request): 
    suppliers = Supplier.objects.all()
    amenitys = Amenity.objects.all()

    context = {'suppliers': suppliers, 'amenitys': amenitys}
    return render(request, 'navbar.hmtl', context)





