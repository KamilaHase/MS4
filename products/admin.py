from django.contrib import admin
from .models import Product, Category, Brand
from reviews.models import ProductReview

""" Renders Models to the Admin View"""


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'amount',
        'category',
        'brand',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'brand_frname',
        'brand_name',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'nickname',
        'description',
        'rating',
        'review_date'
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(ProductReview, ReviewAdmin)
