"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

import gallery.api_views, gallery.views

urlpatterns = [
    path('', gallery.views.home, name='home'),
    path('gallery/', include('gallery.urls')),
    path('admin/', admin.site.urls),
    
    path('api/v1/albums', gallery.api_views.AlbumList.as_view()),
    path('api/v1/albums/new', gallery.api_views.AlbumCreate.as_view()),
    path('api/v1/albums/<int:id>/', gallery.api_views.AlbumRetrieveUpdateDestroy.as_view()),

    path('api/v1/photographs', gallery.api_views.PhotographList.as_view()),
    path('api/v1/photographs/new', gallery.api_views.PhotographCreate.as_view()),
    path('api/v1/photographs/<int:id>/', gallery.api_views.PhotographRetrieveUpdateDestroy.as_view()),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
