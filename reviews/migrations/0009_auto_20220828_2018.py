# Generated by Django 3.0.1 on 2022-08-28 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0008_auto_20220827_1104"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reviews",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="reviews_images/"),
        ),
    ]
