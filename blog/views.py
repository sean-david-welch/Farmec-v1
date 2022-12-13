from django.shortcuts import render
from . models import Blog

# Create your views here.
def blogs(request):
    blogs = Blog.objects.all()

    context = {'blogs': blogs}
    return render(request, 'blog/blogs.html', context)

def blog(request, pk):
    blog = Blog.objects.get(id=pk)

    context = {'blog': blog}
    return render(request, 'blog/blog.html', context)