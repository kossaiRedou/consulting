# Generated by Django 5.1.6 on 2025-02-22 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nene", "0008_softskills_alter_employee_slug_alter_project_slug_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="cv",
            field=models.FileField(blank=True, null=True, upload_to="KOTO\\media\\cvs"),
        ),
    ]
