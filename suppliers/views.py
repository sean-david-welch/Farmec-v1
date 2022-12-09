from django.shortcuts import render
from . models import Supplier, Fact

# Create your views here.
def suppliers(request):
    suppliers = Supplier.objects.all()

    context = {'suppliers': suppliers}
    return render(request, 'suppliers/suppliers.html', context)

# def sipfacts(request):
#     sipfacts = SipFact.objects.all()

#     context = {'sipfacts': sipfacts}
#     return render(request, 'suppliers/suppliers.html', context)