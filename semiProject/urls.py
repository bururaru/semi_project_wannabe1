"""semiProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('attend/', include('attendApp.urls')),
    path('stu/', include('stuApp.urls')),
    path('cal/', include('events.urls')),
    path('boardapp/', include('boardapp.urls')),
    path('common/', include('common.urls')),
    path('hello_app/', include('hello_app.urls')),
    path('opencv_webapp/', include('opencv_webapp.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
