from django.contrib import admin
from .models import Product, Category, GenderCategory, ProductStatus
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    """
    Displays the Product model in the admin panel
    """
    list_display = (
        "sku",
        "name",
        "category",
        "gender_category",
        "has_sizes",
        "old_price",
        "price",
        "rating",
        "product_status",
        "featured",
        "coming_soon",
    )
    summernote_fields = "description, watch_details,  features"
    ordering = ("sku",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Displays the Category model in the admin panel
    """
    list_display = (
        "friendly_name",
        "name",
    )


@admin.register(GenderCategory)
class GenderCategoryAdmin(admin.ModelAdmin):
    """
    Displays the Gender Category model in the admin panel
    """
    list_display = (
        "friendly_name",
        "name",
    )


@admin.register(ProductStatus)
class ProductStatusAdmin(admin.ModelAdmin):
    """
    Displays the Product Status model in the admin panel
    """
    list_display = (
        "friendly_name",
        "name",
    )
