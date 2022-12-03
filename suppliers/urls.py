from django.urls import path
from . import views

urlpatterns = [
    path('suppliers/', views.suppliers, name='suppliers'),
]