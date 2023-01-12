from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Employee, Timeline
from . forms import EmployeeForm, TimelineForm
from suppliers.models import Supplier

# Create your views here.
def about(request):
    employee = Employee.objects.all()
    timeline = Timeline.objects.all()
    suppliers = Supplier.objects.all()

    context = {'employee': employee, 'suppliers': suppliers, 'timeline': timeline,}
    return render(request, 'about/about.html', context)

# Employee Model CRUD:
@login_required(login_url='login')
def createEmployee(request): 
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

    if request.user.is_superuser:
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