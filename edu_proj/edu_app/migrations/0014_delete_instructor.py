# Generated by Django 4.1.1 on 2022-11-27 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("edu_app", "0013_remove_attendance_updated_at_and_more"),
    ]

    operations = [
        migrations.DeleteModel(name="Instructor",),
    ]