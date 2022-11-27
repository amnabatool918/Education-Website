from atexit import register
from django.contrib import admin
from edu_app.models import Student, Attendance

#from.models import Student
#from.models import Attendance

# Register your models here.
#admin.site.register(Student)
#admin.site.register(Attendance)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','Title','First_Name','Last_Name','Father_Name','Email','Program','Roll_no','Subject','CNIC','Martial_status','DOB','Cell_no','Parent_mob','Gender','Admission_date','Country','City','Address','Confirm_address','Zip_code')
    ordering = ('First_Name',)
    search_fields = ('First_Name','Admission_date','Roll_no','Address')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id','subject','attendance_date','session_year','created_at')
    ordering = ('subject',)
