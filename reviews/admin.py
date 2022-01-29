from django.contrib import admin
from .models import ProductReview


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'nickname',
        'decription',
        'rating',
        'review_date'
    )

admin.site.register(ProductReview)