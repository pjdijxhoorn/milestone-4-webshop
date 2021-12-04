from django.shortcuts import render

# Create your views here.

def favourites(request):

    """ displays the products listed as favourites by the user"""

    template = 'favourites/favourite'
    context = {}

    return render(request, template, context)