from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RatingForm
from products.models import Product

# Create your views here.


@login_required
def rating(request, product_id):
    """ A view to show the product rating/ review form  """

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        rating_form_data = {
            'review': request.POST['review'],
            'rating': request.POST['rating'],
            'title': request.POST['title'],
        }
        ratingform = RatingForm(rating_form_data)
        if ratingform.is_valid:
            rating = ratingform.save(commit=False)
            rating.user = request.user
            rating.product = product

            ratingform.save()
            messages.success(request, 'Thank you! Your review has been added.')
            return redirect('product_detail', product.id)
        else:
            messages.error(request, 'review cannot be added, please \
                            recheck the form.')
    else:
        form = RatingForm()
        template = 'rating/rating.html'
        context = {
            'form': form,
            'product': product,
        }
        return render(request, template, context)
