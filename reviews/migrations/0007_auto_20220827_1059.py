# Generated by Django 3.0.1 on 2022-08-27 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0006_auto_20220826_1156"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reviews",
            name="website_review",
        ),
        migrations.AddField(
            model_name="reviews",
            name="service_rating",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=6, null=True
            ),
        ),
        migrations.AddField(
            model_name="reviews",
            name="service_review",
            field=models.TextField(default=10, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="reviews",
            name="product_review",
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name="reviews",
            name="review_name",
            field=models.CharField(max_length=100),
        ),
    ]
