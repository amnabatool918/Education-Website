# Generated by Django 4.1.1 on 2022-10-24 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("edu_app", "0002_adminhod_rename_student_students_delete_admin"),
    ]

    operations = [
        migrations.RenameModel(old_name="AdminHOD", new_name="Adminlogin",),
        migrations.RenameModel(old_name="Counseler", new_name="Instructor",),
        migrations.RenameModel(old_name="Students", new_name="Student",),
        migrations.RenameField(
            model_name="adminlogin", old_name="admin", new_name="adminname",
        ),
    ]