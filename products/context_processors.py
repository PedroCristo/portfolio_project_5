from .models import Product


def products_selected(request):
    """ A context processors to show products selected """
    products_selected = Product.objects.filter(featured=True)

    context = {
        'products_selected': products_selected,
    }

    return context


def products_sales(request):
    """ A context processors to show products sales """
    products_sales = Product.objects.filter(product_status__name="Sales")
  
    context = {
        'products_sales': products_sales,
    }

    return context    


def coming_soon(request):
    """ A context processors to show products coming soon """
    coming_soon = Product.objects.filter(coming_soon=True)

    context = {
        'coming_soon': coming_soon,
    }

    return context