# Generated by Django 3.0.1 on 2022-09-21 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0011_reviews_carousel_review"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reviews",
            name="product_review",
        ),
        migrations.RemoveField(
            model_name="reviews",
            name="rating",
        ),
    ]
