from django import forms
from .models import Reviews


class ReviewsForm(forms.ModelForm):
    """
    Form for Reviews
    """
    class Meta:
        model = Reviews
        fields = ('review_name', 'product_review', 'rating', 'image', 'service_review', 'service_rating')