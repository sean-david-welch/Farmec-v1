from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Blog, Exhibition
from . forms import BlogForm, ExhibitionForm
from suppliers.models import Supplier
from spareparts.models import SupplierPage

# Create your views here.
def blogs(request):
    blogs = Blog.objects.all()
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()

    context = {'blogs': blogs, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'blog/blogs.html', context)

def blog(request, pk):
    blog = Blog.objects.get(id=pk)
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()

    context = {'blog': blog, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'blog/blog.html', context)

def exhibitions(request):
    exhibitions = Exhibition.objects.all()
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()

    context = {'exhibitions': exhibitions, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'blog/exhibitions.html', context)

# Create Blog Form
@login_required(login_url='login')
def createBlog(request):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 
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

    context = {'form': form, 'blog': blog, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'blog/blog_form.html', context)

@login_required(login_url='login')
def updateBlog(request, pk):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 
    blog = Blog.objects.get(id=pk)
    form = BlogForm(instance=blog)
    
    if request.method == 'POST':

        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save()

        return redirect('blog', pk=pk)
 
    context = {'form': form, 'blog': blog, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'blog/blog_form.html', context)

@login_required(login_url='login')
def deleteBlog(request, pk):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 
    blog = Blog.objects.get(id=pk)
    
    if request.method == 'POST':
        blog.delete()
        return redirect('blogs')
 
    context = {'object': blog, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'delete_form.html', context)

# Exhibition Forms:
@login_required(login_url='login')
def createExhibition(request): 
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()
    exhibitions = Exhibition.objects.all
    form = ExhibitionForm()

    if request.user.is_superuser:
        if request.method == 'POST':
            form = ExhibitionForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.owner = exhibitions 
                post.save()
                return redirect('exhibitions')

    context = {'form': form, 'exhibitions': exhibitions, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'blog/blog_form.html', context)

@login_required(login_url='login')
def updateExhibition(request, pk):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()
    exhibition = Exhibition.objects.get(id=pk)
    form = ExhibitionForm(instance=exhibition)
    
    if request.method == 'POST':

        form = ExhibitionForm(request.POST, request.FILES, instance=exhibition)
        if form.is_valid():
            exhibition = form.save()

        return redirect('exhibitions')
 
    context = {'form': form, 'exhibition': exhibition, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'blog/blog_form.html', context)

@login_required(login_url='login')
def deleteExhibition(request, pk):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()
    exhibition = Exhibition.objects.get(id=pk)
    
    if request.method == 'POST':
        exhibition.delete()
        return redirect('exhibitions')
 
    context = {'object': exhibition, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'delete_form.html', context)
