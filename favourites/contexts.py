from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def favourites_contents(request):

    favourites_items = []
    favourites = request.session.get('favourites', {})

    for item_id, quantity in favourites.items():
        product = get_object_or_404(Product, pk=item_id)
        favourites_items.append({
            'item_id': item_id,
            'product': product,
        })

    context = {
        'favourites_items': favourites_items,
    }

    return context
