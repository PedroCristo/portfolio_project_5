# Generated by Django 3.0.1 on 2022-09-11 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0013_auto_20220911_1428"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Gender_category",
            new_name="GenderCategory",
        ),
    ]
