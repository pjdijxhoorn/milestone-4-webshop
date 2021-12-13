from django.contrib import admin
from .models import Rating
# Register your models here.


class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'title',
        'rating',
        'review',
    )


admin.site.register(Rating, RatingAdmin)
