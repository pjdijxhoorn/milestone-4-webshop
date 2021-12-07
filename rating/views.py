from django.shortcuts import render
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Reviews
from .forms import ReviewForm

# Create your views here.


def rating(request):
    """ A view to show the product rating/ review form  """

    form = ReviewForm()
    template = 'rating/rating.html'
    context = {
        'form': form,
    }


    return render(request, template, context)


    