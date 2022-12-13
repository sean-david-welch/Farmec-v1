from django.shortcuts import render
from . models import Blog
from suppliers.models import Supplier
from amenity.models import Amenity

# Create your views here.
def blogs(request):
    blogs = Blog.objects.all()
    suppliers = Supplier.objects.all()
    amenitys = Amenity.objects.all()


    context = {'blogs': blogs, 'suppliers': suppliers, 'amenitys': amenitys}
    return render(request, 'blog/blogs.html', context)

def blog(request, pk):
    blog = Blog.objects.get(id=pk)
    suppliers = Supplier.objects.all()
    amenitys = Amenity.objects.all()


    context = {'blog': blog, 'suppliers': suppliers, 'amenitys': amenitys}
    return render(request, 'blog/blog.html', context)