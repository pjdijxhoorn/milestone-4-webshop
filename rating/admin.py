from django.contrib import admin
from .models import Rating
# Register your models here.


class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'name',
        'title',
    )


admin.site.register(Rating, RatingAdmin)
