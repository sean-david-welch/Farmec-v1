from django.urls import path
from . import views

urlpatterns = [
    path('spare-parts/', views.spareparts, name='spare-parts'),
    path('parts-page/<str:pk>/', views.partspage, name='parts-page'),

    path('warranty-claims/', views.warrantyclaims, name='warranty-claims'),
    path('single-warranty/<str:pk>/', views.singlewarranty, name='single-warranty'),
    path('create-warranty/', views.createWarranty, name='create-warranty'),

    path('machine-registration/', views.machinereg, name='machine-registration'),
    path('regsingle/<str:pk>/', views.regsingle, name='regsingle'),
    path('create-registration/', views.createRegistration, name='create-registration'),
    path('update-registration/<str:pk>/', views.updateRegistration, name='update-registration'),
    path('delete-registration/<str:pk>/', views.deleteRegistration, name='delete-registration'),

    path('create-supplier-page/', views.createPageform, name='create-supplier-page'),
    path('update-supplier-page/<str:pk>/', views.updatePageform, name='update-supplier-page'),
    path('delete-supplier-page/<str:pk>/', views.deletePageform, name='delete-supplier-page'),

    path('create-parts-page/', views.createPartsform, name='create-parts-page'),
    path('update-parts-page/<str:pk>/', views.updatePartsform, name='update-parts-page'),
    path('delete-parts-page/<str:pk>/', views.deletePartsform, name='delete-parts-page'),

]