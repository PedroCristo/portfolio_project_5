# Generated by Django 3.0.1 on 2022-08-26 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0005_auto_20220826_1155"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reviews",
            name="name",
            field=models.CharField(max_length=20),
        ),
    ]
