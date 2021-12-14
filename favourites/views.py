from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from products.models import Product

# Create your views here.


@login_required
def view_favourites(request):
    """ A view that renders the favourites contents page """

    products = Product.objects.all()
    favourites_list = []

    for product in products:
        if product.favourites.filter(id=request.user.id).exists():
            favourites_list.append({
                'product': product,
            })

    context = {
        'favourites_list': favourites_list,
        }

    return render(request, 'favourites/favourites.html', context)


@login_required
def add_to_favourites(request, item_id):
    """toggle products to favourites/ wishlist"""
    url = request.META.get('HTTP_REFERER')
    product = get_object_or_404(Product, pk=item_id)
    if product.favourites.filter(id=request.user.id).exists():
        product.favourites.remove(request.user)
    else:
        product.favourites.add(request.user)

    return HttpResponseRedirect(url)


def remove_from_favourites(request, item_id):
    """remove the favourite from the favourites page"""
    product = get_object_or_404(Product, pk=item_id)
    if product.favourites.filter(id=request.user.id).exists():
        product.favourites.remove(request.user)
    products = Product.objects.all()
    favourites_list = []

    for product in products:
        if product.favourites.filter(id=request.user.id).exists():
            favourites_list.append({
                'product': product,
            })

    context = {
        'favourites_list': favourites_list,
        }

    return render(request, 'favourites/favourites.html', context)
