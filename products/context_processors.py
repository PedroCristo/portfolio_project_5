from .models import *


def products_selected(request):
    """ A view to show products selected """
    products_selected = Product.objects.filter(featured=True)

    context = {
        'products_selected': products_selected,
    }

    return context


def products_promotion(request):
    """ A view to show products selected """
    products_sales = Product.objects.filter(sales=True)

    context = {
        'products_sales': products_sales,
    }

    return context    


def comming_soon(request):
    """ A view to show products selected """
    comming_soon = Product.objects.filter(comming_soon=True)

    context = {
        'comming_soon': comming_soon,
    }

    return context