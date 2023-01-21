from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from django.forms.models import inlineformset_factory
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

    context = {'suppliers': suppliers, 'supplierpage': supplierpage, 'spareparts': spareparts}
    return render(request, 'spareparts/parts-page.html', context)

def warrantyclaims(request):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()
    warranty = WarrantyClaim.objects.all()

    context = {'suppliers': suppliers, 'warranty': warranty, 'spareparts': spareparts}
    return render(request, 'spareparts/warranty_claims.html', context)

def singlewarranty(request, pk):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()
    singlewarranty = WarrantyClaim.objects.get(id=pk)
    partsrequired = PartsRequired.objects.all()

    context = {'suppliers': suppliers, 'singlewarranty': singlewarranty, 'spareparts': spareparts, 'partsrequired': partsrequired}
    return render(request, 'spareparts/claim_single.html', context)

def machinereg(request):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()
    machinereg = MachineRegistration.objects.all()

    context = {'suppliers': suppliers, 'machinereg': machinereg, 'spareparts': spareparts}
    return render(request, 'spareparts/machine_registrations.html', context)

def regsingle(request, pk):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()
    regsingle = MachineRegistration.objects.get(id=pk)

    context = {'suppliers': suppliers, 'regsingle': regsingle, 'spareparts': spareparts}
    return render(request, 'spareparts/reg_single.html', context)

@login_required(login_url='login')
def createWarranty(request):
    warranty = WarrantyClaim.objects.all()
    form = WarrantyClaimForm()
    warrantyformset = inlineformset_factory(WarrantyClaim, PartsRequired, form=WarrantyClaimForm, extra=1)

    if request.user.is_superuser:
        if request.method == 'POST':
            form = WarrantyClaimForm(request.POST, request.FILES)
            formset = warrantyformset(request.POST, request.FILES, instance=WarrantyClaim())
            if form.is_valid() and formset.is_valid():
                post = form.save(commit=False)
                post.owner = request.user
                post.save()
                formset.instance = post
                formset.save()
            return redirect('spare-parts')

    context = {'warranty': warranty, 'form': form, 'formset': warrantyformset}
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

@login_required(login_url='login')
def updateRegistration(request, pk):
    registrations = MachineRegistration.objects.all
    regsingle = MachineRegistration.objects.get(id=pk)

    form = MachineRegistrationForm(instance=regsingle)
    
    if request.method == 'POST':

        form = MachineRegistrationForm(request.POST, request.FILES, instance=regsingle)
        if form.is_valid():
            suppliers = form.save()

        return redirect('spare-parts')
 
    context = {'form': form, 'registrations': registrations, 'regsingle':regsingle}
    return render(request, 'spareparts/page_form.html', context)


@login_required(login_url='login')
def deleteRegistration(request, pk):
    regsingle = MachineRegistration.objects.get(id=pk)
    
    if request.method == 'POST':
        regsingle.delete()
        return redirect('spare-parts')
 
    context = {'object': regsingle}
    return render(request, 'delete_form.html', context)

# Supplier Page Form
@login_required(login_url='login')
def createPageform(request): 
    supplierspage = SupplierPage.objects.all()
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

# Parts Pages Form 
@login_required(login_url='login')
def createPartsform(request): 
    partspage = PartsPage.objects.all
    form = PartsPageForm()

    if request.user.is_superuser:
        if request.method == 'POST':
            form = PartsPageForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.owner = partspage
                post.save()
            return redirect('spare-parts')

    context = {'form': form, 'partspage': partspage}
    return render(request, 'spareparts/page_form.html', context)

@login_required(login_url='login')
def updatePartsform(request, pk):
    supplierspages = PartsPage.objects.all
    partspage = PartsPage.objects.get(id=pk)

    form = PartsPageForm(instance=partspage)
    
    if request.method == 'POST':

        form = PartsPageForm(request.POST, request.FILES, instance=partspage)
        if form.is_valid():
            suppliers = form.save()

        return redirect('spare-parts')
 
    context = {'form': form, 'supplierspages': supplierspages, 'partspage':partspage}
    return render(request, 'spareparts/page_form.html', context)


@login_required(login_url='login')
def deletePartsform(request, pk):
    partspage = PartsPage.objects.get(id=pk)
    
    if request.method == 'POST':
        partspage.delete()
        return redirect('spare-parts')
 
    context = {'object': partspage}
    return render(request, 'delete_form.html', context)