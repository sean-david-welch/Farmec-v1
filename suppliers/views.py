from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from . models import Supplier, Machine, Product
from . forms import SupplierForm, MachineForm, ProductForm

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Create your views here.
def suppliers(request):

    context = {}
    return render(request, 'suppliers/suppliers.html', context)

def get_video_data(video_id, api_key):
    youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)
    video_data = None
    try:
        response = youtube.videos().list(
            part='snippet',
            id=video_id
        ).execute()
        video_data = response['items'][0]['snippet']
    except HttpError as e:
        print('An error occurred: %s' % e)
    return video_data

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
