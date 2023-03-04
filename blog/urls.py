from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blogs, name='blogs'),
    path('blog/<str:pk>/', views.blog, name='blog'),

    path('exhibitions/', views.exhibitions, name='exhibitions'),

    path('create-blog/', views.createBlog, name='create-blog'),
    path('update-blog/<str:pk>/', views.updateBlog, name='update-blog'),
    path('delete-blog/<str:pk>/', views.deleteBlog, name='delete-blog'),

    path('create-exhibition/', views.createExhibition, name='create-exhibition'),
    path('update-exhibition/<str:pk>/', views.updateExhibition, name='update-exhibition'),
    path('delete-exhibition/<str:pk>/', views.deleteExhibition, name='delete-exhibition'),
]