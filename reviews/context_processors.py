from .models import *


def service_reviews(request):
    """
    A view to show customers reviews
    """
    service_reviews = Reviews.objects.filter(
        approved=True, carousel_review=True
    ).order_by("-timestamp")

    context = {
        "service_reviews": service_reviews,
    }

    return context
