# Generated by Django 4.1.6 on 2023-03-18 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user_model", "0002_user_registration"),
    ]

    operations = [
        migrations.DeleteModel(name="User",),
    ]