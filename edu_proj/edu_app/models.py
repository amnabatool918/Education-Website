from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=10)
    First_Name = models.CharField(max_length=100, unique=True)
    Last_Name = models.CharField(max_length=100, unique=True)
    Father_Name = models.CharField(max_length=100, unique=True)
    Email = models.EmailField(max_length=100)
    Program = models.CharField(max_length=50)
    Roll_no = models.CharField('rollno', max_length=15)
    Subject = models.CharField(max_length=100)
    CNIC = models.IntegerField()
    Martial_status = models.CharField(max_length=200)
    DOB = models.DateField(default=timezone.now)
    Cell_no = models.CharField(max_length=200)
    Parent_mob = models.IntegerField()
    Gender = models.CharField(max_length=200)
    Admission_date = models.DateField()
    Country = models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    Address = models.CharField(max_length=250)
    Confirm_address = models.CharField(max_length=250)
    Zip_code = models.IntegerField()

class Attendance(models.Model):
   
    # Subject Attendance
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=200)
    attendance_date = models.DateField(default=timezone.now)
    session_year = models.DateField(null=True)
    created_at = models.DateField(null=True)