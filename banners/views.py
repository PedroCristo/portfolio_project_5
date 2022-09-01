from django.shortcuts import render


def carousel_banners(request):
    """ 
    view to return the home page 
    """
    return render(request, 'banners/banners_carousel.html')
