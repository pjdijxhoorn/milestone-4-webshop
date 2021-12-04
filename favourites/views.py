from django.shortcuts import render

from products.models import Product

# Create your views here.

def view_favourites(request):



    return render(request, 'favourites/favourites.html')


