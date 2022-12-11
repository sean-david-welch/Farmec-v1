from django.shortcuts import render
from django.http import JsonResponse
from . models import Supplier

# Create your views here.
def suppliers(request):
    suppliers = Supplier.objects.all()

    context = {'suppliers': suppliers}
    return render(request, 'suppliers/suppliers.html', context)

def supplier(request, pk):
    supplier = Supplier.objects.get(id=pk)

    context = {'supplier': supplier}
    return render(request, 'suppliers/supplier.html', context)
