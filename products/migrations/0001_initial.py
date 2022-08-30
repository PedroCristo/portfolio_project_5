# Generated by Django 3.2 on 2022-08-30 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('friendly_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Gender_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('friendly_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Gender Categories',
            },
        ),
        migrations.CreateModel(
            name='Product_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('friendly_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Product Status',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('watch_details', models.TextField()),
                ('features', models.TextField()),
                ('has_sizes', models.BooleanField(blank=True, default=False, null=True)),
                ('old_price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products_images/')),
                ('featured', models.BooleanField(default=False)),
                ('promotion', models.BooleanField(default=False)),
                ('comming_soon', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
                ('gender_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.gender_category')),
                ('product_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product_status')),
            ],
        ),
    ]
