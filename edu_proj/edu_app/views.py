from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from edu_app.models import Student, Attendance
from django.views.generic import (TemplateView)
from .forms import  SignUpForm, LoginForm, StudentForm, AttendanceForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

# Create your views here.

#Main page
def base(request):
    edu_proj = Student.objects.order_by('Admission_date')
    date_dict = {'Stu_DOB':edu_proj}
    return render(request, 'edu_app/base.html', context=date_dict)

#About
def About_page(request):
    return render(request, 'edu_app/about.html')

#Academics
def Academics_page(request):
    return render(request, 'edu_app/academics.html')

#Admission
def Admission_page(request):
    return render(request, 'edu_app/admission.html')

#Faculty
def Faculty_page(request):
    return render(request, 'edu_app/faculty.html')

#Research
def Research_page(request):
    return render(request, 'edu_app/research.html')

#Dashboard
def Dashboard_page(request):
    if request.user.is_authenticated:
        attendance = Attendance.objects.all()
        student = Student.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'edu_app/dashboard.html', {'student': student, 'attendance': attendance, 
        'full_name':full_name, 'groups':gps})
    else:
        return HttpResponseRedirect('/login/')

# login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully !!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'edu_app/login.html', {'form':form})
    else:
      return HttpResponseRedirect('/dashboard/')


#Signup
def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations! Your account has been successfully created.')
            user = form.save()
            group = Group.objects.get(name='Instructor')
            user.groups.add(group)
    else:
        form = SignUpForm()
    return render(request, 'edu_app/signup.html', {'form':form})

#logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# Add Student
def add_student(request):
 if request.user.is_authenticated:
    if request.method == 'POST':
            form = StudentForm(request.POST)
            if form.is_valid():
                Title = form.cleaned_data['Title']
                FName = form.cleaned_data['First_Name']
                LName = form.cleaned_data['Last_Name']
                Addr = form.cleaned_data['Address']
                caddr = form.cleaned_data['Confirm_address']
                FTName = form.cleaned_data['Father_Name']
                mail = form.cleaned_data['Email']
                Prog = form.cleaned_data['Program']
                Roll = form.cleaned_data['Roll_no']
                Subj = form.cleaned_data['Subject']
                cnic = form.cleaned_data['CNIC']
                Mstatus = form.cleaned_data['Martial_status']
                dob = form.cleaned_data['DOB']
                Cno = form.cleaned_data['Cell_no']
                Pno = form.cleaned_data['Parent_mob']
                gend = form.cleaned_data['Gender']
                Addate = form.cleaned_data['Admission_date']
                Cou = form.cleaned_data['Country']
                Cit = form.cleaned_data['City']
                Zip = form.cleaned_data['Zip_code']
                stud = Student(Title=Title, First_Name=FName, Last_Name=LName, Address=Addr, Confirm_address=caddr,
                Father_Name=FTName, Email=mail, Program=Prog, Roll_no=Roll,
                Subject=Subj, CNIC=cnic,Martial_status=Mstatus, DOB=dob,
                Cell_no=Cno, Parent_mob=Pno, Gender=gend, Admission_date=Addate,
                Country=Cou, City=Cit, Zip_code=Zip)
                stud.save()
                form = StudentForm()
    else:
        form = StudentForm()
    return render(request, 'edu_app/addstudent.html', {'form':form})
 else:
    return HttpResponseRedirect('/login/')

# Update/Edit Student
def update_student(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Student.objects.get(pk=id)
            form = StudentForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = Student.objects.get(pk=id)
            form = StudentForm(instance=pi)
        return render(request, 'edu_app/updatestudent.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')

        
# Delete Student
def delete_student(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Student.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')

# Add Attendance
def add_attendance(request):
 if request.user.is_authenticated:
    if request.method == 'POST':
            form = AttendanceForm(request.POST)
            if form.is_valid():
                Subj = form.cleaned_data['subject']
                Atdt = form.cleaned_data['attendance_date']
                sesy = form.cleaned_data['session_year']
                crta = form.cleaned_data['created_at']
                Attd = Attendance(subject=Subj, attendance_date=Atdt,
                session_year=sesy, created_at=crta)
                Attd.save()
                form = AttendanceForm()
    else:
        form = AttendanceForm()
    return render(request, 'edu_app/addattendance.html', {'form':form})
 else:
    return HttpResponseRedirect('/login/')

# Delete attendance
def delete_attendance(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Attendance.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')

# Update/Edit attendance
def update_attendance(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Attendance.objects.get(pk=id)
            form = AttendanceForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = Attendance.objects.get(pk=id)
            form = AttendanceForm(instance=pi)
        return render(request, 'edu_app/updatestudent.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')
