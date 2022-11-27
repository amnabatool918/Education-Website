from django import forms
from .models import Student, Attendance
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _


class LoginForm(AuthenticationForm):
  username = UsernameField(widget=forms.TextInput(attrs=
  {'autofocus': True, 'class':'form-control'}))
  password = forms.CharField(label=_('Password'), strip=False,
  widget=forms.PasswordInput(attrs={'autocomplete':
  'current-password', 'class':'form-control'}))

class SignUpForm(UserCreationForm):
  password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
  password2 = forms.CharField(label='Confirm Password(again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
  class Meta:
    model = User
    fields = ['username','first_name','last_name','email']
    labels = {'first_name':'First Name','last_name':'Last Name','email':'Email'}
    widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
    'first_name':forms.TextInput(attrs={'class':'form-control'}),
    'last_name':forms.TextInput(attrs={'class':'form-control'}),
    'email':forms.TextInput(attrs={'class':'form-control'}),
    }

class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['Title', 'First_Name', 'Last_Name', 'Address','Confirm_address','Father_Name','Email','Program','Roll_no','Subject','CNIC',
    'Martial_status','DOB','Cell_no','Parent_mob','Gender','Admission_date','Country','City',
    'Zip_code']
    labels = {'Title':'Title', 'First_Name':'First Name', 'Last_Name':'Last Name', 'Address':'Address','Confirm_address':'Confirm Address',
    'Father_Name':'Father Name','Email':'Email','Program':'Program','Roll_no':'Roll NO','Subject':'Subject',
    'CNIC':'CNIC','Martial_status':'Martial Status','DOB':'DOB','Cell_no':'Cell no','Parent_mob':'Parent mob',
    'Gender':'Gender','Admission_date':'Admission date','Country':'Country','City':'City','Zip_code':'Zip code'}
    widgets = {'Title':forms.TextInput(attrs={'class':'form-control'}),
    'First_Name':forms.TextInput(attrs={'class':'form-control'}),
    'Last_Name':forms.TextInput(attrs={'class':'form-control'}),
    'Address':forms.Textarea(attrs={'class':'form-control'}),
    'Confirm_address':forms.Textarea(attrs={'class':'form-control'}),
    'Father_Name':forms.TextInput(attrs={'class':'form-control'}),
    'Email':forms.TextInput(attrs={'class':'form-control'}),
    'Program':forms.TextInput(attrs={'class':'form-control'}),
    'Roll_no':forms.TextInput(attrs={'class':'form-control'}),
    'Subject':forms.TextInput(attrs={'class':'form-control'}),
    'CNIC':forms.TextInput(attrs={'class':'form-control'}),
    'Martial_status':forms.TextInput(attrs={'class':'form-control'}),
    'DOB':forms.TextInput(attrs={'class':'form-control'}),
    'Cell_no':forms.TextInput(attrs={'class':'form-control'}),
    'Parent_mob':forms.TextInput(attrs={'class':'form-control'}),
    'Gender':forms.TextInput(attrs={'class':'form-control'}),
    'Admission_date':forms.TextInput(attrs={'class':'form-control'}),
    'City':forms.TextInput(attrs={'class':'form-control'}),
    'Zip_code':forms.TextInput(attrs={'class':'form-control'}),
    }

class AttendanceForm(forms.ModelForm):
  class Meta:
    model = Attendance
    fields = ['id','subject','attendance_date','session_year','created_at']
    labels = {'id':'ID','subject':'Subject','attendance_date':'Attendance Date','session_year':'Session Year','created_at':'Created at'}
    widgets = {'id':forms.TextInput(attrs={'class':'form-control'}),
    'subject':forms.TextInput(attrs={'class':'form-control'}),
    'attendance_date':forms.DateTimeInput(attrs={'class':'form-control'}),
    'session_year':forms.DateTimeInput(attrs={'class':'form-control'}),
    'created_at':forms.DateTimeInput(attrs={'class':'form-control'}),
    }