# Generated by Django 5.1.6 on 2025-03-10 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nene", "0002_alter_employee_about"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("nom", models.CharField(max_length=255)),
                ("logo", models.ImageField(upload_to="clients/")),
                (
                    "secteur",
                    models.CharField(
                        choices=[
                            ("tech", "Technologie"),
                            ("finance", "Finance"),
                            ("sante", "Santé"),
                            ("ecommerce", "E-commerce"),
                            ("industrie", "Industrie"),
                            ("autre", "Autre"),
                        ],
                        default="autre",
                        max_length=50,
                    ),
                ),
            ],
        ),
    ]
