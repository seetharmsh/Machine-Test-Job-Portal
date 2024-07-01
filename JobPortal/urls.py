"""
URL configuration for JobPortal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from JobPortalApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name='Home'),
    path('Register',views.UserRegister.as_view(),name='Register'),
    path('Login',views.UserLogin.as_view(),name='Login'),
    path('UserHome',views.UserHome.as_view(),name='UserHome'),
    path('Logout',views.UserLogout.as_view(),name='Logout'),
    path('Create',views.CreateJob.as_view(),name='Create'),
    path('List',views.ListJob.as_view(),name='List'),
    path('Edit/<int:id>',views.EditJob.as_view(),name='Edit'),
    path('Delete/<int:id>',views.DeleteJob.as_view(),name='Delete')
]
