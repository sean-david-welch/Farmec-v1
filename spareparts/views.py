from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import SupplierPage, PartsPage, WarrantyClaim, PartsRequired, MachineRegistration
from . forms import WarrantyClaimForm, PartsRequiredFormSet
from suppliers.models import Supplier

# Create your views here.
def spareparts(request):
    suppliers = Supplier.objects.all()
    supplierpage = SupplierPage.objects.all()
    parts = Supplier.objects.all()

    context = {'suppliers': suppliers, 'supplierpage': supplierpage, 'parts': parts}
    return render(request, 'spareparts/spare-parts.html', context)

@login_required(login_url='login')
def createWarranty(request): 
    warranty = WarrantyClaim.objects.all()
    form = WarrantyClaimForm()
    formset = PartsRequiredFormSet(instance=WarrantyClaim())

    if request.user.is_superuser:
        if request.method == 'POST':
            form = WarrantyClaimForm(request.POST, request.FILES)
            formset = PartsRequiredFormSet(request.POST, request.FILES, instance=WarrantyClaim())
            if form.is_valid() and formset.is_valid():
                post = form.save(commit=False)
                post.owner = request.user
                post.save()
                formset = PartsRequiredFormSet(request.POST, instance=post)
                formset.save()
            return redirect('spare-parts')

    context = {'form': form, 'formset': formset, 'warranty': warranty}
    return render(request, 'spareparts/parts_form.html', context)