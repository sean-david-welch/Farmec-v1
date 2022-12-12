from django.shortcuts import render

from suppliers.models import Supplier

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

# def navbar(request, pk):
#     supplier = Supplier.objects.get(id=pk)

#     context = {'supplier': supplier}
#     return render(request, 'navbar.html', context)



