from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('timeline/', views.timeline, name='timeline')
]