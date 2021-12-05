from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from products.models import Product

# Create your views here.


@login_required
def view_favourites(request):
    """ A view that renders the bag contents page """

    return redirect(reverse)


@login_required
def add_to_favourites(request, item_id):
    """add products to favourites/ wishlist"""
    product = get_object_or_404(Product, pk=item_id)
    favourites = request.session.get('favourites', {})

    favourites[item_id] = 1
    messages.success(request, f'Added {product.name} to your favourites')
    request.session['favourites'] = favourites

    print(favourites)
    print(request.session['favourites'])
    return render(request, 'favourites/favourites.html')

# item_id in list(favourites.keys()):
#     favourites.pop(item_id)
#    messages.success(request, f'Removed {product.name} from your favourites')
