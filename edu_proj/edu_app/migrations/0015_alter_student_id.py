# Generated by Django 4.1.1 on 2022-11-27 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("edu_app", "0014_delete_instructor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="id",
            field=models.AutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                unique=True,
                verbose_name="ID",
            ),
        ),
    ]