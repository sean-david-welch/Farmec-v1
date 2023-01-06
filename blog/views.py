from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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

@login_required(login_url='login')
def createBlog(request): 
    blog = Blog.objects.all
    form = BlogForm()

    if request.user.is_superuser:
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES)
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

        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save()

        return redirect('blogs')
 
    context = {'form': form, 'blog': blog}
    return render(request, 'blog/blog_form.html', context)

def deleteBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    
    if request.method == 'POST':
        blog.delete()
        return redirect('blogs')
 
    context = {'object': blog}
    return render(request, 'delete_form.html', context)
