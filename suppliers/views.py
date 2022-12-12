from django.shortcuts import render
from . models import Supplier, Product, Machine

# Create your views here.
def suppliers(request):
    suppliers = Supplier.objects.all()

    context = {'suppliers': suppliers}
    return render(request, 'suppliers/suppliers.html', context)

def supplier(request, pk):
    supplier = Supplier.objects.get(id=pk)

    context = {'supplier': supplier}
    return render(request, 'suppliers/supplier.html', context)

def machine(request, pk):
    machine = Machine.objects.get(id=pk)

    context = {'machine': machine}
    return render(request, 'suppliers/machine.html', context)
