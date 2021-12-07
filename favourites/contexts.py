from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def favourites_contents(request):

    favourites_items = []
    favourites_list = []
    favourites = request.session.get('favourites', {})

    for item_id, quantity in favourites.items():
        product = get_object_or_404(Product, pk=item_id)
        favourites_items.append({
            'item_id': int(item_id),
            'product': product,
        })
        favourites_list.append(int(item_id))

    context = {
        'favourites_items': favourites_items,
        'favourites_list': favourites_list
    }

    return context
