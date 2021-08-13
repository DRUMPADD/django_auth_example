"""django_auth URL Configuration

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
from django.contrib.auth import views as views_auth
from django.views.generic.base import TemplateView
from authen import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views_auth.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', views_auth.LogoutView.as_view(), name='logout'),
    path('signUp/', views.signUp, name='signup'),
]
