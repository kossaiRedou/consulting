# Generated by Django 5.1.6 on 2025-02-21 16:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nene", "0005_remove_article_notebook"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone", models.CharField(blank=True, max_length=20, null=True)),
                ("linkedin", models.URLField(blank=True, null=True)),
                ("position", models.CharField(max_length=150)),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="profile_pics/"),
                ),
                ("location", models.CharField(max_length=100)),
                ("about", models.TextField(max_length=1200)),
            ],
        ),
        migrations.CreateModel(
            name="Technology",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Education",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("degree", models.CharField(blank=True, max_length=100, null=True)),
                ("specialty", models.CharField(max_length=100)),
                ("university", models.CharField(max_length=100)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(null=True)),
                ("description", models.TextField(max_length=500)),
                ("country", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="educations",
                        to="nene.employee",
                    ),
                ),
            ],
            options={
                "ordering": ["-start_date"],
            },
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="projects/"),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="projects",
                        to="nene.employee",
                    ),
                ),
                (
                    "technologies",
                    models.ManyToManyField(
                        related_name="projects", to="nene.technology"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Experience",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("position", models.CharField(max_length=100)),
                ("company", models.CharField(max_length=100)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(null=True)),
                ("is_current", models.BooleanField(default=False)),
                ("description", models.TextField(max_length=1200)),
                ("city", models.CharField(max_length=100)),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="experiences",
                        to="nene.employee",
                    ),
                ),
                (
                    "technologies",
                    models.ManyToManyField(
                        related_name="experiences", to="nene.technology"
                    ),
                ),
            ],
            options={
                "ordering": ["-start_date"],
            },
        ),
    ]
