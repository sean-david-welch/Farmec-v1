from django.shortcuts import render
from . models import Supplier, Product

# Create your views here.
def suppliers(request):
    suppliers = Supplier.objects.all()

    context = {'supplier': suppliers}
    return render(request, 'suppliers/suppliers.html', context)