from django.shortcuts import render


def home(request):
    """ 
    view to return the home page 
    """
    return render(request, 'home/home.html')


def index(request):
    """ 
    view to return the index page 
    """
    return render(request, 'home/index.html')

