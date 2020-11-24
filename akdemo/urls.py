"""akdemo URL Configuration

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
from django.urls import path

import public.views
import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', public.views.Home.as_view(), name="home"),
    path('about', public.views.About.as_view(), name="about"),
    path('contact', public.views.Contact.as_view(), name="contact"),
    path('resources', public.views.Resources.as_view(), name="resources"),
    path('services', public.views.Services.as_view(), name="services"),
    path('advantage', public.views.Advantage.as_view(), name="advantage"),
    path('login', public.views.Login.as_view(), name="login"),
    path('logout', public.views.Logout.as_view(), name="logout"),
    path('services/<slug:slug>', public.views.Service.as_view(), name="service"),

    path('app/', main.views.Dashboard.as_views(), name="dashboard")
]
