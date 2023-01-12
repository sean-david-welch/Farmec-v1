from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),

    path('create-employee/', views.createEmployee, name='create-employee'),
    path('update-employee/<str:pk>/', views.updateEmployee, name='update-employee'),
    path('delete-employee/<str:pk>/', views.deleteEmployee, name='delete-employee'),

    path('create-timeline/', views.createTimeline, name='create-timeline'),
    path('update-timeline/<str:pk>/', views.updateTimeline, name='update-timeline'),
    path('delete-timeline/<str:pk>/', views.deleteTimeline, name='delete-timeline'),
]