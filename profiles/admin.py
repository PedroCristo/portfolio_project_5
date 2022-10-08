from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Displays the User Profile model in the admin panel
    """
    list_display = (
        "user",
        "default_phone_number",
        "default_town_or_city",
        "default_country",
    )
