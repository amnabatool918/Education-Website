"""edu_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from edu_app import views

urlpatterns = [
    path('edu_app/',include('edu_app.urls')),
    path("admin/", admin.site.urls),
    path('', views.base, name='base'),
    path('about/', views.About_page, name='about'),
    path('academics/', views.Academics_page, name='academics'),
    path('admission/', views.Admission_page, name='admission'),
    path('faculty/', views.Faculty_page,name='faculty'),
    path('research/', views.Research_page,name='research'),
    path('logout', views.user_logout,name='logout'),
    path('login/', views.user_login,name='login'),
    path('dashboard/', views.Dashboard_page,name='dashboard'),
    path('signup/', views.user_signup, name='signup'),
]