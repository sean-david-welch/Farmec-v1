from django.urls import path
from . import views

urlpatterns = [
    path('payments/', views.payments, name='payments'),
    path('charge/', views.charge, name='charge'),
    path('success/<str:args>/', views.successMsg, name='success')
]