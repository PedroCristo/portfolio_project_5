from django.db import models
from django.urls import reverse


class Reviews(models.Model):
    """
    Model for Reviews
    """
    class Meta:
        verbose_name_plural = 'Reviews'
    review_name = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='reviews_images/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    product_review = models.TextField(max_length=300)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    service_review = models.TextField(null=True, max_length=100)
    service_rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Sets absolute URL"""
        return reverse('reviews')
