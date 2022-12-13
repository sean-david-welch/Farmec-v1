from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blogs, name='blogs'),
    path('blog/<str:pk>/', views.blog, name='blog'),
    path('update-blog/<str:pk>/', views.updateBlog, name='update-blog'),
    path('create-blog/', views.createBlog, name='create-blog')
]