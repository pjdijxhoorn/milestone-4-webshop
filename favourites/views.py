from django.shortcuts import render

from products.models import Product

# Create your views here.

def favourites(request):

    """ displays the products listed as favourites by the user"""

    """ get recipe.id  get user  compare if recipe is in users recipe favourite list 

        if icon is clicked toggle remove/add
        return redirect
    
    """

    template = 'favourites/favourites'
    context = {}

    return render(request, template, context)
