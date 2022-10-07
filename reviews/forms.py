from django import forms
from .models import Reviews
from .widgets import CustomClearableFileInput


class ReviewsForm(forms.ModelForm):
    """
    Form for Reviews
    """

    class Meta:
        model = Reviews
        fields = ("review_title", "service_review", "service_rating", "image")

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )
