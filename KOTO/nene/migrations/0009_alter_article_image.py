# Generated by Django 5.1.6 on 2025-03-11 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nene", "0008_alter_article_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="articles/", verbose_name="Image"
            ),
        ),
    ]
