# Generated by Django 4.1.1 on 2022-11-10 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("edu_app", "0005_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student", old_name="Major", new_name="Program",
        ),
    ]
