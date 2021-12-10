from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from products.models import Product

# Create your views here.


@login_required
def view_favourites(request):
    """ A view that renders the favourites contents page """

    user = request.user.id
    products = Product.objects.all()
    favourite = Product.favourites
    favourites_list = []
    
    for product in products:
        if product.favourites.filter(id=request.user.id).exists():
            print(product.name)
            favourites_list.append({
                'product': product,
            })

    context = {
        'favourites_list': favourites_list, 
        }
    
    return render(request, 'favourites/favourites.html', context)


@login_required
def add_to_favourites(request, item_id):
    """add products to favourites/ wishlist"""
    product = get_object_or_404(Product, pk=item_id)
    if product.favourites.filter(id=request.user.id).exists():
        product.favourites.remove(request.user)
    else:    
        product.favourites.add(request.user)
      
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


