# Generated by Django 4.1.6 on 2023-03-28 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("name_user", models.CharField(max_length=255)),
                ("address_user", models.CharField(max_length=255)),
                ("mobile_user", models.CharField(max_length=255)),
                ("id_product", models.CharField(max_length=255)),
                ("category_product", models.CharField(max_length=255)),
                ("name_product", models.CharField(max_length=255)),
                ("amount_product", models.IntegerField()),
                ("description_product", models.TextField()),
                ("price_product", models.FloatField()),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]