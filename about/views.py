from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Employee, Timeline, Privacy, Terms
from . forms import EmployeeForm, TimelineForm, PriacyForm, TermsForm

# Create your views here.
def about(request):
    employee = Employee.objects.all()
    timeline = Timeline.objects.all()

    context = {'employee': employee, 'timeline': timeline,}
    return render(request, 'about/about.html', context)

def terms(request):
    terms = Terms.objects.all()

    context = {'terms': terms}
    return render(request, 'about/terms.html', context)

def privacy(request):
    privacy = Privacy.objects.all()

    context = {'privacy': privacy}
    return render(request, 'about/privacy.html', context)

# Employee Model CRUD:
@login_required(login_url='login')
def createEmployee(request): 

    employees = Employee.objects.all
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = employees
            post.save()
            return redirect('about')

    context = {'form': form, 'employees': employees}
    return render(request, 'about/about_form.html', context)

@login_required(login_url='login')
def updateEmployee(request, pk):

    employees = Employee.objects.all
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    
    if request.method == 'POST':

        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            employees = form.save()

        return redirect('about')
 
    context = {'form': form, 'employees': employees, 'employee':employee}
    return render(request, 'about/about_form.html', context)

@login_required(login_url='login')
def deleteEmployee(request, pk):
    employees = Employee.objects.get(id=pk)
    
    if request.method == 'POST':
        employees.delete()
        return redirect('about')
 
    context = {'object': employees}
    return render(request, 'delete_form.html', context)

# Timeline Model CRUD:
@login_required(login_url='login')
def createTimeline(request): 
    timelines = Timeline.objects.all
    form = TimelineForm()

    if request.method == 'POST':
        form = TimelineForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = timelines
            post.save()
            return redirect('about')

    context = {'form': form, 'timelines': timelines}
    return render(request, 'about/about_form.html', context)

@login_required(login_url='login')
def updateTimeline(request, pk):
    timelines = Timeline.objects.all
    timeline = Timeline.objects.get(id=pk)
    form = TimelineForm(instance=timeline)
    
    if request.method == 'POST':

        form = TimelineForm(request.POST, request.FILES, instance=timeline)
        if form.is_valid():
            timelines = form.save()

        return redirect('about')
 
    context = {'form': form, 'timelines': timelines, 'timeline':timeline}
    return render(request, 'about/about_form.html', context)

@login_required(login_url='login')
def deleteTimeline(request, pk):
    timelines = Timeline.objects.get(id=pk)
    
    if request.method == 'POST':
        timelines.delete()
        return redirect('about')
 
    context = {'object': timelines}
    return render(request, 'delete_form.html', context)

# Privacy Model CRUD:
@login_required(login_url='login')
def createPrivacy(request): 
    privacys = Privacy.objects.all
    form = PriacyForm()

    if request.method == 'POST':
        form = PriacyForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = privacys
            post.save()
            return redirect('privacy')

    context = {'form': form, 'privacys': privacys}
    return render(request, 'about/about_form.html', context)

@login_required(login_url='login')
def updatePrivacy(request, pk):
    privacys = Privacy.objects.all
    privacy = Privacy.objects.get(id=pk)
    form = PriacyForm(instance=privacy)
    
    if request.method == 'POST':

        form = PriacyForm(request.POST, request.FILES, instance=privacy)
        if form.is_valid():
            privacys = form.save()

        return redirect('privacy')
 
    context = {'form': form, 'privacys': privacys, 'privacy':privacy}
    return render(request, 'about/about_form.html', context)

@login_required(login_url='login')
def deletePrivacy(request, pk):
    privacy = Privacy.objects.get(id=pk)
    
    if request.method == 'POST':
        privacy.delete()
        return redirect('privacy')
 
    context = {'object': privacy}
    return render(request, 'delete_form.html', context)

# Terms Model CRUD:
@login_required(login_url='login')
def createTerms(request): 
    terms = Terms.objects.all
    form = TermsForm()

    if request.method == 'POST':
        form = TermsForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = terms
            post.save()
            return redirect('terms')

    context = {'form': form, 'terms': terms}
    return render(request, 'about/about_form.html', context)

@login_required(login_url='login')
def updateTerms(request, pk):
    terms = Terms.objects.all
    term = Terms.objects.get(id=pk)
    form = TermsForm(instance=term)
    
    if request.method == 'POST':

        form = TermsForm(request.POST, request.FILES, instance=term)
        if form.is_valid():
            terms = form.save()

        return redirect('terms')
 
    context = {'form': form, 'terms': terms, 'term':term}
    return render(request, 'about/about_form.html', context)

@login_required(login_url='login')
def deleteTerms(request, pk):
    term = Terms.objects.get(id=pk)
    
    if request.method == 'POST':
        term.delete()
        return redirect('terms')
 
    context = {'object': term}
    return render(request, 'delete_form.html', context)