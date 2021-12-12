from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RatingForm

# Create your views here.


@login_required
def rating(request):
    """ A view to show the product rating/ review form  """
    form = RatingForm(request.POST)
    form.instance.name = "paul Dijxhoorn "

    if request.method == 'POST':

        
        if form.is_valid():

            form.save()
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
