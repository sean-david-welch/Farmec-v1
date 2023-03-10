from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from . models import Supplier, Machine, Product, Video
from . forms import SupplierForm, MachineForm, ProductForm, VideoForm

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime

# Create your views here.
def suppliers(request):

    context = {}
    return render(request, 'suppliers/suppliers.html', context)

def get_video_details(web_url, pk):
    youtube = build('youtube', 'v3', developerKey='<your-developer-key>')
    try:
        supplier = Supplier.objects.get(id=pk)
        video = Video.objects.get(pk=supplier.pk)

        # Call the API's videos().list method to retrieve video details
        video_id = None
        thumbnail_url = None
        try:
            request = youtube.videos().list(
                part="id,snippet",
                fields="items(id,snippet(thumbnails(high(url))))",
                url=Video.web_url
            )
            response = request.execute()
            video_id = response['items'][0]['id']
            thumbnail_url = response['items'][0]['snippet']['thumbnails']['high']['url']

            # update the video model with the retrieved video_id and thumbnail_url
            try:
                video.video_id = video_id
                video.thumbnail_url = thumbnail_url
                video.save()
            except Exception as e:
                print(f"An error occurred while updating the video: {e}")

        except HttpError as error:
            print(f"An error occurred: {error}")
        
        return video_id, thumbnail_url

    except Supplier.DoesNotExist or Video.DoesNotExist:
        print("Supplier or Video does not exist")
        return None, None

def supplier(request, pk):
    supplier = Supplier.objects.get(id=pk)

    context = {'supplier': supplier}
    return render(request, 'suppliers/supplier.html', context)

def machine(request, pk):
    machine = Machine.objects.get(id=pk)

    context = {'machine': machine}
    return render(request, 'suppliers/machine.html', context)

# Supplier Model CRUD:
@login_required(login_url='login')
def createSupplier(request): 
    form = SupplierForm()

    if request.user.is_superuser:
        if request.method == 'POST':
            form = SupplierForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.owner = suppliers
                post.save()
            return redirect('suppliers')

    context = {'form': form}
    return render(request, 'suppliers/supplier_form.html', context)

@login_required(login_url='login')
def updateSupplier(request, pk):
    supplier = Supplier.objects.get(id=pk)
    form = SupplierForm(instance=supplier)
    
    if request.method == 'POST':

        form = SupplierForm(request.POST, request.FILES, instance=supplier)
        if form.is_valid():
            supplier = form.save()

        return redirect('supplier', pk=pk)
 
    context = {'form': form, 'supplier':supplier}
    return render(request, 'suppliers/supplier_form.html', context)

@login_required(login_url='login')
def deleteSupplier(request, pk):
    supplier = Supplier.objects.get(id=pk)
    
    if request.method == 'POST':
        supplier.delete()
        return redirect('suppliers')
 
    context = {'object': supplier}
    return render(request, 'delete_form.html', context)

# Video Model CRUD:
@login_required(login_url='login')
def createVideo(request, pk): 
    videos = Video.objects.all()
    supplier = Supplier.objects.get(id=pk)
    form = VideoForm()

    if request.user.is_superuser:
        if request.method == 'POST':
            form = VideoForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.owner = videos
                post.save()
            return redirect('supplier', pk=pk)

    context = {'form': form, 'videos': videos, 'supplier': supplier}
    return render(request, 'suppliers/supplier_form.html', context)

@login_required(login_url='login')
def updateVideo(request, pk):
    video = Video.objects.get(id=pk)
    form = VideoForm(instance=video)
    
    if request.method == 'POST':

        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            video = form.save()

        return redirect('supplier', pk=video.supplier.pk)

    context = {'form': form}
    return render(request, 'suppliers/supplier_form.html', context)

@login_required(login_url='login')
def deleteVideo(request, pk):
    video = Video.objects.get(id=pk)

    if request.method == 'POST':
        video.delete()
        return redirect('supplier', pk=video.supplier.pk)

    context = {'object': video}
    return render(request, 'delete_form.html', context)

# Machine Model CRUD:
@login_required(login_url='login')
def createMachine(request, pk): 
    machines = Machine.objects.all()
    supplier = Supplier.objects.get(id=pk)
    form = MachineForm()

    if request.user.is_superuser:
        if request.method == 'POST':
            form = MachineForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.owner = machines
                post.save()
            return redirect('supplier', pk=pk)

    context = {'form': form, 'machines': machines, 'supplier': supplier}
    return render(request, 'suppliers/supplier_form.html', context)

@login_required(login_url='login')
def updateMachine(request, pk):
    machines = Machine.objects.all()
    machine = Machine.objects.get(id=pk)
    form = MachineForm(instance=machine)
    
    if request.method == 'POST':

        form = MachineForm(request.POST, request.FILES, instance=machine)
        if form.is_valid():
            machine = form.save()
        return redirect('supplier', pk=machine.supplier.pk)
 
    context = {'form': form, 'machines': machines, 'machine': machine}
    return render(request, 'suppliers/supplier_form.html', context)

@login_required(login_url='login')
def deleteMachine(request, pk):
    machine = Machine.objects.get(id=pk)
    
    if request.method == 'POST':
        machine.delete()
        return redirect('supplier', pk=machine.supplier.pk)
 
    context = {'object': machine}
    return render(request, 'delete_form.html', context)

# Product Model CRUD:
@login_required(login_url='login')
def createProduct(request, pk): 
    products = Product.objects.all()
    machine = Machine.objects.get(id=pk)
    form = ProductForm()

    if request.user.is_superuser:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.owner = products
                post.save()
            return redirect('machine', pk=pk)

    context = {'form': form, 'products': products}
    return render(request, 'suppliers/supplier_form.html', context)

@login_required(login_url='login')
def updateProduct(request, pk):
    products = Product.objects.all()
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    
    if request.method == 'POST':

        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            products = form.save()

        return redirect('machine', pk=product.machine.pk)
 
    context = {'form': form, 'products': products, 'product': product}
    return render(request, 'suppliers/supplier_form.html', context)

@login_required(login_url='login')
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    
    if request.method == 'POST':
        product.delete()
        return redirect('machine', pk=product.machine.pk)
 
    context = {'object': product}
    return render(request, 'delete_form.html', context)
