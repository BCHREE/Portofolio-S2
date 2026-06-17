"""
URL configuration for my_portofolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from portofolio_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='index'),
    path('tentang/', views.about_view, name='tentang'),
    path('jadwal/', views.jadwal_view, name='jadwal'),
    path('galery/', views.galery_view, name='galery'),
    path('project/', views.project_view, name='project'),
    path('feedback/', views.feedback_view, name='feedback'),
]