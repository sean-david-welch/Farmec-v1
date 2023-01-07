from django.urls import path
from . import views

urlpatterns = [
    path('suppliers/', views.suppliers, name='suppliers'),
    path('supplier/<str:pk>/', views.supplier, name='supplier'),
    path('machine/<str:pk>/', views.machine, name='machine'),

]