from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RatingForm
from products.models import Product

# Create your views here.


@login_required
def rating(request, product_id):
    """ A view to show the product rating/ review form  """
    
    if request.method == 'POST':
        rating_form = RatingForm(rating_form_data)
        if rating_form.is_valid:
            rating = rating_form.save(commit=false)
            rating.user = request.user
            review.product = product_obj

            rating.save()
            messages.success(request, 'Thank you! Your review has been added.')
            return redirect(reverse('rating'))
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
