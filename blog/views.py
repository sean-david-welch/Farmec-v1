from django.shortcuts import render, redirect
from . models import Blog
from . forms import BlogForm
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

def createBlog(request): 
    blog = Blog.objects.all
    form = BlogForm()

    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = blog 
            post.save()
            return redirect('blogs')

    context = {'form': form, 'blog': blog}
    return render(request, 'blog/blog_form.html', context)


def updateBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    form = BlogForm(instance=blog)
    
    if request.method == 'POST':

        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save()

        return redirect('blogs')
 
    context = {'form': form, 'blog': blog}
    return render(request, 'blog/blog_form.html', context)
