# Generated by Django 3.0.1 on 2022-09-02 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0011_auto_20220902_1049"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="GenderCategory",
            new_name="Gender_category",
        ),
    ]
