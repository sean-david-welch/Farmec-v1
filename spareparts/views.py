from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import SupplierPage, PartsPage, WarrantyClaim, PartsRequired, MachineRegistration
from . forms import WarrantyClaimForm, PartsRequiredFormSet, SupplierPageForm, PartsPageForm
from suppliers.models import Supplier

# Create your views here.
def spareparts(request):
    suppliers = Supplier.objects.all()
    supplierpage = SupplierPage.objects.all()

    context = {'suppliers': suppliers, 'supplierpage': supplierpage}
    return render(request, 'spareparts/spare-parts.html', context)

def partspage(request, pk):
    suppliers = Supplier.objects.all()
    supplierpage = SupplierPage.objects.get(id=pk)

    context = {'suppliers': suppliers, 'partspage': partspage, 'supplierpage': supplierpage}
    return render(request, 'spareparts/parts-page.html', context)

# Warranty Form
@login_required(login_url='login')
def createWarranty(request): 
    warranty = WarrantyClaim.objects.all
    form = WarrantyClaimForm()
    formset = PartsRequiredFormSet(instance=WarrantyClaim())

    if request.user.is_superuser:
        if request.method == 'POST':
            form = WarrantyClaimForm(request.POST, request.FILES)
            formset = PartsRequiredFormSet(request.POST, request.FILES, instance=WarrantyClaim())
            if form.is_valid() and formset.is_valid():
                post = form.save(commit=False)
                post.owner = warranty
                post.save()
                formset = PartsRequiredFormSet(request.POST, instance=post)
                formset.save()
            return redirect('spare-parts')

    context = {'form': form, 'formset': formset, 'warranty': warranty}
    return render(request, 'spareparts/parts_form.html', context)

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