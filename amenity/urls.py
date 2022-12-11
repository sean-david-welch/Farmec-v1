from django.urls import path 
from . import views

urlpatterns = [
    path('amenity/', views.amenity, name='amenity'),
]