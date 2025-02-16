# Generated by Django 5.1.6 on 2025-02-16 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nene", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Article",
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
                ("title", models.CharField(max_length=255, verbose_name="Titre")),
                ("author", models.CharField(max_length=100, verbose_name="Auteur")),
                (
                    "category",
                    models.CharField(max_length=100, verbose_name="Catégorie"),
                ),
                ("content", models.TextField(verbose_name="Contenu")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="articles/",
                        verbose_name="Image",
                    ),
                ),
                (
                    "published_date",
                    models.DateField(
                        auto_now_add=True, verbose_name="Date de publication"
                    ),
                ),
            ],
        ),
    ]
