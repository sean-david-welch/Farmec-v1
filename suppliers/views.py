from django.shortcuts import render
from . models import Supplier, Product, Machine
from suppliers.models import Supplier
from amenity.models import Amenity



# Create your views here.
def suppliers(request):
    suppliers = Supplier.objects.all()
    amenitys = Amenity.objects.all()

    context = {'suppliers': suppliers, 'amenitys': amenitys}
    return render(request, 'suppliers/suppliers.html', context)

def supplier(request, pk):
    supplier = Supplier.objects.get(id=pk)
    suppliers = Supplier.objects.all()
    amenitys = Amenity.objects.all()


    context = {'supplier': supplier, 'suppliers': suppliers, 'amenitys': amenitys}
    return render(request, 'suppliers/supplier.html', context)

def machine(request, pk):
    machine = Machine.objects.get(id=pk)
    suppliers = Supplier.objects.all()
    amenitys = Amenity.objects.all()


    context = {'machine': machine, 'suppliers': suppliers, 'amenitys': amenitys}
    return render(request, 'suppliers/machine.html', context)

