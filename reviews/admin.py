from django.contrib import admin
from .models import Reviews


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "review_title",
        "timestamp",
        "service_review",
        "service_rating",
        "approved",
        "carousel_review",
    )
