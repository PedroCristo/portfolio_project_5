from .models import *


def banner_carousel(request):
    """ A view to display a imge carousel """
    banners_carousel =  BannerCarousel.objects.filter(featured=True)

    context = {
        'banners_carousel': banners_carousel,
    }

    return context


def banner_bottom(request):
    """ A view to dispaly a banner """
    home_banner_bottom = BannerBottom.objects.filter(featured=True)

    context = {
        'home_banner_bottom': home_banner_bottom,
    }

    return context    


def banner_vertival(request):
    """ A view to dispaly a vertical banner """
    banner_vertival = BannerVerical.objects.filter(featured=True)

    context = {
        'banner_vertival': banner_vertival,
    }

    return context        