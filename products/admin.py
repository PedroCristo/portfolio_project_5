from django.contrib import admin
from .models import Product, Category, Gender_category, Product_status
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'gender_category',
        'old_price',
        'price',
        'rating',
        'product_status',
        'featured',
        'promotion',
        'comming_soon',
    )
    summernote_fields = ('description, watch_details,  features')
    ordering = ('sku',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


@admin.register(Gender_category)
class Gender_categoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


@admin.register(Product_status)
class Product_statusAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )    
