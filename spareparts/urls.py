from django.urls import path
from . import views

urlpatterns = [
    path('spare-parts/', views.spareparts, name='spare-parts'),

    path('create-warranty/', views.createWarranty, name='create-warranty'),
]