from django.contrib import admin

from .models import BannerCarousel, BannerBottom, BannerVertical


@admin.register(BannerCarousel)
class BannerCarouselAdmin(admin.ModelAdmin):
    """
    Displays the Banner Carousel model in the admin panel
    """
    list_display = (
        "name",
        "description",
        "featured",
    )


@admin.register(BannerBottom)
class BannerBottom(admin.ModelAdmin):
    """
    Displays the Banner Bottom model in the admin panel
    """
    list_display = (
        "name",
        "description",
        "featured",
    )


@admin.register(BannerVertical)
class BannerVertical(admin.ModelAdmin):
    """
    Displays the Banner Vertical model in the admin panel
    """
    list_display = (
        "name",
        "description",
        "image_small",
        "featured",
    )
