from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),

    path('home/', include('home.urls')),
    path('home/', include('about.urls')),
    path('home/', include('blog.urls')),
    path('home/', include('payments.urls')),
    path('home/', include('spareparts.urls')),
    path('home/', include('suppliers.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
