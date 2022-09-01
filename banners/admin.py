from django.contrib import admin

from .models import BannerCarousel, BannerBottom, BannerVerical


@admin.register( BannerCarousel)
class  BannerCarouselAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'featured',
    )


@admin.register(BannerBottom)
class BannerBottom(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'featured',
    )


@admin.register(BannerVerical)
class BannerVerical(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'image_small',
        'featured',
    )

