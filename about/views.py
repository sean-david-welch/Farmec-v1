from django.shortcuts import render
from . models import Staff


# Create your views here.
def about(request):
    staff = Staff.objects.all()

    context = {'staff': staff}
    return render(request, 'about/about.html', context)

# def timeline(request):
#     timelines = Timeline.objects.all()

#     context = {'timelines': timelines}
#     return render(request, 'teams/teams.html', context)