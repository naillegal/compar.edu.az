"""compar_new URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from os import getenv
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from compar_new.sitemaps import ArticleSitemap, CategorySitemap, StaticViewSitemap, TagSitemap
from django.conf.urls.i18n import i18n_patterns
from . import views

sitemaps = {
    'static': StaticViewSitemap,
    'article': ArticleSitemap,
    'tag': TagSitemap,
    'category': CategorySitemap
}

urlpatterns = [
    # path('robots.txt', TemplateView.as_view('')),
    path(getenv('ADMIN_URL'), admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'), name='robots'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
] + static(settings.MEDIA_URL)




handler404 = 'compar_new.views.handler_error_view'
handler500  = 'compar_new.views.handler_error_view'


urlpatterns += i18n_patterns(
    path('blog/', include('blog.urls')),
    path('events/', include('event.urls')),
    path('', include('promotion.urls')),
    path('courses/', include('course.urls')),
)