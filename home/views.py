from django.shortcuts import render
from products.models import Product

# Create your views here.


def index(request):
    """ A view to return the index page """

    products = Product.objects.all().order_by('-id')[:4]
    favourites_list = []

    try:
        user = request.user.id

        for product in products:
            if product.favourites.filter(id=request.user.id).exists():
                favourites_list.append(
                    product.id,
                    )
    except:
        print("error")
    context = {
        'products': products,
        'favourites_list': favourites_list,
    }
    return render(request, 'home/index.html', context)
