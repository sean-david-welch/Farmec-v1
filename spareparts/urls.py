from django.urls import path
from . import views

urlpatterns = [
    path('spare-parts/', views.spareparts, name='spare-parts'),
    path('parts-page/<str:pk>/', views.partspage, name='parts-page'),

    path('create-warranty/', views.createWarranty, name='create-warranty'),

    path('create-registration/', views.createRegistration, name='create-registration'),

    path('create-supplier-page/', views.createPageform, name='create-supplier-page'),
    path('update-supplier-page/<str:pk>/', views.updatePageform, name='update-supplier-page'),
    path('delete-supplier-page/<str:pk>/', views.deletePageform, name='delete-supplier-page'),

]