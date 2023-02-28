from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from django.forms.models import inlineformset_factory
from django.core.mail import send_mail
from django.contrib import messages

from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader

from django.conf import settings

from io import BytesIO

from . models import SupplierPage, PartsPage, WarrantyClaim, MachineRegistration
from . models import PartsRequired
from . forms import WarrantyClaimForm, SupplierPageForm, PartsPageForm, MachineRegistrationForm
from suppliers.models import Supplier

# Create your views here.


def generate_pdf(request, pk):
    regsingle = MachineRegistration.objects.get(id=pk)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="machine_registration.pdf"'

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)

    # Add image at the top
    canvas_width, canvas_height = A4
    logo_width, logo_height = 250, 60
    logo_x = (canvas_width - logo_width) / 2

    logo = ImageReader(settings.BASE_DIR / 'static' / 'images' / 'farmeclogo.png')
    pdf.drawImage(logo, logo_x, canvas_height - 100, width=logo_width, height=logo_height)


    # Print registration fields
    y_coordinate = 700
    for field in MachineRegistration._meta.get_fields():
        if field.name == 'id':
            continue
        pdf.drawString(100, y_coordinate, "{}: {}".format(field.verbose_name.title(), getattr(regsingle, field.name)))
        y_coordinate -= 20

    pdf.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='machine_registration.pdf')


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

# Create Warranty Form:
@login_required(login_url='login')
def createWarranty(request):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()
    warranty = WarrantyClaim.objects.all()
    form = WarrantyClaimForm()
    warrantyformset = inlineformset_factory(WarrantyClaim, PartsRequired, form=WarrantyClaimForm, extra=1)

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = WarrantyClaimForm(request.POST, request.FILES)
            formset = warrantyformset(request.POST, request.FILES, instance=WarrantyClaim())
            if form.is_valid() and formset.is_valid():
                post = form.save(commit=False)
                post.owner = request.user
                post.save()
                formset.instance = post
                formset.save()
                send_mail(
                'Warranty Claim Form Created by: ' + post.completed_by,
                f'A new warranty claim form has been filed by {post.completed_by}! Make sure to log in and check the details at: http://127.0.0.1:8000/spareparts/warranty-claims/', 
                'jennie@farmec.ie',
                ['jennie@farmec.ie'],
                fail_silently=False,
                )
                return redirect('spare-parts')
            else:
                messages.error(request, 'Field format is not valid')

    context = {'warranty': warranty, 'form': form, 'formset': warrantyformset, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'spareparts/parts_form.html', context)

@login_required(login_url='login')
def updateWarranty(request, pk):
    warrantysingle = WarrantyClaim.objects.get(id=pk)
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()

    form = WarrantyClaimForm(instance=warrantysingle)
    warrantyformset = inlineformset_factory(WarrantyClaim, PartsRequired, form=WarrantyClaimForm, extra=1)
    formset = warrantyformset(instance=warrantysingle)

    if request.method == 'POST':
        form = WarrantyClaimForm(request.POST, request.FILES, instance=warrantysingle)
        formset = warrantyformset(request.POST, request.FILES, instance=warrantysingle)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
        return redirect('warranty-claims')
 
    context = {'form': form, 'warrantysingle': warrantysingle, 'formset': formset, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'spareparts/parts_form.html', context)

@login_required(login_url='login')
def deleteWarranty(request, pk):
    warrantysingle = WarrantyClaim.objects.get(id=pk)
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()
    
    if request.method == 'POST':
        warrantysingle.delete()
        return redirect('warranty-claims')
 
    context = {'object': warrantysingle, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'delete_form.html', context)

## Machine Registration Form:
@login_required(login_url='login')
def createRegistration(request):
    registration = MachineRegistration.objects.all()
    form = MachineRegistrationForm()
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = MachineRegistrationForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.owner = registration
                post.save()
                send_mail(
                'New Machine Registration Form Created by: ' + post.completed_by,
                f'A new machine registration form has been created by {post.completed_by}! Make sure to log in and check the details at: http://127.0.0.1:8000/spareparts/machine-registration/', 
                'jennie@farmec.ie',
                ['jennie@farmec.ie'],
                fail_silently=False,
                )
                return redirect('spare-parts')
            else:
                messages.error(request, 'Field format is not valid')

    context = {'form': form, 'registration': registration, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'spareparts/page_form.html', context)

@login_required(login_url='login')
def updateRegistration(request, pk):
    registrations = MachineRegistration.objects.all
    regsingle = MachineRegistration.objects.get(id=pk)
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()

    form = MachineRegistrationForm(instance=regsingle)
    
    if request.method == 'POST':

        form = MachineRegistrationForm(request.POST, request.FILES, instance=regsingle)
        if form.is_valid():
            regsingle = form.save()

        return redirect('machine-registration')
 
    context = {'form': form, 'registrations': registrations, 'regsingle': regsingle, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'spareparts/page_form.html', context)


@login_required(login_url='login')
def deleteRegistration(request, pk):
    regsingle = MachineRegistration.objects.get(id=pk)
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()
    
    if request.method == 'POST':
        regsingle.delete()
        return redirect('machine-registration')
 
    context = {'object': regsingle, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'delete_form.html', context)

# Supplier Page Form
@login_required(login_url='login')
def createPageform(request): 
    supplierspage = SupplierPage.objects.all()
    form = SupplierPageForm()
    suppliers = Supplier.objects.all()

    if request.user.is_superuser:
        if request.method == 'POST':
            form = SupplierPageForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.owner = supplierspage
                post.save()
            return redirect('spare-parts')

    context = {'form': form, 'supplierspage': supplierspage, 'suppliers': suppliers}
    return render(request, 'spareparts/page_form.html', context)

@login_required(login_url='login')
def updatePageform(request, pk):
    supplierspages = SupplierPage.objects.all
    suppliers = Supplier.objects.all()
    supplierspage = SupplierPage.objects.get(id=pk)

    form = SupplierPageForm(instance=supplierspage)
    
    if request.method == 'POST':

        form = SupplierPageForm(request.POST, request.FILES, instance=supplierspage)
        if form.is_valid():
            supplierspage = form.save()

        return redirect('spare-parts')
 
    context = {'form': form, 'supplierspages': supplierspages, 'supplierspage': supplierspage, 'suppliers': suppliers}
    return render(request, 'spareparts/page_form.html', context)


@login_required(login_url='login')
def deletePageform(request, pk):
    supplierspage = SupplierPage.objects.get(id=pk)
    suppliers = Supplier.objects.all()
    
    if request.method == 'POST':
        supplierspage.delete()
        return redirect('spare-parts')
 
    context = {'object': supplierspage, 'suppliers': suppliers}
    return render(request, 'delete_form.html', context)

# Parts Pages Form 
@login_required(login_url='login')
def createPartsform(request): 
    partspage = PartsPage.objects.all()
    form = PartsPageForm()
    suppliers = Supplier.objects.all()
    supplierspage = SupplierPage.objects.all()

    if request.user.is_superuser:
        if request.method == 'POST':
            form = PartsPageForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.owner = partspage
                post.save()
            return redirect('spare-parts')

    context = {'form': form, 'partspage': partspage, 'suppliers': suppliers, 'supplierspage': supplierspage}
    return render(request, 'spareparts/page_form.html', context)

@login_required(login_url='login')
def updatePartsform(request, pk):
    supplierspages = SupplierPage.objects.all
    partspage = PartsPage.objects.get(id=pk)
    suppliers = Supplier.objects.all()

    form = PartsPageForm(instance=partspage)
    
    if request.method == 'POST':

        form = PartsPageForm(request.POST, request.FILES, instance=partspage)
        if form.is_valid():
            partspage = form.save()

        return redirect('spare-parts')
 
    context = {'form': form, 'supplierspages': supplierspages, 'partspage': partspage, 'suppliers': suppliers}
    return render(request, 'spareparts/page_form.html', context)


@login_required(login_url='login')
def deletePartsform(request, pk):
    partspage = PartsPage.objects.get(id=pk)
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()
    
    if request.method == 'POST':
        partspage.delete()
        return redirect('spare-parts')
 
    context = {'object': partspage, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'delete_form.html', context)