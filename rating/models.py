from django.db import models
from products.models import Product
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Rating(models.Model):
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=254, null=True, blank=True)
    rating = models.IntegerField(default=5, validators=[MaxValueValidator(5),
            MinValueValidator(1)] )
    review = models.TextField()

    def __str__(self):
        return self.name

