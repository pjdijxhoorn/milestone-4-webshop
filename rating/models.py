from django.db import models
from products.models import Product

# Create your models here.


class Rating(models.Model):
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=254, null=True, blank=True)
    rating = models.DecimalField(max_digits=1, decimal_places=0)
    review = models.TextField()

    def __str__(self):
        return self.name
