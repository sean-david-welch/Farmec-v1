from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blogs, name='blogs'),
    path('blog/<str:pk>/', views.blog, name='blog'),
]