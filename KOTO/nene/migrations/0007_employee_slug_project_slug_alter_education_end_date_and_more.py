# Generated by Django 5.1.6 on 2025-02-21 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nene", "0006_employee_technology_education_project_experience"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name="project",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name="education",
            name="end_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="experience",
            name="end_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
