from .models import Product, ProductStatus


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


def comming_soon(request):
    """ A context processors to show products comming soon """
    comming_soon = Product.objects.filter(comming_soon=True)

    context = {
        'comming_soon': comming_soon,
    }

    return context