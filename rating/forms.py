from django import forms
from .models import Rating
from django.contrib.auth.models import User


class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = '__all__'

    
        