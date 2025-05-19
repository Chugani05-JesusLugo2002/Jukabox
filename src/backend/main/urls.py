"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect

import shared.views

urlpatterns = [
    path('', lambda _: redirect('admin/')),
    path('admin/', admin.site.urls),
    path('django-rq/', include('django_rq.urls')),
    path('api/v1/songs/', include('songs.urls')),
    path('api/v1/artists/', include('artists.urls')),
    path('api/v1/albums/', include('albums.urls')),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/import/', include('importer.urls')),
    path('api/v1/explore/', shared.views.explore, name='explorer')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
