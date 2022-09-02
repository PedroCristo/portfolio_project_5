from django.contrib import admin
from .models import Reviews


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = (
        'review_name',
        'timestamp',
        'rating',
        'approved',
    )
