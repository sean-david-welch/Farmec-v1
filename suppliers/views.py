from django.shortcuts import render
from . models import Supplier, Fact

# Create your views here.
def suppliers(request):
    suppliers = Supplier.objects.all()

    context = {'suppliers': suppliers}
    return render(request, 'suppliers/suppliers.html', context)

def single_supplier(request, pk):
    supplier = Supplier.objects.get(id=pk)

    context = {'supplier': supplier}
    return render(request, 'suppliers/single-supplier.html', context)