from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),

    path('create-employee/', views.createEmployee, name='create-employee'),
    path('update-employee/<str:pk>/', views.updateEmployee, name='update-employee'),
    path('delete-employee/<str:pk>/', views.deleteEmployee, name='delete-employee'),

    path('create-timeline/', views.createTimeline, name='create-timeline'),
    path('update-timeline/<str:pk>/', views.updateTimeline, name='update-timeline'),
    path('delete-timeline/<str:pk>/', views.deleteTimeline, name='delete-timeline'),

    path('create-privacy/', views.createPrivacy, name='create-privacy'),
    path('update-privacy/<str:pk>/', views.updatePrivacy, name='update-privacy'),
    path('delete-privacy/<str:pk>/', views.deletePrivacy, name='delete-privacy'),

    path('create-terms/', views.createTerms, name='create-terms'),
    path('update-terms/<str:pk>/', views.updateTerms, name='update-terms'),
    path('delete-terms/<str:pk>/', views.deleteTerms, name='delete-terms'),
]