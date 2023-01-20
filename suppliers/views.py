from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Supplier, Machine, Product
from . forms import SupplierForm, MachineForm, ProductForm

# Create your views here.
def suppliers(request):
    suppliers = Supplier.objects.all()

    context = {'suppliers': suppliers}
    return render(request, 'suppliers/suppliers.html', context)

def supplier(request, pk):
    supplier = Supplier.objects.get(id=pk)
    suppliers = Supplier.objects.all()

    context = {'supplier': supplier, 'suppliers': suppliers}
    return render(request, 'suppliers/supplier.html', context)

def machine(request, pk):
    machine = Machine.objects.get(id=pk)
    suppliers = Supplier.objects.all()

    context = {'machine': machine, 'suppliers': suppliers}
    return render(request, 'suppliers/machine.html', context)

# Supplier Model CRUD:
@login_required(login_url='login')
def createSupplier(request): 
    suppliers = Supplier.objects.all
    form = SupplierForm()

    if request.user.is_superuser:
        if request.method == 'POST':
            form = SupplierForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.owner = suppliers
                post.save()
            return redirect('suppliers')

    context = {'form': form, 'suppliers': suppliers}
    return render(request, 'suppliers/supplier_form.html', context)

@login_required(login_url='login')
def updateSupplier(request, pk):
    suppliers = Supplier.objects.all
    supplier = Supplier.objects.get(id=pk)
    form = SupplierForm(instance=supplier)
    
    if request.method == 'POST':

        form = SupplierForm(request.POST, request.FILES, instance=supplier)
        if form.is_valid():
            suppliers = form.save()

        return redirect('suppliers')
 
    context = {'form': form, 'suppliers': suppliers, 'supplier':supplier}
    return render(request, 'suppliers/supplier_form.html', context)

@login_required(login_url='login')
def deleteSupplier(request, pk):
    suppliers = Supplier.objects.get(id=pk)
    
    if request.method == 'POST':
        suppliers.delete()
        return redirect('suppliers')
 
    context = {'object': suppliers}
    return render(request, 'delete_form.html', context)

# Machine Model CRUD:
@login_required(login_url='login')
def createMachine(request): 
    machines = Machine.objects.all()
    form = MachineForm()

    if request.user.is_superuser:
        if request.method == 'POST':
            form = MachineForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.owner = machines
                post.save()
            return redirect('suppliers')

    context = {'form': form, 'machines': machines}
    return render(request, 'suppliers/supplier_form.html', context)

@login_required(login_url='login')
def updateMachine(request, pk):
    machines = Machine.objects.all()
    machine = Machine.objects.get(id=pk)
    form = MachineForm(instance=machine)
    
    if request.method == 'POST':

        form = MachineForm(request.POST, request.FILES, instance=machine)
        if form.is_valid():
            machines = form.save()

        return redirect('suppliers')
 
    context = {'form': form, 'machines': machines, 'machine': machine}
    return render(request, 'suppliers/supplier_form.html', context)

@login_required(login_url='login')
def deleteMachine(request, pk):
    machines = Machine.objects.get(id=pk)
    
    if request.method == 'POST':
        machines.delete()
        return redirect('suppliers')
 
    context = {'object': machines}
    return render(request, 'delete_form.html', context)

# Product Model CRUD:
@login_required(login_url='login')
def createProduct(request): 
    products = Product.objects.all
    form = ProductForm()

    if request.user.is_superuser:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.owner = products
                post.save()
            return redirect('suppliers')

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

        return redirect('suppliers')
 
    context = {'form': form, 'products': products, 'product': product}
    return render(request, 'suppliers/supplier_form.html', context)

@login_required(login_url='login')
def deleteProduct(request, pk):
    products = Product.objects.get(id=pk)
    
    if request.method == 'POST':
        products.delete()
        return redirect('suppliers')
 
    context = {'object': products}
    return render(request, 'delete_form.html', context)

