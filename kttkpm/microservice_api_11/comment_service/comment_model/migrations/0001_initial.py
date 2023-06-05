# Generated by Django 4.1.6 on 2023-03-28 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("id_user", models.CharField(max_length=255)),
                ("id_product", models.CharField(max_length=255)),
                ("category_product", models.CharField(max_length=255)),
                ("content", models.TextField()),
                ("date", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
