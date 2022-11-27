from django.contrib import admin
from django.urls import path
from edu_app import views


urlpatterns = [
    path('', views.base, name='base'),
    path('about/', views.About_page,name='about'),
    path('academics/', views.Academics_page,name='academics'),
    path('admission/', views.Admission_page,name='admission'),
    path('faculty/', views.Faculty_page, name='faculty'),
    path('research/', views.Research_page, name='research'),
    path('logout', views.user_logout, name='logout'),    
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.Dashboard_page, name='dashboard'),
    path('signup/', views.user_signup, name='signup'),
    path('addstudent/', views.add_student, name='addstudent'),
    path('updatestudent/<int:id>/', views.update_student, 
    name='updatestudent'),
    path('delete/<int:id>/', views.delete_student, 
    name='deletestudent'), 
    path('addattendance/', views.add_attendance, name='addattendance'),
    path('updateattendance/<int:id>/', views.update_attendance, 
    name='updateattendance'),
    path('deleteattendance/<int:id>/', views.delete_attendance, 
    name='deleteattendance'),
]