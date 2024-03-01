from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from . import views
from .sitemaps import StaticViewSitemap
sitemaps = {
    'static': StaticViewSitemap
}
urlpatterns = [
    path('', views.home, name='home'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),

    path('admin/', admin.site.urls, name='admin'),

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),

    path('home/', include('home.urls')),
    path('about/', include('about.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('blog/', include('blog.urls')),
    path('spareparts/', include('spareparts.urls')),
    path('payments/', include('payments.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)