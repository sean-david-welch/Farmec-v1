from django.urls import path 
from . import views

urlpatterns = [
    path('amenitys/', views.amenitys, name='amenitys'),
    path('amenity/<str:pk>/', views.amenity, name='amenity'),
]