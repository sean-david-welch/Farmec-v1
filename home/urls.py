from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUser, name='register'),

    path('profiles/', views.profiles, name='profiles'),
    path('update-profile/<str:pk>/', views.updateProfile, name='update-profile'),
    path('delete-profile/<str:pk>/', views.deleteProfile, name='delete-profile'),

    path('displays', views.displays, name='displays'),
    
    path('create-stat/', views.createStat, name='create-stat'),
    path('update-stat/<str:pk>/', views.updateStat, name='update-stat'),
    path('delete-stat/<str:pk>/', views.deleteStat, name='delete-stat'),

    path('create-special/', views.createSpecial, name='create-special'),
    path('update-special/<str:pk>/', views.updateSpecial, name='update-special'),
    path('delete-special/<str:pk>/', views.deleteSpecial, name='delete-special'),
]