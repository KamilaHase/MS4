from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Brand(models.Model):

    class Meta:
        verbose_name_plural = 'Brands'

    brand_name = models.CharField(max_length=254)
    brand_frname = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.brand_name

    def get_brand_frname(self):
        return self.brand_frname


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey(
        'Brand', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description_short = models.TextField()
    amount = models.DecimalField(
        max_digits=8, decimal_places=0, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    description_long = models.TextField()
    image = models.ImageField(null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name
