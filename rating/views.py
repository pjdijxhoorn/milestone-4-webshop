from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RatingForm
from products.models import Product

# Create your views here.


@login_required
def rating(request, product_id):
    """ A view to show the product rating/ review form  """
    
    product_obj = get_object_or_404(Product, pk=product_id)
    url = request.META.get('HTTP_REFERER')
    
    if request.method == 'POST':
        rating_form_data = {
            'review': request.POST['review'],
            'rating': request.POST['rating'],
        }
        ratingform = RatingForm(rating_form_data)
        if ratingform.is_valid:
            rating = ratingform.save(commit=false)
            rating.user = request.user
            rating.product = product_obj

            ratingform.save()
            messages.success(request, 'Thank you! Your review has been added.')
            return HttpResponseRedirect(url)
        else:
            messages.error(request, 'review cannot be added, please \
                            recheck the form.')
    else:
        form = RatingForm()
        template = 'rating/rating.html'
        context = {
            'form': form,
        }
        return render(request, template, context)
