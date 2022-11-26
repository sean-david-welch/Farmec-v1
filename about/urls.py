from django.urls import path
from . import views

# Create your Views here
urlpatterns = [
    path('about/', views.about, name='about'),
]