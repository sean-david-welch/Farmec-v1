from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from . models import SupplierPage, PartsPage, WarrantyClaim, MachineRegistration
from . models import PartsRequired
from . forms import WarrantyClaimForm, SupplierPageForm, PartsPageForm, MachineRegistrationForm
from suppliers.models import Supplier

# Create your views here.
def spareparts(request):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()

    context = {'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'spareparts/spare-parts.html', context)

def partspage(request, pk):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()
    supplierpage = SupplierPage.objects.get(id=pk)

    context = {'suppliers': suppliers, 'partspage': partspage, 'supplierpage': supplierpage, 'spareparts': spareparts}
    return render(request, 'spareparts/parts-page.html', context)

## Warranty Form
# @login_required(login_url='login')
# def createWarranty(request): 
#     warranty = WarrantyClaim.objects.all
#     form = WarrantyClaimForm()

#     if request.user.is_superuser:
#         if request.method == 'POST':
#             form = WarrantyClaimForm(request.POST, request.FILES)

#             if form.is_valid():
#                 post = form.save(commit=False)
#                 post.owner = warranty
#                 post.save()
#             return redirect('spare-parts')

#     context = {'form': form, 'warranty': warranty}
#     return render(request, 'spareparts/parts_form.html', context)

@login_required(login_url='login')
def createWarranty(request):
    WarrantyClaimFormSet = inlineformset_factory(WarrantyClaim, PartsRequired, fields=('__all__'))
    warranty = WarrantyClaim.objects.all
    form = WarrantyClaimForm()
    formset = WarrantyClaimFormSet()

    if request.user.is_superuser:
        if request.method == 'POST':
            formset = WarrantyClaimFormSet(request.POST, request.FILES)

            if formset.is_valid():
                post = formset.save(commit=False)
                post.owner = warranty
                post.save()
            return redirect('spare-parts')

    context = {'formset': formset, 'warranty': warranty, 'form': form}
    return render(request, 'spareparts/parts_form.html', context)



## Machine Registration Form:
@login_required(login_url='login')
def createRegistration(request):
    registration = MachineRegistration.objects.all()
    form = MachineRegistrationForm()

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = MachineRegistrationForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.owner = registration
                post.save()
            return redirect('spare-parts')

    context = {'form': form, 'registration': registration}
    return render(request, 'spareparts/page_form.html', context)

# Supplier Page Form
@login_required(login_url='login')
def createPageform(request): 
    supplierspage = SupplierPage.objects.all
    form = SupplierPageForm()

    if request.user.is_superuser:
        if request.method == 'POST':
            form = SupplierPageForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.owner = supplierspage
                post.save()
            return redirect('spare-parts')

    context = {'form': form, 'supplierspage': supplierspage}
    return render(request, 'spareparts/page_form.html', context)

@login_required(login_url='login')
def updatePageform(request, pk):
    supplierspages = SupplierPage.objects.all
    supplierspage = SupplierPage.objects.get(id=pk)

    form = SupplierPageForm(instance=supplierspage)
    
    if request.method == 'POST':

        form = SupplierPageForm(request.POST, request.FILES, instance=supplierspage)
        if form.is_valid():
            suppliers = form.save()

        return redirect('spare-parts')
 
    context = {'form': form, 'supplierspages': supplierspages, 'supplierspage':supplierspage}
    return render(request, 'spareparts/page_form.html', context)


@login_required(login_url='login')
def deletePageform(request, pk):
    supplierspage = SupplierPage.objects.get(id=pk)
    
    if request.method == 'POST':
        supplierspage.delete()
        return redirect('spare-parts')
 
    context = {'object': supplierspage}
    return render(request, 'delete_form.html', context)