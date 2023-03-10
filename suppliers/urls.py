from django.urls import path
from . import views

urlpatterns = [
    path('suppliers/', views.suppliers, name='suppliers'),
    path('supplier/<str:pk>/', views.supplier, name='supplier'),
    path('machine/<str:pk>/', views.machine, name='machine'),


    path('create-supplier/', views.createSupplier, name='create-supplier'),
    path('update-supplier/<str:pk>/', views.updateSupplier, name='update-supplier'),
    path('delete-supplier/<str:pk>/', views.deleteSupplier, name='delete-supplier'),

    path('create-machine/<str:pk>/', views.createMachine, name='create-machine'),
    path('update-machine/<str:pk>/', views.updateMachine, name='update-machine'),
    path('delete-machine/<str:pk>/', views.deleteMachine, name='delete-machine'),

    path('create-product/<str:pk>/', views.createProduct, name='create-product'),
    path('update-product/<str:pk>/', views.updateProduct, name='update-product'),
    path('delete-product/<str:pk>/', views.deleteProduct, name='delete-product'),
]