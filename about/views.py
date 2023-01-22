from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Employee, Timeline, Privacy, Terms
from . forms import EmployeeForm, TimelineForm, PriacyForm, TermsForm
from suppliers.models import Supplier
from spareparts.models import SupplierPage

# Create your views here.
def about(request):
    employee = Employee.objects.all()
    timeline = Timeline.objects.all()
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 

    context = {'employee': employee, 'suppliers': suppliers, 'spareparts': spareparts, 'timeline': timeline,}
    return render(request, 'about/about.html', context)

def terms(request):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 
    terms = Terms.objects.all()

    context = {'suppliers': suppliers, 'spareparts': spareparts, 'terms': terms,}
    return render(request, 'about/terms.html', context)

def privacy(request):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 
    privacy = Privacy.objects.all()

    context = {'suppliers': suppliers, 'spareparts': spareparts, 'privacy': privacy,}
    return render(request, 'about/privacy.html', context)

# Employee Model CRUD:
@login_required(login_url='login')
def createEmployee(request): 
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 
    employees = Employee.objects.all
    form = EmployeeForm()

    if request.user.is_superuser:
        if request.method == 'POST':
            form = EmployeeForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.owner = employees
                post.save()
                return redirect('about')

    context = {'form': form, 'employees': employees, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'about/about_form.html', context)

@login_required(login_url='login')
def updateEmployee(request, pk):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 
    employees = Employee.objects.all
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    
    if request.method == 'POST':

        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            employees = form.save()

        return redirect('about')
 
    context = {'form': form, 'employees': employees, 'employee':employee, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'about/about_form.html', context)

@login_required(login_url='login')
def deleteEmployee(request, pk):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 
    employees = Employee.objects.get(id=pk)
    
    if request.method == 'POST':
        employees.delete()
        return redirect('about')
 
    context = {'object': employees, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'delete_form.html', context)

# Timeline Model CRUD:
@login_required(login_url='login')
def createTimeline(request): 
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 
    timelines = Timeline.objects.all
    form = TimelineForm()

    if request.user.is_superuser:
        if request.method == 'POST':
            form = TimelineForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.owner = timelines
                post.save()
                return redirect('about')

    context = {'form': form, 'timelines': timelines, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'about/about_form.html', context)

@login_required(login_url='login')
def updateTimeline(request, pk):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 
    timelines = Timeline.objects.all
    timeline = Timeline.objects.get(id=pk)
    form = TimelineForm(instance=timeline)
    
    if request.method == 'POST':

        form = TimelineForm(request.POST, request.FILES, instance=timeline)
        if form.is_valid():
            timelines = form.save()

        return redirect('about')
 
    context = {'form': form, 'timelines': timelines, 'timeline':timeline, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'about/about_form.html', context)

@login_required(login_url='login')
def deleteTimeline(request, pk):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 
    timelines = Timeline.objects.get(id=pk)
    
    if request.method == 'POST':
        timelines.delete()
        return redirect('about')
 
    context = {'object': timelines, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'delete_form.html', context)

# Privacy Model CRUD:
@login_required(login_url='login')
def createPrivacy(request): 
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 
    privacys = Privacy.objects.all
    form = PriacyForm()

    if request.user.is_superuser:
        if request.method == 'POST':
            form = PriacyForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.owner = privacys
                post.save()
                return redirect('privacy')

    context = {'form': form, 'privacys': privacys, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'about/about_form.html', context)

@login_required(login_url='login')
def updatePrivacy(request, pk):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 
    privacys = Privacy.objects.all
    privacy = Privacy.objects.get(id=pk)
    form = PriacyForm(instance=privacy)
    
    if request.method == 'POST':

        form = PriacyForm(request.POST, request.FILES, instance=privacy)
        if form.is_valid():
            privacys = form.save()

        return redirect('privacy')
 
    context = {'form': form, 'privacys': privacys, 'privacy':privacy, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'about/about_form.html', context)

@login_required(login_url='login')
def deletePrivacy(request, pk):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 
    privacy = Privacy.objects.get(id=pk)
    
    if request.method == 'POST':
        privacy.delete()
        return redirect('privacy')
 
    context = {'object': privacy, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'delete_form.html', context)

# Terms Model CRUD:
@login_required(login_url='login')
def createTerms(request): 
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 
    terms = Terms.objects.all
    form = TermsForm()

    if request.user.is_superuser:
        if request.method == 'POST':
            form = TermsForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.owner = terms
                post.save()
                return redirect('terms')

    context = {'form': form, 'terms': terms, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'about/about_form.html', context)

@login_required(login_url='login')
def updateTerms(request, pk):
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 
    terms = Terms.objects.all
    term = Terms.objects.get(id=pk)
    form = TermsForm(instance=term)
    
    if request.method == 'POST':

        form = TermsForm(request.POST, request.FILES, instance=term)
        if form.is_valid():
            terms = form.save()

        return redirect('terms')
 
    context = {'form': form, 'terms': terms, 'term':term, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'about/about_form.html', context)

@login_required(login_url='login')
def deleteTerms(request, pk):
    term = Terms.objects.get(id=pk)
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all() 
    
    if request.method == 'POST':
        term.delete()
        return redirect('terms')
 
    context = {'object': term, 'suppliers': suppliers, 'spareparts': spareparts}
    return render(request, 'delete_form.html', context)