# Generated by Django 3.0.1 on 2022-09-11 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20220911_1450'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product_status',
            new_name='ProductStatus',
        ),
    ]
